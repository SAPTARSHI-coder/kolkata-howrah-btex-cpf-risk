"""
Master Reproduction and Verification Pipeline
Title: Conditional Probability Function (CPF) Polar Vectors, BTEX Speciation,
       and Inhalation Carcinogenic Risk Assessment across Kolkata and Howrah
Target Journal: Environmental Pollution (Elsevier)
Author: Saptarshi Sadhu (Adamas University, Kolkata, India)
"""

import os
import glob
import pandas as pd
import numpy as np

script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(script_dir, '..'))

base_candidates = [
    os.environ.get('STATION_DATA_DIR', ''),
    os.path.join(project_root, 'data', 'Cleaned_Station_Data'),
    os.path.join(script_dir, '..', 'data', 'Cleaned_Station_Data')
]
data_dir = next((p for p in base_candidates if p and os.path.exists(p)), None)

if not data_dir:
    raise FileNotFoundError(f"Cleaned station data directory not found in: {base_candidates}")

stn_map = {
    "BG": "Ballygunge",
    "SVSPA": "Barrackpore (SVSPA)",
    "BM": "Belur Math",
    "BN": "Bidhannagar",
    "BOG": "Botanical Garden",
    "DN": "Dasnagar",
    "FW": "Fort William",
    "GH": "Ghusuri",
    "JD": "Jadavpur",
    "PP": "Padmapukur",
    "RBU": "Rabindra Bharati Univ",
    "RS": "Rabindra Sarovar",
    "VC": "Victoria Memorial"
}

# Chemical Kinetics and Reactivity Parameters
k_OH = {
    "Benzene": 1.22,
    "Toluene": 5.63,
    "Eth-Benzene": 7.00,
    "mp-Xylene": 23.60,
    "o-Xylene": 13.60,
    "Propene": 26.30
}

MIR = {
    "Benzene": 0.72,
    "Toluene": 3.97,
    "Eth-Benzene": 2.70,
    "mp-Xylene": 9.75,
    "o-Xylene": 7.49
}

MW = {
    "Benzene": 78.11,
    "Toluene": 92.14,
    "Eth-Benzene": 106.16,
    "mp-Xylene": 106.16,
    "o-Xylene": 106.16
}

records = []

for year in [2024, 2025]:
    for code, name in stn_map.items():
        fname = os.path.join(data_dir, f"{code}_{year}_MLL.xlsx")
        if not os.path.exists(fname):
            continue
        
        df = pd.read_excel(fname)
        b = df["Benzene"].mean() if "Benzene" in df.columns else np.nan
        t = df["Toluene"].mean() if "Toluene" in df.columns else np.nan
        e = df["Eth-Benzene"].mean() if "Eth-Benzene" in df.columns else np.nan
        mpx = df["mp-Xylene"].mean() if "mp-Xylene" in df.columns else np.nan
        ox = df["o-Xylene"].mean() if "o-Xylene" in df.columns else np.nan
        
        sum_btex = b + t + e + mpx + ox
        tb = t / b if (b and b > 0) else np.nan
        xe = (mpx + ox) / e if (e and e > 0) else np.nan
        hq = b / 30.0 if (b and b > 0) else np.nan
        ilcr_who = b * 6.0e-6 if (b and b > 0) else np.nan
        ilcr_iris = b * 5.0e-6 if (b and b > 0) else np.nan
        
        # Carter MIR OFP (ug/m3)
        ofp_b = b * MIR["Benzene"]
        ofp_t = t * MIR["Toluene"]
        ofp_e = e * MIR["Eth-Benzene"]
        ofp_mpx = mpx * MIR["mp-Xylene"]
        ofp_ox = ox * MIR["o-Xylene"]
        ofp_tot = ofp_b + ofp_t + ofp_e + ofp_mpx + ofp_ox
        
        pct_b = (ofp_b / ofp_tot) * 100.0 if ofp_tot > 0 else np.nan
        pct_t = (ofp_t / ofp_tot) * 100.0 if ofp_tot > 0 else np.nan
        pct_xyl = ((ofp_mpx + ofp_ox) / ofp_tot) * 100.0 if ofp_tot > 0 else np.nan
        pct_eb = (ofp_e / ofp_tot) * 100.0 if ofp_tot > 0 else np.nan
        
        # Propene-Equivalent Concentration (ug/m3)
        pro_eq = (b * k_OH["Benzene"] + t * k_OH["Toluene"] + e * k_OH["Eth-Benzene"] + 
                  mpx * k_OH["mp-Xylene"] + ox * k_OH["o-Xylene"]) / k_OH["Propene"]
        
        # Hydroxyl radical chemical loss rate L_OH (s^-1) via Eq. 10 number-density conversion
        loh = 0.602214 * (k_OH["Benzene"] * b / MW["Benzene"] + 
                         k_OH["Toluene"] * t / MW["Toluene"] + 
                         k_OH["Eth-Benzene"] * e / MW["Eth-Benzene"] + 
                         k_OH["mp-Xylene"] * mpx / MW["mp-Xylene"] + 
                         k_OH["o-Xylene"] * ox / MW["o-Xylene"])
        
        records.append({
            "Year": year,
            "Station_Code": code,
            "Station_Name": name,
            "Valid_Observations": len(df),
            "Benzene_ug_m3": round(b, 2),
            "Toluene_ug_m3": round(t, 2),
            "Eth_Benzene_ug_m3": round(e, 2),
            "mp_Xylene_ug_m3": round(mpx, 2),
            "o_Xylene_ug_m3": round(ox, 2),
            "Sum_BTEX_ug_m3": round(sum_btex, 2),
            "T_B_Ratio": round(tb, 2),
            "X_E_Ratio": round(xe, 2),
            "Hazard_Quotient_HQ": round(hq, 2),
            "ILCR_WHO_x10_6": round(ilcr_who * 1e6, 2),
            "ILCR_IRIS_x10_6": round(ilcr_iris * 1e6, 2),
            "OFP_Total_ug_m3": round(ofp_tot, 2),
            "Pct_OFP_Benzene": round(pct_b, 1),
            "Pct_OFP_Toluene": round(pct_t, 1),
            "Pct_OFP_Xylenes": round(pct_xyl, 1),
            "Pct_OFP_EthBenz": round(pct_eb, 1),
            "Pro_Equiv_ug_m3": round(pro_eq, 2),
            "L_OH_s_inv": round(loh, 2)
        })

df_results = pd.DataFrame(records)

# Save to both data/ and scripts/
data_csv = os.path.join(project_root, "data", "btex_cpf_risk_results.csv")
script_csv = os.path.join(script_dir, "btex_cpf_risk_results.csv")

df_results.to_csv(data_csv, index=False)
df_results.to_csv(script_csv, index=False)

print("=" * 80)
print("Master Verification Pipeline Completed Successfully")
print(f"Total station-year records processed: {len(df_results)}")
print(f"Outputs written to:\n  - {data_csv}\n  - {script_csv}")
print("=" * 80)

# Display 2024 Table verification summary
print("\n--- 2024 Verified Results (Table 2 & Table 4) ---")
cols_2024 = ["Station_Code", "Benzene_ug_m3", "Toluene_ug_m3", "Sum_BTEX_ug_m3", "T_B_Ratio", "ILCR_WHO_x10_6", "OFP_Total_ug_m3", "L_OH_s_inv"]
print(df_results[df_results["Year"] == 2024][cols_2024].to_string(index=False))

# Display 2025 Table verification summary
print("\n--- 2025 Verified Results (Table 3 & Table 4) ---")
print(df_results[df_results["Year"] == 2025][cols_2024].to_string(index=False))

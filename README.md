# BTEX Speciation, Conditional Probability Function (CPF) Polar Vectors, and Inhalation Carcinogenic Risk Assessment across Kolkata and Howrah

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)

**Author:** Saptarshi Sadhu  
**Affiliation:** School of Engineering and Technology, Adamas University, Kolkata 700126, West Bengal, India  
**Correspondence:** `saptarshi1.sadhu@stu.adamasuniversity.ac.in` / `saptarshisadhuofficial@gmail.com`  
**Repository:** [https://github.com/SAPTARSHI-coder/kolkata-howrah-btex-cpf-risk](https://github.com/SAPTARSHI-coder/kolkata-howrah-btex-cpf-risk)

---

## Overview
This repository contains the research data, computational verification pipelines, and polar directional analysis workflows for the multi-station investigation into speciated volatile organic compounds (BTEX: Benzene, Toluene, Ethylbenzene, $m,p$-Xylene, and $o$-Xylene) across the Kolkata–Howrah conurbation in the lower Gangetic plain.

The study synthesizes **721,193 valid 15-minute continuous chromatography observations** collected across all 13 statutory Continuous Ambient Air Quality Monitoring System (CAAQMS) stations during 2024 and 2025. Key research dimensions include:
1. **Empirical Speciation & Stoichiometric Closure:** Speciation dynamics across contrasting industrial foundry, dense vehicular roadside, riverbank, and parkland microclimates.
2. **Observational Periodicity Deconstruction:** Objective evaluation of seasonal sampling windows and boundary-layer inversion impacts.
3. **Reactivity & Photochemical Paradox:** Ozone Formation Potential (OFP) via Carter Maximum Incremental Reactivity (MIR), Propene-equivalent concentrations, and hydroxyl radical loss rates ($L_{\text{OH}}$).
4. **Receptor Directional Vectors:** Conditional Probability Function (CPF) polar analysis coupling high-concentration threshold exceedances with synchronized wind vectors.
5. **Inhalation Carcinogenic Risk Assessment:** Contemporary concentration-based Inhalation Unit Risk (WHO / USEPA RAGS Part F / IRIS) and chronic non-carcinogenic Hazard Quotients (HQ).

---

## Airshed Monitoring Network (13 CAAQMS Stations)

| Station Name | Code | Latitude | Longitude | Elevation | Classification | Dominant Emission Drivers |
| :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **Ballygunge** | BG | 22.526°N | 88.369°E | 8 m | Residential/Commercial | High-density vehicular traffic, domestic fuel, commercial solvents |
| **Barrackpore** | SVSPA | 22.766°N | 88.365°E | 11 m | Industrial/Suburban | Paper mills, textile printing, suburban arterial freight corridor |
| **Belur Math** | BM | 22.636°N | 88.352°E | 9 m | Religious/Riverbank | Ferry diesel exhaust, Grand Trunk Road vehicular traffic, rail idling |
| **Bidhannagar** | BN | 22.580°N | 88.433°E | 6 m | Commercial/IT Park | IT transit fleet, architectural coating solvents, commercial diesel generators |
| **Botanical Garden** | BOG | 22.547°N | 88.294°E | 7 m | Green Background | River-borne advection of industrial foundry plumes from adjacent Howrah belt |
| **Dasnagar** | DN | 22.592°N | 88.305°E | 8 m | Heavy Industrial | Metal casting foundries, rolling mills, chemical plants, solvent evaporation |
| **Fort William** | FW | 22.553°N | 88.344°E | 9 m | Semi-Urban/Parkland | Military cantonment transit, central Maidan buffer, perimeter transit |
| **Ghusuri** | GH | 22.582°N | 88.316°E | 7 m | Heavy Industrial | Glass furnaces, steel foundries, diesel freight terminals, chemical storage |
| **Jadavpur** | JD | 22.499°N | 88.371°E | 7 m | Mixed Urban/Traffic | Small-scale engineering workshops, intense stop-and-go vehicular exhaust |
| **Padmapukur** | PP | 22.565°N | 88.307°E | 6 m | Industrial/Residential | Water treatment chlorination, localized foundries, Kona Expressway freight |
| **Rabindra Bharati Univ** | RBU | 22.593°N | 88.372°E | 8 m | Traffic Hotspot | High-density arterial junction (BT Road), heavy vehicle braking and idling |
| **Rabindra Sarovar** | RS | 22.508°N | 88.358°E | 7 m | Urban Park | Lake water-body buffer, perimeter Southern Avenue vehicular road network |
| **Victoria Memorial** | VC | 22.544°N | 88.343°E | 8 m | Urban Background | Heritage parkland green buffer, perimeter tourism transit, central river breeze |

---

## Directory Structure
```
kolkata-howrah-btex-cpf-risk/
├── README.md                      # Comprehensive project documentation
├── LICENSE                        # MIT License
├── requirements.txt               # Python package dependencies
├── data/
│   ├── Cleaned_Station_Data/      # 26 station-year continuous 15-minute telemetry Excel files
│   │   ├── BG_2024_MLL.xlsx ... VC_2024_MLL.xlsx
│   │   └── BG_2025_MLL.xlsx ... VC_2025_MLL.xlsx
│   └── btex_cpf_risk_results.csv  # Master numerical verification output across all metrics
├── figures/                       # Publication-quality spatial maps and polar plots
│   ├── Fig 2/                     # Geographic map and station layout
│   └── CPF_Plots/                 # High-resolution polar CPF diagnostic plots
└── scripts/
    ├── btex_cpf_risk_proof.py     # Master Python reproduction pipeline
    └── run_proof.sh               # Execution shell wrapper
```

---

## Reproducibility Instructions

### 1. Environment Setup
Clone this repository and install dependencies:
```bash
git clone https://github.com/SAPTARSHI-coder/kolkata-howrah-btex-cpf-risk.git
cd kolkata-howrah-btex-cpf-risk
pip install -r requirements.txt
```

### 2. Execute Master Reproduction Pipeline
Run the verification script to process all raw station telemetry and recalculate speciation concentrations, diagnostic ratios, photochemical metrics, and health risks:
```bash
python scripts/btex_cpf_risk_proof.py
```
Or use the execution wrapper:
```bash
bash scripts/run_proof.sh
```

The pipeline outputs:
* Full stoichiometric BTEX concentrations ($\text{Benzene}, \text{Toluene}, \text{Eth-Benzene}, m,p\text{-Xylene}, o\text{-Xylene}, \sum\text{BTEX}$)
* Diagnostic ratios ($T/B$, $X/E$)
* Carter OFP, species percentage contributions, and propene-equivalent concentrations
* Avogadro molecular number-density converted hydroxyl radical loss rates ($L_{\text{OH}}$)
* Inhalation Unit Risk carcinogenic estimates ($\text{ILCR}_{\text{WHO}}$, $\text{ILCR}_{\text{IRIS}}$) and non-carcinogenic Hazard Quotients (HQ)
* Outputs exported to `data/btex_cpf_risk_results.csv` and printed to console.

---

## Data Availability
Continuous ambient air quality and BTEX monitoring telemetry used in this study are published by the Central Pollution Control Board (CPCB) and West Bengal Pollution Control Board (WBPCB) via the open-access National Clean Air Programme portal ([https://airquality.cpcb.gov.in](https://airquality.cpcb.gov.in)). All cleaned, quality-controlled 15-minute station datasets supporting this investigation are archived within `data/Cleaned_Station_Data/`.

---

## License
This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

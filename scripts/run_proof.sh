#!/usr/bin/env bash
# Standalone execution wrapper for BTEX CPF and health risk verification script
set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Detect Python interpreter
if [ -f "/Users/saptarshisadhu/miniconda3/envs/EDA/bin/python" ]; then
    PYTHON_EXE="/Users/saptarshisadhu/miniconda3/envs/EDA/bin/python"
elif command -v python3 &> /dev/null; then
    PYTHON_EXE="python3"
elif command -v python &> /dev/null; then
    PYTHON_EXE="python"
else
    echo "Error: Python interpreter not found." >&2
    exit 1
fi

echo "Executing btex_cpf_risk_proof.py..."
"$PYTHON_EXE" "$SCRIPT_DIR/btex_cpf_risk_proof.py"
echo "Execution finished with status: $?"

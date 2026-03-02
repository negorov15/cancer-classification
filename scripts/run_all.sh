#!/usr/bin/env bash
set -euo pipefail

# Execute both classifier notebooks and save executed copies
python3 scripts/run_notebook.py source/RF_classifier.ipynb
python3 scripts/run_notebook.py source/ann_classifier.ipynb

echo "All notebooks executed."

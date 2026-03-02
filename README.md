# Cancer Classification — TEP-based classifiers

Liquid biopsies have the potential to transform cancer diagnostics by offering a minimally invasive way to detect and monitor disease. Among the various blood-based biomarkers under investigation, Tumor-Educated Platelets (TEPs) stand out because their RNA profiles are reshaped by the systemic and local influences of tumor growth. ([Best et al. (2015)](https://www.sciencedirect.com/science/article/pii/S1535610815003499?via%3Dihub)) showed that TEP-derived RNA signatures, when analyzed with a Support Vector Machine, can accurately distinguish early-stage cancer patients from healthy individuals and even identify specific tumor types. Advancing machine learning approaches for TEP data could further enhance early cancer detection and treatment, ultimately improving patient survival.


The goal of this project is to build and evaluate machine-learning classifiers that use Tumor-Educated Platelet (TEP) RNA-Seq profiles to:

- Binary Classification: Differentiate healthy donors from cancer patients (“any cancer”).
- Multiclass Classification: Distinguish healthy donors from specific cancer types (e.g., breast, colorectal, lung, etc.).

Model performance is evaluated on a held-out dataset, examining feature importance alongside overall diagnostic accuracy.

Contents
- `data/` — The tumor-educated platelet RNA-Seq dataset published by ([Best et al. (2015)](https://www.sciencedirect.com/science/article/pii/S1535610815003499?via%3Dihub)) (primary: `GSE68086_TEP_data_matrix.txt`). The dataset consists of RNA-sequencing profiles of blood platelets from 228 cancer patients (spanning six tumor types) and 55 healthy controls.

- `source/` — analysis and model notebooks: `RF_classifier.ipynb`, `ann_classifier_cancer.ipynb`. Each notebook performs preprocessing, trains a model (Random Forest or an ANN), and reports standard evaluation metrics such as accuracy, confusion matrix, and ROC AUC.


## Quick start

1. Create and activate a Python virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:

```bash
# Example: install typical data-science packages
pip install -r requirements.txt
```

If a `requirements.txt` is not present, install packages used in the notebooks, for example:

```bash
pip install jupyterlab numpy pandas scikit-learn tensorflow matplotlib seaborn
```

3. Launch Jupyter and open a notebook from `source/`:

```bash
jupyter lab
# or
jupyter notebook
```

## Reproducing results
- Activate the virtual environment and install dependencies.
- Use the run scripts in `scripts/` to execute the notebooks headlessly and produce executed notebooks with outputs.
- After running the scripts you'll get executed notebooks (filename suffix `_executed.ipynb`) containing the training logs, evaluation metrics, and plots. 
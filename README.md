# Harmful Ingredient Detector

A deep learning project for detecting harmful ingredients in beauty and personal care products. The system classifies ingredient lists as **safe** or **harmful** using both traditional machine learning and transformer-based models.

## 🎯 Project Goal

To help users identify potentially harmful ingredients in cosmetic and skincare products by leveraging:

- Public datasets (Open Beauty Facts)
- External ingredient blacklists (EWG, FDA)
- NLP and deep learning models (DistilBERT)

---

## 🧠 Models Used

| Model        | Framework      | Accuracy | F1 Score |
|--------------|----------------|----------|----------|
| Logistic Reg | scikit-learn   | 96.5%    | 0.97     |
| DistilBERT   | HuggingFace 🤗 | 97.3%    | 0.98     |

Models are trained on labeled ingredient text. See the `results/` directory (DVC-tracked) for training curves, confusion matrices, and classification reports.

---

## 🧪 Project Structure

```plaintext
harmful-ingredient-detector/
├── data/                # Raw and cleaned datasets (DVC-tracked)
├── models/              # Saved model weights (DVC-tracked)
├── results/             # Training outputs & evaluations (DVC-tracked)
├── notebooks/           # Jupyter notebooks for experiments
├── preprocessing/       # Scripts to clean, label, and parse ingredients
├── .gitignore
├── README.md
├── requirements.txt
├── data.dvc             # DVC metadata for datasets
├── models.dvc           # DVC metadata for model artifacts
└── results.dvc          # DVC metadata for evaluation results
```

## Data and Model Versioning with DVC

This project uses **[DVC (Data Version Control)](https://dvc.org/)** for managing large datasets and model files. 

To keep Git lightweight, large files in `data/`, `results/`, and `models/` directories are **tracked with DVC** and are **not pushed to GitHub**.

> 🔒 If cloning this project, please request access to the dataset or use your own DVC remote to fetch required files.

To initialize or restore data:

```bash
dvc pull
```

## Step up

1. Clone this repo:
git clone <https://github.com/cnorteye/harmful-ingredient-detector.git>
cd harmful-ingredient-detector

2. Install dependencies:
```pip install -r requirements.txt```

3. (Optional) Configure DVC:
```dvc init```

## You must set up a DVC remote to pull full datasets/models

This project uses DVC for *local tracking only*

### Note on Data & DVC

Large files like raw PDFs, model checkpoints, and result logs are not pushed to GitHub

These files are tracked locally using DVC

If you’re collaborating, request access or use your own DVC remote

You can still run the code with small sample data or your own inputs

## Contact

Author: @cnorteye
📧 Email: <cnortye@gmail.com>

## Disclaimer

Ingredient safety classifications are based on publicly available third-party data and blacklists (e.g., EWG, FDA). This tool is for educational and academic use only and should not be used for medical or commercial decision-making.

from pathlib import Path

# ======================================
# Project Directories
# ======================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
MODELS_DIR = BASE_DIR / "models"
OUTPUTS_DIR = BASE_DIR / "outputs"

# ======================================
# Dataset
# ======================================

DATASET_NAME = "FraudShield_Transactions_ML_Training.csv"

DATASET_PATH = DATA_DIR / DATASET_NAME

# ======================================
# Create Required Directories
# ======================================

MODELS_DIR.mkdir(parents=True, exist_ok=True)
OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
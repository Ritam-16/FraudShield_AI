from pathlib import Path

# ======================================
# Project Directories
# ======================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

MODEL_FOLDER = PROJECT_ROOT / "models"

# ======================================
# Model Selection
# ======================================

MODEL_NAME = "logistic_model.pkl"

MODEL_PATH = MODEL_FOLDER / MODEL_NAME
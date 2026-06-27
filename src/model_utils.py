import joblib

from src.config import MODELS_DIR


# Create models directory if it doesn't exist
MODELS_DIR.mkdir(parents=True, exist_ok=True)


def save_model(model, filename):
    """
    Save a trained model.
    """

    model_path = MODELS_DIR / filename

    joblib.dump(model, model_path)

    print(f"Model saved to: {model_path.resolve()}")


def load_model(filename):
    """
    Load a trained model.
    """

    model_path = MODELS_DIR / filename

    model = joblib.load(model_path)

    print(f"Model loaded from: {model_path.resolve()}")

    return model
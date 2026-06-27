import pandas as pd

from src.config import DATASET_PATH


def load_data():
    """
    Load the fraud detection dataset.

    Returns
    -------
    pandas.DataFrame
        Loaded transaction dataset.
    """

    try:
        dataframe = pd.read_csv(DATASET_PATH)

        print(f"Dataset loaded successfully: {DATASET_PATH.name}")

        return dataframe

    except FileNotFoundError:

        raise FileNotFoundError(
            f"Dataset not found: {DATASET_PATH}"
        )
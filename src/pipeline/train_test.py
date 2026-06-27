from sklearn.model_selection import train_test_split


TEST_SIZE = 0.20
RANDOM_STATE = 42


def split_dataset(X, y):
    """
    Split dataset into training and testing sets.
    """

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
        stratify=y
    )

    return X_train, X_test, y_train, y_test
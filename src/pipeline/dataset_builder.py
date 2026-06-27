class DatasetBuilder:

    FEATURES = [
        "amount",
        "hour",
        "high_value",
        "off_hours",
        "log_amount"
    ]

    TARGET = "is_fraud"

    def __init__(self, dataframe):
        self.df = dataframe.copy()

    def select_features(self):
        X = self.df[self.FEATURES]
        y = self.df[self.TARGET]
        return X, y
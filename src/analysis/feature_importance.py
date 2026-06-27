import pandas as pd
import matplotlib.pyplot as plt


def plot_feature_importance(model, X):

    importance = pd.DataFrame({

        "Feature": X.columns,

        "Importance": model.feature_importances_

    })

    importance = importance.sort_values(

        by="Importance",

        ascending=False

    )

    print(importance)

    plt.figure(figsize=(10,6))

    plt.barh(

        importance["Feature"],

        importance["Importance"]

    )

    plt.gca().invert_yaxis()

    plt.title("Feature Importance")

    plt.show()
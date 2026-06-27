import matplotlib.pyplot as plt

def plot_fraud_distribution(df):

    fraud_counts = df["is_fraud"].value_counts()

    plt.figure(figsize=(6,4))

    plt.bar(
        fraud_counts.index.astype(str),
        fraud_counts.values
    )

    plt.title("Fraud Distribution")

    plt.xlabel("Fraud")

    plt.ylabel("Count")

    plt.show()


def amount_distribution(df):

    plt.figure(figsize=(8,5))

    plt.hist(df["amount"], bins=40)

    plt.title("Transaction Amount Distribution")

    plt.xlabel("Amount")

    plt.ylabel("Frequency")

    plt.show()

def fraud_vs_amount(df):
        plt.figure(figsize=(8, 5))

        plt.scatter(
            df["amount"],
            df["is_fraud"],
            alpha=0.3
        )

        plt.xlabel("Amount")

        plt.ylabel("Fraud")

        plt.title("Fraud vs Amount")

        plt.show()
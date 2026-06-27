from sklearn.model_selection import cross_val_score

def cross_validate_model(model, X, y):
    scores = cross_val_score(
        model,
        X,
        y,
        cv=5,
        scoring="f1"
    )

    print("Cross Validation F1 Scores:", scores)
    print("Average:", scores.mean())
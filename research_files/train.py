import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler


def train_model(name, path, class_weight=None):

    df = pd.read_csv(path)

    X = df.drop(columns=["Date", "target"])
    y = df["target"]

    split = int(len(df) * 0.8)
    X_train, X_test = X[:split], X[split:]
    y_train, y_test = y[:split], y[split:]

    scaler = StandardScaler()

    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    model = LogisticRegression(
        max_iter=1000,
        class_weight=class_weight
    )

    model.fit(X_train, y_train)

    # SAVE EVERYTHING
    pickle.dump(model, open(f"models/{name}_model.pkl", "wb"))
    pickle.dump(scaler, open(f"models/{name}_scaler.pkl", "wb"))
    pickle.dump(X.columns.tolist(), open(f"models/{name}_features.pkl", "wb"))

    print(f"{name} trained")


def main():

    print("Training all models...\n")

    train_model("crisis", "processed/crisis_features.csv")
    train_model("medium", "processed/medium_features.csv",
                class_weight="balanced")
    train_model("peaceful", "processed/peaceful_features.csv",
                class_weight="balanced")

    print("\nAll models trained successfully!")


if __name__ == "__main__":
    main()

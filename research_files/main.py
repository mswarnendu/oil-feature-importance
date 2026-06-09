import pickle
import pandas as pd
import numpy as np


def display_results(name):

    model = pickle.load(open(f"models/{name}_model.pkl", "rb"))
    features = pickle.load(open(f"models/{name}_features.pkl", "rb"))

    weights = model.coef_.flatten()

    df = pd.DataFrame({
        "Feature": features,
        "Weight": weights,
        "AbsWeight": np.abs(weights)
    }).sort_values("AbsWeight", ascending=False)

    print(f"\n{name.upper()}:\n")
    print(df.head(5).to_string(index=False))

    df.to_csv(f"results/{name}_results.csv")


def main():

    print("RESULTS")

    display_results("crisis")
    display_results("peaceful")
    display_results("medium")


if __name__ == "__main__":
    main()

import pandas as pd

def load_catalogue(path="data/shl_catalogue.csv"):
    df = pd.read_csv(path)
    df["combined_text"] = (
        df["title"].fillna("") + " " +
        df["description"].fillna("") + " " +
        df["skills"].fillna("")
    )
    return df
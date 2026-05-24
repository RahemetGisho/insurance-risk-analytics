import pandas as pd


def load_data(path):
    df = load_data("../data/insurance_data.csv")
    df = pd.read_csv(path)

    return df
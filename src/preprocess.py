import pandas as pd


def preprocess_data(input_path: str, output_path: str):
    """
    Clean and preprocess insurance dataset.
    """

    # Load data
    df = pd.read_csv(input_path)

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Convert transaction date to datetime
    df["TransactionDate"] = pd.to_datetime(df["TransactionDate"])

    # Example feature engineering
    df["LossRatio"] = (
        df["TotalClaims"] / df["TotalPremium"]
    )

    # Save cleaned dataset
    df.to_csv(output_path, index=False)

    print("Cleaned dataset saved successfully.")
    print(f"Shape: {df.shape}")


if __name__ == "__main__":

    preprocess_data(
        "data/insurance_data.csv",
        "data/insurance_data_cleaned.csv"
    )
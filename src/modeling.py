from sklearn.metrics import mean_squared_error, r2_score
import numpy as np


def evaluate_regression_model(y_true, y_pred):

    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    r2 = r2_score(y_true, y_pred)

    return {
        "RMSE": rmse,
        "R2": r2
    }


def create_classification_target(df):

    df["HasClaim"] = (df["TotalClaims"] > 0).astype(int)

    return df
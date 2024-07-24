"""Prepare data for Plotly Dash."""
import numpy as np
import pandas as pd


def create_dataframe():
    """Create Pandas DataFrame from local CSV."""
    df = pd.read_csv("ML-Diabetes-Prediction/app/data/diabetes_clean_pruned.csv")

    return df

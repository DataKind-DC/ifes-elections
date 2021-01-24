"""Utilities for reading processed data."""
import pandas as pd
from src import utils


def elections():
    """Read processed elections data.

    Returns:
        pandas.DataFrame: Processed elections data.
    """
    path = utils.PATHS["processed"] / "elections.csv"
    return pd.read_csv(path, index_col="election_id")


def voting_methods():
    """Read processed voting methods data.

    Returns:
        pandas.DataFrame: Processed voting methods data.
    """
    path = utils.PATHS["processed"] / "voting_methods.csv"
    return pd.read_csv(path, index_col=["election_id", "method_id"])

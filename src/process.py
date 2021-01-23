"""Utilities for processing raw json exports.
"""
import pandas as pd


def extract_results(raw):
    """Extract results from raw data JSON.

    Args:
        raw (list): Pages of raw elections JSON.

    Returns:
        list: Results extracted from all pages.
    """
    results = []
    for page in raw:
        results.extend(page["results"])
    return results


def tidy_names(results):
    """Extract names from elections json.

    Args:
        results (list): Results from elections json.

    Returns:
        pandas.Series: election names, indexed by election ID.
    """
    # Extract election names.
    records = dict()
    for result in results:
        records[result["election_id"]] = result["election_name"]["en_US"]

    # Make an election name series.
    return (pd.Series(records, name="election_name")
              .rename_axis(index="election_id"))

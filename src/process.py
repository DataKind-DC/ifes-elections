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


def process_elections(results):
    """Process elections data from raw results json.

    Args:
        results (list): Results from elections json.

    Returns:
        pandas.DataFrame: election data, indexed by election ID.
    """
    e = tidy_elections(results)
    n = tidy_names(results)
    d = tidy_districts(results)
    v = tidy_verified(results)
    return pd.concat([e, n, d, v], axis=1)


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


def tidy_districts(results):
    """Extract district information from elections json.

    Args:
        results (list): Results from elections json.

    Returns:
        pandas.DataFrame: election district information, indexed by election ID.
    """
    # Extract district information.
    records = dict()
    for result in results:
        records[result["election_id"]] = result["district"]

    # Make a districts dataframe.
    return (pd.DataFrame.from_dict(records, orient="index")
              .rename_axis("election_id"))


def tidy_elections(results):
    """Extract elections information from elections json.

    Args:
        results (list): Results from elections json.

    Returns:
        pandas.DataFrame: election information, indexed by election ID.
    """
    # Identify the unique election index.
    index = "election_id"

    # Exclude nested data structures.
    exclude = [
        "election_name",
        "district",
        "voting_methods",
        "third_party_verified"
    ]

    # Return a dataframe of election data.
    return (pd.DataFrame.from_records(results, index=index, exclude=exclude)
              .rename_axis(index="election_id"))


def tidy_verified(results):
    """Extract verification information from elections json.

    Args:
        results (list): Results from elections json.

    Returns:
        pandas.DataFrame: verification information, indexed by election ID.
    """
    # Extract district information.
    records = dict()
    for result in results:
        records[result["election_id"]] = result["third_party_verified"]

    # Make a districts dataframe.
    columns = {"is_verified": "verified", "date": "verified_date"}
    return (pd.DataFrame.from_dict(records, orient="index")
              .rename_axis(index="election_id")
              .rename(columns=columns))

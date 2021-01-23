"""Utilities for processing raw json exports.
"""


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

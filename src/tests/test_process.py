import pandas as pd
import pandas.testing as pdt
import pytest
from src import process


@pytest.fixture
def results():
    """Example election records from raw JSON."""
    return [
        {
            "election_id": "0",
            "election_name": {"en_US": "Election 0"},
        },
        {
            "election_id": "1",
            "election_name": {"en_US": "Election 1"},
        },
    ]

def test_extract_results():
    raw = [
        {"results": ["r00", "r01"]},
        {"results": ["r10", "r11"]}
    ]
    expected = ["r00", "r01", "r10", "r11"]
    assert process.extract_results(raw) == expected


def test_tidy_names(results):
    values = ["Election 0", "Election 1"]
    index = pd.Index(["0", "1"], name="election_id")
    expected = pd.Series(values, index=index, name="election_name")
    result = process.tidy_names(results)
    pdt.assert_series_equal(result, expected)

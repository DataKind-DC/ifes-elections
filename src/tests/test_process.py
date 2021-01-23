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
            "district": {
                "district_name": "dn0",
                "district_type": "dt0",
                "district_ocd_id": "do0",
                "district_country": "dc0",
            },
        },
        {
            "election_id": "1",
            "election_name": {"en_US": "Election 1"},
            "district": {
                "district_name": "dn1",
                "district_type": "dt1",
                "district_ocd_id": "do1",
                "district_country": "dc1",
            },
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


def test_tidy_districts(results):
    data = {
        "district_name": ["dn0", "dn1"],
        "district_type": ["dt0", "dt1"],
        "district_ocd_id": ["do0", "do1"],
        "district_country": ["dc0", "dc1"],
    }
    index = pd.Index(["0", "1"], name="election_id")
    expected = pd.DataFrame(data, index)
    result = process.tidy_districts(results)
    pdt.assert_frame_equal(result, expected)

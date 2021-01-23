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
            "election_key": "ek0",
            "election_year": 2020,
            "voting_methods": [],
            "third_party_verified": {
                "is_verified": False,
                "date": "2020-01-01",
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
            "election_key": "ek1",
            "election_year": 2021,
            "voting_methods": [],
            "third_party_verified": {
                "is_verified": True,
                "date": "2021-01-01",
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


def test_process_elections(results):
    index = pd.Index(["0", "1"], name="election_id")
    result = process.process_elections(results)
    assert result.shape == (2, 9)
    pdt.assert_index_equal(index, result.index)


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


def test_tidy_elections(results):
    data = {
        "election_key": ["ek0", "ek1"],
        "election_year": [2020, 2021],
    }
    index = pd.Index(["0", "1"], name="election_id")
    expected = pd.DataFrame(data, index)
    result = process.tidy_elections(results)
    pdt.assert_frame_equal(result, expected)


def test_tidy_verified(results):
    data = {
        "verified": [False, True],
        "verified_date": ["2020-01-01", "2021-01-01"],
    }
    index = pd.Index(["0", "1"], name="election_id")
    expected = pd.DataFrame(data, index)
    result = process.tidy_verified(results)
    pdt.assert_frame_equal(result, expected)

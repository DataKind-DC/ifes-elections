from src import process


def test_extract_results():
    raw = [
        {"results": ["r00", "r01"]},
        {"results": ["r10", "r11"]}
    ]
    expected = ["r00", "r01", "r10", "r11"]
    assert process.extract_results(raw) == expected

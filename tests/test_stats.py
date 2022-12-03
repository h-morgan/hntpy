import hntpy as hnt


def test_stats():
    resp = hnt.get_blockchain_stats()
    assert isinstance(resp, dict)
    assert "token_supply" in resp
    assert "counts" in resp


def test_get_token_supply():
    resp = hnt.get_token_supply()
    assert isinstance(resp, dict)
    assert "token_supply" in resp

    # test the raw response format (returns as text, so it's a string)
    raw = hnt.get_token_supply(format="raw")
    assert isinstance(raw, str)

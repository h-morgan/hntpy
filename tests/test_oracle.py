import hntpy as hnt
from types import GeneratorType


def test_oracle_current_price():
    data = hnt.current_oracle_price()
    assert isinstance(data, dict)
    assert "timestamp" in data
    assert "price" in data


def test_oracle_price_list():
    data = hnt.list_oracle_prices(max_block=366700)
    assert isinstance(data, list)
    assert len(data) > 1

    item = data[0]
    assert "timestamp" in item
    assert "price" in item

    # test generator
    gen = hnt.list_oracle_prices(max_block=366700, gen=True)
    assert isinstance(gen, GeneratorType)


def test_oracle_price_stats():
    data = hnt.oracle_price_stats(min_time="2022-10-10", max_time="2022-10-17")
    assert isinstance(data, dict)
    assert "avg" in data
    assert "max" in data


def test_oracle_price_at_block():
    data = hnt.oracle_price_at_block(471570)
    assert isinstance(data, dict)
    assert "price" in data
    assert data["block"] == 471570


def test_list_oracle_activity():
    data = hnt.list_oracle_activity(
        min_time="2022-01-01", max_time="2022-02-01", limit=10
    )
    assert isinstance(data, list)
    assert len(data) == 10
    assert data[0]["type"] == "price_oracle_v1"
    assert data[0]["time"] == 1643673519

    # test generator
    gen = hnt.list_oracle_activity(
        min_time="2022-01-01", max_time="2022-02-01", limit=10, gen=True
    )
    assert isinstance(gen, GeneratorType)
    for batch in gen:
        for d in batch:
            assert d["type"] == "price_oracle_v1"
            assert "time" in d

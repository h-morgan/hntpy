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

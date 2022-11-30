from hntpy import Hotspot
from types import GeneratorType

TEST_HOTSPOT_ID = "11Z6K426LMUow2Jyvf7MdP7js9qsdt7Kp9D9koxg9xoJSMLTy1y"


def test_hotspot_id():
    hotspot = Hotspot(TEST_HOTSPOT_ID)
    assert hotspot.address == TEST_HOTSPOT_ID


def test_get_hotspot_details():
    hotspot = Hotspot(TEST_HOTSPOT_ID)
    data = hotspot.get_details()

    assert isinstance(data, dict)

    # check for some expected keys in the response
    assert "name" in data
    assert "location" in data
    assert "owner" in data


def test_get_hotspot_roles():
    hotspot = Hotspot(TEST_HOTSPOT_ID)
    data = hotspot.roles(limit=10)

    assert isinstance(data, list)
    assert len(data) == 10

    # check if the generator works
    gen = hotspot.roles(limit=10, filter_types="rewards_v2", gen=True)
    assert isinstance(gen, GeneratorType)
    for batch in gen:
        for activity in batch:
            assert activity["type"] == "rewards_v2"

    # check if min and max time filters work
    data2 = hotspot.roles(min_time="2022-11-01", max_time="2022-11-02")

    # get a reward, ensure it's on the day we requested
    reward = data2[0]
    assert "type" in reward
    # we know this is the time for the first reward on this day, so check that it's working
    reward_time = reward["time"]
    assert reward_time == 1667336306


def test_hotspot_role_counts():
    hotspot = Hotspot(TEST_HOTSPOT_ID)
    data = hotspot.role_counts()

    assert isinstance(data, dict)
    assert "rewards_v2" in data

    # test filtering
    data = hotspot.role_counts(filter_types="add_gateway_v1,oui_v1")
    assert isinstance(data, dict)
    assert "add_gateway_v1" in data
    assert "oui_v1" in data
    assert "coinbase_v1" not in data


def test_rewards():
    hotspot = Hotspot(TEST_HOTSPOT_ID)

    resp = hotspot.rewards(min_time="2021-11-20", max_time="2021-11-21")
    assert isinstance(resp, list)

    # get a reward, ensure it's on the day we requested
    reward = resp[0]
    reward_time = reward["timestamp"]
    assert "2021-11-20" in reward_time

    # test generator
    resp2 = hotspot.rewards(min_time="2021-11-20", max_time="2021-11-21", gen=True)
    assert isinstance(resp2, GeneratorType)


def test_reward_totals():
    hotspot = Hotspot(TEST_HOTSPOT_ID)
    resp = hotspot.rewards_sum(min_time="2021-11-20", max_time="2021-11-21")

    assert isinstance(resp, dict)
    assert "sum" in resp

    resp = hotspot.rewards_sum(
        min_time="2022-01-20", max_time="2022-06-21", bucket="week"
    )

    assert isinstance(resp, list)
    assert len(resp) > 0


def test_elections():
    hotspot = Hotspot(TEST_HOTSPOT_ID)
    data = hotspot.elections(limit=10, min_time="2021-01-01", max_time="2021-01-05")

    assert isinstance(data, list)
    assert len(data) <= 10

    # check if the generator works
    gen = hotspot.elections(
        limit=10, min_time="2021-01-01", max_time="2021-01-05", gen=True
    )
    assert isinstance(gen, GeneratorType)


def test_challenges():
    hotspot = Hotspot(TEST_HOTSPOT_ID)
    data = hotspot.challenges(limit=10, min_time="2021-01-01", max_time="2021-01-05")

    assert isinstance(data, list)
    assert len(data) <= 10

    # check if the generator works
    gen = hotspot.challenges(
        limit=10, min_time="2021-01-01", max_time="2021-01-05", gen=True
    )
    assert isinstance(gen, GeneratorType)


def test_witnesses():
    hotspot = Hotspot(TEST_HOTSPOT_ID)
    data = hotspot.witnesses()

    assert isinstance(data, list)
    assert len(data) > 0

    # look at one of the items to make sure it's what we expect
    d = data[0]
    assert "status" in d
    assert "payer" in d
    assert "owner" in d


def test_witnessed():
    hotspot = Hotspot(TEST_HOTSPOT_ID)
    data = hotspot.witnessed()

    assert isinstance(data, list)
    assert len(data) > 0

    # look at one of the items to make sure it's what we expect
    d = data[0]
    assert "status" in d
    assert "payer" in d
    assert "owner" in d

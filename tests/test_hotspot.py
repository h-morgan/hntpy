from hntpy import Hotspot
from types import GeneratorType

TEST_HOTSPOT_ID = "11Z6K426LMUow2Jyvf7MdP7js9qsdt7Kp9D9koxg9xoJSMLTy1y"


def test_hotspot_id():
    hotspot_id = "1234"
    hotspot = Hotspot(hotspot_id)
    assert hotspot.hotspot_id == hotspot_id


def test_get_hotspot_details():
    hotspot = Hotspot(TEST_HOTSPOT_ID)
    data = hotspot.get_hotspot_details()

    assert isinstance(data, dict)

    # check for some expected keys in the response
    assert "name" in data
    assert "location" in data
    assert "owner" in data


def test_get_hotspot_activity():
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

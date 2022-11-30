from hntpy import Validator
from types import GeneratorType

TEST_VALIDATOR_ID = "11NzRc42WHnj2u2fSGGdwYJ411RM289AWVbwjQ8MpNurqkDfB4J"


def test_validator_addr():
    val = Validator(TEST_VALIDATOR_ID)
    assert val.address == TEST_VALIDATOR_ID


def test_get_validator_details():
    val = Validator(TEST_VALIDATOR_ID)
    data = val.get_details()

    assert isinstance(data, dict)

    # check for some expected keys in the response
    assert "name" in data
    assert "status" in data
    assert "owner" in data


def test_get_validator_roles():
    validator = Validator(TEST_VALIDATOR_ID)
    data = validator.roles(limit=3)

    assert isinstance(data, list)
    assert len(data) == 3

    # check if the generator works
    gen = validator.roles(limit=5, filter_types="rewards_v2", gen=True)
    assert isinstance(gen, GeneratorType)
    for batch in gen:
        for activity in batch:
            assert activity["type"] == "rewards_v2"

    # check if min and max time filters work
    data2 = validator.roles(min_time="2022-11-01", max_time="2022-11-02")

    # get a reward, ensure it's on the day we requested
    reward = data2[0]
    assert "type" in reward
    # we know this is the time for the first reward on this day, so check that it's working
    reward_time = reward["time"]
    assert reward_time == 1667347083


def test_validator_role_counts():
    validator = Validator(TEST_VALIDATOR_ID)
    data = validator.role_counts()

    assert isinstance(data, dict)
    assert "rewards_v2" in data

    # test filtering
    data = validator.role_counts(filter_types="add_gateway_v1,oui_v1")
    assert isinstance(data, dict)
    assert "add_gateway_v1" in data
    assert "oui_v1" in data
    assert "rewards_v2" not in data


def test_rewards():
    validator = Validator(TEST_VALIDATOR_ID)

    resp = validator.rewards(min_time="2022-11-20", max_time="2022-11-21")
    assert isinstance(resp, list)

    # get a reward, ensure it's on the day we requested
    reward = resp[0]
    reward_time = reward["timestamp"]
    assert "2022-11-20" in reward_time

    # test generator
    resp2 = validator.rewards(min_time="2022-11-20", max_time="2022-11-21", gen=True)
    assert isinstance(resp2, GeneratorType)


def test_reward_totals():
    validator = Validator(TEST_VALIDATOR_ID)
    resp = validator.rewards_sum(min_time="2022-11-20", max_time="2022-11-25")

    assert isinstance(resp, dict)
    assert "sum" in resp

    resp = validator.rewards_sum(
        min_time="2022-10-01", max_time="2022-11-29", bucket="week"
    )

    assert isinstance(resp, list)
    assert len(resp) > 0

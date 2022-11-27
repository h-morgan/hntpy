from hntpy import Account
from types import GeneratorType


def test_account_details():
    account_id = "13d5xg6qzdE2sVtep6GtbYtJ3fPCvxwpjMWSD4L7hBtSVrrjfZR"
    account = Account(account_id)
    details = account.get_details()

    assert "address" in details

    # get address returned from API response, should match our original account address
    api_addr = details["address"]
    assert api_addr == account_id


def test_get_hotspots():
    account = Account(address="13d5xg6qzdE2sVtep6GtbYtJ3fPCvxwpjMWSD4L7hBtSVrrjfZR")
    details = account.hotspots()

    assert isinstance(details, list)
    assert len(details) > 0


def test_get_hotspots_with_filter():
    # NOTE: the filter param doesn't seem to work on Helium API queries anyways
    account = Account(address="13d5xg6qzdE2sVtep6GtbYtJ3fPCvxwpjMWSD4L7hBtSVrrjfZR")

    # test a valid filter
    filter_mode = "dataonly"
    details = account.hotspots(filter_modes=filter_mode)
    assert isinstance(details, list)

    # test invalid filter
    filter_mode = "bad"
    details = account.hotspots(filter_modes=filter_mode)

    assert isinstance(details, list)


def test_get_validators():
    account = Account(address="13d5xg6qzdE2sVtep6GtbYtJ3fPCvxwpjMWSD4L7hBtSVrrjfZR")
    details = account.validators()

    assert isinstance(details, list)


def test_get_ouis():
    account = Account(address="13d5xg6qzdE2sVtep6GtbYtJ3fPCvxwpjMWSD4L7hBtSVrrjfZR")
    details = account.ouis()

    assert isinstance(details, list)

    # get generator
    gen = account.ouis(gen=True)
    assert isinstance(gen, GeneratorType)


def test_get_roles():
    account = Account(address="1d5xg6qzdE2sVtep6GtbYtJ3fPCvxwpjMWSD4L7hBtSVrrjfZR")
    details = account.roles()

    assert isinstance(details, list)

    # get generator
    gen = account.roles(gen=True)
    assert isinstance(gen, GeneratorType)


def test_role_counts():
    account = Account(address="13d5xg6qzdE2sVtep6GtbYtJ3fPCvxwpjMWSD4L7hBtSVrrjfZR")
    details = account.role_counts()

    assert isinstance(details, dict)
    assert "add_gateway_v1" in details

    # test that filter types works
    resp = account.role_counts(filter_types="token_burn_v1")
    assert "token_burn_v1" in resp
    assert len(resp) == 1


def test_rewards():
    account = Account(address="13d5xg6qzdE2sVtep6GtbYtJ3fPCvxwpjMWSD4L7hBtSVrrjfZR")

    resp = account.rewards(min_time="2021-11-20", max_time="2021-11-21")
    assert isinstance(resp, list)

    # get a reward, ensure it's on the day we requested
    reward = resp[0]
    reward_time = reward["timestamp"]
    assert "2021-11-20" in reward_time

    # test generator
    resp2 = account.rewards(min_time="2021-11-20", max_time="2021-11-21", gen=True)
    assert isinstance(resp2, GeneratorType)


def test_reward_totals():
    account = Account(address="13d5xg6qzdE2sVtep6GtbYtJ3fPCvxwpjMWSD4L7hBtSVrrjfZR")
    resp = account.rewards_sum(min_time="2021-11-20", max_time="2021-11-21")

    assert isinstance(resp, dict)
    assert "sum" in resp

    resp = account.rewards_sum(
        min_time="2022-01-20", max_time="2022-06-21", bucket="week"
    )

    assert isinstance(resp, list)
    assert len(resp) > 0


def test_get_stats():
    account = Account(address="13d5xg6qzdE2sVtep6GtbYtJ3fPCvxwpjMWSD4L7hBtSVrrjfZR")
    data = account.stats()

    assert isinstance(data, dict)
    assert "last_week" in data
    assert "last_month" in data
    assert "last_day" in data

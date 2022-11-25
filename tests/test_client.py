from hntpy.helium_client import HeliumClient
from types import GeneratorType


def test_client_setup():
    client = HeliumClient()

    assert client.base_url == "https://api.helium.io/v1/"


def test_client_generator():

    client = HeliumClient()
    gen = client.get_account_gen(
        wallet_id="e14pfGBDvijGgyDtxVDqVEwRbKEgLhTsKLbV1fCxAJ4yU3FkdpWh", suffix="roles"
    )

    for data in gen:
        assert isinstance(data, list)
    assert isinstance(gen, GeneratorType)

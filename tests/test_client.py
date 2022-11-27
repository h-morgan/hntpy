from hntpy.helium_client import HeliumClient
from types import GeneratorType


def test_client_setup():
    client = HeliumClient()

    assert client.api_url == "https://api.helium.io/v1/"


def test_client_generator():

    client = HeliumClient()
    account_id = "e14pfGBDvijGgyDtxVDqVEwRbKEgLhTsKLbV1fCxAJ4yU3FkdpWh"
    url = f"accounts/{account_id}/ouis"
    gen = client.gen_data(url)

    for data in gen:
        assert isinstance(data, list)
    assert isinstance(gen, GeneratorType)

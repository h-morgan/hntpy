from hntpy.helium_client import HeliumClient

# for these requests, we don't want to have to instantiate a class to be able to call methods,
# so keep these functions at the file level

client = HeliumClient()
BASE_URL = "stats"


def get_blockchain_stats():
    """Retrieve stats for the blockchain"""
    url = BASE_URL
    return client.get_data(url)


def get_token_supply(format="json"):
    """Returns the circulating token supply"""
    url = BASE_URL + "/token_supply"

    # validate format value by turning it to all lowercase, just in case
    format = format.lower()
    format = format if format in ("json", "raw") else "json"
    params = {"format": format}

    return client.get_data(url, params=params)

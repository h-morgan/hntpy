from hntpy.helium_client import HeliumClient
from typing import Union
from types import GeneratorType

# for these requests, we don't want to have to instantiate a class to be able to call methods,
# so keep these functions at the file level

client = HeliumClient()
BASE_URL = "oracle"
PRICE_URL = BASE_URL + "/prices"


def current_oracle_price() -> dict:
    """Retrieve the current Oracle Price and at which block it took effect"""
    url = PRICE_URL + "/current"
    return client.get_data(url)


def list_oracle_prices(
    max_block: int = None, gen: bool = False
) -> Union[list, GeneratorType]:
    """Retrieve the current and historical Oracle Prices and at which block they took effect

    Args:
        - max_block: max block # of which to include data for
    """
    url = PRICE_URL
    params = {"max_block": max_block} if max_block is not None else {}

    if gen:
        data = client.gen_data(url, params=params)
    else:
        data = client.get_data(url, params=params)
    return data


def oracle_price_stats(min_time: str, max_time: str) -> dict:
    """Gets statistics on Oracle prices.

    Args:
        - min_time: (YYYY-mm-dd) First time to include data for (YYYY-mm-dd)
        - max_time: (YYYY-mm-dd) Last time to include data for (exclusive)
    """
    url = PRICE_URL + "/stats"

    params = {"max_time": max_time, "min_time": min_time}

    return client.get_data(url, params=params)


def oracle_price_at_block(block_num: int) -> dict:
    """Provides the oracle price at a specific block.

    Args:
        - block_num (required): the integer block # to get oracle price for
    """
    url = PRICE_URL + f"/{block_num}"
    return client.get_data(url)


def list_oracle_activity(
    min_time: str = None, max_time: str = None, limit: int = None, gen: bool = False
) -> Union[list, GeneratorType]:
    """List oracle price report transactions for all oracle keys.

    Args:
        min_time (optional): (YYYY-mm-dd) First time to include data for
        max_time (optional): (YYYY-mm-dd) Last time to include data for (exclusive)
        limit (optional): 	Maximum number of items to return
        gen (optional): if True, yield results with a generator. if false, return a list

    """
    url = BASE_URL + f"/activity"

    params = {}
    if max_time:
        params["max_time"] = max_time
    if min_time:
        params["min_time"] = min_time
    if limit:
        params["limit"] = limit

    if gen:
        data = client.gen_data(url, params=params)
    else:
        data = client.get_data(url, params=params)

    return data

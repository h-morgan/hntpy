from hntpy.helium_client import HeliumClient
from typing import Union
from hntpy.resources.base import BaseAddrResource


class Account(BaseAddrResource):

    client = HeliumClient()
    base_url = "accounts"

    def __init__(self, address: str):
        self.address = address

    def hotspots(self, filter_modes: str = None) -> list:
        """Get a list of hotspots and their details for the account

        filter_mode is an optional parameter, which can be one or more of the following options:
        - full,dataonly,light
        """
        # only possible combinations of filter_mode param (per Helium API docs)
        if filter_modes:
            params = {"filter_modes": filter_modes}
        else:
            params = {}

        url = self.base_url + f"/{self.address}/hotspots"
        data = self.client.get_data(url, params=params)

        return data

    def validators(self) -> list:
        """Get a list of validators and their details for the account"""
        url = self.base_url + f"/{self.address}/validators"
        data = self.client.get_data(url)
        return data

    def ouis(self, gen: bool = False) -> list:
        """Get a list of all ouis owned by an account. Can optionally return data as a generator."""
        url = self.base_url + f"/{self.address}/ouis"
        if gen:
            data = self.client.gen_data(url)
        else:
            data = self.client.get_data(url)
        return data

    def stats(self) -> dict:
        """Fetches account statistics for a given account. This currently includes account balance information (in bones) for the last month (daily), last week (every 8 hours), and daily (hourly)."""
        url = self.base_url + f"/{self.address}/stats"
        data = self.client.get_data(url)
        return data

from hntpy.helium_client import HeliumClient
from hntpy.resources.base import BaseAddrResource
from typing import Union
from types import GeneratorType


class Hotspot(BaseAddrResource):

    client = HeliumClient()
    base_url = "hotspots"

    def __init__(self, address: str):
        self.address = address
        self.validate_addr()

    def witnesses(self) -> dict:
        """Retrieves the list of witnesses for a given hotspot over about the last 5 days of blocks"""
        url = self.base_url + f"/{self.address}/witnesses"
        data = self.client.get_data(url)
        return data

    def witnessed(self) -> dict:
        """Retrieves the list of hotspots the given hotspot witnessed over the last 5 days."""
        url = self.base_url + f"/{self.address}/witnessed"
        data = self.client.get_data(url)
        return data

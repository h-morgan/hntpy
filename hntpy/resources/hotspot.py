from hntpy.helium_client import HeliumClient
from hntpy.resources.base import BaseAddrResource
from typing import Union
from types import GeneratorType


class Hotspot(BaseAddrResource):

    client = HeliumClient()
    base_url = "hotspots"

    def __init__(self, address: str):
        self.address = address

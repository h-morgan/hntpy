from hntpy.helium_client import HeliumClient
from hntpy.resources.base import BaseAddrResource
from typing import Union
from types import GeneratorType


class Validator(BaseAddrResource):

    client = HeliumClient()
    base_url = "validators"

    def __init__(self, address: str):
        self.address = address
        self.validate_addr()

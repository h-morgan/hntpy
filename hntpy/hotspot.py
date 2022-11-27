from hntpy.helium_client import HeliumClient
from typing import Union
from types import GeneratorType


class Hotspot:

    client = HeliumClient()
    base_url = "hotspots"

    def __init__(self, hotspot_id: str):
        self.hotspot_id = hotspot_id

    def get_hotspot_details(self) -> dict:
        """Fetch the hotspot details"""
        url = self.base_url + f"/{self.hotspot_id}"
        return self.client.get_data(url)

    def roles(
        self,
        filter_types: str = None,
        min_time: str = None,
        max_time: str = None,
        limit: int = None,
        gen: bool = False,
    ) -> Union[list, GeneratorType]:
        """Fetches all blockchain transactions that the hotspot was involved in

        Args:
            filter_types (optional): comma-separated list of transaction types
            min_time (optional): First time to include data for
            max_time (optional): Last time to include data for (exclusive)
            limit (optional): 	Maximum number of items to return
            gen (optional): if True, yield results with a generator. if false, return a list

        """
        url = self.base_url + f"/{self.hotspot_id}/roles"

        params = {}
        if max_time:
            params["max_time"] = max_time
        if min_time:
            params["min_time"] = min_time
        if filter_types:
            params["filter_types"] = filter_types
        if limit:
            params["limit"] = limit

        if gen:
            data = self.client.gen_data(url, params=params)
        else:
            data = self.client.get_data(url, params=params)

        return data

    def role_counts(self, filter_types: str = None) -> dict:
        """Gets counts of all role (transactions) types for a hotspot.

        filter_types is an optional parameter, which can should be a comma-separated list (wihtout spaces) of one or more of a transaction type.
        Example: filter_types="gen_gateway_v1,poc_request_v1"

        If no filter_types arg provided, counts for all role types are returned.
        """
        url = self.base_url + f"/{self.hotspot_id}/roles/count"
        if filter_types:
            params = {"filter_types": filter_types}
        else:
            params = {}
        data = self.client.get_data(url, params=params)
        return data

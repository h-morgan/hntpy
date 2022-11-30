from hntpy.helium_client import HeliumClient
from typing import Union
from types import GeneratorType


class BaseAddrResource:
    """Abstract resource class to be inherited by concrete resources that have IDs to setup functionality
    for requests to the Helium API that require an address (accounts, hotspots, validators, etc.).

    These share a lot of the same methods, with the difference being the ID and a portion of the request endpoint
    """

    client = HeliumClient()
    address = None

    def get_details(self) -> dict:
        url = self.base_url + f"/{self.address}"
        return self.client.get_data(url)

    def validate_addr(self) -> bool:
        if len(self.address) != 51:
            raise ResourceAddressError()

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
        url = self.base_url + f"/{self.address}/roles"

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
        """Gets counts of all role (transaction) types for the address.

        filter_types is an optional parameter, which can should be a comma-separated list (without spaces) of one or more of a transaction type.
        Example: filter_types="gen_gateway_v1,poc_request_v1"

        If no filter_types arg provided, counts for all role types are returned.
        """
        url = self.base_url + f"/{self.address}/roles/count"
        if filter_types:
            params = {"filter_types": filter_types}
        else:
            params = {}
        data = self.client.get_data(url, params=params)
        return data

    def rewards(
        self, max_time: str = None, min_time: str = None, gen: bool = False
    ) -> list:
        """Gets all rewards for an address, in a given timebound between max_time and min_time

        Notes:
            - max_time and min_time should be date strings, in the format "YYYY-mm-dd".
            - The block that contains the `max_time` stamp is excluded from result (upper bound not inclusive)
            - max_time and min_time both default to `now`, so at least one bound should be provided
            - timestamps are returned in UTC
        """
        url = self.base_url + f"/{self.address}/rewards"

        params = {}
        if max_time:
            params["max_time"] = max_time
        if min_time:
            params["min_time"] = min_time

        if gen:
            data = self.client.gen_data(url, params=params)
        else:
            data = self.client.get_data(url, params=params)

        return data

    def rewards_sum(
        self, max_time: str = None, min_time: str = None, bucket: str = None
    ) -> Union[dict, list]:
        """Gets rewards totals for an address. Time range optional, between max_time and min_time. Bucket can optionally can group rewards.

        Notes:
            - max_time and min_time should be ISO date strings, in the format "YYYY-mm-dd".
            - valid bucket values = "hour", "day", or "week"
            - The block that contains the `max_time` stamp is excluded from result (upper bound not inclusive)
            - when timestmaps are omitted, current time is assumed
            - if bucket param provided, a list of rewards sums broken up by requested bucket-length is returns

        Returns (2 cases):
            dict: if no bucket arg provided
            list: if bucket provided
        """
        url = self.base_url + f"/{self.address}/rewards/sum"

        params = {}
        if max_time:
            params["max_time"] = max_time
        if min_time:
            params["min_time"] = min_time
        if bucket:
            params["bucket"] = bucket

        data = self.client.get_data(url, params=params)

        return data

    def elections(
        self,
        min_time: str = None,
        max_time: str = None,
        limit: int = None,
        gen: bool = False,
    ) -> Union[list, GeneratorType]:
        """Fetches all electionss that the address (single hotspot or all hotspots for an account) was involved in

        Args:
            min_time (optional): First time to include data for
            max_time (optional): Last time to include data for (exclusive)
            limit (optional): 	Maximum number of items to return
            gen (optional): if True, yield results with a generator. if false, return a list

        """
        url = self.base_url + f"/{self.address}/elections"

        params = {}
        if max_time:
            params["max_time"] = max_time
        if min_time:
            params["min_time"] = min_time
        if limit:
            params["limit"] = limit

        if gen:
            data = self.client.gen_data(url, params=params)
        else:
            data = self.client.get_data(url, params=params)

        return data

    def challenges(
        self,
        min_time: str = None,
        max_time: str = None,
        limit: int = None,
        gen: bool = False,
    ) -> Union[list, GeneratorType]:
        """Fetches all challenges that the address (single hotspot or all hotspots for an account)
        was a challenger, challengee, or witness in.

        Args:
            min_time (optional): First time to include data for
            max_time (optional): Last time to include data for (exclusive)
            limit (optional): 	Maximum number of items to return
            gen (optional): if True, yield results with a generator. if false, return a list

        """
        url = self.base_url + f"/{self.address}/challenges"

        params = {}
        if max_time:
            params["max_time"] = max_time
        if min_time:
            params["min_time"] = min_time
        if limit:
            params["limit"] = limit

        if gen:
            data = self.client.gen_data(url, params=params)
        else:
            data = self.client.get_data(url, params=params)

        return data


class ResourceAddressError(Exception):
    def __init__(self, message=None):
        if message is None:
            message = "Address is invalid - please provide a valid 51 character Helium resource address."
        super().__init__(message)

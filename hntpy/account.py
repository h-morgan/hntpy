from hntpy.helium_client import HeliumClient
from typing import Union


class Account:

    client = HeliumClient()
    base_url = "accounts"

    def __init__(self, account_id: str):
        self.account_id = account_id

    def get_account_id(self) -> str:
        return self.account_id

    def get_account_details(self) -> dict:
        url = self.base_url + f"/{self.account_id}"
        return self.client.get_data(url)

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

        url = self.base_url + f"/{self.account_id}/hotspots"
        data = self.client.get_data(url, params=params)

        return data

    def validators(self) -> list:
        """Get a list of validators and their details for the account"""
        url = self.base_url + f"/{self.account_id}/validators"
        data = self.client.get_data(url)
        return data

    def ouis(self, gen: bool = False) -> list:
        """Get a list of all ouis owned by an account. Can optionally return data as a generator."""
        url = self.base_url + f"/{self.account_id}/ouis"
        if gen:
            data = self.client.gen_data(url)
        else:
            data = self.client.get_data(url)
        return data

    def roles(self, gen: bool = False) -> list:
        """Gets list of all roles (transactions) that indicate an account as a participant. Can optionally return data as a generator."""
        url = self.base_url + f"/{self.account_id}/roles"
        if gen:
            data = self.client.gen_data(url)
        else:
            data = self.client.get_data(url)
        return data

    def role_counts(self, filter_types: str = None) -> dict:
        """Gets counts of all role (transaction) types.

        filter_types is an optional parameter, which can should be a comma-separated list (wihtout spaces) of one or more of a transaction type.
        Example: filter_types="gen_gateway_v1,poc_request_v1"

        If no filter_types arg provided, counts for all role types are returned.
        """
        url = self.base_url + f"/{self.account_id}/roles/count"
        if filter_types:
            params = {"filter_types": filter_types}
        else:
            params = {}
        data = self.client.get_data(url, params=params)
        return data

    def rewards(
        self, max_time: str = None, min_time: str = None, gen: bool = False
    ) -> list:
        """Gets all rewards for an account, in a given timebound between max_time and min_time

        Notes:
            - max_time and min_time should be date strings, in the format "YYYY-mm-dd".
            - The block that contains the `max_time` stamp is excluded from result (upper bound not inclusive)
            - max_time and min_time both default to `now`, so at least one bound should be provided
            - timestamps are returned in UTC
        """
        url = self.base_url + f"/{self.account_id}/rewards"

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
        """Gets rewards totals for an account. Time range optional, between max_time and min_time. Bucket can optionally can group rewards.

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
        url = self.base_url + f"/{self.account_id}/rewards/sum"

        params = {}
        if max_time:
            params["max_time"] = max_time
        if min_time:
            params["min_time"] = min_time
        if bucket:
            params["bucket"] = bucket

        data = self.client.get_data(url, params=params)

        return data

    def stats(self) -> dict:
        """Fetches account statistics for a given account. This currently includes account balance information (in bones) for the last month (daily), last week (every 8 hours), and daily (hourly)."""
        url = self.base_url + f"/{self.account_id}/stats"
        data = self.client.get_data(url)
        return data

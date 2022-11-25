from hntpy.helium_client import HeliumClient


class Account:

    client = HeliumClient()

    def __init__(self, account_id: str):
        self.account_id = account_id

    def get_account_id(self) -> str:
        return self.account_id

    def get_account_details(self) -> dict:
        return self.client.get_account_data(self.account_id)

    def hotspots(self, filter_mode: str = None) -> list:
        """Get a list of hotspots and their details for the account

        filter_mode is an optional parameter, which can be one or more of the following options:
        - full,dataonly,light
        """
        # only possible combinations of filter_mode param (per Helium API docs)
        filter_modes = [
            "full",
            "dataonly",
            "light",
            "full,dataonly,light",
            "full,dataonly" "full,light",
            "dataonly,light",
        ]
        if filter_mode in filter_modes:
            param = {"filter_mode": filter_mode}
        else:
            param = {}
        data = self.client.get_account_data(
            self.account_id, suffix="hotspots", params=param
        )

        return data

    def validators(self) -> list:
        """Get a list of validators and their details for the account"""
        data = self.client.get_account_data(self.account_id, suffix="validators")
        return data

    def ouis(self, gen=False) -> list:
        """Get a list of ouis owned by an account. Can optionally return data as a generator."""
        if gen:
            data = self.client.get_account_gen(self.account_id, suffix="ouis")
        else:
            data = self.client.get_account_data(self.account_id, suffix="ouis")
        return data

    def roles(self, gen=False) -> list:
        """Gets list of transactions that indicate an account as a participant. Can optionally return data as a generator."""
        if gen:
            data = self.client.get_account_gen(self.account_id, suffix="roles")
        else:
            data = self.client.get_account_data(self.account_id, suffix="roles")
        return data

    def role_counts(self) -> dict:
        data = self.client.get_account_data(self.account_id, suffix="roles/count")
        return data

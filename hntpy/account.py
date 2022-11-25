from hntpy.helium_client import HeliumClient


class Account:

    client = HeliumClient()

    def __init__(self, account_id:str):
        self.account_id = account_id

    def get_account_id(self) -> str:
        return self.account_id
    
    def get_account_details(self) -> dict:
        return self.client.get_account_data(self.account_id)

    def hotspots(self, filter_mode:str = None) -> list:
        """Get a list of hotspots and their details for the account

        filter_mode is an optional parameter, which can be one or more of the following options:
        - full, dataonly, light

        ids_only is an optional param, when true it only returns the id values of the hotspots (not full data)
        """
        # only possible combinations of filter_mode param (per Helium API docs)
        filter_modes = [
            "full",
            "dataonly",
            "light",
            "full,dataonly,light",
            "full,dataonly"
            "full,light",
            "dataonly,light"
        ]
        if filter_mode in filter_modes:
            param = {"filter_mode": filter_mode}
        else:
            param = {}
        resp = self.client.get_account_data(self.account_id, suffix="hotspots", params=param)

        return resp["data"]

    def validators(self) -> list:
        """Get a list of validators and their details for the account
        """
        resp = self.client.get_account_data(self.account_id, suffix="validators")
        return resp["data"]

    def ouis(self) -> list:
        """Get a list of ouis owned by a account (account)
        """
        resp = self.client.get_account_data(self.account_id, suffix="validators")
        return resp["data"]


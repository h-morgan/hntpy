from hntpy.helium_client import HeliumClient

class Wallet:

    client = HeliumClient()

    def __init__(self, wallet_id):
        self.wallet_id = wallet_id

    def get_wallet_id(self):
        return self.wallet_id
    
    def get_account_details(self):
        return self.client.get_wallet(self.wallet_id)

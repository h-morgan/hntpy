from hntpy.helium_client import HeliumClient
from hntpy.wallet import Wallet

def sandbox():

    #client = HeliumClient(base_url="https://api.helium.io/v1")

    #client.get_accounts(url_suffix="accounts/rich")

    wallet_id = '46ucP1youkC74YSqUi6aSPJawvK1bw2H3ZZqfwTaeHeUWCd7xp'
    wallet = Wallet(wallet_id)
    print(wallet.get_account_details())

if __name__ == "__main__":
    sandbox()
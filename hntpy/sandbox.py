from hntpy.helium_client import HeliumClient
from hntpy.account import Account

def sandbox():

    #client = HeliumClient(base_url="https://api.helium.io/v1")

    #client.get_accounts(url_suffix="accounts/rich")

    account_id_2 = "13ZNCUTCV9g3vpFpsc1QXSxvcwXsqKVbJtUHwU947vw3TPDCCa8"
    account_id = '13d5xg6qzdE2sVtep6GtbYtJ3fPCvxwpjMWSD4L7hBtSVrrjfZR'
    account = Account(account_id_2)
    
    resp = account.validators()
    print(resp)

if __name__ == "__main__":
    sandbox()
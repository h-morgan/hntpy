from hntpy import Wallet

def test_hnt_py():
    wallet_id = "1234"
    wallet = Wallet(wallet_id)
    assert wallet.get_wallet_id() == wallet_id

def test_wallet_id():
    wallet_id = "1234"
    wallet = Wallet(wallet_id)
    assert wallet.get_wallet_id() == wallet_id

def test_valid_wallet_details():
    wallet_id = "13d5xg6qzdE2sVtep6GtbYtJ3fPCvxwpjMWSD4L7hBtSVrrjfZR"
    wallet = Wallet(wallet_id)
    details = wallet.get_account_details()
    
    assert "data" in details
    assert "address" in details["data"]
    
    # get address returned from API response, should match our original wallet address
    api_addr = details["data"]["address"]
    assert api_addr == wallet_id




from hntpy import Account

def test_hnt_py():
    account_id = "1234"
    account = Account(account_id)
    assert account.get_account_id() == account_id

def test_account_id():
    account_id = "1234"
    account = Account(account_id)
    assert account.get_account_id() == account_id

def test_account_details():
    account_id = "13d5xg6qzdE2sVtep6GtbYtJ3fPCvxwpjMWSD4L7hBtSVrrjfZR"
    account = Account(account_id)
    details = account.get_account_details()
    
    assert "data" in details
    assert "address" in details["data"]
    
    # get address returned from API response, should match our original account address
    api_addr = details["data"]["address"]
    assert api_addr == account_id

def test_get_hotspots():
    account = Account(account_id="13d5xg6qzdE2sVtep6GtbYtJ3fPCvxwpjMWSD4L7hBtSVrrjfZR")
    details = account.hotspots()
    
    assert isinstance(details, list)


def test_get_hotspots_with_filter():
    # NOTE: the filter param doesn't seem to work on Helium API queries anyways
    account = Account(account_id="13d5xg6qzdE2sVtep6GtbYtJ3fPCvxwpjMWSD4L7hBtSVrrjfZR")

    # test a valid filter
    filter_mode = "dataonly"
    details = account.hotspots(filter_mode=filter_mode)
    assert isinstance(details, list)

    # test invalid filter
    filter_mode = "bad"
    details = account.hotspots(filter_mode=filter_mode)
    
    assert isinstance(details, list)

def test_get_validators():
    account = Account(account_id="13d5xg6qzdE2sVtep6GtbYtJ3fPCvxwpjMWSD4L7hBtSVrrjfZR")
    details = account.validators()
    
    assert isinstance(details, list)

    




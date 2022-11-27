# hntpy

<p align="left">
    <a alt="Version" href="https://pypi.org/project/hntpy/">
    <img src="https://img.shields.io/badge/version-0.0.6-blue"/></a>
    <a href="https://github.com/h-morgan/hntpy/blob/main/LICENSE" alt="License">
    <img src="https://img.shields.io/github/license/h-morgan/hntpy"/></a>
    <a alt="Coverage" href="#">
    <img src="https://img.shields.io/badge/coverage-92%25-green"/></a>
</p>

## Introduction

hntpy is a Python wrapper for Helium API to simplify requests and interaction with Helium blockchain. The aim of this project is to enable retrieval of Helium data from the API in a Pythonic way.

For comprehensive documentation (with examples), review the full usage docs on [Github](https://github.com/h-morgan/hntpy/tree/main/docs).

For more detail on exact API responses/data, please see the officical [Helium documentation](https://docs.helium.com/api/blockchain/introduction).

This project is continually under development. If you notice a bug, or have a feature request, please submit a Github issue [here](https://github.com/h-morgan/hntpy/issues).

## Install

To use the latest version of this Python package, download from PyPi:

```
pip install hntpy
```

## Example Usage

See complete documentation and more examples [here](https://github.com/h-morgan/hntpy/tree/main/docs).

### The Account module

The `Account` module allows you to interact with/get data about your Helium account in a simplified way.

[Official Helium Accounts API documentation](https://docs.helium.com/api/blockchain/accounts).

To instantiate an Account instance for your Helium account:

```python
from hntpy import Account

# pass your 51-digit Helium account/wallet address
account = Account("your-helium-account-addr-here")

# your Helium account address will be stored/accessible here
addr = account.account_id
```

To retrieve your account details:

```python
details = account.get_account_details()
```

#### List hotspots and validators for an account

The `details` variable is now a python `dict` containing your account details from the Helium API.

To get a list of hotspots, and their data, for your account:

```python
hotposts = account.hotspots()
```

The `hotspots` variable is now a list of hotspots and their data, for example:

```
[
    {
      "lng": -81.70707772367822,
      "lat": 41.480133219396784,
      "status": {
        "online": "online",
        "height": 435166,
        "gps": "good_fix"
      },
      "score_update_height": 435153,
      "score": 0.9222412109375,
      "owner": "13GCcF7oGb6waFBzYDMmydmXx4vNDUZGX4LE3QUh8eSBG53s5bx",
      "nonce": 1,
      "name": "sneaky-violet-penguin",
      "location": "8c2ab38f19a43ff",
      "geocode": {
        "short_street": "W 32nd St",
        "short_state": "OH",
        "short_country": "US",
        "short_city": "Cleveland",
        "long_street": "West 32nd Street",
        "long_state": "Ohio",
        "long_country": "United States",
        "long_city": "Cleveland",
        "city_id": "Y2xldmVsYW5kb2hpb3VuaXRlZCBzdGF0ZXM"
      },
      "block_added": 96087,
      "block": 435241,
      "address": "1182nyT3oXZPMztMSww4mzaaQXGXd5T7JwDfEth6obSCwwxxfsB"
    }
  ]
```

To get a list of the validators, and their data, associated with your account:

```python
validators = account.validators()
```

#### OUIS and roles for an account

For OUIs and roles, these endpoints sometimes return large amounts of data that take a while to retrieve from the Helium API. For these methods, you have the option of requesting how you want the data returned to you, either:

- list format
- generator of batches of lists

If you'd like to wait and receive one giant list of data, simply run:

```python
# to get ouis for your account
ouis = account.ouis()

# to get roles for your account
roles = account.roles()
```

**Note:** Depending on the amount of data these requests have to return, you may need to wait a bit while the reqeuests complete. In instances where there are many pages of data being returned from the Helium API, these requests can sometimes take minutes.

If you'd like to return batches of lists, using a generator, for each page of data retrieved from the API, simply pass the `gen=True` argument:

```python
# to get ouis for your account
ouis = account.ouis(gen=True)

# to get roles for your account
roles = account.roles(gen=True)
```

You can then iterate over these variables like you would any Python generator, to view your data in batches. For example:

```python
for batch in roles:
    ## batch is now a list of role items returned from Helium
    for role in batch:
        hash_id = role["hash"]
        # ...
```

To get the role counts (transaction/activity counts) for an account:

```python
role_counts = account.role_counts()
```

# The Account module

## Introduction

This module sets up an `Account` object to make requests on behalf of a given Helium account address. This allows you to interact with/get data about your Helium account in a Pythonic way. The methods on this module, their naming, and their responses align with the [official Helium Accounts API](https://docs.helium.com/api/blockchain/accounts).

To import it into your file:

```python
from hntpy import Account
```

## Instantiating the Account object

To instantiate an Account instance for your Helium account:

```python
from hntpy import Account

# pass your 51-digit Helium account/wallet address
account = Account("your-helium-account-addr-here")

# your Helium account address will be stored/accessible here
addr = account.address
```

To retrieve your account details:

```python
details = account.get_details()
```

The `details` variable is now a python `dict` containing your account details from the Helium API.

**Note:** All of the following sections assume an instantiation of an `Account` object, stored in a variable named `account`.

## Get hotspots for an account

To get a list of hotspots, and their data, for your account:

```python
hotposts = account.hotspots(filter_modes="full")
```

The `filter_modes` parameter can be used to filter hotspots by how they were added to the blockchain. Supported values are `full`, `dataonly`, or `light`. A comma separated list (no whitespace) can be used to filter for multiple modes.

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

## Get validators for an account

To get a list of the validators, and their data, associated with the account:

```python
validators = account.validators()
```

## Get OUIs for an account

Fetches OUIs owned by a given account address.

**Note:** this method supports generator return type.

```python
# to get ouis for your account
ouis = account.ouis()

# get ouis for your account, and return them in batches
ouis_gen = account.ouis(gen=True)
```

The `ouis_gen` variable is now a `GeneratorType` object, that can be iterated over in realtime instead of waiting for the full request to the blockchain to complete. For example:

```python
for batch in ouis_gen:
    for oui in batch:
        # do something with each oui here...
```

## Get roles (activity) for an account

Fetches transactions that indicate an account as a participant. This includes any transaction that involves the account, usually as a payer, payee or owner.

**Note:** this method supports generator return type.

```python
roles = account.roles()
```

Optionally, you can pass the following arguments to the `roles()` method:

- `filter_types` (str): Comma separated list of transaction types (no whitespace). For example "payment_v1,token_burn_v1"
- `min_time` (str): date format of "YYYY-mm-dd", lower time bound (inclusive)
- `max_time` (str): date format of "YYYY-mm-dd", upper time bound (exclusive)
- `limit` (int): maximum number of items to return
- `gen` (bool): defaults to `False`, set to `True` if you want the response to be a generator

## Get role counts for an account

To get the role counts (transaction/activity counts) for an account:

```python
role_counts = account.role_counts()
```

Optionally you can pass the following argument to the `role_counts()` method:

- `filter_types` (str): Comma separated list of transaction types (no whitespace). For example "payment_v1,token_burn_v1"

## Get rewards for an account

Returns reward entries by block and gateway for a given account in a timeframe. Timestamps are given in ISO 8601 format.

**Note:** this method supports generator return type.

```python
roles = account.rewards()
```

Optionally, you can pass the following arguments to the `rewards()` method:

- `min_time` (str): date format of "YYYY-mm-dd", lower time bound (inclusive)
- `max_time` (str): date format of "YYYY-mm-dd", upper time bound (exclusive)
- `gen` (bool): defaults to `False`, set to `True` if you want the response to be a generator

## Get rewards totals for an account

Returns the total rewards for a given account in a given timeframe. The results can also be bucketed in time by specifying a `bucket` query parameter which buckets information per bucket in the given timeframe. Data is bucketed per hotspot and time for the account to make hotspot performance comparison possible. Valid bucket values include `hour`, `day` and `week`).

```python
roles = account.rewards_sum()
```

Optionally, you can pass the following arguments to the `rewards_sum()` method:

- `min_time` (str): date format of "YYYY-mm-dd", lower time bound (inclusive)
- `max_time` (str): date format of "YYYY-mm-dd", upper time bound (exclusive)
- `bucket` (str): defaults to `None`. If bucketing is desired, valid values are `hour`, `day` and `week`

## Get challenges for an account

Fetches challenges that hotspots owned by the given account are involved in as a challenger, challengee, or witness.

**Note:** this method supports generator return type.

```python
roles = account.challenges()
```

Optionally, you can pass the following arguments to the `challenges()` method:

- `min_time` (str): date format of "YYYY-mm-dd", lower time bound (inclusive)
- `max_time` (str): date format of "YYYY-mm-dd", upper time bound (exclusive)
- `limit` (int): maximum number of items to return
- `gen` (bool): defaults to `False`, set to `True` if you want the response to be a generator

## Get elections for an account

Fetches elections that hotspots for the given account are elected in.

**Note:** this method supports generator return type.

```python
roles = account.elections()
```

Optionally, you can pass the following arguments to the `elections()` method:

- `min_time` (str): date format of "YYYY-mm-dd", lower time bound (inclusive)
- `max_time` (str): date format of "YYYY-mm-dd", upper time bound (exclusive)
- `limit` (int): maximum number of items to return
- `gen` (bool): defaults to `False`, set to `True` if you want the response to be a generator

## Get statistics for an account

Fetches account statistics for a given account. This currently includes account balance information (in bones) for the last month (daily), last week (every 8 hours), and daily (hourly).

```python
stats = account.stats()
```

# The Validator module

## Introduction

This module sets up a `Validator` object to make requests on behalf of a given Helium validator address. This allows you to interact with/get data about your validator in a Pythonic way. The methods on this module, their naming, and their responses align with the [official Helium Validators API](https://docs.helium.com/api/blockchain/validators).

To import it into your file:

```python
from hntpy import Validator
```

## Instantiating the Validator object

To instantiate a Validator instance:

```python
from hntpy import Validator

# pass your 51-character Helium validator address
validator = Validator("your-helium-validator-addr-here")

# your validator address will be stored/accessible here
addr = validator.address
```

To retrieve the validator details:

```python
details = validator.get_details()
```

The `details` variable is now a python `dict` containing a `dict` of the validator details, as returned from the Helium API.

**Note:** All of the following sections assume an instantiation of a `Validator` object, stored in a variable named `validator`.

## Get roles (activity) for a validator

Lists all blockchain transactions that the given validator was involved in.

**Note:** this method supports generator return type.

```python
roles = validator.roles()
```

Optionally, you can pass the following arguments to the `roles()` method:

- `filter_types` (str): Comma separated list of transaction types (no whitespace). For example "payment_v1,token_burn_v1"
- `min_time` (str): date format of "YYYY-mm-dd", lower time bound (inclusive)
- `max_time` (str): date format of "YYYY-mm-dd", upper time bound (exclusive)
- `limit` (int): maximum number of items to return
- `gen` (bool): defaults to `False`, set to `True` if you want the response to be a generator

## Get role counts for a validator

Count transactions that indicate activity for a validator.

The results are a map keyed by the given `filter_types` and the count of transaction of that type.

```python
role_counts = validator.role_counts()
```

Optionally you can pass the following argument to the `role_counts()` method:

- `filter_types` (str): Comma separated list of transaction types (no whitespace). For example "payment_v1,rewards_v2"

## Get rewards for a validator

Returns rewards for a given validator per reward block the validator is in, for a given timeframe. Timestamps are given in ISO 8601 format.

The result will be a list of rewards between `min_time` and `max_time` both given in UTC. Both default to "now" which means that at least one of the two parameters is required.

**Note:** this method supports generator return type.

```python
roles = validator.rewards()
```

Optionally, you can pass the following arguments to the `rewards()` method:

- `min_time` (str): date format of "YYYY-mm-dd", lower time bound (inclusive)
- `max_time` (str): date format of "YYYY-mm-dd", upper time bound (exclusive)
- `gen` (bool): defaults to `False`, set to `True` if you want the response to be a generator

## Get rewards totals for a validator

Returns the total rewards earned for a given validator over a given time range. Timestamps are given in ISO 8601 format. The results can also be bucketed in time by specifying a `bucket` query parameter which buckets information per bucket in the given timeframe. Valid bucket values include `hour`, `day` and `week`).

```python
roles = validator.rewards_sum()
```

Optionally, you can pass the following arguments to the `rewards_sum()` method:

- `min_time` (str): date format of "YYYY-mm-dd", lower time bound (inclusive)
- `max_time` (str): date format of "YYYY-mm-dd", upper time bound (exclusive)
- `bucket` (str): defaults to `None`. If bucketing is desired, valid values are `hour`, `day` and `week`

# The Hotspot module

## Introduction

This module sets up a `Hotspot` object to make requests on behalf of a given Helium hotspot address. This allows you to interact with/get data about your hotspot in a Pythonic way. The methods on this module, their naming, and their responses align with the [official Helium Hotspots API](https://docs.helium.com/api/blockchain/hotspots).

To import it into your file:

```python
from hntpy import Hotspot
```

## Instantiating the Hotspot object

To instantiate a Hotspot instance:

```python
from hntpy import Hotspot

# pass your 51-character Helium hotspot address
hotspot = Hotspot("your-helium-hotspot-addr-here")

# your hotspot address will be stored/accessible here
addr = hotspot.address
```

To retrieve the hotspot details:

```python
details = hotspot.get_details()
```

The `details` variable is now a python `dict` containing a `dict` of the hotspot details, as returned from the Helium API.

## Get roles (activity) for a hotspot

Lists all blockchain transactions that the given Hotspot was involved in.

**Note:** this method supports generator return type.

```python
roles = hotspot.roles()
```

Optionally, you can pass the following arguments to the `roles()` method:

- `filter_types` (str): Comma separated list of transaction types (no whitespace). For example "payment_v1,token_burn_v1"
- `min_time` (str): date format of "YYYY-mm-dd", lower time bound (inclusive)
- `max_time` (str): date format of "YYYY-mm-dd", upper time bound (exclusive)
- `limit` (int): maximum number of items to return
- `gen` (bool): defaults to `False`, set to `True` if you want the response to be a generator

## Get role counts for a hotspot

Count transactions that indicate the hotspot as a participant.

The results are a map keyed by the given `filter_types` and the count of transaction of that type.

```python
role_counts = hotspot.role_counts()
```

Optionally you can pass the following argument to the `role_counts()` method:

- `filter_types` (str): Comma separated list of transaction types (no whitespace). For example "payment_v1,token_burn_v1"

## Get rewards for a hotspot

Returns rewards for a given hotspot per reward block the hotspot is in, for a given timeframe. Timestamps are given in ISO 8601 format.

The result will be a list of rewards between `min_time` and `max_time` both given in UTC. Both default to "now" which means that at least one of the two parameters is required.

**Note:** this method supports generator return type.

```python
roles = hotspot.rewards()
```

Optionally, you can pass the following arguments to the `rewards()` method:

- `min_time` (str): date format of "YYYY-mm-dd", lower time bound (inclusive)
- `max_time` (str): date format of "YYYY-mm-dd", upper time bound (exclusive)
- `gen` (bool): defaults to `False`, set to `True` if you want the response to be a generator

## Get rewards totals for a hotspot

Returns the total rewards earned for a given hotspot over a given time range. Timestamps are given in ISO 8601 format. The results can also be bucketed in time by specifying a `bucket` query parameter which buckets information per bucket in the given timeframe. Valid bucket values include `hour`, `day` and `week`).

```python
roles = hotspot.rewards_sum()
```

Optionally, you can pass the following arguments to the `rewards_sum()` method:

- `min_time` (str): date format of "YYYY-mm-dd", lower time bound (inclusive)
- `max_time` (str): date format of "YYYY-mm-dd", upper time bound (exclusive)
- `bucket` (str): defaults to `None`. If bucketing is desired, valid values are `hour`, `day` and `week`

## Get challenges for a hotspot

Lists the challenge (receipts) that the given hotspot was a challenger, challengee or witness in.

**Note:** this method supports generator return type.

```python
roles = hotspot.challenges()
```

Optionally, you can pass the following arguments to the `challenges()` method:

- `min_time` (str): date format of "YYYY-mm-dd", lower time bound (inclusive)
- `max_time` (str): date format of "YYYY-mm-dd", upper time bound (exclusive)
- `limit` (int): maximum number of items to return
- `gen` (bool): defaults to `False`, set to `True` if you want the response to be a generator

## Get elections for a hotspot

Lists the consensus group transactions that the given hotspot was involved in.

**Note:** this method supports generator return type.

```python
roles = hotspot.elections()
```

Optionally, you can pass the following arguments to the `elections()` method:

- `min_time` (str): date format of "YYYY-mm-dd", lower time bound (inclusive)
- `max_time` (str): date format of "YYYY-mm-dd", upper time bound (exclusive)
- `limit` (int): maximum number of items to return
- `gen` (bool): defaults to `False`, set to `True` if you want the response to be a generator

## Get witnesses for a hotspot

Retrieves the list of witnesses for a given hotspot over about the last 5 days of blocks.

```python
witnesses = hotspot.witnesses()
```

## Get witnessed for a hotspot

Retrieves the list of hotspots the given hotspot witnessed over the last 5 days.

```python
witnessed = hotspot.witnessed()
```

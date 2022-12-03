# Retrieving Helium network data

## Contents

- [0. Introduction](#0-introduction)
- [1. Stats](#1-stats)
- [2. Oracle prices](#2-oracle-prices)

## 0. Introduction

This page covers the functions within the `hntpy` package that can be used to accessed data about the Helium blockchain/network, and it's associated resources.

To retrieve detailed information about a specific account, hotspot, or validator, see their respective module documentation pages.

For all examples below, we will assume the `hntpy` module has been imported, using:

```python
import hntpy
```

<hr>

## 1. Stats

### Blockchain stats

Retrieve basic stats for the blockchain such as total token supply, and average block and election times over a number of intervals.

```python
stats = hntpy.get_blockchain_stats()
```

### Token supply

Returns the circulating token supply in either JSON or raw form.

```
supply = hntpy.get_token_supply()
```

Optionally, you can pass the following argument to specify return type:

- `format` (str): either "JSON" or "raw" (for a raw number). Defaults to JSON.

<hr>

## 2. Oracle prices

### Current Oracle price

The current Oracle Price and at which block it took effect.

```python
data = hntpy.current_oracle_price()
```

### Current and historic Oracle prices

Retrieve list of the current and historical Oracle Prices and at which block they took effect.

**Note:** this method supports generator return type.

```python
data = hntpy.list_oracle_prices()
```

Optionally, you can pass the following arguments:

- `max_block` (int): Last block number to include in the results.
- `gen` (bool): defaults to `False`, set to `True` if you want the response to be a generator.

### Oracle price stats

Gets statistics on Oracle prices.

```python
data = hntpy.oracle_price_stats(min_time="2022-06-01", max_time="2022-07-01")
```

Where `min_time` and `max_time` are both required.

- `min_time` (str): date format of "YYYY-mm-dd", lower time bound (inclusive)
- `max_time` (str): date format of "YYYY-mm-dd", upper time bound (exclusive)

### Oracle price at specific block

Provides the Oracle price at a specific block and at which block it initially took effect.

```python
data = hntpy.oracle_price_at_block(block_num=471570)
```

Where `block_num` is a required argument.

### List Oracle activity

List Oracle price report transactions for all Oracle keys.

```python
data = hntpy.list_oracle_activity()
```

Optionally, you can pass the following arguments:

- `min_time` (str): date format of "YYYY-mm-dd", lower time bound (inclusive)
- `max_time` (str): date format of "YYYY-mm-dd", upper time bound (exclusive)
- `limit` (int): maximum number of items to return
- `gen` (bool): defaults to `False`, set to `True` if you want the response to be a generator

### Get predicted HNT Oracle prices

This returns a list of expected times when the Oracle Price is expected to change.

```python
data = hntpy.predict_oracle_price()
```

# Retrieving Helium network data

## Contents

- [0. Introduction](#0-introduction)
- [1. Stats](#1-stats)

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

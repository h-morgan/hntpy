# hntpy

<p align="left">
    <a alt="Version" href="https://pypi.org/project/hntpy/">
    <img src="https://img.shields.io/badge/version-0.0.8-blue"/></a>
    <a href="https://github.com/h-morgan/hntpy/blob/main/LICENSE" alt="License">
    <img src="https://img.shields.io/github/license/h-morgan/hntpy"/></a>
    <a href="#">
    <img src="https://img.shields.io/badge/coverage-99%25-green"/></a>
</p>

## Introduction

hntpy is a Python wrapper for Helium API to simplify requests and interaction with Helium blockchain. The aim of this project is to enable retrieval of Helium data from the API in a Pythonic way.

For comprehensive documentation (with examples), review the full usage [docs](https://github.com/h-morgan/hntpy/tree/main/docs).

For more detail on exact API responses/data, please see the officical [Helium documentation](https://docs.helium.com/api/blockchain/introduction).

This project is continually under development. If you notice a bug, or have a feature request, please submit a Github issue [here](https://github.com/h-morgan/hntpy/issues).

## Install

To use the latest version of this Python package, download from PyPi:

```
pip install hntpy
```

## Example Usage

Below are a couple of examples to show how the `hntpy` package can be used. For comprehensive documentation, including all function definitions, argument examples, and more, view the [full docs](https://github.com/h-morgan/hntpy/tree/main/docs).

```python
from hntpy import Account, Hotspot, Validator

# ===================================

## sample account functionality
account = Account(address="51-character-account-address")

# get validators and hotspots associated with an account
validators = account.validators()
hotspots = account.hotspots()

# get a generator of rewards, in a given timewindow, for an account (optionally can also return a list)
rewards_generator = account.rewards(min_time="2022-01-01", max_time="2022-06-01", gen=True)

for batch in rewards_generator:
    for reward in batch:
        # do some processing with the reward here...

# ===================================

## sample hotspot functionality

hotspot = Hotspot(address="51-character-hotspot-address")

# get roles (activity) for a hotspot, can optionally provide timeframe and response limit
roles = hotspot.roles(min_time="2022-01-01", limit=100)

# get the total reward sum for the hotspot, optionally in a given timeframe
rewards = hotspot.rewards(min_time="2022-01-01", max_time="2022-06-01")

# get hotspots that the given hotspot witnessed over the last 5 days
witnessed = hotspot.witnessed()

# ===================================

## sample validator functionality

validator = Validator(address="51-character-validator-address")

# get roles (activity) for a hotspot, can optionally provide timeframe and response limit
roles = validator.roles(limit=200)

```

## Return types

The Helium API returns either JSON objects (loaded as `dicts`) of data, or `lists` of data. All of the functions in the `hntpy` package that make requests to the Helium API return either:

- `list`
- `dict`
- `GeneratorType`

For requests that have the potential to return large amounts of data, there is the option to provide a `gen=True` argument to the method, which will yield the data in batches (rather than compile and return one single large list). By default, `gen` parameter is set to `False` for all methods.

To see available return types for specific methods, see method definitions in the respective module's documentation page.

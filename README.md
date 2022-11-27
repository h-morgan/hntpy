# hntpy

<p align="left">
    <a alt="Version" href="https://pypi.org/project/hntpy/">
    <img src="https://img.shields.io/badge/version-0.0.7-blue"/></a>
    <a href="https://github.com/h-morgan/hntpy/blob/main/LICENSE" alt="License">
    <img src="https://img.shields.io/github/license/h-morgan/hntpy"/></a>
    <a href="#">
    <img src="https://img.shields.io/badge/coverage-99%25-green"/></a>
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

These are just a couple of examples to show how the `hntpy` package can be used. For comprehensive documentation, including all function definitions, argument examples, and more, view the [Github docs](https://github.com/h-morgan/hntpy/tree/main/docs).

```python
from hntpy import Account, Hotspot

# account functions

account = Account(address="51-character-account-address")

validators = account.validators()
hotspots = account.hotspots()

rewards_generator = account.rewards(min_time="2022-01-01", max_time="2022-06-01", gen=True)

for batch in rewards_generator:
    for reward in batch:
        # do some processing with the reward here...


# hotspot functions

hotspot = Hotspot(address="51-character-hotspot-address")

roles = hotspot.roles(min_time="2022-01-01", limit=100)

witnessed = hotspot.witnessed()
```

## Return types

The Helium API returns either JSON objects (loaded as `dicts`) of data, or `lists` of data. All of the functions in the `hntpy` package that make requests to the Helium API return either:

- `list`
- `dict`
- `GeneratorType`

For requests that have the potential to return large amounts of data, there is the option to provide a `gen=True` argument to the method, which will yield the data in batches (rather than compile and return one single large list). By default, `gen` parameter is set to `False` for all methods.

To see available return types for specific methods, see method definitions in the respective module's documentation page.

# hntpy Documentation

This is the documentation and usage instructions for the `hntpy` Python package. If you need to install it or view package information, head over to the official package page on [PyPI](https://pypi.org/project/hntpy/#description).

## Introduction

`hntpy` is a Python package created to enable easy interaction with the Helium API. For further information about the Helium API, including information about requests and responses, view their [API documentation](https://docs.helium.com/api/blockchain/introduction).

To use this module, you need to import it in full, or it's part you intend to use into your Python file. So far, we have the following modules that can be imported/used to make requests:

- `Account`
- `Hotspot`

To import this whole package, add this to the top of your Python file:

```python
import hntpy
```

## Module Documentation

For specific information and more comprehensive examples of using these modules, see their respective documentation pages:

- [Account module docs](https://github.com/h-morgan/hntpy/blob/main/docs/account.md)
- [Hotspot module docs](https://github.com/h-morgan/hntpy/blob/main/docs/hotspot.md)

## Return types

The Helium API returns either JSON objects (loaded as `dicts`) of data, or `lists` of data. All of the functions in the `hntpy` package that make requests to the Helium API return either:

- `list`
- `dict`
- `GeneratorType`

For requests that have the potential to return large amounts of data, there is the option to provide a `gen=True` argument to the method, which will yield the data in batches (rather than compile and return one single large list). By default, `gen` parameter is set to `False` for all methods.

To see available return types for specific methods, see method definitions in the respective module's documentation page.

## Blockchain data note

Depending on the amount of data these requests have to return, you may need to wait a bit while the requests complete. In instances where there are many pages of data being returned from the Helium API, these requests can sometimes take minutes if a generator is not used.

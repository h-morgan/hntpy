import os
from loguru import logger
import requests
from requests import adapters
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from urllib.parse import urljoin


class HeliumClient:
    """
    Base client that sets up connection to Helium API
    """

    service_name = "HELIUM API"

    # Helium API updates as of 11/2021 require passing User-Agent param in header in requests - mocking a browser here
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"  # This is another valid field
    }

    def __init__(self, api_url: str = "https://api.helium.io/v1/"):
        self.api_url = api_url or os.getenv("HELIUM_API_URL")

        # setup request session
        session = requests.Session()
        retry = Retry(
            total=25, backoff_factor=1, status_forcelist=(500, 502, 503, 504, 429)
        )
        retry.BACKOFF_MAX = 420
        adapter = HTTPAdapter(max_retries=retry)
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        self._session = session

        # keep these stored in case we want to perform requesuts using them no matter what instance
        self.URL_ACCOUNTS_BASE = urljoin(self.api_url, "accounts")
        self.URL_HOTSPOTS_BASE = urljoin(self.api_url, "hotspots")
        self.URL_ORACLE_BASE = urljoin(self.api_url, "oracle/prices")
        self.URL_VALIDATORS_BASE = urljoin(self.api_url, "validators")

    def get_data(self, endpoint, params: dict = {}) -> dict:

        next_cursor = None
        data = []
        while True:

            url = self.api_url + f"{endpoint}"

            if next_cursor:
                params["cursor"] = next_cursor

            # make request, raise exceptions if they come up
            logger.debug(f"[{self.service_name}] accounts request URL: {url}")
            logger.debug(f"[{self.service_name}] accounts request params: {params}")
            resp = self._session.get(url, headers=self.HEADERS, params=params)
            resp.raise_for_status()

            logger.debug(
                f"[{self.service_name}] response status code: {resp.status_code}"
            )

            # opt to return just the data from the response, where possible
            try:
                resp_data = resp.json()["data"]
            # in the case where the response is not a JSON body, just return the text
            except TypeError:
                resp_data = resp.text

            # do some stuff to log number of items in response
            if isinstance(resp_data, list):
                num_items = len(resp_data)
            else:
                num_items = 1
            logger.debug(
                f"[{self.service_name}] retrieved {num_items} results from API"
            )

            if isinstance(resp_data, list):
                data.extend(resp_data)

                if "cursor" in resp.json():
                    next_cursor = resp.json()["cursor"]
                    logger.debug(
                        f"[{self.service_name}] Next page cursor: {next_cursor}"
                    )
                else:
                    break

            # if we got a dict back, there is no cursor (paginated data returned in lists)
            else:
                return resp_data

        return data

    def gen_data(self, endpoint, params: dict = {}) -> dict:

        next_cursor = None
        while True:

            url = self.api_url + f"{endpoint}"

            if next_cursor:
                params["cursor"] = next_cursor

            # make request, raise exceptions if they come up
            logger.debug(f"[{self.service_name}] accounts request URL: {url}")
            logger.debug(f"[{self.service_name}] accounts request params: {params}")
            resp = self._session.get(url, headers=self.HEADERS, params=params)
            resp.raise_for_status()

            logger.debug(
                f"[{self.service_name}] response status code: {resp.status_code}"
            )

            # opt to return just the data from the response, where possible
            resp_data = resp.json()["data"]
            logger.debug(
                f"[{self.service_name}] retrieved {len(resp_data)} results from API"
            )

            yield resp_data

            # update cursor for next page of results
            if "cursor" in resp.json():
                next_cursor = resp.json()["cursor"]
                logger.debug(f"[{self.service_name}] Next page cursor: {next_cursor}")
            else:
                break

import os
from loguru import logger
import requests
from requests import adapters
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from urllib.parse import urljoin


class HeliumClient:
    """
    Client that sets up connection to Helium API
    """

    service_name = "HELIUM API"

    # Helium API updates as of 11/2021 require passing User-Agent param in header in requests - mocking a browser here
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"  # This is another valid field
    }

    def __init__(self, base_url: str = "https://api.helium.io/v1/"):
        self.base_url = base_url or os.getenv("HELIUM_API_URL")

        session = requests.Session()
        retry = Retry(
            total=25, backoff_factor=1, status_forcelist=(500, 502, 503, 504, 429)
        )
        retry.BACKOFF_MAX = 420
        adapter = HTTPAdapter(max_retries=retry)
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        self._session = session

        self.URL_ACCOUNTS_BASE = urljoin(self.base_url, "accounts")
        self.URL_HOTSPOTS_BASE = urljoin(self.base_url, "hotspots")
        self.URL_ORACLE_BASE = urljoin(self.base_url, "oracle/prices")
        self.URL_VALIDATORS_BASE = urljoin(self.base_url, "validators")

    def get_accounts(self, url_suffix: str) -> dict:

        url = self.base_url + f"/{url_suffix}"

        # make request, raise exceptions if they come up
        resp = self._session.get(url, headers=self.HEADERS)
        logger.debug(f"[{self.service_name}] accounts request URL: {url}")
        resp.raise_for_status()

        logger.debug(f"[{self.service_name}] response status code: {resp.status_code}")

        return resp.json()

    def get_account_data(
        self, wallet_id: str, suffix: str = None, params: dict = {}
    ) -> dict:

        next_cursor = None
        data = []
        while True:

            url = self.URL_ACCOUNTS_BASE + f"/{wallet_id}"

            if suffix:
                url = url + f"/{suffix}"

            if next_cursor:
                url = "?".join([url, f"cursor={next_cursor}"])

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

    def get_account_gen(
        self, wallet_id: str, suffix: str = None, params: dict = {}
    ) -> dict:

        next_cursor = None
        while True:

            url = self.URL_ACCOUNTS_BASE + f"/{wallet_id}"

            if suffix:
                url = url + f"/{suffix}"

            if next_cursor:
                url = "?".join([url, f"cursor={next_cursor}"])

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

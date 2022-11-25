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

    service_name = 'HELIUM API'

    # Helium API updates as of 11/2021 require passing User-Agent param in header in requests - mocking a browser here
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'# This is another valid field
    }

    def __init__(self, base_url="https://api.helium.io/v1/"):
        self.base_url = base_url or os.getenv("HELIUM_API_URL")

        session = requests.Session()
        retry = Retry(total=25, backoff_factor=1, status_forcelist=(500, 502, 503, 504, 429))
        retry.BACKOFF_MAX = 420
        adapter = HTTPAdapter(max_retries=retry)
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        self._session = session

        self.URL_ACCOUNTS_BASE = urljoin(self.base_url, "accounts")
        self.URL_HOTSPOTS_BASE = urljoin(self.base_url, "hotspots")
        self.URL_ORACLE_BASE = urljoin(self.base_url, "oracle/prices")
        self.URL_VALIDATORS_BASE = urljoin(self.base_url, "validators")

    def get_accounts(self, url_suffix, params=None):
        
        url = self.base_url + f'/{url_suffix}'

        # make request, raise exceptions if they come up
        resp = self._session.get(url, headers=self.HEADERS)
        logger.debug(f"[{self.service_name}] accounts URL: {url}")
        resp.raise_for_status()

        logger.debug(f"[{self.service_name}] response status code: {resp.status_code}")
        
        return resp.json()

    def get_wallet(self, wallet_id, params=None):
        
        url = self.URL_ACCOUNTS_BASE + f'/{wallet_id}'

        # make request, raise exceptions if they come up
        resp = self._session.get(url, headers=self.HEADERS)
        logger.debug(f"[{self.service_name}] wallets URL: {url}")
        resp.raise_for_status()

        logger.debug(f"[{self.service_name}] response status code: {resp.status_code}")

        return resp.json()




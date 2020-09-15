#!/usr/bin/env python3

import backoff
import requests
from requests.exceptions import RequestException
from os import environ
from .data_sourcing import DataSourcing
from typing import List,Dict

BACKEND_HOST = environ.get('BACKEND_HOST')
BACKEND_PORT = environ.get('BACKEND_PORT')
API_SECRET = environ.get('API_SECRET')

class APIDataSource(DataSourcing):

    def fetch_raw_app_size(self) -> List[Dict]:
        return self.__fetch_ipa_size()

    def fetch_code_metrics(self) -> List[Dict]:
        return self.__fetch_code_metrics()

    # Private

    @backoff.on_exception(backoff.expo, RequestException, max_tries=5)
    def __fetch_ipa_size(self) -> List[Dict]:
        ipa_size_url = f'{self.__base_url()}/app_size'
        r = requests.request(
            method='GET',
            url=ipa_size_url,
            headers=self.__headers()
        )
        return r.json()

    @backoff.on_exception(backoff.expo, RequestException, max_tries=5)
    def __fetch_code_metrics(self) -> List[Dict]:
        code_metrics_url = f'{self.__base_url()}/code_metrics'
        r = requests.request(
            method='GET',
            url=code_metrics_url,
            headers=self.__headers()
        )
        return r.json()

    def __base_url(self) -> str:
        return f'{BACKEND_HOST}:{BACKEND_PORT}/api'

    def __headers(self) -> dict:
        return {'Accept': 'application/json', 'X-API-Token': API_SECRET}
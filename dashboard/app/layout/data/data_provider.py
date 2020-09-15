#!/usr/bin/env python3

from .data_sourcing import DataSourcing
import pandas as pd
from .models import IPASize
from collections import namedtuple
from typing import List

RepresentableKey = namedtuple('RepresentableKey', 'key description')
RepresentableData = namedtuple('RepresentableData', 'data labels')
AppSizeRepresentableData = namedtuple('AppSizeRepresentableData', 'uncompressed_size download_size')

class DataConstants(object):

    @staticmethod
    def app_name() -> RepresentableKey:
        return RepresentableKey('app_name', 'App name')

    @staticmethod
    def size_type() -> RepresentableKey:
        return RepresentableKey('size_type', 'Kind of size')    

    @staticmethod
    def size_in_mb() -> RepresentableKey:
        return RepresentableKey('size_in_mb', 'Size in MB')

    @staticmethod
    def date() -> RepresentableKey:
        return RepresentableKey('date', 'Sampling date')


class DataProvider(object):
    def __init__(self, data_source: DataSourcing):
        self.data_source = data_source

    def fetch_ipa_size(self) -> AppSizeRepresentableData:
        raw_ipa_sizes = self.data_source.fetch_raw_app_size()
        ipa_sizes = [IPASize(** i) for i in raw_ipa_sizes]

        install_data = [i.uncompressed_size_data for i in ipa_sizes]
        download_data = [i.download_size_data for i in ipa_sizes]

        return (self.__size_data(install_data), self.__size_data(download_data))

    def __size_data(self, data: List[List[str]]) -> RepresentableData:
        representable_keys = [
            DataConstants.app_name(), 
            DataConstants.date(), 
            DataConstants.size_in_mb()
        ]
        return RepresentableData(
            pd.DataFrame(data, columns=[r.key for r in representable_keys]),
            { rk.key : rk.description for rk in representable_keys }
        )

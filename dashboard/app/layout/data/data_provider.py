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
        return (self.__uncompressed_size_data(ipa_sizes), self.__uncompressed_size_data(ipa_sizes))

    # Transforming raw data into representable DataFrame

    def __uncompressed_size_data(self, ipa_sizes: List[IPASize]) -> RepresentableData:
        representable_keys = [
            DataConstants.app_name(), 
            DataConstants.date(), 
            DataConstants.size_in_mb()
        ]
        data = [i.uncompressed_size_data for i in ipa_sizes]
        return RepresentableData(
            pd.DataFrame(data, columns=[r.key for r in representable_keys]),
            { rk.key : rk.description for rk in representable_keys }
        )

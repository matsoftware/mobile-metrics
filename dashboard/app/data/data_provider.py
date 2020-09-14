#!/usr/bin/env python3

from .data_sourcing import DataSourcing
import pandas as pd
from .models import IPASize
from collections import namedtuple

RepresentableKey = namedtuple('RepresentableKey', 'key description')
RepresentableData = namedtuple('RepresentableData', 'data labels')

class DataConstants(object):

    @staticmethod
    def size_types() -> RepresentableKey:
        return RepresentableKey('size_types', 'Kind of size')

    @staticmethod
    def size_in_mb() -> RepresentableKey:
        return RepresentableKey('size_in_mb', 'Size in MB')

    @staticmethod
    def date() -> RepresentableKey:
        return RepresentableKey('date', 'Sampling date')


class DataProvider(object):
    def __init__(self, data_source: DataSourcing):
        self.data_source = data_source

    def fetch_ipa_size(self, name: str = '') -> RepresentableData:
        raw_ipa_size = self.data_source.fetch_raw_app_size(name=name)
        data = [size for subsize in [IPASize(** i).as_data for i in raw_ipa_size] for size in subsize]
        representable_keys = [DataConstants.size_types(), DataConstants.date(), DataConstants.size_in_mb()]
        return RepresentableData(
            pd.DataFrame(data, columns=[r.key for r in representable_keys]),
            { rk.key : rk.description for rk in representable_keys }
        )

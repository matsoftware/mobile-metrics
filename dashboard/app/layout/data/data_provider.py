#!/usr/bin/env python3

from .data_sourcing import DataSourcing
import pandas as pd
from .models import IPASize, SourceCodeMetric
from .config import Config
from collections import namedtuple
from .data_constants import DataConstants, RepresentableKey
from typing import List

RepresentableData = namedtuple('RepresentableData', 'data labels')
AppSizeRepresentableData = namedtuple('AppSizeRepresentableData', 'uncompressed_size download_size')
CodeMetricsRepresentableData = namedtuple('CodeMetricsRepresentableData', 'loc dependencies')

class DataProvider(object):
    def __init__(self, data_source: DataSourcing, config: Config):
        self.data_source = data_source
        self.config = config

    # App Size

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
        return self.__make_representable_data(data, representable_keys)

    # Code metrics
    def fetch_code_metrics(self) -> CodeMetricsRepresentableData:
        raw_metrics_sizes = self.data_source.fetch_code_metrics()
        metrics_sizes = [SourceCodeMetric(** s) for s in raw_metrics_sizes]

        loc_data = [s.loc_data for s in metrics_sizes]
        deps_data = [s.deps_data for s in metrics_sizes]

        return (self.__loc_data(loc_data), self.__deps_data(deps_data))

    def __loc_data(self, data: List[List[str]]) -> RepresentableData:
        representable_keys = [
            DataConstants.app_name(), 
            DataConstants.date(), 
            DataConstants.deps_test_loc(),
            DataConstants.deps_prod_loc(),
            DataConstants.repo_test_loc(),
            DataConstants.repo_prod_loc(),
            DataConstants.repo_dupl_loc()
        ]
        transformed_data = {r.key: [row[ind] for row in data] for ind, r in enumerate(representable_keys)}
        return self.__make_representable_data(transformed_data, representable_keys, True)

    def __deps_data(self, data: List[List[str]]) -> RepresentableData:
        representable_keys = [
            DataConstants.app_name(), 
            DataConstants.date(), 
            DataConstants.internal_deps(),
            DataConstants.external_deps()
        ]
        return self.__make_representable_data(data, representable_keys)

    # Private
    def __make_representable_data(self, data, repr_keys: List[RepresentableKey], pass_raw_data: bool = False) -> RepresentableData:
        return RepresentableData(
            data if pass_raw_data else pd.DataFrame(data, columns=[r.key for r in repr_keys]),
            { rk.key : rk.description.replace(DataConstants.repo_placeholder(), self.config.repo_name) for rk in repr_keys }
        )
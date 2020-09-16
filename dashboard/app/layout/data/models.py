#!/usr/bin/env python3
from dateutil.parser import parse

class TimeSeriesModel(object):
    def __init__(self, metadata: str, createdAt: str, updatedAt: str):
        self.metadata = metadata        
        self.createdAt = parse(createdAt) 
        self.updatedAt = parse(updatedAt)

    @staticmethod
    def created_key() -> str:
        return "createdAt"

    def base_reporting_data(self) -> list:
        return [self.name, self.createdAt]


class IPASize(TimeSeriesModel):

    def __init__(self, id: int, name: float, total_uncompressed_size: float, total_universal_size: str, metadata: str, createdAt: str, updatedAt: str):
        TimeSeriesModel.__init__(self, metadata, createdAt, updatedAt)
        self.id = id
        self.name = name
        self.total_uncompressed_size = total_uncompressed_size
        self.total_universal_size = total_universal_size

    @property
    def uncompressed_size_data(self) -> list:
        return self.base_reporting_data() + [ self.total_uncompressed_size ]

    @property
    def download_size_data(self) -> list:
        return self.base_reporting_data() + [ self.total_universal_size ]


class SourceCodeMetric(TimeSeriesModel):

    def __init__(self, 
        id: int, 
        name: float, 
        deps_test_loc: int, 
        deps_prod_loc: int, 
        repo_test_loc: int, 
        repo_prod_loc: int, 
        repo_dupl_loc: int,
        internal_deps: int,
        external_deps: int,
        metadata: str, 
        createdAt: str, 
        updatedAt: str
    ):
        TimeSeriesModel.__init__(self, metadata, createdAt, updatedAt)
        self.id = id
        self.name = name
        self.deps_test_loc = deps_test_loc
        self.deps_prod_loc = deps_prod_loc 
        self.repo_test_loc = repo_test_loc 
        self.repo_prod_loc = repo_prod_loc
        self.repo_dupl_loc = repo_dupl_loc
        self.internal_deps = internal_deps
        self.external_deps = external_deps

    @property
    def loc_data(self) -> list:
        return self.base_reporting_data() + [n/1000 for n in [ self.deps_test_loc, self.deps_prod_loc, self.repo_test_loc, self.repo_prod_loc, self.repo_dupl_loc]]

    @property
    def deps_data(self) -> list:
        return self.base_reporting_data() + [ self.internal_deps, self.external_deps ]
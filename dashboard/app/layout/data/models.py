#!/usr/bin/env python3
from dateutil.parser import parse

class SequelizeModel(object):
    def __init__(self, createdAt: str, updatedAt: str):
        self.createdAt = parse(createdAt) 
        self.updatedAt = parse(updatedAt)

    @staticmethod
    def created_key() -> str:
        return "createdAt"

class IPASize(SequelizeModel):

    def __init__(self, id: int, name: float, total_uncompressed_size: float, total_universal_size: str, metadata: str, createdAt: str, updatedAt: str):
        SequelizeModel.__init__(self, createdAt, updatedAt)
        self.id = id
        self.name = name
        self.total_uncompressed_size = total_uncompressed_size
        self.total_universal_size = total_universal_size
        self.metadata = metadata        

    @property
    def uncompressed_size_data(self) -> list:
        return [self.name, self.createdAt, self.total_uncompressed_size ]

    @property
    def download_size_data(self) -> list:
        return [self.name, self.createdAt, self.total_universal_size ]

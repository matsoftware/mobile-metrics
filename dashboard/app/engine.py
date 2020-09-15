#!/usr/bin/env python3

from .layout.layout import Layout
from .layout.data.api_data_source import APIDataSource
from .layout.data.data_provider import DataProvider
from .layout.header_layout_provider import HeaderLayoutProvider
from .layout.app_size_layout_provider import AppSizesLayoutProvider

class Engine(object):
    def  __init__(self):
        self.data_provider = DataProvider(data_source=APIDataSource())

    def create_metrics_layout(self) -> Layout:
        return Layout(layouts=[
            HeaderLayoutProvider(),
            AppSizesLayoutProvider(data_provider=self.data_provider)
        ])
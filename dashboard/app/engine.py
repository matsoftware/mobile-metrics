#!/usr/bin/env python3

from .layout.data.config import load 
from .layout.layout import Layout
from .layout.data.api_data_source import APIDataSource
from .layout.data.data_provider import DataProvider
from .layout.header_layout_provider import HeaderLayoutProvider
from .layout.app_size_layout_provider import AppSizesLayoutProvider
from .layout.code_metrics_layout_provider import CodeMetricsLayoutProvider

class Engine(object):
    def  __init__(self):
        self.config = load()
        self.data_provider = DataProvider(data_source=APIDataSource(), config=self.config)

    def create_metrics_layout(self) -> Layout:
        return Layout(layouts=[
            HeaderLayoutProvider(),
            AppSizesLayoutProvider(data_provider=self.data_provider, config=self.config),
            CodeMetricsLayoutProvider(data_provider=self.data_provider, config=self.config)
        ])
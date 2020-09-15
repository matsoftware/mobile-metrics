#!/usr/bin/env python3

import dash_core_components as dcc
import dash_html_components as html
from .layout_providing import LayoutProviding
from .data.data_provider import DataConstants, DataProvider, AppSizeRepresentableData, RepresentableData
import plotly.express as px

class AppSizesLayoutProvider(LayoutProviding):

    def __init__(self, data_provider: DataProvider):
        self.data_provider = data_provider

    def create_components(self) -> list:
        uncompressed_size_data, download_size_data = self.data_provider.fetch_ipa_size()
        return [
            html.H2(
                children='App sizes breakdown'
            ),
            dcc.Graph(
                id='APP-DOWNLOAD-SIZE',
                figure=self.__download_size_figure(download_size_data)
            )
        ]

    def __download_size_figure(self, rep_data: RepresentableData) -> px.line:
        return px.line(rep_data.data,
            x=DataConstants.date().key,
            y=DataConstants.size_in_mb().key,
            color=DataConstants.app_name().key,
            title='App Download Size trend',
            labels=rep_data.labels
        )

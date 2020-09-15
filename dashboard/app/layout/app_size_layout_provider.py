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
                figure=self.__app_size_figure(title='App Download Size trend', rep_data=download_size_data)
            ),
            dcc.Graph(
                id='APP-INSTALL-SIZE',
                figure=self.__app_size_figure(title='App Install Size trend', rep_data=uncompressed_size_data)
            ),
        ]

    def __app_size_figure(self, title: str, rep_data: RepresentableData) -> px.line:
        return px.line(rep_data.data,
            x=DataConstants.date().key,
            y=DataConstants.size_in_mb().key,
            color=DataConstants.app_name().key,
            title=title,
            labels=rep_data.labels
        )
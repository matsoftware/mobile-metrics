#!/usr/bin/env python3

import dash_core_components as dcc
import dash_html_components as html
from .layout_providing import LayoutProviding
from .data.config import Config
from .data.data_provider import DataProvider, AppSizeRepresentableData, RepresentableData
from .data.data_constants import DataConstants
import plotly.express as px

class AppSizesLayoutProvider(LayoutProviding):

    def __init__(self, data_provider: DataProvider, config: Config):
        self.data_provider = data_provider
        self.config = config

    def create_components(self) -> list:
        uncompressed_size_data, download_size_data = self.data_provider.fetch_ipa_size()
        should_render = self.config.render_metrics['app_size']['download_size_trend'] or self.config.render_metrics['app_size']['install_size_trend']
        if not should_render:
            return []
        return [
            html.H2(
                children='App sizes breakdown'
            )] + self.__download_size(download_size_data) + self.__app_install_size(uncompressed_size_data)

    def __download_size(self, rep_data: RepresentableData) -> list:
        if not self.config.render_metrics['app_size']['download_size_trend']:
            return []
        return [
            dcc.Graph(
                id='APP-DOWNLOAD-SIZE',
                figure=self.__app_size_figure(title='App Download Size trend', rep_data=rep_data)
            )
        ]

    def __app_install_size(self, rep_data: RepresentableData) -> list:
        if not self.config.render_metrics['app_size']['install_size_trend']:
            return []
        return [
            dcc.Graph(
                id='APP-INSTALL-SIZE',
                figure=self.__app_size_figure(title='App Install Size trend', rep_data=rep_data)
            )
        ]

    def __app_size_figure(self, title: str, rep_data: RepresentableData) -> px.line:
        return px.line(rep_data.data,
            x=DataConstants.date().key,
            y=DataConstants.size_in_mb().key,
            color=DataConstants.app_name().key,
            title=title,
            labels=rep_data.labels
        )
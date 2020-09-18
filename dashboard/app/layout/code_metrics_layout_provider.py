#!/usr/bin/env python3

import dash_core_components as dcc
import dash_html_components as html
from .data.config import Config
from .layout_providing import LayoutProviding
from .data.data_provider import DataProvider, RepresentableData
from .data.data_constants import DataConstants
from .data.config import Config
import plotly.graph_objects as go
from typing import List
import plotly.express as px

class CodeMetricsLayoutProvider(LayoutProviding):

    def __init__(self, data_provider: DataProvider, config: Config):
        self.data_provider = data_provider
        self.config = config

    def create_components(self) -> list:
        loc_data, deps_data = self.data_provider.fetch_code_metrics()
        should_render = self.config.render_metrics['code_metrics']['total_loc'] or self.config.render_metrics['code_metrics']['main_repo_loc'] or self.config.render_metrics['code_metrics']['n_of_dependencies']
        if not should_render:
            return []
        return [
            html.H2(
                children='Source Code Metrics'
            )] + self.__total_loc(loc_data=loc_data) + self.__repo_loc(loc_data=loc_data) + self.__deps(deps_data=deps_data)

    def __total_loc(self, loc_data: RepresentableData) -> list:
        if not self.config.render_metrics['code_metrics']['main_repo_loc']:
            return []
        return [
            dcc.Graph(
                id='TOTAL-LOC',
                figure=self.__total_loc_figure(title='Total LOC (Lines of Code) growth', rep_data=loc_data)
            )
        ]

    def __repo_loc(self, loc_data: RepresentableData) -> list:
        if not self.config.render_metrics['code_metrics']['total_loc']:
            return []
        return [
            dcc.Graph(
                id='REPO-LOC',
                figure=self.__main_repo_loc_figure(title=f'{self.config.repo_name} LOC (Lines of Code) growth', rep_data=loc_data)
            )
        ]

    def __deps(self, deps_data: RepresentableData) -> list:
        if not self.config.render_metrics['code_metrics']['n_of_dependencies']:
            return []
        return [
            dcc.Graph(
                id='DEPS',
                figure=self.__n_of_dependencies_figure(title='Number of dependencies over time', rep_data=deps_data)
            )
        ]

    def __total_loc_figure(self, title: str, rep_data: RepresentableData) -> go.Figure:
        data, legend = rep_data
        x = data[DataConstants.date().key]
        traces = [
            go.Scatter(
                x=x, 
                y=data[DataConstants.deps_test_loc().key],
                hoverinfo='x+y',
                mode='lines',
                name=legend[DataConstants.deps_test_loc().key],
                line_color='darkslateblue',
                stackgroup='one'
            ),
            go.Scatter(
                x=x, 
                y=data[DataConstants.deps_prod_loc().key],
                hoverinfo='x+y',
                mode='lines',
                name=legend[DataConstants.deps_prod_loc().key],
                line_color='darkblue',
                stackgroup='one'
            ),
            go.Scatter(
                x=x, 
                y=data[DataConstants.repo_test_loc().key],
                hoverinfo='x+y',
                mode='lines',
                name=legend[DataConstants.repo_test_loc().key],
                line_color='firebrick',
                stackgroup='one'
            ),
            go.Scatter(
                x=x, 
                y=data[DataConstants.repo_prod_loc().key],
                hoverinfo='x+y',
                mode='lines',
                name=legend[DataConstants.repo_prod_loc().key],
                line_color='red',
                stackgroup='one'
            )
        ]
        return self.__build_filled_area_chart(title=title, traces=traces, yaxis_title=DataConstants.kloc().description)

    def __main_repo_loc_figure(self, title: str, rep_data: RepresentableData) -> go.Figure:
        data, legend = rep_data
        x = data[DataConstants.date().key]
        traces = [
            go.Scatter(
                x=x, 
                y=data[DataConstants.repo_test_loc().key],
                hoverinfo='x+y',
                mode='lines',
                name=legend[DataConstants.repo_test_loc().key],
                line_color='firebrick',
                stackgroup='one'
            ),
            go.Scatter(
                x=x, 
                y=data[DataConstants.repo_prod_loc().key],
                hoverinfo='x+y',
                mode='lines',
                name=legend[DataConstants.repo_prod_loc().key],
                line_color='red',
                stackgroup='one'
            ),
            go.Scatter(
                x=x, 
                y=data[DataConstants.repo_dupl_loc().key],
                name=legend[DataConstants.repo_dupl_loc().key],
                line=dict(color='black', width=5, dash='dash')
            ),
        ]
        return self.__build_filled_area_chart(title=title, traces=traces, yaxis_title=DataConstants.kloc().description)

    def __n_of_dependencies_figure(self, title: str, rep_data: RepresentableData) -> px.line:
        data, legend = rep_data
        x = data[DataConstants.date().key]
        traces = [
            go.Scatter(
                x=x, 
                y=data[DataConstants.external_deps().key],
                hoverinfo='x+y',
                mode='lines',
                name=legend[DataConstants.external_deps().key],
                line_color='lightseagreen',
                stackgroup='one'
            ),
            go.Scatter(
                x=x, 
                y=data[DataConstants.internal_deps().key],
                hoverinfo='x+y',
                mode='lines',
                name=legend[DataConstants.internal_deps().key],
                line_color='lightsalmon',
                stackgroup='one'
            )
        ]
        return self.__build_filled_area_chart(title=title, traces=traces, yaxis_title=DataConstants.n_of_deps().description)


    def __build_filled_area_chart(self, title: str, traces: List[go.Scatter], yaxis_title: str) -> go.Figure:
        fig = go.Figure()
        for trace in traces:
            fig.add_trace(trace)

        fig.update_layout(
            title=title,
            xaxis_title=DataConstants.date().description,
            yaxis_title=yaxis_title
        )
        
        return fig
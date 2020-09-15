#!/usr/bin/env python3

import dash_core_components as dcc
import dash_html_components as html
from .layout_providing import LayoutProviding
from .data.data_provider import DataProvider, RepresentableData
from .data.data_constants import DataConstants
import plotly.graph_objects as go

class CodeMetricsLayoutProvider(LayoutProviding):

    def __init__(self, data_provider: DataProvider):
        self.data_provider = data_provider

    def create_components(self) -> list:
        loc_data, deps_data = self.data_provider.fetch_code_metrics()
        return [
            html.H2(
                children='Source Code Metrics'
            ),
            dcc.Graph(
                id='LOC',
                figure=self.__loc_figure(title='LOC (Lines of Code) growth', rep_data=loc_data)
            )
        ]

    def __loc_figure(self, title: str, rep_data: RepresentableData) -> go.Figure:
        data, legend = rep_data
        x = data[DataConstants.date().key]

        traces = [self.__create_trace(
            x=x,
            y=data[representable.key],
            name=legend[representable.key]
        ) for representable in [
            DataConstants.deps_test_loc(),
            DataConstants.deps_prod_loc(),
            DataConstants.repo_test_loc(),
            DataConstants.repo_prod_loc()
        ]]

        fig = go.Figure()
        for trace in traces:
            fig.add_trace(trace)

        fig.update_layout(
            title=title,
            xaxis_title=legend[DataConstants.date().key],
            yaxis_title=DataConstants.kloc().description
        )
        
        return fig

    def __create_trace(self, x, y, name, group: str = 'one') -> go.Scatter:
        return go.Scatter(
            x=x, 
            y=y,
            hoverinfo='x+y',
            mode='lines',
            name=name,
            stackgroup=group
        )
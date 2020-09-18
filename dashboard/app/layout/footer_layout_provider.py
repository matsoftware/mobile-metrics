#!/usr/bin/env python3

import dash_html_components as html
from .layout_providing import LayoutProviding
from .data.config import Config

class FooterLayoutProvider(LayoutProviding):

    def __init__(self, config: Config):
        self.config = config

    def create_components(self) -> list:
        return [
            html.Div(
                children=self.config.footer_text,
                style={
                    'textAlign': 'center',
                }), 
            html.Div(
                children=['Created with ', html.A('Mobile Metrics', href='<a href="https://github.com/matsoftware/mobile-metrics">Mobile Metrics</a>')],
                style={
                    'textAlign': 'center',
                })
        ]
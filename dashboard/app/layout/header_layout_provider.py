#!/usr/bin/env python3

import dash_html_components as html
from .layout_providing import LayoutProviding
from .data.config import Config

class HeaderLayoutProvider(LayoutProviding):

    def __init__(self, config: Config):
        self.config = config

    def create_components(self) -> list:
        return [
            html.H1(
                children=self.config.title,
                style={
                    'textAlign': 'center',
                }
            )
        ]
#!/usr/bin/env python3

import dash_html_components as html
from .layout_providing import LayoutProviding

class HeaderLayoutProvider(LayoutProviding):

    def create_components(self) -> list:
        return [
            html.H1(
                children='Mobile Metrics Dashboard',
                style={
                    'textAlign': 'center',
                }
            )
        ]
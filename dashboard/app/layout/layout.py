#!/usr/bin/env python3

import dash_html_components as html
from typing import List
from .layout_providing import LayoutProviding

class Layout(object):

    def __init__(self, layouts: List[LayoutProviding]):
        self.layouts = layouts

    def serve_layout(self):
        return html.Div(children=[layout for sub_layout in [layout.create_components() for layout in self.layouts] for layout in sub_layout])

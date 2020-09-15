#!/usr/bin/env python3

import dash
from .engine import Engine

# Initialize Dash application
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Create and serve layout
app.layout = Engine().create_metrics_layout().serve_layout

def run():
    app.run_server(debug=True)
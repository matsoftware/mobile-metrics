#!/usr/bin/env python3

import dash
from .engine import Engine
from os import environ

# Initialize Dash application
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Create and serve layout
app.layout = Engine().create_metrics_layout().serve_layout

# Run the server
DEBUG = environ.get('DEBUG') or False

def run():
    app.run_server(debug=DEBUG)
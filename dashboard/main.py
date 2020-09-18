#!/usr/bin/env python3

import dash
from app.engine import Engine
from os import environ
from app.layout.data.config import load 

# Initialize Dash application
config = load()
external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin': 'anonymous'
    }
]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = config.title
server = app.server

# Create and serve layout
layout = Engine(config=config).create_metrics_layout()
app.layout = layout.serve_layout

# Run the server
DEBUG = environ.get('DEBUG') or False

if __name__ == '__main__':
    app.run_server(debug=DEBUG)
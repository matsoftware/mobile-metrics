import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from data.data_provider import DataProvider, DataConstants
from data.api_data_source import APIDataSource
from data.models import IPASize

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}


def create_fig() -> px.line:
    data_provider = DataProvider(data_source=APIDataSource())
    df_app_size, labels = data_provider.fetch_ipa_size()
    return px.line(df_app_size, 
    x=DataConstants.date().key, 
    y=DataConstants.size_in_mb().key, 
    color=DataConstants.size_types().key, 
    title='App size',
    labels=labels)


def serve_layout():

    return html.Div(children=[
    html.H1(
        children='Mobile Metrics Dashboard',
        style={
            'textAlign': 'center',
        }
    ),
    html.H2(
        children='App sizes breakdown'
    ),
    dcc.Graph(
        id='APP-SIZE',
        figure=create_fig()
    )
])

app.layout = serve_layout

if __name__ == '__main__':
    app.run_server(debug=True)
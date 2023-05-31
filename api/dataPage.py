
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
from dash import dash_table as dt

import pandas as pd

import plotly.graph_objects as go

from dash.dependencies import Input, Output, State
from dblpGetNewData import getData, getDataCSV


from modelInteraction import getOrdersDf
from globals import *
from maindash import dashApp


def getDataPage():
 
    return html.Div([
                html.H1("Data", className="display-4"),
                html.Hr(),
                html.P("Orders:", className="lead"),
                dcc.Graph(
                    id="orders-table",
                    figure=getOrdersTable()
                ),
            ], className="p-5 bg-light rounded-3")


def getOrdersTable():
    df = getOrdersDf()
    return go.Figure(
        data=[
            go.Table(
                header=dict(
                    values=list(df.columns),
                    align='left',
                ),
                cells=dict(
                    values=df.transpose().values.tolist(),
                    align='left',
                ),
            )
        ],
         layout=go.Layout(
                    margin=dict(b=20, l=5, r=5, t=40),
                    paper_bgcolor="#f8f9fa",
                    plot_bgcolor="#f8f9fa",
                )
    )

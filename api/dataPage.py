
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
from dash import dash_table as dt

import pandas as pd

import plotly.graph_objects as go

from dash.dependencies import Input, Output, State
from dblpGetNewData import getData, getDataCSV


from modelInteraction import getOrdersDf
from modelInteraction import postNewOrder
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
                ,style={'height': '250px'}),
                html.H1("Place Order", className="display-4"),
                html.Hr(),
                html.Div([
                    dbc.Row([
                        dbc.Col(
                            html.Label("Keyword:"),
                            className="col-sm-2 col-form-label"
                        ),
                        dbc.Col(
                            # input field for anzahl entries
                            dcc.Input(
                                id="input-keyword",
                                type="text",
                                placeholder="",
                                value="",
                            ),
                            className="col-sm-3"
                        ),
                        dbc.Col(
                            html.Label("Start NodeID:"),
                            className="col-sm-2 col-form-label"
                        ),
                        dbc.Col(
                            dcc.Input(
                                id="input-nodeId",
                                type="text",
                                placeholder="",
                                value="",
                            ),
                            className="col-sm-3"
                        ),
                    ]),
                ]),
                html.Div([
                    dbc.Row([
                        dbc.Col(
                            html.Label("Email:"),
                            className="col-sm-2 col-form-label"
                        ),
                        dbc.Col(
                            # input field for anzahl entries
                            dcc.Input(
                                id="input-email",
                                type="text",
                                placeholder="",
                                value="",
                            ),
                            className="col-sm-3"
                        ),
                        dbc.Col(
                            html.Label("Max Distance:"),
                            className="col-sm-2 col-form-label"
                        ),
                        dbc.Col(
                            dcc.Input(
                                id="input-maxDistance",
                                type="text",
                                placeholder="",
                                value="",
                            ),
                            className="col-sm-3"
                        ),
                        dbc.Col(
                            dbc.Button("Add Order", id="filter-button", className="btn btn-primary"),
                            className="col-sm-2"
                        ),
                    ]),
                ]),
                html.Div(id="output-div-filterPost"),
            ], className="p-5 bg-light rounded-3")



@dashApp.callback(
    [Output("orders-table", "figure"),
     Output("output-div-filterPost", "children")],
    Input("filter-button", "n_clicks"),
    [
        State("input-keyword", "value"),
        State("input-nodeId", "value"),
        State("input-email", "value"),
        State("input-maxDistance", "value"),
    ]
)
def addFilter(n_clicks, keyword, nodeId, email, maxDistance):
    loggerlist = []
    if n_clicks is not None:
        maxDistance = int(maxDistance) if maxDistance != "" else -1
        postNewOrder(keyword, nodeId, email, maxDistance)
        loggerlist.append("Order placed in to database")
        return getOrdersTable(), html.Div([
                html.Hr(),
                html.P("Order Log:",style={'fontWeight': 'bold'}),
                html.Ul([html.Li(x) for x in loggerlist])
            ],style={'backgroundColor': 'rgb(201, 255, 204)','paddingLeft': '5px', 'paddingBottom': '1em'})
    return getOrdersTable(), None

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

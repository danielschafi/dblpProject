
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
from dash import dash_table as dt

import pandas as pd

import plotly.graph_objects as go

from dash.dependencies import Input, Output, State
from dblpGetNewData import getData, getDataCSV


from modelInteraction import getOrdersDf
from modelInteraction import postNewOrder
from modelInteraction import getDataId
from globals import *
from maindash import dashApp


def getDataPage():
 
    return html.Div([
                html.H1("Data", className="display-4"),
                html.Hr(),
                dcc.Graph(
                    id="orders-table",
                    figure=getOrdersTable()
                ,style={'height': '250px'}),
                html.H1("Place Order", className="display-4", style={'paddingTop': '0.5em'}),
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
                html.H1("Get Start Node", className="display-4", style={'paddingTop': '0.5em'}),
                html.Hr(),
                html.Div([
                    dbc.Row([
                        dbc.Col(
                            html.Label("Title:"),
                            className="col-sm-1 col-form-label"
                        ),
                        dbc.Col(
                            dcc.Input(
                                id="input-title-get",
                                type="text",
                                placeholder="Search for a title",
                                value="",
                                style={'width': '100%'}
                            ),
                            className="col-sm-8"
                        ),
                        dbc.Col(
                            html.Label("Art: "),
                            className="col-sm-1 col-form-label"
                        ),
                        dbc.Col(
                            dcc.Dropdown(
                                id="input-art-get",
                                options=[
                                    {'label': 'Article', 'value': 'article'},
                                    {'label': 'Inproceedings', 'value': 'inproceedings'},
                                    {'label': 'Proceedings', 'value': 'proceedings'},
                                    {'label': 'Book', 'value': 'book'},
                                    {'label': 'Incollection', 'value': 'incollection'},
                                    {'label': 'Phdthesis', 'value': 'phdthesis'},
                                    {'label': 'Mastersthesis', 'value': 'mastersthesis'},
                                    {'label': 'Www', 'value': 'www'},
                                    {'label': 'Data', 'value': 'data'},
                                ],
                                value='article',
                                style={'width': '100%'}
                            ),
                            className="col-sm-2"
                        ),
                    ]),
                    dbc.Row([
                        dbc.Col(
                            dbc.Button("Search Title", id="search-button", className="btn btn-primary", style={'width': '100%'}),
                        ),
                    ]),
                ]),
                html.Div(id="output-div-searchForTitle"),
            ], className="p-5 bg-light rounded-3")

@dashApp.callback(
    Output("output-div-searchForTitle", "children"),
    Input("search-button", "n_clicks"),
    [
        State("input-title-get", "value"),
        State("input-art-get", "value"),
    ]
)
def searchForTitle(n_clicks, title, art):
    if n_clicks is not None:
        df = getDataId(title, art)
        return html.Div([
                dcc.Graph(
                    id="search-table",
                    figure=getSearchTable(df)
                ,style={'height': '250px'}),
            ],style={'backgroundColor': 'rgb(248, 249, 250)','paddingLeft': '5px', 'paddingBottom': '1em'})
        
    return None, None

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


def getSearchTable(df):
    return go.Figure(
        data=[go.Table(
            header=dict(
                values=list(df.columns),
                align='left',
            ),
            cells=dict(
                values=df.transpose().values.tolist(),
                align='left',
            ),
        )],
         layout=go.Layout(
                    margin=dict(b=20, l=5, r=5, t=40),
                    paper_bgcolor="#f8f9fa",
                    plot_bgcolor="#f8f9fa",
                )
    )

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

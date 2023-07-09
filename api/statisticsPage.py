from dash import Input, Output, dcc, html
import plotly.graph_objects as go
import pandas as pd
import networkx as nx
import dash_bootstrap_components as dbc

from modelInteraction import getOrderDropdown, getAllConnectData, getNodeData
      

from globals import *
from maindash import dashApp
import plotly.express as px


def getStatisticsPage():
    orders, defaultOrder = getOrderDropdown()
    return html.Div([
        html.Div([
            dbc.Row([
                html.H1("Dataset Overview", className="display-4"),
                html.Hr(),
                
                html.Div([
                    html.P("Select Order:", className="lead"),
                    dcc.Dropdown(orders, defaultOrder, id="active-order-dropdown") 
                    ]),
                
                dbc.Col([
                    html.P("Publication media distribution", className="lead"),
                    dcc.Graph(id="publication-media-distribution-pie"),
                    ]),
                dbc.Col([
                    html.P("Publication media distribution", className="lead"),
                    dcc.Graph(id="publication-media-distribution-pie-bar"),
                ]),
            ])
        ])
    ], className="p-5 bg-light rounded-3"),
        

@dashApp.callback(
    #Output('avg-publications-bar', 'figure'),
    Output('publication-media-distribution-pie', 'figure'),
    Input('active-order-dropdown', 'value'))
def update_network_graph(value):
    if value is None:
        return 
    df = getAllConnectData(value)
    if df is None:
        return
    return pubMediaDistPie(df)

@dashApp.callback(
    Output('publication-media-distribution-pie-bar', 'figure'),
    Input('active-order-dropdown', 'value'))
def update_network_graph(value):
    if value is None:
        return 
    df = getAllConnectData(value)
    if df is None:
        return
    return pubMediaDistPieBar(df)

def pubMediaDistPieBar(df):
    df['count'] = 1
    df = df.groupby(['tablename']).count()
    df = df.reset_index()
    df = df.sort_values(by=['count'], ascending=False)
    fig = px.bar(df, x='tablename', y='count', color='tablename')
    return fig
    
def pubMediaDistPie(df):
    fig = px.pie(df, names='tablename')
    fig.update_layout(
                    hovermode="closest",
                    margin=dict(b=20, l=5, r=5, t=40),
                    paper_bgcolor="#f8f9fa",
                    plot_bgcolor="#f8f9fa",
                    )
    return fig


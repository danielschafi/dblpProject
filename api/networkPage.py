from dash import Input, Output, dcc, html
import plotly.graph_objects as go
import pandas as pd
import networkx as nx
import dash_bootstrap_components as dbc

from modelInteraction import *
      

from globals import *
from maindash import dashApp


def getNetworkPage():
    orders, defaultOrder = getOrderDropdown()
    return html.Div([
        html.Div([
            html.H1("Overview", className="display-4"),
            html.Hr(),
            html.P(
                "Welcome to our dashboard about the DBLP dataset", className="lead"
                ),
            html.P(
                "This dashboard is made by: Adrian Joost, Daniel Schafhäutle, Sangeeths Chandrakumar"
                ),
        
        dbc.Row([
            html.H1("Network Graph", className="display-4"),
            html.Hr(),
            
            html.Div([
                html.P("Select Order:", className="lead"),
                dcc.Dropdown(orders, defaultOrder, id="active-order-dropdown") 
                ]),

            dbc.Col([
                dcc.Graph(id="network-distance-graph")
                ], width=8),
            
            dbc.Col([
                dcc.Graph(id="network-distance-bar"),
                dcc.Graph(id="network-reached-stacked-bar"),
                ], width=4)            
            ])
        ])
    ], className="p-5 bg-light rounded-3"),
        

@dashApp.callback(
    Output('network-distance-graph', 'figure'),
    Output('network-distance-bar', 'figure'),
    Output('network-reached-stacked-bar', 'figure'),
    Input('active-order-dropdown', 'value'))
def update_network_graph(value):
    if value is None:
        return 
    df = getAllConnectData(value)
    if df is None:
        return
  
    reached = df.shape[0]
    df = df[df["precedent_node"].isnull() == False]
    notReached = df.shape[0]
    df["Color"] = df['distance'].apply(lambda x: colors[int(x)])

    return networkDistanceGraph(df), networkDistanceBar(df), networkReachedStackedBar(reached, notReached)


def networkDistanceGraph(df):
    df = df.sort_values(by="distance")
    G = nx.from_pandas_edgelist(df, source="node", target="precedent_node", edge_attr=None)    
    
    #Node positions
    #kamada_kawai_layout
    pos = nx.spring_layout(G)
    
    node_x = [pos[cord][0] for cord in list(G.nodes())]
    node_y = [pos[cord][1] for cord in list(G.nodes())]


    # Trace for nodes
    node_trace = go.Scatter(
        x=node_x,
        y=node_y,
        mode="markers",
        marker=dict(
            size=10,
            color=df["Color"],
            opacity=0.8,
            ),
        text=[getNodeData(node['node']) for _, node in df.iterrows()],
        hoverinfo="text",
    )



    # Trace for edges
    edge_x = []
    edge_y = []
    for edge in G.edges():
        x_start, y_start = pos[edge[0]]
        x_end, y_end = pos[edge[1]]
        edge_x.extend([x_start,x_end,None])
        edge_y.extend([y_start,y_end,None])


    edge_trace = go.Scatter(
        x=edge_x,
        y=edge_y,
        mode="lines",
        line=dict(
            width=2,
            )
        )
    

    return go.Figure(data=[edge_trace, node_trace],
                layout=go.Layout(
                    showlegend=False,
                    hovermode="closest",
                    margin=dict(b=20, l=5, r=5, t=40),
                    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                    width=1000,
                    height=1000,
                    paper_bgcolor="#f8f9fa",
                    plot_bgcolor="#f8f9fa",
                )
    )
    
    
    
    
def networkDistanceBar(df):

    # Calculate the count for each distance
    counts = df["distance"].value_counts().sort_index()
    bar_colors = [colors[c] for c in counts.index]

    # Create a bar trace with custom colors
    bar_trace = go.Bar(
        x=counts.index,
        y=counts.values,
        marker=dict(color=bar_colors),
        )


    return go.Figure(data=[bar_trace],
                layout=go.Layout(
                    showlegend=False,
                    hovermode="closest",
                    margin=dict(b=20, l=5, r=5, t=40),
                    paper_bgcolor="#f8f9fa",
                    plot_bgcolor="#f8f9fa",
                )
    )
    
    
    
def networkReachedStackedBar(reached, notReached):
    percentageReached = (reached /(reached + notReached)) * 100
    percentageNotReached = 100 - percentageReached
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        y=[''],
        x=[reached],
        name='Reached',
        orientation='h',
        marker=dict(
            line=dict(width=3),
        ),
        width=0.5,
        hovertext=f"Reached {round(percentageReached, 2)}%"
    ))
    fig.add_trace(go.Bar(
        y=[''],
        x=[notReached],
        name='Not Reached',
        orientation='h',
        marker=dict(
            line=dict(width=3)
        ),
        width=0.5,
        hovertext=f"Not Reached {round(percentageNotReached,2)}%"
    ))

    fig.update_layout(barmode='stack')
    fig.update_layout(
        go.Layout(
            showlegend=False,
            hovermode="closest",
            margin=dict(b=20, l=5, r=5, t=40),
            paper_bgcolor="#f8f9fa",
            plot_bgcolor="#f8f9fa",
        ))
    return fig
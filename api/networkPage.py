from dash import Input, Output, dcc, html
import plotly.graph_objects as go
import pandas as pd
import networkx as nx
import dash_bootstrap_components as dbc

from modelInteraction import getOrderDropdown
      

from globals import *
from maindash import dashApp


def getNetworkPage():
    orders, defaultOrder = getOrderDropdown()
    return html.Div([
        html.Div([
            html.Div([
                dcc.Dropdown(orders, defaultOrder, id="active-order-dropdown") 
                ]),
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

            dbc.Col([
                dcc.Graph(id="network-distance-graph",
                        figure=networkDistanceGraph())
                ], width=8),
            
            dbc.Col([
                dcc.Graph(id="network-distance-bar", 
                        figure=networkDistanceBar())
                ], width=4)
            ])
        ])
    ], className="p-5 bg-light rounded-3"),
        




def networkDistanceGraph():
    df = pd.read_csv("sample_networkGraphData.csv", usecols=[0,1,2])    




    df["Color"] = df["Distance"].apply(lambda x: colors[x])
    
    G = nx.from_pandas_edgelist(df, source="Previous", target="Id", edge_attr=True)    
    
    #Node positions
    pos=nx.kamada_kawai_layout(G)
    
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
        text=[f"{node['Id']}" for _, node in df.iterrows()],
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
                    #autosize=False,
                    width=1000,
                    height=1000,
                    paper_bgcolor="#f8f9fa",
                    plot_bgcolor="#f8f9fa",
                )
    )
    
    
    
    
def networkDistanceBar():
    df = pd.read_csv("sample_networkGraphData.csv", usecols=[0,1,2])    


    def colFunc(distance):
        return colors[distance]
    df["Color"] = df["Distance"].apply(colFunc)
    

    # Calculate the count for each distance
    counts = df["Distance"].value_counts().sort_index()
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
    
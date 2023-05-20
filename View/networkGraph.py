import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
import plotly.graph_objects as go
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


def networkGraph(app):
    df = pd.read_csv("sample_networkGraphData.csv")
    
    colors = [(230, 25, 75), (60, 180, 75), (255, 225, 25), (0, 130, 200), (245, 130, 48), (145, 30, 180), (70, 240, 240), (240, 50, 230), (210, 245, 60), (250, 190, 212), (0, 128, 128), (220, 190, 255), (170, 110, 40), (255, 250, 200), (128, 0, 0), (170, 255, 195), (128, 128, 0), (255, 215, 180), (0, 0, 128), (128, 128, 128), (255, 255, 255), (0, 0, 0)]

    df["color"] = colors[df["distance"]]
    
    G = nx.from_pandas_edgelist(df, source="Id", target="destination", edge_attr=True)    
    
    node_color=df["color"]
    pos=nx.fruchterman_reingold_layout(G)
    
    node_x = pos
   
    
    return dcc.Graph(
                    id="network-graph",
                    figure={
                        "data": [
                            go.Scatter(
                                x=[1, 2, 3, 4],
                                y=[2, 3, 1, 4],
                                mode="markers",
                                marker=dict(
                                    size=10,
                                    color=[0, 1, 2, 3],
                                    colorscale="Viridis",
                                    opacity=0.8,
                                ),
                                text=["Node 1", "Node 2", "Node 3", "Node 4"],
                                hoverinfo="text",
                            ),
                            go.Scatter(
                                #get all connections
                                x=[1, 2, 3, 4, 1, 2, 3, 4, 1, 4],
                                y=[2, 3, 1, 4, 2, 3, 1, 4, 2, 3],
                                mode="lines",
                                line=dict(
                                    color="rgb(125,125,125)",
                                    width=2,
                                ),
                            ),
                        ],
                        "layout": go.Layout(
                            title="Network Graph",
                            showlegend=False,
                            hovermode="closest",
                            xaxis=dict(showgrid=False, zeroline=False),
                            yaxis=dict(showgrid=False, zeroline=False),
                            margin=dict(b=20, l=5, r=5, t=40),
                        ),
                    },
                )
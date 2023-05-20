import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
import plotly.graph_objects as go



def networkGraph(app):
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
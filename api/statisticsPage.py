
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html

import plotly.graph_objects as go

from dash.dependencies import Input, Output, State

from dblpGetNewData import getData, getDataCSV



from maindash import dashApp


def getStatisticsPage():

        return html.Div([
            
            #split page in 2 X 2
            html.Div([
                html.Div([
                    html.H1("Number of publications per year", className="display-4"),
                    html.Hr(),
                    #plot bar chart with number of publications per year
                    dcc.Graph(
                        id="bar-chart",
                        figure={
                            "data": [
                                go.Bar(
                                    x=[1, 2, 3, 4],
                                    y=[2, 3, 1, 4],
                                    marker=dict(
                                        color="rgb(255, 0, 0)",
                                    ),
                                ),
                            ],
                            "layout": go.Layout(
                                title="Bar Chart",
                                xaxis={"title": "X Axis"},
                                yaxis={"title": "Y Axis"},
                                hovermode="closest",
                            ),
                        },
                    ),
                ], className="p-5 bg-light rounded-3"),
                html.Div([
                    html.H1("Number of publications per year", className="display-4"),
                    html.Hr(),
                    # plot line chart with number of publications per year
                    dcc.Graph(
                        id="line-chart",
                        figure={
                            "data": [
                                go.Scatter(
                                    x=[1, 2, 3, 4],
                                    y=[2, 3, 1, 4],
                                    mode="lines+markers",
                                    marker=dict(
                                        color="rgb(255, 0, 0)",
                                    ),
                                ),
                            ],
                            "layout": go.Layout(
                                title="Line Chart",
                                xaxis={"title": "X Axis"},
                                yaxis={"title": "Y Axis"},
                                hovermode="closest",
                            ),
                        },
                    ),
                ], className="p-5 bg-light rounded-3"),
        ], className="p-5 bg-light rounded-3")
        ], className="p-5 bg-light rounded-3")


    


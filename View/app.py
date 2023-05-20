import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
import plotly.io as pio
import plotly.io._templates as templates
import plotly.graph_objects as go
import pandas as pd
import networkx as nx

import networkGraph 


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME])

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.Img(src=app.get_asset_url('DBLP_Logo.png'), style={'width':'100%'}),
        html.H2("Sidebar", className="display-4"),
        html.Hr(),
        html.P(
            "Welcome to our dashboard about the DBLP dataset", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink([html.I(className="fas fa-home"), " Overview"], href="/", active="exact"),
                dbc.NavLink([html.I(className="fas fa-chart-bar"), " Analyse"], href="/page-1", active="exact"),
                dbc.NavLink([html.I(className="fas fa-cog"), " Settings"], href="/page-2", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)


content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return html.Div([
        html.Div([
            html.H1("Overview", className="display-4"),
            html.Hr(),
            html.P(
                "Welcome to our dashboard about the DBLP dataset", className="lead"
            ),
            html.P(
                "This dashboard is made by: Adrian Joost, Daniel Schafhäutle, Sangeeths Chandrakumar")
        ], className="p-5 bg-light rounded-3"),
        html.Div([
            html.H1("Network Graph", className="display-4"),
            html.Hr(),
            #plot network graph 2d with connections
            html.Div([networkGraph.networkGraph(app)]),
            
        ], className="p-5 bg-light rounded-3"),
        ])
    elif pathname == "/page-1":
        return html.Div([
            #split page in 2 X 2
            html.Div([
                html.Div([
                    html.h1("Number of publications per year", className="display-4"),
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
                    html.h1("Number of publications per year", className="display-4"),
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
    elif pathname == "/page-2":
        return html.P("Oh cool, this is page 2!")
    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )


if __name__ == "__main__":
    app.run_server(port=8888)
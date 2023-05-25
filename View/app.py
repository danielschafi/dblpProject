import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
from flask import send_file
import plotly.io as pio
import plotly.io._templates as templates
import plotly.graph_objects as go
import pandas as pd
import networkx as nx
import csv
import io
import base64
import requests

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

@app.callback(Output('output-div', 'children'), [Input('export-button', 'n_clicks')])
def export_data(n_clicks):
    if n_clicks is not None and n_clicks > 0:
        data = [
            {'Name': 'John', 'Age': 25, 'City': 'New York'},
            {'Name': 'Jane', 'Age': 30, 'City': 'Los Angeles'},
            {'Name': 'Sam', 'Age': 35, 'City': 'Chicago'}
        ]

        # do a api call to get the data
        # data = api_call()
        
        # Create a CSV string from the data
        csv_string = io.StringIO()
        writer = csv.DictWriter(csv_string, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
        
        # Encode the CSV string to base64
        encoded_csv = base64.b64encode(csv_string.getvalue().encode()).decode()
        
        # Create the download link and redirect the browser
        return dcc.Location(href=f"data:text/csv;base64,{encoded_csv}", id='download-link', refresh=True)

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
            dcc.Graph(id="network-graph",
                       figure=networkGraph.networkGraph(app))
            
        ], className="p-5 bg-light rounded-3"),
        ])
    elif pathname == "/page-1":
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
    elif pathname == "/page-2":
        return html.Div([
                html.H1("Settings", className="display-4"),
                html.Hr(),
                html.P("Here you can set which year of the DBLP dataset you want to import"),
                html.Div([
                    dbc.Row([
                        dbc.Col(
                            html.Label("Select Year:"),
                            className="mr-1"
                        ),
                        dbc.Col(
                            dcc.Dropdown(
                                id='year-dropdown',
                                options=[
                                    {'label': '2000', 'value': '2000'},
                                    {'label': '2001', 'value': '2001'},
                                    {'label': '2002', 'value': '2002'},
                                    {'label': '2003', 'value': '2003'},
                                    {'label': '2004', 'value': '2004'},
                                    {'label': '2005', 'value': '2005'},
                                    {'label': '2006', 'value': '2006'},
                                    {'label': '2007', 'value': '2007'},
                                    {'label': '2008', 'value': '2008'},
                                    {'label': '2009', 'value': '2009'},
                                    {'label': '2010', 'value': '2010'},
                                    {'label': '2011', 'value': '2011'},
                                    {'label': '2012', 'value': '2012'},
                                    {'label': '2013', 'value': '2013'},
                                    {'label': '2014', 'value': '2014'},
                                    {'label': '2015', 'value': '2015'},
                                    {'label': '2016', 'value': '2016'},
                                    {'label': '2017', 'value': '2017'},
                                    {'label': '2018', 'value': '2018'},
                                    {'label': '2019', 'value': '2019'},
                                    {'label': '2020', 'value': '2020'},
                                    {'label': '2021', 'value': '2021'},
                                    {'label': '2022', 'value': '2022'},
                                    {'label': '2023', 'value': '2023'},
                                ],
                                value='2023'
                            ),
                            className="mr-1"
                        ),
                        dbc.Col(
                            html.Label("Select Entries:"),
                            className="mr-1"
                        ),
                        dbc.Col(
                            # input field for anzahl entries
                            dcc.Input(
                                id="input-anzahl",
                                type="number",
                                placeholder="Anzahl",
                                min=1,
                                max=1000,
                                step=1,
                                value=10,
                            ),
                            className="mr-1"
                        ),
                        dbc.Col(
                            html.Label("Select Art:"),
                            className="mr-1"
                        ),
                        dbc.Col(
                            #select art of publication
                            dcc.Dropdown(
                                id='art-dropdown',
                                options=[
                                    {'label': 'Article', 'value': 'article'},
                                    {'label': 'Inproceedings', 'value': 'inproceedings'},
                                    {'label': 'Proceedings', 'value': 'proceedings'},
                                    {'label': 'Book', 'value': 'book'},
                                    {'label': 'Incollection', 'value': 'incollection'},
                                    {'label': 'Phdthesis', 'value': 'phdthesis'},
                                    {'label': 'Mastersthesis', 'value': 'mastersthesis'},
                                    {'label': 'Www', 'value': 'www'}
                                ],
                                value='article'
                            ),
                            className="mr-1"
                        ), 
                    ]),
                ]),
                html.Div([
                    dbc.Row([
                        dbc.Col(
                            dbc.Button([html.I(className="fas fa-file-import fa"), " Important"], color="primary", className="col-6"),
                            dbc.Button([html.I(className="fas fa-file-export fa"), "Export"], color="primary", className="col-6")
                        ),
                    ]),
                ]),
                html.Div(id="output-div"),
            ], className="p-5 bg-light rounded-3")
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
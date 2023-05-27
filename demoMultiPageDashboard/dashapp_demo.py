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
import sys
from pathlib import Path
projectdict= Path(__file__).parents[1]
sys.path.insert(0, str(projectdict))
#from dbreset import db






from maindash import app
from views.page1 import getPage1
from views.page2 import getPage2

if __name__ == '__main__':
    
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
                    dbc.NavLink(["Page1"], href="/", active="exact"),
                    dbc.NavLink(["Page2"], href="/page-2", active="exact"),
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
            return getPage1()
                
        elif pathname == "/page-2":
            return getPage2()
        
        
        
        
        
        
        
    app.run_server(debug=True)

    
    


import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
from flask import make_response, send_file

import sys
from dash.dependencies import Input, Output, State
from pathlib import Path
projectdict= Path(__file__).parents[1]
sys.path.insert(0, str(projectdict))
from dblpGetNewData import getData, getDataCSV

from globals import *

from maindash import dashApp
from dataPage import getDataPage
from importPage import getImportPage
from statisticsPage import getStatisticsPage
from networkPage import getNetworkPage

if __name__ == '__main__':
    
    SIDEBAR_STYLE = {
        "position": "fixed",
        "top": 0,
        "left": 0,
        "bottom": 0,
        "width": "16rem",
        "padding": "2rem 1rem",
        "background-color": "#f8f9fa"
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
            html.Img(src=dashApp.get_asset_url('DBLP_Logo.png'), style={'width':'100%'}),
            html.H2("Dashboard", className="display-5"),
            html.Hr(),
            html.P(
                "Welcome to our dashboard about the DBLP dataset", className="lead"
            ),
            dbc.Nav(
                [
                    dbc.NavLink([html.I(className="fas fa-home"), " Network"], href="/", active="exact"),
                    # dbc.NavLink([html.I(className="fas fa-chart-bar"), " Statistics"], href="/statistics", active="exact"),
                    dbc.NavLink([html.I(className="fas fa-cog"), " Data"], href="/data", active="exact"),
                    dbc.NavLink([html.I(className="fas fa-file-import"), " Import/Export"], href="/Import", active="exact"),

                    #import icon
                ],
                vertical=True,
                pills=True,
            ),
        ],
        style=SIDEBAR_STYLE,
    )

      
    content = html.Div(id="page-content", style=CONTENT_STYLE)
    dashApp.layout = html.Div([dcc.Location(id="url"), sidebar, content])
    
    
    
    @dashApp.callback(Output("page-content", "children"), [Input("url", "pathname")])
    def render_page_content(pathname):
        if pathname == "/":
            return getNetworkPage()
                
        elif pathname == "/statistics":
            return getStatisticsPage()
        
        elif pathname == "/data":
            return getDataPage()
        
        elif pathname == "/Import":
            return getImportPage()
        

        return html.Div(
            [
                html.H1("404: Not found", className="text-danger"),
                html.Hr(),
                html.P(f"The pathname {pathname} was not recognised..."),
            ],
            className="p-3 bg-light rounded-3",
        )
            
        
    dashApp.run_server(debug=True, port=8888)
    
    



import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html

import plotly.graph_objects as go

import csv
import io
import base64
import requests
import sys
from dash.dependencies import Input, Output, State
from pathlib import Path
projectdict= Path(__file__).parents[1]
sys.path.insert(0, str(projectdict))
from dblpGetNewData import getData, getDataCSV



from constants import *
from maindash import app


def getDataPage():
    return html.Div([
                html.H1("Settings", className="display-4"),
                html.Hr(),
                html.P("Here you can set which year of the DBLP dataset you want to import"),
                html.Div([
                    dbc.Row([
                        dbc.Col(
                            html.Label("Select Year:"),
                            className="col-sm-1 col-form-label"
                        ),
                        dbc.Col(
                            dcc.Dropdown(
                                id='year-dropdown',
                                options=yearList,
                                value='2023'
                            ),
                            className="col-sm-3"
                        ),
                        dbc.Col(
                            html.Label("Select Entries:"),
                            className="col-sm-1 col-form-label"
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
                            className="col-sm-3"
                        ),
                        dbc.Col(
                            html.Label("Select Art:"),
                            className="col-sm-1 col-form-label"
                        ),
                        dbc.Col(
                            #select art of publication
                            dcc.Dropdown(
                                id='art-dropdown',
                                options=artList,
                                value='article'
                            ),
                            className="col-sm-3"
                        ),
                    ]),
                    dbc.Row([
                            dbc.Col(
                                #create button to import data
                                dbc.Button("Import Data", id="import-button", color="primary", className="w-75"),
                            ),
                            dbc.Col(
                                #create button to export data
                                dbc.Button("Export Data", id="export-button", color="primary",class_name="w-75"),
                            ),
                        ],
                        className="g-0",
                    ),
                ]),
                dcc.Download(id="download-csv"),
                dbc.Alert("This is a success alert! Well done!", color="success",id="alert-success", dismissable=True),
                html.Div(id="output-div-import"),
            ], className="p-5 bg-light rounded-3")


@app.callback([Output("download-csv", "data"),
               Output("alert-success", "is_open")],
               [Input('export-button', 'n_clicks')],
                [State('year-dropdown', 'value'),
                State('input-anzahl', 'value'),
                State('art-dropdown', 'value')],
                prevent_initial_call=True,)
def export_data(n_clicks, year, anzahl, art):
    if n_clicks is not None and n_clicks > 0:
        dataframe = getDataCSV(year, anzahl, art)
        return dcc.send_data_frame(dataframe.to_csv, "dblp.csv"), True
         
@app.callback(Output('output-div-import', 'children'),
               [Input('import-button', 'n_clicks')],
               [State('year-dropdown', 'value'),
                State('input-anzahl', 'value'),
                State('art-dropdown', 'value')])
def import_data(n_clicks, year, anzahl, art):
    if n_clicks is not None and n_clicks > 0:
        if art == "All":
            art = None
        getData(year, anzahl, art)
        return "Data imported"
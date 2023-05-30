
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
from dash import dash_table as dt

import pandas as pd

import plotly.graph_objects as go

from dash.dependencies import Input, Output, State
from dblpGetNewData import getData, getDataCSV


from modelInteraction import getOrdersDf
from globals import *
from maindash import dashApp


def getDataPage():
 
    return html.Div([
                html.H1("Data", className="display-4"),
                html.Hr(),
                html.P("Orders:", className="lead"),
                dcc.Graph(
                    id="orders-table",
                    figure=getOrdersTable()
                ),
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
                                dbc.Button("Export Data", id="export-button", color="primary",class_name="w-75", style={'float': 'right'}),
                            ),
                        ],
                        className="g-0",
                        style={'paddingTop': '1em'}
                    ),
                ]),
                dcc.Download(id="download-csv"),
            html.Div(id="output-div-import"),
            html.Div(id="output-div-export")
            ], className="p-5 bg-light rounded-3")



@dashApp.callback([Output("download-csv", "data"),Output('output-div-export', 'children')],
               [Input('export-button', 'n_clicks')],
                [State('year-dropdown', 'value'),
                State('input-anzahl', 'value'),
                State('art-dropdown', 'value')],
                prevent_initial_call=True,)
def export_data(n_clicks, year, anzahl, art):
    if n_clicks is not None and n_clicks > 0:
        if art == "All":
            art = None
        dataframe,loggerlist = getDataCSV(year, anzahl, art)
        return dcc.send_data_frame(dataframe.to_csv, "dblp.csv"), html.Div([
            html.Hr(),
            html.P("Exported Data:",style={'fontWeight': 'bold'}),
            html.Ul([html.Li(x) for x in loggerlist])
        ],style={'backgroundColor': 'rgb(201, 255, 204)','paddingLeft': '5px', 'paddingBottom': '1em'})
         
@dashApp.callback(Output('output-div-import', 'children'),
               [Input('import-button', 'n_clicks')],
               [State('year-dropdown', 'value'),
                State('input-anzahl', 'value'),
                State('art-dropdown', 'value')])
def import_data(n_clicks, year, anzahl, art):
    if n_clicks is not None and n_clicks > 0:
        if art == "All":
            art = None
        logger = getData(year, anzahl, art)
        # logger.append(f"Imported {anzahl} entries of type {art} from year {year}")
        return html.Div([
            html.Hr(),
            html.P("Imported Data:",style={'fontWeight': 'bold'}),
            html.Ul([html.Li(x) for x in logger])
        ],style={'backgroundColor': 'rgb(201, 255, 204)','paddingLeft': '5px', 'paddingBottom': '1em'})
        
        



def getOrdersTable():
    df = getOrdersDf()
    return go.Figure(
        data=[
            go.Table(
                header=dict(
                    values=list(df.columns),
                    align='left',
                ),
                cells=dict(
                    values=df.transpose().values.tolist(),
                    align='left',
                    
                ),
            )
        ],
         layout=go.Layout(
                    margin=dict(b=20, l=5, r=5, t=40),
                    paper_bgcolor="#f8f9fa",
                    plot_bgcolor="#f8f9fa",
                )
    )

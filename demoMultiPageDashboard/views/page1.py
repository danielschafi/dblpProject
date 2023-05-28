from maindash import app
from dash.dependencies import Input, Output

from dash import Dash, dcc, html, Input, Output

def getPage1():
    return html.Div([
        dcc.Input(id='my-id', value='initial value', type='text'),
        html.Div(id='my-div')
    ])

@app.callback(Output(component_id='my-div', component_property='children'),
              [Input(component_id='my-id', component_property='value')])
def update_output_div(input_value):
    return 'You\'ve entered "{}"'.format(input_value)
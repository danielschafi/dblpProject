import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
import plotly.graph_objects as go
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
import plotly.io as pio
import plotly.io._templates as templates
import plotly.graph_objects as go
import pandas as pd
import networkx as nx



def networkGraph(app):
    df = pd.read_csv("sample_networkGraphData.csv", usecols=[0,1,2])    

    colors = ["rgb"+ val for val in ['(230, 25, 75)', '(60, 180, 75)', '(255, 225, 25)', '(0, 130, 200)', '(245, 130, 48)', '(145, 30, 180)',
              '(70, 240, 240)', '(240, 50, 230)', '(210, 245, 60)', '(250, 190, 212)', '(0, 128, 128)', '(220, 190, 255)', 
              '(170, 110, 40)', '(255, 250, 200)', '(128, 0, 0)', '(170, 255, 195)', '(128, 128, 0)', '(255, 215, 180)', 
              '(0, 0, 128)', '(128, 128, 128)', '(255, 255, 255)', '(0, 0, 0)']]

    def colFunc(distance):
        return colors[distance]
    df["Color"] = df["Distance"].apply(colFunc)
    
    G = nx.from_pandas_edgelist(df, source="Id", target="Previous", edge_attr=True)    
    
    #Node positions
    pos=nx.fruchterman_reingold_layout(G)
    
    node_x = [pos[cord][0] for cord in list(G.nodes())]
    node_y = [pos[cord][1] for cord in list(G.nodes())]


    # Trace for nodes
    node_trace = go.Scatter(
        x=node_x,
        y=node_y,
        mode="markers",
        marker=dict(
            size=10,
            color=df["Color"],
            opacity=0.8,
            ),
        text=[f"Dist: {node['Distance']} | From: {node['Id']} | To: {node['Previous']}" for _, node in df.iterrows()],
        hoverinfo="text",
    )
    
    # Trace for edges
    edge_x = []
    edge_y = []
    for edge in G.edges():
        x_start, y_start = pos[edge[0]]
        x_end, y_end = pos[edge[1]]
        edge_x.extend([x_start,x_end,None])
        edge_y.extend([y_start,y_end,None])


    edge_trace = go.Scatter(
        x=edge_x,
        y=edge_y,
        mode="lines",
        line=dict(
            width=2,
        )
    )
    

    

    return go.Figure(data=[edge_trace, node_trace],
                layout=go.Layout(
                    title="Network Graph",
                    showlegend=False,
                    hovermode="closest",
                    margin=dict(b=20, l=5, r=5, t=40),
                    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
                )
)
    
    
    
    
    
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME])


app.layout = dcc.Graph(id="network-graph",
                       figure=networkGraph(app))


if __name__ == "__main__":
    app.run_server(port=8888)
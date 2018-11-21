# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np 
x = np.linspace(0,10,100)
y = np.sin(x)
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': x, 'y': y, 'name': 'sin(x)'},
                {'x': x, 'y': y + 3, 'name': 'sin(x) + 3'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

#https://www.aprenderpython.net/graficos-vivo-guis-visualizacion-datos-dash/

#https://plot.ly/products/dash/?gclid=EAIaIQobChMI3Zz_hoC23gIVUhitBh38_wLNEAEYASAAEgLL-fD_BwE

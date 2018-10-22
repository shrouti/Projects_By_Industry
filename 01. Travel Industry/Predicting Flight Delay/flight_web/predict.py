import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
from __init__ import app
from etl import merged
import dashboard



def predict_chosen():
    return [html.P("Enter in the date and airport you will be flying from"),
    html.P("Let's see if we can guess if you'll be delayed"),
    html.Div([
        html.Div([
            html.H3('Line'),
            dcc.Graph(id='g1', figure={'data': [{'y': [1, 2, 3]}]})
        ], className="six columns"),

        html.Div([
            html.H3('Bend'),
            dcc.Graph(id='g2', figure={'data': [{'y': [5, 15, 10]}]})
        ], className="six columns"),
    ], className="row")]

#

import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
from __init__ import app
from etl import merged
import dashboard


def findings_chosen():
    return [html.H2("Look at what we found"),
    html.P("there are some graphs and some charts\t We are working with\
    if an airplane will be delayed given weather factors")]

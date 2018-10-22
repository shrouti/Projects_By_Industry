from flask import render_template, jsonify, json
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from __init__ import app
import dashboard

app.layout = html.Div(children=[
    html.H1("Flights"),
    html.H3("More text")
])

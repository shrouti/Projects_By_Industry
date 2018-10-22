import dash
import dash_core_components as dcc
import dash_html_components as html
from flask import Flask, render_template
from dash.dependencies import Input, Output
import pandas as merged
import os

app = dash.Dash(__name__, url_base_pathname='/')

app.server.config['DEBUG'] = True
app.server.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flights.db'
app.server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# server.config['SQLALCHEMY_ECHO'] = True
app.config['suppress_callback_exceptions'] = True

# db = SQLAlchemy(app.server)

import dashboard

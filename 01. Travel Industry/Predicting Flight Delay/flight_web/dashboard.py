import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
from __init__ import app
from etl import merged
# import colorlover as cl
# import plotly.plotly as py
# import plotly.graph_objs as go
import pandas as pd
from findings import *
from models import *
from predict import *
# import dash_table_experiments as dt

app.layout = html.Div(children=[
    html.H1("Flight Delays",
        style ={'textAlign': 'center'}),

    html.H4("Take a look at our findings"),
     dcc.Tabs(
            tabs=[
            {'label': 'Findings', 'value': 'F'},
            {'label': 'Models', 'value': 'M'},
            {'label': 'Predict', 'value': 'P'},
        ],
        value='F',
        id='tabs'
    ),
    html.Div(id='tab-output'),

    # html.P(merged)

])

app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

#callback for when a tab is chosen
@app.callback(
    Output('tab-output', 'children'),
    [Input('tabs', 'value')])
def update_tab(value):
    if value == 'F':
        # return html.H2("Look at what we found")
        return  findings_chosen()
    elif value == 'M':
        # return html.H2("Let's play with some of our models")
        return  model_chosen()
    else:
        # return html.H2("Shall we make some predictions?")
        return predict_chosen()



# #When findings choose, retrun written page of our Findings
# def findings_chosen():
#     return [html.H2("Look at what we found"),
#     html.P("there are some graphs and some charts\t We are working with\
#     if an airplane will be delayed given weather factors")]

#
#when model tab choosen return dropdowns
# def model_chosen():
#       return [dcc.Dropdown(
#         id='month-dropdown',
#         options=[
#             {'label': 'Jan', 'value': '1'},
#             {'label': 'Feb', 'value': '2'},
#             {'label': 'March', 'value' : '3'},
#             {'label': 'April', 'value': '4'},
#             {'label': 'May', 'value': '5'},
#             {'label': 'June', 'value': '6'},
#             {'label': 'July', 'value' : '7'},
#             {'label': 'Aug', 'value': '8'},
#             {'label': 'Sept', 'value': '9'},
#             {'label': 'Oct', 'value': '10'},
#             {'label': 'Nov', 'value' : '1'},
#             {'label': 'Dec', 'value': '12'}
#             ]),
#             html.Div(id='choose-month'),
#




#prdiction has been choosen
# def predict_chosen():
#     return [html.P("Enter in the date and airport you will be flying from")]
#

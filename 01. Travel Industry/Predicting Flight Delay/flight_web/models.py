import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_table_experiments as dt
from dash.dependencies import Input, Output
from __init__ import app
from etl import merged
import dashboard
import pandas as pd
import pdb

def model_chosen():
    return[
    # html.Div(dtable.DataTable(rows=[{}]), style={‘display’: ‘none’}),
    html.Div([
        html.Label('Choose an Airport to Explore its\' Data'),
        dcc.Checklist(
        id='airport-dropdown',
        options=[
            {'label': 'JFK', 'value': 'JFK'},
            {'label': 'LAX', 'value': 'LAX'},
            {'label': 'O\'Hare', 'value' : 'ORD'},
            {'label': 'Dallas-Fort Worth', 'value': 'DFW'},
            {'label': 'Miami', 'value': 'MIA'}
            ],
            values=[],
            labelStyle={'display': 'inline-block'}),
            html.Div(id='choose-airport'),

        html.Label('Choose Months to Explore Data'),
        dcc.Checklist(
            id='month-dropdown',
            options=[
                {'label': 'January', 'value': 1},
                {'label': 'February', 'value': 2},
                {'label': 'March', 'value' : 3},
                {'label': 'April', 'value': 4},
                {'label': 'May', 'value': 5},
                {'label': 'June', 'value': 6},
                {'label': 'July', 'value' : 7},
                {'label': 'August', 'value': 8},
                {'label': 'September', 'value': 9},
                {'label': 'October', 'value': 10},
                {'label': 'November', 'value' : 11},
                {'label': 'December', 'value': 12}
                ],
                values = [],
                labelStyle={'display': 'inline-block'}),
                html.Div(id='choose-month'),

                # dt.DataTable(
                # rows=[{}], style={‘display’: ‘none’})
                # html.Div(id='datatable')

                # html.Div(id = "data-table")
    ])
            ]


# @app.callback(
#     dash.dependencies.Output('choose-airport', 'options'),
#     [dash.dependencies.Input('airport-dropdown', 'value')])
# def set_cities_options(airport):
#     dep = merged[(merged['Origin'] == airport)]
#     pdb.set_trace()
#     return [build_df(dep,max_rows=100)]
#
#
# @app.callback(
#     dash.dependencies.Output('choose-month', 'value'),
#     [dash.dependencies.Input('month-dropdown', 'options')])
# def set_cities_value(month):
#     dep = merged[(merged['Month'] == month)]
#     pdb.set_trace()
#     return [build_df(dep,max_rows=100)]

@app.callback(
    Output(component_id='choose-airport', component_property='options'),
    [Input(component_id='airport-dropdown', component_property='values'),
    Input('month-dropdown', 'values')])
def update_table(values, month):
    pdb.set_trace()
    spot = "top"
    fly_df = get_df(values,month)
    pdb.set_trace()
    return fly_df #build_df(fly,max_rows=100)

def get_df(flight= [] ,month=[]):
    fly = pd.DataFrame()
    if month == []:
        spot = "just flight"
        for air in flight:
            delay = pd.DataFrame(specific_df(f =air))
            hold = fly.append(delay)
            fly = hold
            pdb.set_trace()
    elif flight == []:
        spot = "just month"
        for time in month:
            delay = pd.DataFrame(specific_df(m=time))
            hold = fly.append(delay)
            fly = hold
            pdb.set_trace()
    else:
        spot = "Both"
        for air in flight:
            for time in month:
                delay = pd.DataFrame(specific_df(air,time))
                hold = fly.append(delay)
                fly = hold
                pdb.set_trace()
    print(spot)
    return fly

def specific_df(f = None , m = 0):
    if m == 0:
        spot = "df for flight"
        dept = merged[merged['Origin'] == f]
        pdb.set_trace()
    elif f == None:
        spot = 'df for month'
        dept = merged[merged['Month'] == m]
        pdb.set_trace()
    else:
        spot = "df for both"
        dept = merged[(merged['Origin'] == f) & (merged['Month'] == m)]
        pdb.set_trace()
    print(spot)
    return dept

def build_df(airport,max_rows=100):
    return [
    html.Table(
        # Header
        [html.Tr([html.Th(col) for col in airport.columns])] +

        # Body
        [html.Tr([
            html.Td(airport.iloc[i][col]) for col in airport.columns
        ]) for i in range(min(len(airport), max_rows))])]

# @app.callback(Output('datatable', 'rows'),
# [Input(component_id='airport-dropdown', component_property='values'),
# Input('month-dropdown', 'values')])
# def update_datatable(user_selection):
#     """
#     For user selections, return the relevant table
#     """
#     if user_selection == 'Summary':
#         return DATA.to_dict('records')
#     else:
#         return SOMEOTHERDATA.to_dict('records')




# callback for airport checkbox
# @app.callback(
#     Output(component_id='choose-airport', component_property='options'),
#     [Input(component_id='airport-dropdown', component_property='values')])
#     # Input('month-dropdown', 'values')])
# def update_flight(values):
#     pdb.set_trace()
#     if values== 'JFK':
#         return [html.H2("You chose JFK")]
#         # return get_df('JFK')
#     elif values == 'LAX':
#         return [html.H2("You chose LAX, Just chill bro")]
#         # return get_df('LAX')
#     if values == 'ORD':
#         return html.H2("You chose ORD, DA BEARS")
#         # return get_df('ORD')
#     elif values == 'DFW':
#         return html.H2("Howdy yall, you chose DFW")
#         # return get_df('DFW')
#     elif values == 'MIA':
#         return html.H2("You chose MIA, Welcome to sunny Miami ")
#         # return get_df('MIA')
#     else:
#         return html.H2("Please choose a city and or month to see some cool information")
#
# def get_df(flight):
#     fly = pd.DataFrame()
#     for air in flight:
#         delay = pd.DataFrame(specific_df(air))
#         hold = fly.append(delay)
#         fly = hold
#             # pdb.set_trace()
#     return fly
#
# def specific_df(f):
#     dept = merged[(merged['Origin'] == f)]
#     return dept
#
# def build_df(airport,max_rows=100):
#     return [
#     html.Table(
#         # Header
#         [html.Tr([html.Th(col) for col in airport.columns])] +
#
#         # Body
#         [html.Tr([
#             html.Td(airport.iloc[i][col]) for col in airport.columns
#         ]) for i in range(min(len(dataframe), max_rows))])]
# #callback for month checkbox

# @app.callback(
#     Output(component_id='choose-month', component_property='options'),
#     [Input(component_id='month-dropdown', component_property='values'),
# def update_month(values):
#     if value == '1':
#         return html.H2("January")
#             # get_df('JFK')]
#     elif value == '2':
#         return html.H2("February")
#             # get_df('LAX')]
#     if value == '3':
#         return html.H2("March")
#             # get_df('ORD')]
#     elif value == '4':
#         return html.H2("April")
#             # get_df('DFW')]
#     elif value == '5':
#         return html.H2("May")
#             # get_df('MIA')]
#     if value == '6':
#         return html.H2("June")
#             # get_df('JFK')]
#     elif value == '7':
#         return html.H2("July")
#             # get_df('LAX')]
#     if value == '8':
#         return html.H2("August")
#             # get_df('ORD')]
#     elif value == '9':
#         return html.H2("September")
#             # get_df('DFW')]
#     elif value == '10':
#         return html.H2("October")
#             # get_df('MIA')]
#     elif value == '11':
#         return html.H2("November")
#             # get_df('DFW')]
#     elif value == '12':
#         return html.H2("December")
#             # get_df('MIA')]
#     else:
#         return html.H2("Would you loke to choose a month ")
#

# def get_df(flight):
#     fly = pd.DataFrame()
#     for air in flight:
#         delay = pd.DataFrame(specific_df(air))
#         hold = fly.append(delay)
#         fly = hold
#         # pdb.set_trace()
#     return fly
# def specific_df(f):
#     dept = merged[(merged['Origin'] == f)]
#     return dept







#When run this code in Jupyter notebook everything is working well
#but something off in Dash, maybe callbacks are not correct
# def update_table(values, month):
#     spot = "top"
#     fly = get_df(values,month)
# #     pdb.set_trace()
#     print(spot)
#     return fly
#
# def get_df(flight= [] ,month=[]):
#     fly = pd.DataFrame()
#     if month == []:
#         spot = "just flight"
#         for air in flight:
#             delay = pd.DataFrame(specific_df(f =air))
#             hold = fly.append(delay)
#             fly = hold
# #             pdb.set_trace()
#     elif flight == []:
#         spot = "just month"
#         for time in month:
#             delay = pd.DataFrame(specific_df(m=time))
#             hold = fly.append(delay)
#             fly = hold
# #             pdb.set_trace()
#     else:
#         spot = "Both"
#         for air in flight:
#             for time in month:
#                 delay = pd.DataFrame(specific_df(air,time))
#                 hold = fly.append(delay)
#                 fly = hold
# #                 pdb.set_trace()
#     print(spot)
#     return fly
#
# def specific_df(f = None , m = 0):
#     if m == 0:
#         spot = "df for flight"
#         dept = merged[merged['Origin'] == f]
# #         pdb.set_trace()
#     elif f == None:
#         spot = 'df for month'
#         dept = merged[merged['Month'] == m]
# #         pdb.set_trace()
#     else:
#         spot = "df for both"
#         dept = merged[(merged['Origin'] == f) & (merged['Month'] == m)]
# #         pdb.set_trace()
#     print(spot)
#     return dept
#
# update_table(['MIA'], [])

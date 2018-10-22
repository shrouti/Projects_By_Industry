@app.server.route('/movies')
def movies():
    all_movies_dict = [movie.to_dict() for movie in Movie.query.all()]
    return render_template('movies.html',movies=all_movies_dict)
#render template to read html



app.layout = html.Div(children =[
    html.H1('Welcome to our Movie Database.'),
    html.H3('To fully enjoy your experience, play around with different routes to learn more about movie performance.'),
    html.H2('Our movies genres'),
    dcc.Dropdown(
        id='genre-dropdown',
        options=[
            {'label': 'Average', 'value': 'AVG'},
            {'label': 'Count', 'value': 'CT'},
            {'label': 'Runtime', 'value' : 'RUN'},
            {'label': 'Total', 'value': 'TOT'}

        ],
        value='CT'
    ),

    html.P(),
    dcc.Checklist(
        id='genre-specific',
        options=genre_setup()
        ,
        values = [1],
        labelStyle={'display': 'inline-block'}
    ),
    html.Div(id='month_genres')



])


@app.callback(
    Output('genres-graph', 'children'),
    [Input('genre-dropdown', 'value')])

def update_output(value):
    if value == 'CT':
        return dcc.Graph(
            id = "Genres_total",
            figure = genre_count_layout())
    elif value == 'TOT':
        return dcc.Graph(
            id = "Genres_total",
            figure = genre_total_layout())
    elif value == 'AVG':
        return dcc.Graph(
            id = "Genres_total",
            figure = genre_avg_layout())
    elif value == 'RUN':
        return dcc.Graph(
            id = "Genres_total",
            figure = genre_runtime())
    else:
        return "Error, no value"


@app.callback(
    Output('month_genres', 'children'),
    [Input('genre-specific', 'values'),
    Input ('genre-radio', 'value')])

def update_gen_months(value, radio):
    if radio == 'MANY':
        return genre_months(value)
    elif radio == 'REV':
        return genre_tot_months(value)
    elif radio == 'PRO':
        return genre_profits_months(value)


 {'data' : [{
                 'x' : [genre['name'] for genre in genre_order],
                 'y' : all_run,
                 'name' : "Movie Genres",
                 'type' : 'bar'
                 }],
                 'layout' : {'title': "Average Runtime Per Genre"}


# def color_df(data):
#     colors = cl.scales['5']['seq']['Redss']
#     # data = {'DepDelay' : [<15, 15-30, 30-60, 60-120, >120],
#     #         'Color' : colors}
#     df = generate_table(data, max_rows=25)
#
#
#     trace0 = go.Table(
#       header = dict(
#         values = [df.columns],
#         line = dict(color = 'white'),
#         fill = dict(color = 'white'),
#         align = ['center'],
#         font = dict(color = 'black', size = 12)
#       ),
#       cells = dict(
#         values = [df.Color, df.Year],
#         line = dict(color = [df.Color]),
#         fill = dict(color = [df.Color]),
#         align = 'center',
#         font = dict(color = 'black', size = 11)
#         ))
#
#     data = [trace0]
#
#     py.iplot(data, filename = "row variable color")
                 }

import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
import os

cwd = os.getcwd()

merged = pd.read_csv(cwd+'/merged.csv', index_col=0, low_memory=False)

# data = merged.to_dict('records')
#
# df = pd.DataFrame(data)
# # html.Table(
#     # Header
#     [html.Tr([html.Th(col) for col in dataframe.columns])] +
#
#     # Body
#     [html.Tr([
#         html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
#     ]) for i in range(min(len(dataframe), max_rows))])

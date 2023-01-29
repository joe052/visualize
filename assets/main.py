import dash
from dash import html
from dash import dcc
import plotly.express as px

app = dash.Dash()
app.layout = html.Div([html.Div("Visualizer"),
                       html.H1('Dashboard'),
                       html.Div(dcc.Dropdown(id='dropdown', options=[{"label": "California", "value": "california"},
                                                                     {"label": "Illinois",
                                                                         "value": "illinois"},
                                                                     {"label": "New york",
                                                                         "value": "new york"},
                                                                     ]))
                       ]
                      )

app.run_server(debug=True)

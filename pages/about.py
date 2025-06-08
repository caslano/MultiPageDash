import dash
from dash import html

dash.register_page(__name__)

layout = html.Div([
    html.H2("About Page"),
    html.P("This is the about page.")
])

import dash
import dash_bootstrap_components as dbc
from dash import html

dash.register_page(__name__)



layout = dbc.Container(
    [
        html.H2("About Page"),
        html.P("This is the about page.")
    ])


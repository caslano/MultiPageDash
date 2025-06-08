import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__)

layout = dbc.Container(
    [
        html.H2("Contact Page"),
        html.P("Get in touch through the contact page.")
    ])
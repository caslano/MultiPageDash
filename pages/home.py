import dash
import dash_bootstrap_components as dbc
from dash import html

dash.register_page(__name__, path="/")

layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Home Page"),
                        html.P("Welcome to the home page.")
                    ]
                ),
                dbc.Col(
                    [
                        html.H2("Latest news"),
                        html.P("This is the latest news.")
                    ]
                )
            ]
        )
    ])

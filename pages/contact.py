import dash
from dash import html

dash.register_page(__name__)

layout = html.Div([
    html.H2("Contact Page"),
    html.P("Get in touch through the contact page.")
])

import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

# Create Dash app with Bootstrap theme
app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server  # For deployment

# Create navbar using dbc
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dcc.Link(page["name"], href=page["path"], className="nav-link"))
        for page in dash.page_registry.values()
    ],
    brand="My Dash App",
    color="primary",
    dark=True,
    class_name="mb-4"
)

# App layout
app.layout = html.Div([
    navbar,
    dbc.Container(dash.page_container, className="pt-4")
])

if __name__ == "__main__":
    app.run(debug=True)

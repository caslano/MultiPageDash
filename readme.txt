#app.py

import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.PULSE])
server = app.server

# Generate navigation items
def create_nav_items(current_path):
    items = []

    for page in dash.page_registry.values():
        nav_item = dbc.NavItem(
            dcc.Link(
                page["name"],
                href=page["path"],
                className=f"nav-link {'active' if page['path'] == current_path else ''}"
            )
        )
        items.append(nav_item)

    return items

# Layout with navbar
app.layout = html.Div([
    dcc.Location(id='url'),  # Tracks current URL

    dbc.Navbar(
        dbc.Container([
            dbc.NavbarBrand("My Dash App", href="/"),
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            dbc.Collapse(
                id="navbar-collapse",
                is_open=False,
                navbar=True,
                children=dbc.Nav(id="navbar-nav", navbar=True, className="ms-auto")
            ),
        ]),
        color="primary",
        dark=True,
        className="mb-4"
    ),

    dbc.Container(dash.page_container, className="pt-4"),
])

# Toggle collapse on small screens
@app.callback(
    Output("navbar-collapse", "is_open"),
    Input("navbar-toggler", "n_clicks"),
    prevent_initial_call=True
)
def toggle_navbar(n):
    return n % 2 == 1

# Update nav items dynamically to highlight active page
@app.callback(
    Output("navbar-nav", "children"),
    Input("url", "pathname")
)
def update_nav(pathname):
    return create_nav_items(pathname)

if __name__ == "__main__":
    app.run(debug=True)

#about.py

import dash
import dash_bootstrap_components as dbc
from dash import html

dash.register_page(__name__)



layout = dbc.Container(
    [
        html.H2("About Page"),
        html.P("This is the about page.")
    ])


#contact.py

import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__)

layout = dbc.Container(
    [
        html.H2("Contact Page"),
        html.P("Get in touch through the contact page.")
    ])

#home.py

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


# style.css

/* style.css */

.nav-link.active {
  font-weight: bold;
  /* color: #ffc107 !important; */ /* Bootstrap warning color */
  background-color: rgba(0, 0, 0, 0.1);
  border-radius: 0.25rem;
}


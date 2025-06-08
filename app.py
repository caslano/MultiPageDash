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

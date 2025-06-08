import dash
from dash import html, dcc

# Create the app instance with pages enabled
app = dash.Dash(__name__, use_pages=True)
server = app.server  # For deployment if needed

app.layout = html.Div([
    html.H1("My Multi-Page Dash App"),

    html.Div([
        dcc.Link(page["name"] + " | ", href=page["path"])
        for page in dash.page_registry.values()
    ]),

    dash.page_container  # Renders the current page content
])

if __name__ == "__main__":
    app.run(debug=True)

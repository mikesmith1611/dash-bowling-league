import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
from app import app
from apps import leagueEditor


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([dt.DataTable(rows=[{}])], style={'display': 'none'}),
    html.Div(id='page-content'),
])

layout = html.Div([
    dcc.Link('Create New League', href='/leagueEditor')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    print(pathname)
    if pathname == '/':
        return layout
    elif pathname == '/leagueEditor':
        return leagueEditor.layout


if __name__ == "__main__":
    app.run_server(debug=True, port=8051)

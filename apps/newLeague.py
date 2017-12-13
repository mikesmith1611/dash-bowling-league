import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
from bowlingLeague import io
from app import app

leagues = io.getLeagueNames()


layout = html.Div([
    dt.DataTable(rows=[],
                 columns=['Id', 'Name'],
                 row_selectable=True,
                 id='newLeagueTable'),
    dcc.Input(placeholder='League Name..', id='newLeagueName'),
    dcc.Input(placeholder='Player Name..', id='newLeaguePlayerName'),
    html.Button('Add Player', id='addPlayerButton'),
    dcc.Link('Save League', id='saveLeagueButton', href='/')
])


@app.callback(Output('newLeagueTable', 'rows'),
              [Input('addPlayerButton', 'n_clicks')],
              state=[State('newLeaguePlayerName', 'value'),
                     State('newLeagueTable', 'rows')])
def addPlayer(n_clicks, name, table):
    if name is not None:
        row = {'Name': name, 'Id': len(table)}
        table.append(row)
    print(table)
    return table

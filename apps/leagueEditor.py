import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
from bowlingLeague import io
from app import app
import json

leagues = io.getLeagueNames()


layout = html.Div([
    dt.DataTable(rows=[],
                 columns=['Id', 'Name'],
                 row_selectable=True,
                 sortable=True,
                 selected_row_indices=[],
                 id='newLeagueTable'),
    dcc.Input(placeholder='League Name..', id='newLeagueName'),
    dcc.Input(placeholder='Player Name..', id='newLeaguePlayerName'),
    html.Button('Add Player', id='addPlayerButton'),
    html.Button('Save League', id='saveLeagueButton'),
    html.Div(id='newLeagueStatus')
])


@app.callback(Output('newLeagueTable', 'rows'),
              [Input('addPlayerButton', 'n_clicks')],
              state=[State('newLeaguePlayerName', 'value'),
                     State('newLeagueTable', 'rows'),
                     State('newLeagueTable', 'selected_row_indices')])
def addPlayer(n_clicks, name, table, selected):
    if name is None:
        name = ''
    if name == '' and len(selected) == 0:
        return table
    elif name == '' and len(selected) > 0:
        for s in selected:
            table.pop(s)
    elif name != '':
        row = {'Name': name, 'Id': len(table)}
        table.append(row)
    print(table)
    return table


@app.callback(Output('newLeagueStatus', 'children'),
              [Input('saveLeagueButton', 'n_clicks'),
               Input('newLeagueTable', 'rows')],
              state=[State('newLeagueTable', 'rows'),
                     State('newLeagueName', 'value')])
def saveLeague(n_clicks, table, name):
    filename = 'data/leagues/{0}.json'.format(name)
    if name in leagues:
        saved = json.load(open(filename))
        return 'Leage {0} already exists'.format(name)
    elif name is None:
        return 'Add League name first!'

    with open(filename, 'w+') as newLeaguefile:
        json.dump(table, newLeaguefile)

    return 'League Created!'

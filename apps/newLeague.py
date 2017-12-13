import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
from bowlingLeague import io
from app import app

leagues = io.getLeagueNames()


layout = html.Div([
    dt.DataTable(rows=[{}], id='table'),
    dcc.Input(placeholder='League Name..', id='leagueName'),
    dcc.Input(placeholder='Player Name..', id='playerName'),
    html.Button('Add Player'),
    html.Button('Save League')
])


@app.callback(Output('table', 'rows'),
              [Input('')])

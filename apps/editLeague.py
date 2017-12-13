import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
from bowlingLeague import io
from app import app

leagues = [''] io.getLeagueNames()


layout = html.Div([
    dcc.DropDown(options=[{'label': i, 'value': i for i in leagues}])
    dt.DataTable(rows=[{}]),
    dcc.Input(placeholder='League Name..'),
    dcc.Input(placeholder='Player Name..'),
    html.Button('Add Player'),
    html.Button('Save League')
])

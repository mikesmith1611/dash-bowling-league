import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt

app = dash.Dash()
app.config.suppress_callback_exceptions = True


def create_league():
    league = html.Div([
        table=dt.DataTable(rows=[{}]),
    ])

    return league

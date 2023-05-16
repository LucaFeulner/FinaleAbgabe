import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go


import Balkendiagramm
import Liniendiagramm
import Streudiagramm
import Mapbox
import Mapbox01


app = dash.Dash()








app.layout = html.Div([
    html.H1("Visualisierungen des Datensets"),
    dcc.Graph(
        id= "Liniendiagramm",
        figure= Liniendiagramm.fig,
        style={'width': '100%', 'height': '600px'}
            ),
        
    dcc.Graph(
        id= "Streudiagramm",
        figure= Streudiagramm.fig,
        style={'width': '100%', 'height': '600px'}
            ),
    dcc.Graph(
        id= "Balkendiagramm",
        figure= Balkendiagramm.fig,
        style={'width': '100%', 'height': '600px'}
            ),
    dcc.Graph(
        id= "Mapbox01",
        figure= Mapbox01.fig,
        style={'width': '100%', 'height': '600px'}
            ),
    dcc.Graph(
        id= "Mapbox",
        figure= Mapbox.fig,
        style={'width': '100%', 'height': '700px'}
            )
])
       


if __name__ == "__main__":
    app.run_server()
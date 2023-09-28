import dash
import dash_bootstrap_components as dbc
import math
from dash.dependencies import Input, Output
#Importamos el frontend

from frontend.main import layout

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = layout

@app.callback(
    Output('salidaCirculo', 'children'),
    Input('entradaCirculo', 'value'),
)

def areaCirculo(entradaCirculo):
    areaCalculadaCirculo = math.pi * (entradaCirculo**2)
    return 'El área del círculo es: ' + str(areaCalculadaCirculo)

if __name__ == '__main__':
    app.run_server(debug=True)
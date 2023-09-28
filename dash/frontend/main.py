import dash
import dash_bootstrap_components as dbc
from dash import html
from navegador.navegador import navegador
from izquierdo.izquierdo import izquierdo
from derecho.derecho import derecho
from barra.barra import boton_inicio, boton_programa_estudiantes, boton_programa_profesional

# Inicializa la aplicación Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Contenido de la página
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(navegador, md=12, style={'background-color': 'teal', 'text-align': 'center'}),
    ]),
    dbc.Row([
        dbc.Col(boton_inicio, md=4, style={'text-align':'center'}),
        dbc.Col(boton_programa_estudiantes, md=4, style={'text-align':'center'}),
        dbc.Col(boton_programa_profesional, md=4, style={'text-align':'center'}),
    ]),
    dbc.Row([
        dbc.Col(izquierdo, md=8, style={'background-color':'papayawhip'}),
        dbc.Col(derecho, md=4, style={'background-color':'snow'}),
    ]),
])

if __name__ == '__main__':
    app.run_server(debug=True)


import dash_bootstrap_components as dbc
from dash import html

# En esta parte se crean lo botones para la barra de navegación

boton_inicio = dbc.NavLink("Inicio", href="#") # En el numeral se coloca la ruta donde se va a llegar
boton_programa_estudiantes = dbc.NavLink("Programa Estudiantes", href="#")
boton_programa_profesional = dbc.NavLink("Programa Profesional", href="#")


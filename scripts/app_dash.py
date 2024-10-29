import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import sqlite3

# Configuración de la aplicación Dash
app = dash.Dash(__name__)

# Ruta de la base de datos SQLite
DB_PATH = "./data/inventario.db"

def cargar_inventario():
    """Carga los datos de inventario desde la base de datos SQLite y los devuelve como un DataFrame."""
    conn = sqlite3.connect(DB_PATH)
    query = "SELECT producto, cantidad, ubicacion FROM inventario"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def cargar_pedidos():
    """Carga los datos de pedidos desde la base de datos (a configurar) y los devuelve como un DataFrame."""
    # Aquí puedes implementar una función para cargar pedidos si tienes una tabla de pedidos en la base de datos.
    return pd.DataFrame({
        "Producto": ["Producto_A", "Producto_B", "Producto_C"],
        "Cantidad": [10, 20, 30],
        "Fecha": ["2024-10-28", "2024-10-27", "2024-10-26"]
    })

# Layout de la aplicación
app.layout = html.Div([
    html.H1("Panel de Control - Gestión de Inventario", style={"textAlign": "center"}),

    # Sección del gráfico de inventario
    html.Div([
        html.H2("Estado del Inventario"),
        dcc.Graph(id="inventario-grafico")
    ], style={"padding": "20px"}),

    # Sección de la tabla de pedidos
    html.Div([
        html.H2("Pedidos Recientes"),
        dcc.Graph(id="pedidos-tabla")
    ], style={"padding": "20px"})
])

# Callback para actualizar el gráfico de inventario
@app.callback(
    Output("inventario-grafico", "figure"),
    Input("inventario-grafico", "id")
)
def actualizar_grafico_inventario(_):
    # Cargar datos del inventario
    df_inventario = cargar_inventario()

    # Crear gráfico de barras para el inventario
    fig = px.bar(
        df_inventario,
        x="producto",
        y="cantidad",
        color="ubicacion",
        title="Inventario por Producto",
        labels={"producto": "Producto", "cantidad": "Cantidad", "ubicacion": "Ubicación"}
    )
    return fig

# Callback para mostrar los pedidos en una tabla
@app.callback(
    Output("pedidos-tabla", "figure"),
    Input("pedidos-tabla", "id")
)
def actualizar_tabla_pedidos(_):
    # Cargar datos de pedidos (esta función se puede mejorar con una base de datos de pedidos)
    df_pedidos = cargar_pedidos()

    # Crear tabla con pedidos
    fig = px.bar(
        df_pedidos,
        x="Producto",
        y="Cantidad",
        title="Pedidos Recientes",
        labels={"Producto": "Producto", "Cantidad": "Cantidad"}
    )
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)

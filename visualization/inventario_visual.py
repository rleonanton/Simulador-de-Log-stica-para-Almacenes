import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scripts.db_config import DB_PATH


def visualizar_inventario():
    """Visualiza el estado del inventario en un gráfico de barras desde la base de datos SQLite."""
    try:
        # Conectarse a la base de datos
        conn = sqlite3.connect(DB_PATH)
        query = "SELECT producto, cantidad FROM inventario"
        inventario = pd.read_sql_query(query, conn)
        conn.close()

        if inventario.empty:
            print("El inventario está vacío. No hay datos para visualizar.")
            return

        # Crear un gráfico de barras para mostrar las cantidades de cada producto
        plt.figure(figsize=(10, 5))
        plt.bar(inventario['producto'], inventario['cantidad'], color='skyblue')
        plt.xlabel('Producto')
        plt.ylabel('Cantidad')
        plt.title('Estado del Inventario')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    except sqlite3.Error as e:
        print(f"Error al acceder a la base de datos: {e}")

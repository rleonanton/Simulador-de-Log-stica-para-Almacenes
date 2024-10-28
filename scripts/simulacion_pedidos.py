import pandas as pd
import random
from datetime import datetime

# Ruta del archivo CSV de pedidos
PEDIDOS_CSV = "./data/pedidos.csv"

def cargar_pedidos():
    """Carga los datos de pedidos desde un archivo CSV."""
    try:
        pedidos = pd.read_csv(PEDIDOS_CSV)
        if pedidos.empty or pedidos.columns.tolist() != ["ID Pedido", "Producto", "Cantidad", "Fecha"]:
            raise ValueError("Archivo de pedidos vacío o columnas incorrectas")
        print("Pedidos cargados correctamente.")
    except (FileNotFoundError, ValueError):
        print("Archivo de pedidos no encontrado o vacío. Creando uno nuevo.")
        pedidos = pd.DataFrame(columns=["ID Pedido", "Producto", "Cantidad", "Fecha"])
        pedidos.to_csv(PEDIDOS_CSV, index=False)
    return pedidos


def generar_pedido(inventario):
    """
    Genera un pedido aleatorio basado en los productos disponibles en el inventario.
    """
    productos_disponibles = inventario["Producto"].values
    if len(productos_disponibles) == 0:
        print("No hay productos disponibles para generar pedidos.")
        return None

    producto = random.choice(productos_disponibles)
    cantidad = random.randint(1, 5)  # Cantidad aleatoria entre 1 y 5
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return {"Producto": producto, "Cantidad": cantidad, "Fecha": fecha}

def procesar_pedido(inventario, pedidos, pedido):
    """
    Procesa un pedido y actualiza el inventario si el producto está disponible.
    """
    if pedido is None:
        print("No se pudo generar el pedido.")
        return

    producto = pedido["Producto"]
    cantidad = pedido["Cantidad"]

    if producto in inventario["Producto"].values:
        stock_actual = inventario.loc[inventario["Producto"] == producto, "Cantidad"].values[0]
        if stock_actual >= cantidad:
            # Actualizar inventario
            inventario.loc[inventario["Producto"] == producto, "Cantidad"] -= cantidad
            # Registrar pedido
            nuevo_pedido = {
                "ID Pedido": len(pedidos) + 1,
                "Producto": producto,
                "Cantidad": cantidad,
                "Fecha": pedido["Fecha"]
            }
            pedidos = pedidos.append(nuevo_pedido, ignore_index=True)
            print(f"Pedido procesado correctamente: {nuevo_pedido}")
        else:
            print(f"Stock insuficiente para el producto: {producto}")
    else:
        print(f"Producto no encontrado en el inventario: {producto}")

    return pedidos

def guardar_pedidos(pedidos):
    """Guarda los datos de los pedidos en un archivo CSV."""
    pedidos.to_csv(PEDIDOS_CSV, index=False)
    print("Pedidos guardados correctamente.")

import sqlite3
from db_config import DB_PATH

def conectar_bd():
    """Establece una conexión con la base de datos."""
    return sqlite3.connect(DB_PATH)

def cargar_inventario():
    """Carga los datos del inventario desde la base de datos SQLite."""
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("SELECT producto, cantidad, ubicacion FROM inventario")
    inventario = cursor.fetchall()
    conn.close()
    if not inventario:
        print("El inventario está vacío.")
    return inventario

def consultar_inventario():
    """Muestra el inventario actual desde la base de datos."""
    inventario = cargar_inventario()
    if inventario:
        print("Inventario Actual:")
        for producto, cantidad, ubicacion in inventario:
            print(f"Producto: {producto}, Cantidad: {cantidad}, Ubicación: {ubicacion}")

def agregar_producto(producto, cantidad, ubicacion="No especificada"):
    """Agrega un nuevo producto al inventario en la base de datos."""
    conn = conectar_bd()
    cursor = conn.cursor()

    # Verificar si el producto ya existe
    cursor.execute("SELECT cantidad FROM inventario WHERE producto = ?", (producto,))
    resultado = cursor.fetchone()

    if resultado:
        # Actualizar la cantidad existente
        cursor.execute("UPDATE inventario SET cantidad = cantidad + ? WHERE producto = ?", (cantidad, producto))
    else:
        # Insertar un nuevo producto
        cursor.execute("INSERT INTO inventario (producto, cantidad, ubicacion) VALUES (?, ?, ?)", (producto, cantidad, ubicacion))

    conn.commit()
    conn.close()
    print(f"Producto '{producto}' agregado/actualizado correctamente.")

def actualizar_stock(producto, cantidad):
    """Actualiza el stock de un producto en el inventario."""
    conn = conectar_bd()
    cursor = conn.cursor()

    # Verificar si el producto existe
    cursor.execute("SELECT cantidad FROM inventario WHERE producto = ?", (producto,))
    resultado = cursor.fetchone()

    if resultado:
        # Actualizar la cantidad existente
        cursor.execute("UPDATE inventario SET cantidad = cantidad + ? WHERE producto = ?", (cantidad, producto))
        conn.commit()
        print(f"Stock actualizado para el producto: {producto}")
    else:
        print(f"Producto '{producto}' no encontrado en el inventario.")
    
    conn.close()

import sqlite3
from db_config import DB_PATH

def cargar_productos_iniciales():
    """Carga 20 productos iniciales en la base de datos SQLite."""
    productos = [
        ("Producto_A", 50, "Ubicacion_1"),
        ("Producto_B", 30, "Ubicacion_2"),
        ("Producto_C", 20, "Ubicacion_3"),
        ("Producto_D", 60, "Ubicacion_4"),
        ("Producto_E", 10, "Ubicacion_5"),
        ("Producto_F", 45, "Ubicacion_6"),
        ("Producto_G", 35, "Ubicacion_7"),
        ("Producto_H", 15, "Ubicacion_8"),
        ("Producto_I", 70, "Ubicacion_9"),
        ("Producto_J", 25, "Ubicacion_10"),
        ("Producto_K", 55, "Ubicacion_1"),
        ("Producto_L", 40, "Ubicacion_2"),
        ("Producto_M", 65, "Ubicacion_3"),
        ("Producto_N", 30, "Ubicacion_4"),
        ("Producto_O", 75, "Ubicacion_5"),
        ("Producto_P", 20, "Ubicacion_6"),
        ("Producto_Q", 50, "Ubicacion_7"),
        ("Producto_R", 35, "Ubicacion_8"),
        ("Producto_S", 60, "Ubicacion_9"),
        ("Producto_T", 45, "Ubicacion_10")
    ]

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Insertar los productos
    cursor.executemany("INSERT INTO inventario (producto, cantidad, ubicacion) VALUES (?, ?, ?)", productos)
    
    conn.commit()
    conn.close()
    print("20 productos cargados en el inventario correctamente.")

# Ejecutar la función para cargar los productos iniciales
if __name__ == "__main__":
    cargar_productos_iniciales()

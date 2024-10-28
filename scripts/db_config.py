import sqlite3

# Ruta de la base de datos SQLite
DB_PATH = "./data/inventario.db"

def crear_tabla_inventario():
    """Crea la tabla de inventario si no existe."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Crear la tabla de inventario
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inventario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            producto TEXT NOT NULL,
            cantidad INTEGER NOT NULL,
            ubicacion TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    print("Tabla de inventario creada correctamente.")

if __name__ == "__main__":
    crear_tabla_inventario()

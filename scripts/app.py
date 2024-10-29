import tkinter as tk
from tkinter import ttk, messagebox
from gestion_inventario import consultar_inventario, actualizar_stock, agregar_producto
from simulacion_pedidos import cargar_pedidos, generar_pedido, procesar_pedido, guardar_pedidos
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.optimizacion_rutas import optimizar_ruta
from visualization.inventario_visual import visualizar_inventario

def configurar_estilos():
    style = ttk.Style()
    style.theme_use("clam")  # Puedes cambiar el tema a "alt", "default", etc.
    style.configure("TButton", font=("Arial", 12, "bold"), background="#00adb5", foreground="#ffffff")
    style.configure("TLabel", font=("Arial", 12), background="#2e3f4f", foreground="#ffffff")
    style.configure("TNotebook", background="#2e3f4f")
    style.configure("TNotebook.Tab", font=("Arial", 12))

def mostrar_inventario():
    """Función para consultar y mostrar el inventario en la interfaz."""
    inventario = consultar_inventario()
    if not inventario:
        messagebox.showinfo("Inventario", "El inventario está vacío.")
    else:
        messagebox.showinfo("Inventario", "\n".join([f"{p[0]}: {p[1]} unidades" for p in inventario]))

def agregar_producto_interfaz():
    """Función para agregar un producto al inventario mediante un formulario en la interfaz."""
    def guardar_producto():
        producto = entry_producto.get()
        cantidad = int(entry_cantidad.get())
        ubicacion = entry_ubicacion.get()
        
        agregar_producto(producto, cantidad, ubicacion)
        messagebox.showinfo("Éxito", f"Producto '{producto}' agregado correctamente.")
        window_agregar.destroy()

    window_agregar = tk.Toplevel(root)
    window_agregar.title("Agregar Producto")

    ttk.Label(window_agregar, text="Producto:").pack(pady=5)
    entry_producto = ttk.Entry(window_agregar)
    entry_producto.pack(pady=5)

    ttk.Label(window_agregar, text="Cantidad:").pack(pady=5)
    entry_cantidad = ttk.Entry(window_agregar)
    entry_cantidad.pack(pady=5)

    ttk.Label(window_agregar, text="Ubicación:").pack(pady=5)
    entry_ubicacion = ttk.Entry(window_agregar)
    entry_ubicacion.pack(pady=5)

    ttk.Button(window_agregar, text="Guardar", command=guardar_producto).pack(pady=10)

def actualizar_stock_interfaz():
    """Función para actualizar el stock de un producto mediante un formulario en la interfaz."""
    def guardar_actualizacion():
        producto = entry_producto.get()
        cantidad = int(entry_cantidad.get())
        
        actualizar_stock(producto, cantidad)
        messagebox.showinfo("Éxito", f"Stock del producto '{producto}' actualizado correctamente.")
        window_actualizar.destroy()

    window_actualizar = tk.Toplevel(root)
    window_actualizar.title("Actualizar Stock")

    ttk.Label(window_actualizar, text="Producto:").pack(pady=5)
    entry_producto = ttk.Entry(window_actualizar)
    entry_producto.pack(pady=5)

    ttk.Label(window_actualizar, text="Cantidad a agregar/reducir:").pack(pady=5)
    entry_cantidad = ttk.Entry(window_actualizar)
    entry_cantidad.pack(pady=5)

    ttk.Button(window_actualizar, text="Guardar", command=guardar_actualizacion).pack(pady=10)

def visualizar_inventario_interfaz():
    """Función para visualizar el estado del inventario en un gráfico."""
    visualizar_inventario()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Gestión de Inventario")
root.geometry("500x400")
root.configure(bg="#2e3f4f")

# Configurar estilos
configurar_estilos()

# Configuración de pestañas
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# Pestaña para gestionar el inventario
frame_inventario = ttk.Frame(notebook)
notebook.add(frame_inventario, text="Inventario")

ttk.Button(frame_inventario, text="Consultar Inventario", command=mostrar_inventario).pack(pady=10)
ttk.Button(frame_inventario, text="Agregar Producto", command=agregar_producto_interfaz).pack(pady=10)
ttk.Button(frame_inventario, text="Actualizar Stock", command=actualizar_stock_interfaz).pack(pady=10)

# Pestaña para visualizar el inventario
frame_visualizacion = ttk.Frame(notebook)
notebook.add(frame_visualizacion, text="Visualización")

ttk.Button(frame_visualizacion, text="Visualizar Inventario", command=visualizar_inventario_interfaz).pack(pady=20)

# Botón de salida en la ventana principal
ttk.Button(root, text="Salir", command=root.quit).pack(pady=20)

# Ejecutar la ventana principal
root.mainloop()
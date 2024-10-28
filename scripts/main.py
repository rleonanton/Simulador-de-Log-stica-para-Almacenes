from gestion_inventario import consultar_inventario, actualizar_stock, agregar_producto
from simulacion_pedidos import cargar_pedidos, generar_pedido, procesar_pedido, guardar_pedidos
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.optimizacion_rutas import optimizar_ruta
from visualization.inventario_visual import visualizar_inventario

def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Consultar Inventario")
    print("2. Agregar Producto")
    print("3. Actualizar Stock")
    print("4. Simular Pedido")
    print("5. Guardar Pedidos")
    print("6. Optimizar Ruta")
    print("7. Visualizar Inventario")
    print("8. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            consultar_inventario()
        elif opcion == "2":
            producto = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            ubicacion = input("Ubicación (opcional): ")
            agregar_producto(producto, cantidad, ubicacion)
        elif opcion == "3":
            producto = input("Nombre del producto: ")
            cantidad = int(input("Cantidad a actualizar (puede ser negativa): "))
            actualizar_stock(producto, cantidad)
        elif opcion == "4":
            print("Función para simular pedido aún no está implementada para SQLite.")
        elif opcion == "5":
            print("Función para guardar pedidos aún no está implementada para SQLite.")
        elif opcion == "6":
            optimizar_ruta()
        elif opcion == "7":
            visualizar_inventario()
        elif opcion == "8":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione nuevamente.")

if __name__ == "__main__":
    main()

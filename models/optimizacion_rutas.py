from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import pandas as pd

# Ruta del archivo CSV de rutas
RUTAS_CSV = "./data/rutas.csv"

def cargar_datos_rutas():
    """Carga los datos de rutas desde un archivo CSV."""
    datos = pd.read_csv(RUTAS_CSV)
    return datos

def calcular_matriz_distancias(datos):
    """Calcula la matriz de distancias entre los puntos."""
    num_puntos = len(datos)
    matriz_distancias = [[0] * num_puntos for _ in range(num_puntos)]

    for i in range(num_puntos):
        for j in range(num_puntos):
            if i != j:
                distancia = ((datos.loc[i, "Coordenada_X"] - datos.loc[j, "Coordenada_X"])**2 + 
                             (datos.loc[i, "Coordenada_Y"] - datos.loc[j, "Coordenada_Y"])**2) ** 0.5
                matriz_distancias[i][j] = int(distancia)
    
    return matriz_distancias

def optimizar_ruta():
    """Optimiza las rutas utilizando OR-Tools."""
    datos = cargar_datos_rutas()
    matriz_distancias = calcular_matriz_distancias(datos)

    # Parámetros del problema
    num_puntos = len(matriz_distancias)
    num_vehiculos = 1
    nodo_inicio = 0

    # Crear el gestor de datos
    gestor = pywrapcp.RoutingIndexManager(num_puntos, num_vehiculos, nodo_inicio)

    # Crear el modelo de enrutamiento
    routing = pywrapcp.RoutingModel(gestor)

    # Crear una función de distancia entre puntos
    def distance_callback(from_index, to_index):
        # Convierte los índices de enrutamiento a los índices de la matriz de distancia
        from_node = gestor.IndexToNode(from_index)
        to_node = gestor.IndexToNode(to_index)
        return matriz_distancias[from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Establecer la función de costo de la distancia
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Solucionar el problema de enrutamiento
    parametros = pywrapcp.DefaultRoutingSearchParameters()
    parametros.first_solution_strategy = (routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
    solucion = routing.SolveWithParameters(parametros)

    # Imprimir la solución
    if solucion:
        print("Ruta óptima encontrada:")
        index = routing.Start(0)
        ruta = []
        while not routing.IsEnd(index):
            ruta.append(gestor.IndexToNode(index))
            index = solucion.Value(routing.NextVar(index))
        ruta.append(gestor.IndexToNode(index))
        print(" -> ".join(str(datos.loc[i, "Punto"]) for i in ruta))
    else:
        print("No se encontró una solución óptima.")


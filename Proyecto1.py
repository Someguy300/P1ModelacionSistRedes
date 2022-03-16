import math
import collections
from sys import maxsize
from collections import deque
from collections import defaultdict

# agregamos lado

def add_edge(adj, src, dest, weight):
    adj[src][dest] = weight
    adj[dest][src] = weight

# Eliminar nodo para cuando no tenga visa

def delete_node(adj, vertex):
    for neighbor in list(adj[vertex]):
        if neighbor != vertex:
            adj[neighbor].pop(vertex)
    del adj[vertex]

# Metodo de camino corto

def find_paths(paths, path, parents, vertices, dest, all_cities):

    # Inicio de la funcion recursiva
    if (dest == -1):
        paths.append(path.copy())
        return

    # Ir eliminando todos los nodos padres hasta llegar al destino
    for parent in parents[dest]:

        # Agregamos el nodo destino
        path.append(dest)

        # recursividad
        find_paths(paths, path, parents, vertices, parent, all_cities)

        # sacar nodo
        path.pop()


def bfs(adj, parent, vertices, source, all_cities):
    # Busqueda por anchura
    dist = [maxsize for _ in range(vertices)]
    queue = deque()

    # Insertamos el destino en la cola, asi de tal forma que el padre esta en -1 consiguiendo una distancia de 0 consigo mismo
    queue.append(source)
    parent[source] = [-1]
    dist[source] = 0

    # No nos detenemos hasta que no haya mas cola
    while queue:

        u = queue[0]
        queue.popleft()

        for v in adj[u]:

            if (dist[v] > dist[u] + 1):

                # para cortar distancia borramos padres 
                dist[v] = dist[u] + 1
                queue.append(v)
                parent[v].clear()
                parent[v].append(u)

            elif (dist[v] == dist[u] + 1):
                # Sacamos el candidato a 
                parent[v].append(u)


def print_paths(old_adj, vertices, start, dest, all_cities):

    # Pasamos los nombres de las ciudades a una lista vacia para poder recorrerlas 
    adj = []
    for key, value in old_adj.items():
        node_list = []
        for neighbor in value:
            node_list.append(all_cities.index(neighbor))
        adj.append(node_list)
    # valores iniciales 
    paths = []
    path = []
    parent = [[] for i in range(vertices)]

    bfs(adj, parent, vertices, start, all_cities)
    find_paths(paths, path, parent, vertices, dest, all_cities)

    # La ruta mas corta
    print("La(s) ruta(s) con menos segmentos es(son): ")
    for path in paths:

        # Revertimos el orden la la lista ya que tomamos todo desde el destino
        path = reversed(path)

        # los nodos
        print("[", end=" ")
        for node in path:
            print(all_cities[node], end=", ")
        print("]")


# ** cheapest path
# def dijkstra(graph, source, target):
#
#    unvisited_nodes = graph
#    shortest_distance = {}
#    path = []
#    predecessor = {}
#
#    # Iterating through all the unvisited nodes
#    for nodes in unvisited_nodes:
#        shortest_distance[nodes] = math.inf
#
    # The distance of a point to itself is 0.
#    shortest_distance[source] = 0
#
#   while(unvisited_nodes):
#
#       # setting the value of min_node as None
#        min_node = None
#
#        for current_node in unvisited_nodes:
#
#            if min_node is None:
#                min_node = current_node
#            elif shortest_distance[min_node] > shortest_distance[current_node]:
#                min_node = current_node
#
#        for child_node, value in unvisited_nodes[min_node].items():
#
#            if value + shortest_distance[min_node] < shortest_distance[child_node]:
#
#                shortest_distance[child_node] = value + \
#                    shortest_distance[min_node]
#                predecessor[child_node] = min_node
#
#        unvisited_nodes.pop(min_node)
#
#    node = target
#
#    while node != source:
#
#        try:
#            path.insert(0, node)
#            node = predecessor[node]
#        except Exception:
#            print('No hay forma de llegar')
#            break
#
#    path.insert(0, source)
#
#    if shortest_distance[target] != math.inf:
#
#        print('La ruta mas barata tiene un costo de ' +
#              str(shortest_distance[target]) + ', y el camino es ' + str(path))


#Class to represent a graph
class Graph:

    # A utility function to find the
    # vertex with minimum dist value, from
    # the set of vertices still in queue
    def minDistance(self, dist, queue):
        # Initialize min value and min_index as -1
        minimum = float("Inf")
        min_index = -1

        # from the dist array,pick one which
        # has min value and is till in queue
        for i in range(len(dist)):
            if dist[i] < minimum and i in queue:
                minimum = dist[i]
                min_index = i
        return min_index

    # Function to print shortest path
    # from source to j
    # using parent array

    def printPath(self, parent, j):

        #Base Case : If j is source
        if parent[j] == -1:
            print(j, end=" ")
            return
        self.printPath(parent, parent[j])
        print(j, end=" ")

    # A utility function to print
    # the constructed distance
    # array

    def printSolution(self, dist, parent):
        src = 0
        print("Vertex \t\tDistance from Source\tPath")
        for i in range(1, len(dist)):
            print("\n%d --> %d \t\t%d \t\t\t\t\t" % (src, i, dist[i]), end=" ")
            self.printPath(parent, i)


  # def dijkstra(graph, source, target):
    def dijkstra(self, graph, src):

        row = len(graph)
        col = len(graph[0])

        # The output array. dist[i] will hold
        # the shortest distance from src to i
        # Initialize all distances as INFINITE
        dist = [float("Inf")] * row

        #Parent array to store
        # shortest path tree
        parent = [-1] * row

        # Distance of source vertex
        # from itself is always 0
        dist[src] = 0

        # Add all vertices in queue
        queue = []
        for i in range(row):
            queue.append(i)

        #Find shortest path for all vertices
        while queue:

            # Pick the minimum dist vertex
            # from the set of vertices
            # still in queue
            u = self.minDistance(dist, queue)

            # remove min element
            queue.remove(u)

            # Update dist value and parent
            # index of the adjacent vertices of
            # the picked vertex. Consider only
            # those vertices which are still in
            # queue
            for i in range(col):
                '''Update dist[i] only if it is in queue, there is
                an edge from u to i, and total weight of path from
                src to i through u is smaller than current value of
                dist[i]'''
                if graph[u][i] and i in queue:
                    if dist[u] + graph[u][i] < dist[i]:
                        dist[i] = dist[u] + graph[u][i]
                        parent[i] = u

        # print the constructed distance array
        self.printSolution(dist, parent)


g = Graph()



# Print the solution
#g.dijkstra(graph, 0)


# main

# variables
all_cities = ["CCS", "AUA", "BON", "CUR", "SXM",
              "SDQ", "SBH", "POS", "BGI", "FDF", "PTP"]
places = all_cities
need_visa_cities = ["AUA", "BON", "CUR", "SXM", "SDQ"]
vertices = len(all_cities)
index = 0

# we create the adjacency list
adj = collections.defaultdict(dict)

# we create the graph
add_edge(adj, "CCS", "AUA", 40)
add_edge(adj, "CCS", "CUR", 35)
add_edge(adj, "CCS", "BON", 60)
add_edge(adj, "CCS", "SDQ", 180)
add_edge(adj, "CCS", "POS", 150)
add_edge(adj, "CCS", "BGI", 180)
add_edge(adj, "AUA", "CUR", 15)
add_edge(adj, "AUA", "BON", 15)
add_edge(adj, "CUR", "BON", 15)
add_edge(adj, "SDQ", "SXM", 50)
add_edge(adj, "SXM", "SBH", 45)
add_edge(adj, "POS", "BGI", 35)
add_edge(adj, "POS", "SXM", 90)
add_edge(adj, "POS", "PTP", 80)
add_edge(adj, "POS", "FDF", 75)
add_edge(adj, "BGI", "SXM", 70)
add_edge(adj, "PTP", "SXM", 100)
add_edge(adj, "PTP", "SBH", 80)
add_edge(adj, "CUR", "SXM", 80)
add_edge(adj, "AUA", "SXM", 85)

# we ask if the person has a visa
print("Bienvenido a la Agencias de Viajes Metro Travel.")
print("¿Usted posee visa para viajar?")
print("[1] Sí")
print("[2] No")

# we have to validate the user input
while True:
    try:
        has_visa = int(input())
    except ValueError:
        print("¿Usted posee visa para viajar?")
        print("[1] Sí")
        print("[2] No")
        continue
    else:
        # we validate if the selected option is available
        if (has_visa == 1 or has_visa == 2):
            break
        else:
            print("¿Usted posee visa para viajar?")
            print("[1] Sí")
            print("[2] No")
            continue

# if he doesn't have a visa, delete the cities that need visa from the graph
if has_visa == 2:
    for city_visa in need_visa_cities:
        delete_node(adj, city_visa)
        all_cities.remove(city_visa)

# first, we ask the origin and destiny
while True:
    print("Los aeropuertos disponibles son:")
    for city in all_cities:
        print(city, end=', ')
    print("Ingrese el codigo del aeropuerto de origen para su viaje:")
    src = input().upper()
    if src.strip() == '':
        print("Debe ingresar un nombre")
        continue
    elif src not in all_cities:
        print("Ingrese un codigo valido")
        continue
    else:
        break

while True:
    print("Los aeropuertos disponibles son:")
    for city in all_cities:
        print(city, end=', ')
    print("Ingrese el codigo del aeropuerto de destino para su viaje:")
    dest = input().upper()
    if dest.strip() == '':
        print("Debe ingresar un nombre")
        continue
    elif dest not in all_cities:
        print("Ingrese un codigo valido")
        continue
    else:
        break


# now, we ask which type of route he wants
print("Seleccione el tipo de ruta que desea")
print("[1] Ruta mas barata")
print("[2] Ruta con menos segmentos")

while True:
    try:
        route_type = int(input())
    except ValueError:

        print("Seleccione el tipo de ruta que desea")
        print("[1] Ruta mas barata")
        print("[2] Ruta con menos segmentos")
        continue
    else:
        # we validate if the selected option is available
        if (route_type == 1 or route_type == 2):
            break
        else:

            print("Seleccione el tipo de ruta que desea")
            print("[1] Ruta mas barata")
            print("[2] Ruta con menos segmentos")
            continue

if has_visa == 2 and dest in need_visa_cities:
    print("No posee la visa requerida para entrar")
elif route_type == 1:
    dijkstra(adj, src)
else:
    print_paths(adj, vertices, all_cities.index(
        src), all_cities.index(dest), all_cities)






print("""Sistema de gestion de viajes Agencia de Viajes Metro Travel
Antes de gestionar su viaje debemos preguntarle:""")

while True:
    print("¿Usted posee visa?")
    print("Presione [y] y [Enter] para Si")
    print("Presione [n] y [Enter] para No")
    inputVisa = input()
    if inputVisa == 'y' or inputVisa == 'n':
        break
    else:
        print("Ingrese un valor valido [y] o [n]")


print()
if inputVisa == 'y':
    print("Dada su disponibilidad de visa estas sus sus siguientes opciones para su aeropuerto de origen")
else:
    print("Dada su no disponibilidad de visa estas sus sus siguientes opciones para su aeropuerto de origen")

#INSERTAR AEROPUERTOS DE ORIGEN E INPUT AQUI

print()
print("Los aeropuertos disponibles como aeropuertos destino son:")

#INSERTAR AEROPUERTOS DESTINO E INPUT AQUI

print()
print("""Como desea planear su viaje?
Escogiendo la ruta mas barata? ó
Escogiendo la ruta con numero de vuelos minima?""")



while True:
    try:
        print("Presione [1] y [Enter] para ruta mas barata")
        print("Presione [2] y [Enter] para numero de vuelos minima")
        inputCriterio = int(input())
    except Exception:
        print("Ingrese un valor valido [1] o [2]")
        continue
    else:
        if inputCriterio == 1 or inputCriterio == 2:
            break
        else:
            print("Ingrese un valor valido [1] o [2]")

print()
if inputVisa == 1:
    print("Su viaje de acuerdo a la ruta mas barata es el siguiente")
else:
    print("Su viaje de acuerdo a la ruta con el minimo numero de vuelos es el siguiente")

#MOSTRAR RUTAS CON COSTO AQUI

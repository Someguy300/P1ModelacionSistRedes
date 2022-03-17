import sys
import math
import collections
from sys import maxsize
from collections import deque
from collections import defaultdict
from typing import final

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
    print("La ruta con menos segmentos es: ")
    weight = 0
    i=0
    for path in paths:
        # Revertimos el orden la la lista ya que tomamos todo desde el destino
        path = reversed(path)
        path = list(path)
        # los nodos
        for node in path:
            i = i+1
            print(all_cities[node], end=" -> ")
            try:
                weight = weight + old_adj[all_cities[node]][all_cities[path[i]]]
            except Exception:
                pass
    print("Y tiene un costo de: " + str(weight))


class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)
        
    def construct_graph(self, nodes, init_graph):
        '''
        This method makes sure that the graph is symmetrical. In other words, if there's a path from node A to B with a value V, there needs to be a path from node B to node A with a value V.
        '''
        graph = {}
        for node in nodes:
            graph[node] = {}
        
        graph.update(init_graph)
        
        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value
                    
        return graph
    
    def get_nodes(self):
        "Returns the nodes of the graph."
        return self.nodes
    
    def get_outgoing_edges(self, node):
        "Returns the neighbors of a node."
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections
    
    def value(self, node1, node2):
        "Returns the value of an edge between two nodes."
        return self.graph[node1][node2]


def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node
    
    while node != start_node:
        path.append(node)
        node = previous_nodes[node]
 
    # Add the start node manually
    path.append(start_node)
    
    print("La ruta mas barata tiene un costo de {}.".format(shortest_path[target_node]))
    print("Y la ruta es: ")
    print(" -> ".join(reversed(path)))

def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())
 
    # We'll use this dict to save the cost of visiting each node and update it as we move along the graph   
    shortest_path = {}
 
    # We'll use this dict to save the shortest known path to a node found so far
    previous_nodes = {}
 
    # We'll use max_value to initialize the "infinity" value of the unvisited nodes   
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    # However, we initialize the starting node's value with 0   
    shortest_path[start_node] = 0
    
    # The algorithm executes until we visit all nodes
    while unvisited_nodes:
        # The code block below finds the node with the lowest score
        current_min_node = None
        for node in unvisited_nodes: # Iterate over the nodes
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
                
        # The code block below retrieves the current node's neighbors and updates their distances
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                # We also update the best path to the current node
                previous_nodes[neighbor] = current_min_node
 
        # After visiting its neighbors, we mark the node as "visited"
        unvisited_nodes.remove(current_min_node)
    
    return previous_nodes, shortest_path



# main

while True:
    # variables
    all_cities = ["CCS", "AUA", "BON", "CUR", "SXM",
                "SDQ", "SBH", "POS", "BGI", "FDF", "PTP"]
    need_visa_cities = ["AUA", "BON", "CUR", "SXM", "SDQ"]
    vertices = len(all_cities)
    index = 0
    repeatProgram = 0

    init_graph = {}
    for node in all_cities:
        init_graph[node] = {}
    # we create the graph
    init_graph["CCS"]["AUA"]=40
    init_graph["CCS"]["CUR"]=35
    init_graph["CCS"]["BON"]=60
    init_graph["CCS"]["SDQ"]=180
    init_graph["CCS"]["POS"]=150
    init_graph["CCS"]["BGI"]=180
    init_graph["AUA"]["CUR"]=15
    init_graph["AUA"]["BON"]=15
    init_graph["CUR"]["BON"]=15
    init_graph["SDQ"]["SXM"]=50
    init_graph["SXM"]["SBH"]=45
    init_graph["POS"]["BGI"]=35
    init_graph["POS"]["SXM"]=90
    init_graph["POS"]["PTP"]=80
    init_graph["POS"]["FDF"]=75
    init_graph["BGI"]["SXM"]=70
    init_graph["PTP"]["SXM"]=100
    init_graph["PTP"]["SBH"]=80
    init_graph["CUR"]["SXM"]=80
    init_graph["AUA"]["SXM"]=85
    graph = Graph(all_cities, init_graph)

    # we ask if the person has a visa
    print("--------------------------------------------------------------")
    print()
    print("Bienvenido a la Agencias de Viajes Metro Travel.")


    # we have to validate the user input
    while True:
        try:
            print("¿Usted posee visa para viajar?")
            print("Presione [1] y Enter para Sí")
            print("Presione [2] y Enter para No")
            has_visa = int(input())
        except Exception:
            print()
            print("Valor incorrecto, presione las teclas indicadas")
            print()
            continue
        else:
            # we validate if the selected option is available
            if (has_visa == 1 or has_visa == 2):
                break
            else:
                print()
                print("Valor incorrecto, presione las teclas indicadas")
                print()
                continue

    print("--------------------------------------------------------------")
    print()

    # if he doesn't have a visa, delete the cities that need visa from the graph
    if has_visa == 2:
        for city_visa in need_visa_cities:
            delete_node(init_graph, city_visa)
            all_cities.remove(city_visa)

    # first, we ask the origin and destiny
    while True:
        print("De acuerdo a su disponibilidad de visa los aeropuertos para iniciar su viaje disponibles son:")
        for city in all_cities:
            print(city, end=', ')
        print()
        print("Ingrese el codigo del aeropuerto de origen para su viaje:")
        src = input().upper()
        if src.strip() == '':
            print()
            print("Valor incorrecto, debe ingresar un nombre valido de la lista")
            print()
            continue
        elif src not in all_cities:
            print()
            print("Ingrese un codigo valido")
            print()
            continue
        else:
            break

    print("--------------------------------------------------------------")
    print()

    while True:
        print("Los aeropuertos destino disponibles son:")
        for city in all_cities:
            print(city, end=', ')
        print()
        print("Ingrese el codigo del aeropuerto de destino para su viaje:")
        dest = input().upper()
        if dest.strip() == '':
            print()
            print("Debe ingresar un nombre valido de la lista")
            print()
            continue
        elif dest not in all_cities:
            print()
            print("Ingrese un codigo valido")
            print()
            continue
        else:
            break

    print("--------------------------------------------------------------")
    print()
    # now, we ask which type of route he wants
    while True:
        try:
            print("Seleccione el tipo de ruta que desea")
            print("Presione [1] y [Enter] Ruta mas barata")
            print("Presione [2] y [Enter] Ruta con menos segmentos")
            route_type = int(input())
        except Exception:
            print()
            print("Valor incorrecto, presione las teclas indicadas")
            print()
            continue
        else:
            # we validate if the selected option is available
            if (route_type == 1 or route_type == 2):
                break
            else:
                print()
                print("Valor incorrecto, presione las teclas indicadas")
                print()
                continue

    if has_visa == 2 and dest in need_visa_cities:
        print("No posee la visa requerida para entrar")
    elif route_type == 1:
        previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node=src)
        print_result(previous_nodes, shortest_path, start_node=src, target_node=dest)
    else:
        print_paths(init_graph, vertices, all_cities.index(src), all_cities.index(dest), all_cities)
    print()
    print("Presione [Enter] para continuar")
    input()

    print("--------------------------------------------------------------")
    print()
    
    # we have to validate the user input
    while True:
        try:
            print("¿Desea correr de nuevo el programa?")
            print("Presione [1] y Enter para Sí")
            print("Presione [2] y Enter para No")
            repeatProgram = int(input())
        except Exception:
            print()
            print("Valor incorrecto, presione las teclas indicadas")
            continue
        else:
            # we validate if the selected option is available
            if (repeatProgram == 1 or repeatProgram == 2):
                break
            else:
                print()
                print("Valor incorrecto, presione las teclas indicadas")
                continue

    if (repeatProgram == 1):
        continue
    elif repeatProgram == 2:
        print()
        print("Gracias por usar el programa de la Agencias de Viajes Metro Travel")
        break
    






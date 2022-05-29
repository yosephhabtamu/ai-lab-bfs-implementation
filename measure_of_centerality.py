
from fileinput import close
from graph_algorithms_implemetations import *

from graph_analysis import *


class Centrality_measure:
    def __init__(self, file_name: str) -> None:
        self.graph = create_graph(file_name)[0]
        self.heuristic = create_graph(file_name)[1]

    def find_degree_of_vertex(self, vertex: Node):
        return len(vertex.edge_list)

    def measure_degree(self):
        largest_nodes = []
        num = -inf
        for i in self.graph._verticies:
            temp = self.find_degree_of_vertex(self.graph._verticies[i])
            if temp > num:
                largest_nodes = []
                largest_nodes.append(i)
                num = temp
            elif temp == num:
                largest_nodes.append(i)
        return largest_nodes

    def closeness_for_djikstra(self):
        total_distance = {}
        for i in self.graph._verticies:
            distance = self.graph.dijkstra_algorithm(i)
            total = 0
            for j in distance:
                total += distance[j]
            total_distance[i] = (len(self.graph._verticies)/total)*1000
        most_connected = []
        num = -inf
        for i in total_distance:
            temp = total_distance[i]
            if temp > num:
                most_connected = []
                most_connected.append(i)
                num = temp
            elif temp == num:
                most_connected.append(i)

        return total_distance, most_connected

    def closeness_for_a_star(self):
        total_distance = {}
        for i in self.graph._verticies:
            for j in self.graph._verticies:
                if i == j:
                    continue
                distance = self.graph.a_star_search(i, j, self.heuristic)[0]
            total = 0
            for j in distance:
                if distance[j] == inf:
                    continue
                total += distance[j]
            total_distance[i] = (len(self.graph._verticies)/total)*1000
        most_connected = []
        num = -inf
        for i in total_distance:
            temp = total_distance[i]
            if temp > num:
                most_connected = []
                most_connected.append(i)
                num = temp
            elif temp == num:
                most_connected.append(i)

        return total_distance, most_connected


c = Centrality_measure('data.txt')
result = c.closeness_for_djikstra()
print(result)

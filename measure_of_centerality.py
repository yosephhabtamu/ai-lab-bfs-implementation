

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
        each_node_and_degree = {}
        num = -inf
        for i in self.graph._verticies:
            temp = self.find_degree_of_vertex(self.graph._verticies[i])

            each_node_and_degree[i] = (temp /
                                       (len(self.graph._verticies)-1))
            if temp > num:
                largest_nodes = []
                largest_nodes.append(i)
                num = temp
            elif temp == num:
                largest_nodes.append(i)
        return largest_nodes, each_node_and_degree

    def closeness_for_djk(self):
        total_distance = {}
        for i in self.graph._verticies:
            distance = self.graph.dijkstra_algorithm(i)[0]
            total = 0
            for j in distance:
                total += distance[j]
            total_distance[i] = (len(self.graph._verticies)/total)
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
            total = 0
            for j in self.graph._verticies:
                if i == j:
                    continue
                distance = self.graph.a_star_search(i, j, self.heuristic)[0]
                total += distance[j]
            total_distance[i] = (len(self.graph._verticies)/total)
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

    def betweeness_for_djk(self):
        num_of_repitition = {}
        nodes = list(self.graph._verticies.keys())
        divisor = ((len(nodes)-1)*(len(nodes)-2)/2)
        for i in range(len(nodes)):
            node = nodes[i]
            num_of_repitition[node] = 0
        for i in range(len(nodes)):
            node1 = self.graph._verticies[nodes[i]]
            for j in range(i+1, len(nodes)):
                node2 = self.graph._verticies[nodes[j]]
                path = djk_a_star_path(
                    node1.name, node2.name, self.graph.dijkstra_algorithm(node1.name, node2.name)[1])
                path = path.split(' => ')
                if len(path) == 2:
                    continue
                else:
                    for node in path[1:-1]:
                        num_of_repitition[node] += (1/divisor)
        largest = []
        temp = 0
        for node in num_of_repitition.keys():
            if num_of_repitition[node] > temp:
                largest = [node]
                temp = num_of_repitition[node]
            elif num_of_repitition[node] == temp:
                largest.append(node)
        return largest, num_of_repitition

    def betweeness_for_a_star(self):
        num_of_repitition = {}
        nodes = list(self.graph._verticies.keys())
        divisor = ((len(nodes)-1)*(len(nodes)-2)/2)
        for i in range(len(nodes)):
            node = nodes[i]
            num_of_repitition[node] = 0
        for i in range(len(nodes)):
            node1 = self.graph._verticies[nodes[i]]
            for j in range(i+1, len(nodes)):
                node2 = self.graph._verticies[nodes[j]]
                path = djk_a_star_path(node1.name, node2.name, self.graph.a_star_search(
                    node1.name, node2.name, self.heuristic)[1])
                path = path.split(' => ')
                if len(path) == 2:
                    continue
                else:
                    for node in path[1:-1]:
                        num_of_repitition[node] += (1/divisor)

        largest = []
        temp = 0
        for node in num_of_repitition.keys():
            if num_of_repitition[node] > temp:
                largest = [node]
                temp = num_of_repitition[node]
            elif num_of_repitition[node] == temp:
                largest.append(node)
        return largest, num_of_repitition


c = Centrality_measure('graph_romania_roads.txt')
result = c.betweeness_for_a_star()

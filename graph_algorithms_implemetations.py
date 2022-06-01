

from math import *
import heapq
import time


class Node:

    def __init__(self, name):
        self.name = name

        self.edge_list = []

    def connect(self, node):
        con = (self.name, node.name)
        self.edge_list.append(con)


class Edge:

    def __init__(self, left, right, weight):
        self.left = left
        self.right = right
        self.weight = weight


class Graph:

    def __init__(self):
        self._verticies = {}
        self.edges = {}

    def add_node(self, node):
        self._verticies[node.name] = node

    def add_edge(self, left, right, weight):
        if left.name not in self._verticies:
            self._verticies[left.name] = left

        if right.name not in self._verticies:
            self._verticies[right.name] = right

        e = Edge(left, right, weight)

        key = (left.name, right.name)
        self.edges[key] = e

        key = (right.name, left.name)
        self.edges[key] = e

        left.connect(right)
        right.connect(left)

    def heuristic_function(self, start, destination, heuristic_data):
        lon1 = radians(float(heuristic_data[start][1]))
        lon2 = radians(float(heuristic_data[destination][1]))
        lat1 = radians(float(heuristic_data[start][0]))
        lat2 = radians(float(heuristic_data[destination][0]))
        # Haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2

        c = 2 * asin(sqrt(a))
        rad = 6371

        return(c * rad)

# the BFS_search method accepts initial and end node names and
# computes the path through the graph and returns a dictionary
# with a name of the node as a string and a list of its edges
# along with start and end time for the algorithm

    def BFS_search(self, a: str, b: str):
        a = self._verticies[a]
        b = self._verticies[b]
        # A list used as a queue to store the neighboring nodes
        tracker = [a.name]
        # a list used to display the route taken by the algorithm
        # to find the search result
        path = {}
        # setting up a dictionary to keep track of visited node
        # Takes the node.name as a key and boolean as a value
        checked_dict = {}
        for i in self._verticies:
            checked_dict[i] = False
        # BFS search algorithm starts here
        start = time.time()
        while tracker != []:
            vertex = tracker.pop(0)
            lst = []
            for i in self._verticies[vertex].edge_list:
                if checked_dict[i[1]] == False:
                    tracker.append(i[1])
                    lst.append(i[1])
                    path[vertex] = lst
            checked_dict[vertex] = True
        end = time.time()

        return path, start, end

    def DFS_search(self, a: str, b: str):
        a = self._verticies[a]
        b = self._verticies[b]

        # A list used as a stack to store the neighboring nodes
        tracker = [a.name]

        # a list used to display the route taken by the algorithm
        # to find the search result
        path = {}

        # setting up a dictionary to keep track of visited node
        # Takes the node.name as a key and boolean as a value
        checked_dict = {}
        for i in self._verticies:
            checked_dict[i] = False

        # DFS search algorithm starts here
        start = time.time()
        while tracker != []:
            vertex = tracker.pop()
            lst = []
            for i in self._verticies[vertex].edge_list:
                if checked_dict[i[1]] == False:
                    tracker.append(i[1])
                    lst.append(i[1])
                    path[vertex] = lst

            checked_dict[vertex] = True
        end = time.time()
        return path, start, end

    def dijkstra_algorithm(self, a, b=None):
        a = self._verticies[a]
        if b != None:
            b = self._verticies[b]
        shortest_distance_from_initial = {a.name: 0}
        previous_vertex_from_the_node = {}
        visited = {a: False}
        unvisited_nodes = []
        heapq.heappush(unvisited_nodes, (0, a.name))
        for i in self._verticies:
            if self._verticies[i] == a:
                continue
            visited[self._verticies[i]] = False
            shortest_distance_from_initial[i] = inf
        start = time.time()
        while unvisited_nodes != []:
            next_smallest_node = self._verticies[heapq.heappop(
                unvisited_nodes)[1]]
            for i in next_smallest_node.edge_list:
                start_node = self._verticies[i[0]]
                end_node = self._verticies[i[1]]
                check_if_visited = visited.get(end_node)
                total_weight = shortest_distance_from_initial[i[0]
                                                              ] + self.edges[i].weight
                if total_weight < shortest_distance_from_initial[i[1]]:
                    shortest_distance_from_initial[i[1]] = total_weight
                    previous_vertex_from_the_node[end_node.name] = start_node.name
                if check_if_visited == False:
                    heapq.heappush(
                        unvisited_nodes, (shortest_distance_from_initial[i[1]], end_node.name))
            visited[start_node] = True
        end = time.time()
        return shortest_distance_from_initial, previous_vertex_from_the_node, start, end

    def a_star_search(self, a: str, b: str, heuristic_value):
        shortest_distance = {a: 0}
        previous_vertex_from_the_node = {}
        total_heuristic = {}
        visited = {a: False}
        unvisited_nodes = []
        heuristic = {}
        heapq.heappush(unvisited_nodes, (0, a))
        for i in self._verticies:
            if i == a:
                heuristic[a] = self.heuristic_function(
                    a, b, heuristic_value)
                continue
            visited[i] = False
            heuristic[i] = self.heuristic_function(
                i, b, heuristic_value)
            shortest_distance[i] = inf

        start = time.time()
        while visited[b] != True:
            next_smallest_node = self._verticies[heapq.heappop(
                unvisited_nodes)[1]]
            for i in next_smallest_node.edge_list:
                start_node = i[0]
                end_node = i[1]
                current_heuristic = shortest_distance[i[0]] + \
                    float(heuristic[end_node]) + self.edges[i].weight
                total_distance = shortest_distance[i[0]] + self.edges[i].weight
                if i[1] not in total_heuristic.keys() or current_heuristic < total_heuristic[i[1]]:
                    shortest_distance[i[1]] = total_distance
                    previous_vertex_from_the_node[end_node] = start_node
                    total_heuristic[i[1]] = current_heuristic
                    heapq.heappush(
                        unvisited_nodes, (current_heuristic, end_node))
            visited[start_node] = True
        end = time.time()
        return shortest_distance, previous_vertex_from_the_node, start, end

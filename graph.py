

class Node:

    def __init__(self, name):
        self.name = name
        
        self.edge_list = []

    def connect(self, node):
        con = (self.name, node.name)
        self.edge_list.append(con)


class Edge:

    def __init__(self, left, right, weight=1):
        self.left = left
        self.right = right
        self.weight = weight


class Graph:

    def __init__(self):
        self.verticies = {}
        self.edges = {}

    def add_node(self, node):
        self.verticies[node.name] = node

    def add_edge(self, left, right, weight=1):
        if left.name not in self.verticies:
            self.verticies[left.name] = left

        if right.name not in self.verticies:
            self.verticies[right.name] = right

        e = Edge(left, right, weight=1)

        key = (left.name, right.name)
        self.edges[key] = e

        key = (right.name, left.name)
        self.edges[key] = e

        left.connect(right)
        right.connect(left)

    def search(self, a, b):
        
        # A list used as a queue to store the neighboring nodes
        tracker = [a.name]
        
        # a list used to display the route taken by the algorithm
        #to find the search result
        path = []
        

        # setting up a dictionary to keep track of visited node
        # Takes the node.name as a key and boolean as a value
        checked_dict = {} 
        for i in self.verticies:
            checked_dict[i] = False 
        
        
        #BFS search algorithm starts here
        while tracker != []:
            vertex = tracker.pop(0)
            for i in self.verticies[vertex].edge_list:
                
                if checked_dict[i[0]] == False and checked_dict[i[1]] == False:
                    tracker.append(i[1])
                        
            if vertex == b.name:
                path.append(vertex)
                checked_dict[self.verticies[vertex].name] = True
                break
            path.append(vertex)
            checked_dict[self.verticies[vertex].name] = True
        print(path)
        print(checked_dict)

    def to_aj_matrix(self):
        pass




for iv, (k, v) in enumerate(g.verticies.items()):
    print(v.name)

for iv, (k, edge) in enumerate(g.edges.items()):
    print(edge.right.name, edge.left.name, edge.weight)

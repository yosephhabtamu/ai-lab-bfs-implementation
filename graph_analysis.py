
from time import *


from graph_algorithms_implemetations import *


def create_graph(file_name):
    file = open(file_name, 'r')
    f = file.readlines()
    g = Graph()
    heuristic_data = {}

    for line in f:
        arr = line.split(' ')

        if arr[0] == 'node':
            node = Node(arr[1])
            g.add_node(node)

        if arr[0] == 'edge':
            left = g._verticies[arr[1]]
            right = g._verticies[arr[2]]
            weight = int(arr[3][:-1])
            g.add_edge(left, right, weight)
        elif arr[0] == 'heuristic':
            heuristic_data[arr[1]] = (arr[2], arr[3])
    return g, heuristic_data


g = create_graph('graph_50_nodes.txt')[0]
heuristic_from_file = create_graph('graph_50_nodes.txt')[1]


def djk_a_star_path(start_node: str, end_node: str, previous_node: dict):
    prev = end_node
    path = []
    while True:
        if prev == start_node:
            path.append(start_node)
            break
        path.append(prev)
        prev = previous_node[prev]
    path = path[::-1]
    return ' => '.join(path)


def BFS_DFS_path(start_node, end_node, previous_node: dict):

    path = [end_node]
    prev = end_node
    while True:
        for key, value in previous_node.items():

            if prev in value:
                prev = key
                path.append(prev)
        if prev == start_node:
            break

    path = path[::-1]
    return ' => '.join(path)


def BFS_DFS_solution_length(start_node: str, end_node: str, func):
    result = func(start_node, end_node)

    path = BFS_DFS_path(start_node, end_node, result[0])

    path = path.split(" => ")
    sum = 0
    for i in range(len(path)-1):
        sum += g.edges[(path[i], path[i+1])].weight

    return sum


def BFS_DFS_analysis(func):
    final_time_each_node = {}
    soln_len = {}
    avg_time = 0
    avg_soln_len = 0

    for i in g._verticies:
        grand_mean = 0
        total_soln_len = 0
        sum = 0
        for j in g._verticies:

            if i == j:
                continue
            else:
                solution_length = BFS_DFS_solution_length(i, j, func)
                measured_time = func(i, j)
                start = measured_time[-2]
                end = measured_time[-1]
                total_soln_len += solution_length
                sum += (end-start)/len(g._verticies)
        grand_mean += sum
        final_soln_len = total_soln_len/len(g._verticies)
        soln_len[i] = final_soln_len
        final_time_each_node[i] = grand_mean
    for i in final_time_each_node.values():
        avg_time += i
    for i in soln_len.values():
        avg_soln_len += i
    avg_soln_len = avg_soln_len / len(g._verticies)
    avg_time = avg_time / len(g._verticies)

    return avg_time, avg_soln_len


def a_star_analysis():
    final_time_each_node = {}
    avg_time = 0
    avg_soln_len = 0
    soln_len = {}

    for i in g._verticies:
        total_soln_len = 0
        grand_mean = 0
        sum = 0
        for j in g._verticies:

            if i == j:
                continue
            else:

                result = g.a_star_search(i, j, heuristic_from_file)
                solution_length = result[0][j]
                start = result[2]
                end = result[3]
                total_soln_len += solution_length
                sum += (end-start)/len(g._verticies)

        grand_mean += sum
        final_soln_len = total_soln_len/len(g._verticies)
        soln_len[i] = final_soln_len
        final_time_each_node[i] = grand_mean
    for i in final_time_each_node.values():
        avg_time += i
    for i in soln_len.values():
        avg_soln_len += i
    avg_time = avg_time / len(g._verticies)
    avg_soln_len = avg_soln_len/len(g._verticies)

    return avg_time, avg_soln_len


def DJK_analysis():
    final_time_each_node = {}
    avg_time = 0
    avg_soln_len = 0
    length = len(g._verticies)
    soln_len = {}

    for i in g._verticies:
        total_soln_len = 0
        grand_mean = 0
        sum = 0
        result = g.dijkstra_algorithm(i)

        for j in result[0]:
            solution_length = result[0][j]
            total_soln_len += solution_length
        start = result[2]
        end = result[3]

        sum += (end-start)/length
        grand_mean += sum
        final_soln_len = total_soln_len/length
        soln_len[i] = final_soln_len
        final_time_each_node[i] = grand_mean
        print(i)
    for i in final_time_each_node.values():
        avg_time += i
    for i in soln_len.values():
        avg_soln_len += i
    avg_time = avg_time / length
    avg_soln_len = avg_soln_len/length

    return avg_time, avg_soln_len


# print('bfs: ', BFS_DFS_analysis(g.BFS_search))
# print('dfs: ', BFS_DFS_analysis(g.DFS_search))
# print('DJK: ', DJK_analysis())
print('a star: ', a_star_analysis())

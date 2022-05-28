
import decimal
from time import *


from graph_algorithms_implemetations import *


def path(start_node, end_node, previous_node):
    temp = previous_node[end_node]
    path = [end_node]
    while temp != start_node:
        path.append(temp)
        temp = previous_node[temp]
    path.append(start_node)
    path = path[::-1]
    return ' => '.join(path)


def read_file(file_name):
    file = open(file_name, 'r')
    f = file.readlines()
    g = Graph()
    heuristic_data = {}

    for line in f:
        arr = line.split(' ')

        if arr[0] == 'node':
            node = Node(arr[1])
            g.add_node(node)

        elif arr[0] == 'edge':
            left = g._verticies[arr[1]]
            right = g._verticies[arr[2]]
            weight = int(arr[3][:-1])
            g.add_edge(left, right, weight)
        elif arr[0] == 'heuristic':
            heuristic_data[arr[1]] = (arr[2], arr[3][:-1])
    return g, heuristic_data


g = read_file('data.txt')[0]
heuristic_from_file = read_file('data.txt')[1]
print(heuristic_from_file)
# result = path('zerind', 'urziceni', g.DFS_search('zerind', 'urziceni'))
# result = g.a_star_search('zerind', 'urziceni', heuristic)
# result = g.DFS_search('urziceni', 'zerind')


def measure_time(func):
    final_time_each_node = {}
    avg = 0

    for i in g._verticies:
        grand_mean = 0

        for k in range(50):
            sum = 0
            for j in g._verticies:

                if i == j:
                    continue
                else:
                    start = decimal.Decimal(time())
                    func(i, j)
                    end = decimal.Decimal(time())
                    sum += (end-start)/len(g._verticies)
            grand_mean += sum/50
        final_time_each_node[i] = grand_mean
    for i in final_time_each_node.values():
        avg += i
    avg = avg / len(g._verticies)

    return avg


def measure_time_a_star():
    final_time_each_node = {}
    avg = 0

    for i in g._verticies:
        grand_mean = 0
        sum = 0
        for j in g._verticies:

            if i == j:
                continue
            else:
                start = decimal.Decimal(time())
                g.a_star_search(i, j, heuristic_from_file)
                end = decimal.Decimal(time())
                sum += (end-start)/len(g._verticies)
            grand_mean += sum/50
        final_time_each_node[i] = grand_mean
    for i in final_time_each_node.values():
        avg += i
    avg = avg / len(g._verticies)

    return avg


print('the BFS-search is: ', measure_time(g.BFS_search))
print('-------------------------------------------------------------------------------')
print('the dijkstra is: ', measure_time(g.dijkstra_algorithm))
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('the DFS analysis: ', measure_time(g.DFS_search))
print('..........................................................................')
print('the a star analysis: ', measure_time_a_star())

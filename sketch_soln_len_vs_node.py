from graph_analysis import *

graph_15 = create_graph('graph_15_nodes.txt')
graph_15_graph = graph_15[0]
graph_15_heuristics = graph_15[1]


graph_20 = create_graph('graph_20_nodes.txt')
graph_20_graph = graph_20[0]
graph_20_heuristics = create_graph('graph_20_nodes.txt')[1]

graph_30 = create_graph('graph_30_nodes.txt')
graph_30_graph = graph_30[0]
graph_30_heuristics = graph_30[1]


graph_50 = create_graph('graph_50_nodes.txt')
graph_50_graph = graph_50[0]
graph_50_heuristics = graph_50[1]


def sketch_graph():

    x = [15, 20, 30, 50]
    y_a_star = [a_star_analysis(graph_15_graph, graph_15_heuristics)[1],
                a_star_analysis(graph_20_graph, graph_20_heuristics)[1],
                a_star_analysis(graph_30_graph, graph_30_heuristics)[1],
                a_star_analysis(graph_50_graph, graph_50_heuristics)[1]
                ]
    y_BFS = [BFS_DFS_analysis(graph_15_graph, graph_15_graph.BFS_search)[1],
             BFS_DFS_analysis(graph_20_graph, graph_20_graph.BFS_search)[1],
             BFS_DFS_analysis(graph_30_graph, graph_30_graph.BFS_search)[1],
             BFS_DFS_analysis(graph_50_graph, graph_50_graph.BFS_search)[1]
             ]
    y_DFS = [BFS_DFS_analysis(graph_15_graph, graph_15_graph.DFS_search)[1],
             BFS_DFS_analysis(graph_20_graph, graph_20_graph.DFS_search)[1],
             BFS_DFS_analysis(graph_30_graph, graph_30_graph.DFS_search)[1],
             BFS_DFS_analysis(graph_50_graph, graph_50_graph.DFS_search)[1]
             ]
    y_DJK = [DJK_analysis(graph_15_graph)[1],
             DJK_analysis(graph_20_graph)[1],
             DJK_analysis(graph_30_graph)[1],
             DJK_analysis(graph_50_graph)[1]
             ]
    plt.title('solution length vs number of nodes')
    plt.ylabel('solution length')
    plt.xlabel('number of nodes')
    plt.plot(x, y_BFS, label='BFS search')
    plt.plot(x, y_DFS, label='DFS search')
    plt.plot(x, y_DJK, label='djikstra')
    plt.plot(x, y_a_star, label='a star')
    plt.legend(loc='upper right')

    plt.show()


sketch_graph()

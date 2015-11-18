# import networkx
import networkx as nx
 
# create directed graph
G = nx.DiGraph()
 
# add node to graph with negative (!) supply for each supply node 
G.add_node(1, demand = -90)
 
# you can ignore transshipment nodes with zero supply when you are working with the mcfp-solver 
# of networkx
# add node to graph with positive (!) demand for each demand node
G.add_node(4, demand = 90)
 
# add arcs to the graph: fromNode,toNode,capacity,cost (=weight)
G.add_edge(1, 2, capacity = 100, weight = 1)
G.add_edge(1, 3, capacity = 100, weight = 1)
G.add_edge(2, 3, capacity = 100, weight = 1)
G.add_edge(2, 4, capacity = 1, weight = 1)
G.add_edge(3, 4, capacity = 100, weight = 1)
G.add_edge(3, 2, capacity = 100, weight = 1)
# solve the min cost flow problem
# flowDict contains the optimized flow
# flowCost contains the total minimized optimum
length,path=nx.bidirectional_dijkstra(G,1,4)
print list(nx.all_shortest_paths(G, 1, 4, weight='weight'))
flowCost, flowDict = nx.network_simplex(G)
print "O menor caminho com base no weigth eh ", (path)
print nx.dijkstra_path(G, 1, 4)
 
print "Optimum: %s" %flowCost  #should be 14
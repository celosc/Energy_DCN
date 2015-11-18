import networkx as nx
from networkx.algorithms.flow import shortest_augmenting_path

G = nx.DiGraph()
G.add_edge('x','a', capacity=100)
G.add_edge('x','b', capacity=100)
G.add_edge('a','c', capacity=100)
G.add_edge('b','c', capacity=100)
G.add_edge('b','d', capacity=100)
G.add_edge('d','e', capacity=100)
G.add_edge('c','y', capacity=100)
G.add_edge('e','y', capacity=100)
R = shortest_augmenting_path(G, 'x', 'y')
flow_value = nx.maximum_flow_value(G, 'x', 'y')
print flow_value

print flow_value == R.graph['flow_value']
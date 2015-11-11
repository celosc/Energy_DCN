from networkx.readwrite import json_graph
import networkx as nx
import json
import matplotlib.pyplot as plt

energy_hosts=3
energy_switches=50

# Faz a leitura do arquivo JSON formatado para o grafo
g = json_graph.node_link_graph(json.load(open("fattree.js")))
print "Nodes do grafo: {}".format(g.nodes())  # Lista os nodos
#print "graph nodes: {}".format(g.nodes("id"))  # Lists nodes
#print "graph links: {}".format(g.edges())  #  Shows link info
print "Todas as informacoes dos links do grafo: {}".format(g.edges(data=True))  #  Shows link info
'''
for n in g.nodes():  # See that hosts are assigned addresses
    if g.node[n]["type"] == 'host':
        print "Host {}, IP = {}, MAC = {}".format(n, g.node[n]['ip'], g.node[n]['mac'])
    
'''
#Calculo de energia
nodes = g.nodes()
hosts = [n for n in nodes if g.node[n]['type'] == 'host']
switches = [n for n in nodes if g.node[n]['type'] == 'switch']
nr_hosts=len(hosts)
nr_switches=len(switches)
energy_h=energy_hosts*nr_hosts
energy_s=energy_switches*nr_switches

print "O consumo dos hosts eh", energy_h
print "O consumo dos switches eh", energy_s

print "O consumo total da topologia eh", energy_h+energy_s

#print "O numero de hosts na topologia eh:", nr_hosts
#print "O numero de switches na topologia eh:", nr_switches
#print ("Lista de Hosts da Topologia", hosts)
#print ("Lista de Switches da Topologia", switches)

# Computa o caminho mais curto do H1 para todos os demais hosts
'''
paths = nx.shortest_path(g, "H1",  "H8",weight="capacity")
paths = nx.all_shortest_paths(g, "H1",  "H8",weight="capacity")
for dest in paths.keys():  # Nicely output all those paths
    print "Shortest Path from H1 to {} is:".format(dest)
    print "{}".format(paths[dest])
'''
#print list(nx.all_simple_paths(g, "H1",  "H8"))

length,path=nx.bidirectional_dijkstra(g,"H1","H6")
#print (length) #Com base no parametro "weight"
print "O menor caminho eh ", (path)

#print list(nx.shortest_path(g, "H1",  "H8",weight="capacity")      
nx.draw_networkx(g, node_size=800,)
plt.title ("Fattree Energy Topology")
pos=nx.shell_layout(g) # Posicao de todos os nodes
plt.show()


#hosts = [('h' + str(i), {'type':'host'})
#    for i in range (g.node)]

#print hosts
from networkx.readwrite import json_graph
import networkx as nx
import json
import matplotlib.pyplot as plt


def print_energy(energy_hosts, energy_switches, g):
    nodes = g.nodes()
    hosts = [n for n in nodes if g.node[n]['type'] == 'host']
    switches = [n for n in nodes if g.node[n]['type'] == 'switch']
    nr_hosts = len(hosts)
    nr_switches = len(switches)
    energy_h = energy_hosts * nr_hosts
    energy_s = energy_switches * nr_switches
    total_portas = 0
    for e in g.edges(data=True):
        cost = e[2]['capacity'] == 10 and 1.5 or e[2]['capacity'] == 100 and 2.5 or 5.0
        if (e[0][0] == 'S'):
            total_portas += cost
        if (e[1][0] == 'S'):
            total_portas += cost
    
#print "O consumo dos hosts eh", energy_h
    print "O consumo dos switches eh", energy_s, "W/h"
    print "O consumo total das portas e:", total_portas, "W/h"
    print "O consumo total da topologia eh ", energy_s + total_portas, "W/h"

energy_hosts=3
energy_switches=50
energy_of_ports = dict({10: 1.5, 100: 2.5, 1000: 5})

'''
energy_of_ports = dict({10M: 1.5, 100M: 2.5, 1G : 5})
10 Mbps = 0,15 W/h
100 Mbps = 0,3W/h
1 Gbps = 1W/h  
Switch de 48 portas varia de 70W/h
'''
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
print_energy(energy_hosts, energy_switches, g)

length,path=nx.bidirectional_dijkstra(g,"H1","H6")

#path=nx.bidirectional_dijkstra(g,"H1","H8", weight='weight')
#print (length) #Com base no parametro "weight"
print "O menor caminho eh ", (path)

# altera a capacidade de todos os switches para 10
for ed in g.edge.iteritems():
    for n in ed[1].iteritems():
        n[1][0]['capacity'] = 10
        

print "\n DEPOIS DE MUDAR A CAPACIDADE \n"
    
print_energy(energy_hosts, energy_switches, g)

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

#path=nx.bidirectional_dijkstra(g,"H1","H8", weight='weight')
#print (length) #Com base no parametro "weight"
print "O menor caminho eh ", (path)

#print list(nx.shortest_path(g, "H1",  "H8",weight="capacity")      
nx.draw_networkx(g, node_size=800,)
plt.title ("Fattree Energy Topology")
pos=nx.shell_layout(g) # Posicao de todos os nodes
#plt.show()

#hosts = [('h' + str(i), {'type':'host'})
#    for i in range (g.node)]

#print hosts
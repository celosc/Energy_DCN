'''Consumo de energia da rede baseado em:
Mahadevan, Priya, et al. "A power benchmarking framework for network devices." 
NETWORKING 2009. Springer Berlin Heidelberg, 2009. 795-808.

Wang, Xiaodong, et al. "Carpo: Correlation-aware power optimization in data center networks." 
INFOCOM, 2012 Proceedings IEEE. IEEE, 2012.

10 Mbps = 0,15 W/h
100 Mbps = 0,3W/h
1 Gbps = 1W/h  
Switch de 48 portas 70W/h
'''
from networkx.readwrite import json_graph
import networkx as nx
import json
import matplotlib.pyplot as plt

energy_switches=50

def power_efficiency(energy_switches, g): #Algoritimo Power Efficiency
    for ed in g.edge.iteritems():
        for n in ed[1].iteritems():
            n[1][0]['capacity'] = 10
    
    print "\n DEPOIS DE MUDAR A CAPACIDADE \n"
    print_energy(energy_switches, g)

#ports: [{nr:1, status: on, link: 10}, {inr:2, status: off, link: 1000}]


def print_energy(energy_switches, g): #Funcao que verifica o consumo de energia
    nodes = g.nodes()
    switches = [n for n in nodes if g.node[n]['type'] == 'switch']
    nr_switches = len(switches)
    energy_s = energy_switches * nr_switches
    total_portas = 0
    #Verifica as portas existentes nos switches da topologia e atribui o consumo para elas
    for e in g.edges(data=True):
        cost = e[2]['capacity'] == 10 and 1.5 or e[2]['capacity'] == 100 and 2.5 or 5.0
        if (e[0][0] == 'S'):
            total_portas += cost
        if (e[1][0] == 'S'):
            total_portas += cost
    
    print "O consumo dos switches eh: ", energy_s, "W/h"
    print "O consumo das portas eh: ", total_portas, "W/h"
    print "O consumo total da topologia eh: ", energy_s + total_portas, "W/h"


# Faz a leitura do arquivo JSON com as informacoes da topologia
g = json_graph.node_link_graph(json.load(open("fattree.js")))
#print "Nodes do grafo: {}".format(g.nodes())  # Lista os nodos
#print "graph nodes: {}".format(g.nodes("id"))  # Lists nodes
#print "graph links: {}".format(g.edges())  #  Shows link info
#print "Todas as informacoes dos links do grafo: {}".format(g.edges(data=True))  #  Shows link info
'''
for n in g.nodes():  # See that hosts are assigned addresses
    if g.node[n]["type"] == 'host':
        print "Host {}, IP = {}, MAC = {}".format(n, g.node[n]['ip'], g.node[n]['mac'])
    
'''
print_energy(energy_switches, g)

#Utiliza o algoritimo de Djisktra para a escolha do melhor caminho
length,path=nx.bidirectional_dijkstra(g,"H1","H6")

print "O menor caminho com base no weigth eh ", (path)

# altera a capacidade de todos os switches para 10
power_efficiency(energy_switches, g)

print "O menor caminho com base no weigth eh ", (path)

'''
#Faz a plotagem do grafo   
nx.draw_networkx(g, node_size=800,)
plt.title ("Fattree Energy Topology")
pos=nx.shell_layout(g) # Posicao de todos os nodes
plt.show()
'''
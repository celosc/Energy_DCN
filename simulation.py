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
#import matplotlib.pyplot as plt

def power_efficiency(g): #Algoritimo Power Efficiency
    for ed in g.edge.iteritems():
        for n in ed[1].iteritems():
            n[1][0]['capacity'] = 10
    
    print "\n DEPOIS DE MUDAR A CAPACIDADE "
    print_energy(g)

#ports: [{nr:1, status: on, link: 10}, {inr:2, status: off, link: 1000}]


def print_energy(g): #Funcao que verifica o consumo de energia
    #Define o consumo dos switches com base no tipo de equipamento (Access, Aggregation, Core)
    energy_sw = 0
    for n in g.nodes():  #
        if g.node[n]["type"] == 'switch':
            layer_sw = g.node[n]['layer'] == "access" and 60.0 or g.node[n]['layer'] == "aggregation" and 140.0 or 150.0
            energy_sw += layer_sw
            
    #Verifica as portas existentes nos switches da topologia e atribui o consumo para elas
    total_portas = 0
    for e in g.edges(data=True):
        cost = e[2]['capacity'] == 10 and 1.5 or e[2]['capacity'] == 100 and 2.5 or 5.0
        if (e[0][0] == 'S'):
            total_portas += cost
        if (e[1][0] == 'S'):
            total_portas += cost
    
    print "\nO consumo dos switches eh: ", energy_sw, "W/h"
    print "O consumo das portas eh: ", total_portas, "W/h"
    print "O consumo total da topologia eh: ", energy_sw + total_portas, "W/h"

# Faz a leitura do arquivo JSON com as informacoes da topologia
g = json_graph.node_link_graph(json.load(open("fattree.js")))


def status_sw(g): #Funcao que verifica quais sw estao ligados
    sw_on = 0
    sw_off = 0
    for n in g.nodes(): #
        if g.node[n]["type"] == 'switch':
            if g.node[n]["status"] == 'on':
                sw_on = n
                #print "O switch %s esta ligado" %n
                print "O switch %s esta ligado" %sw_on
            if g.node[n]["status"] == 'off':
                sw_off = n
                #print "O switch %s esta desligado\n " %n
                print "O switch %s esta desligado " %sw_off

status_sw(g)


print_energy(g)

#Utiliza o algoritimo de Djisktra para a escolha do melhor caminho
length,path=nx.bidirectional_dijkstra(g,"H1","H6")

print "O menor caminho com base no weigth eh ", (path)

# altera a capacidade de todos os switches para 10
power_efficiency(g)

print "O menor caminho com base no weigth eh ", (path)

'''
#Faz a plotagem do grafo   
nx.draw_networkx(g, node_size=800,)
plt.title ("Fattree Energy Topology")
pos=nx.shell_layout(g) # Posicao de todos os nodes
plt.show()
'''


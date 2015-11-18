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

def power_efficiency(g): #Esboco do metodo para alteracao das velocidade das portas 
    for ed in g.edge.iteritems():
        for n in ed[1].iteritems():
            n[1][0]['capacity'] = 10
    
    print "\n DEPOIS DE MUDAR A CAPACIDADE "
    print_energy(g)

def print_energy(g): #Funcao que verifica o consumo de energia
    '''
        Define o consumo dos switches com base no tipo de equipamento (Access, Aggregation, Core) e as
        portas ligadas/desligadas e seu consumo pela velocidade do link
    '''
    
    # Variavel que armazena a energia total consumida por todos os switches
    energy_sw = 0
      
    for n in g.nodes():  # para cada nodo do grafo
        if g.node[n]["type"] == 'switch':  # verifica se eh do tipo switch
            if g.node[n]["status"] == 'on':  # se for do tipo switch, verifica se esta ligado
                
                # se estiver ligado, verifica o tipo e atribui o consumo do chassi
                layer_sw = g.node[n]['layer'] == "access" and 60.0 or g.node[n]['layer'] == "aggregation" and 140.0 or 150.0
                
                # variavel que guarda o acumulado de consumo das portas do sw
                layer_sw_port_consumption_sum = 0
                
                for link in g.node[n]['ports']:  # para cada sw, procura a capacidade de cada porta
                    
                    if link['status'] == 'on':  # verifica se a porta esta ligada
                        
                        # calcula o consumo da porta baseada na sua velocidade
                        link_consumption = link['link'] == 10 and 1.5 or link['link'] == 100 and 2.5 or 5.0
                    
                        # acumula o consumo da porta
                        layer_sw_port_consumption_sum += link_consumption
                        
                        # print o consumo para cada porta 
                        print "node: {} | port_energy: {} | link: {}".format(n, link_consumption, link)
                
                # print a soma total do consumo das portas
                print ">>>>>>>> node: {} | total port consumption: {}".format(n, layer_sw_port_consumption_sum)
                
                # energia total para o switch
                energy_sw += layer_sw + layer_sw_port_consumption_sum
                
                print " -----> node: {} | chassi: {} | total node energy: {}".format(n, layer_sw, layer_sw + layer_sw_port_consumption_sum)
            
    # Verifica as portas existentes nos switches da topologia e atribui o consumo para elas
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

def bw_edge_capacity(edge, graph):
    '''
        Recebe uma aresta da rede, olha para os nodos e pega a MENOR capacidade entre eles
    '''
    
    node_left = edge[0]
    node_right = edge[1]
    
    node_left_cap = 100 # pega a capacidade olhando para o nodo no grafo
    node_right_cap = 1000 # pega a capacidade olhando para o nodo no grafo
    
    smaller = 0
    
    if node_left_cap < node_right_cap:
        smaller = node_left_cap
    elif node_left_cap > node_right_cap:
        smaller  = node_right_cap
    else:
        smaller = node_right_cap
    
    
    print "esquerda: {} | direita: {}| menor: {} |edge: {}".format(node_left, node_right, smaller, edge)

    pass


def can_my_network_handle_the_workload(workload, graph):
    '''
        Verifica se a rede atual atende o workload especificado
        
        @param workload: inteiro que representa a 
        capacidade minima necessaria para atender o workload (BW)
        
        @param grap: a rede
        
        @return: True se a rede atende a tua demanda ou False se a rede nao atende a demanda
    '''
    
    # faz as verificacoes
    
    for edge in graph.edges(data=True):  # para cada link, verifica se atende a capacidade
        bw = bw_edge_capacity(edge, graph)
        
        if workload > bw:
            return False
    
    return True
    
    
g = json_graph.node_link_graph(json.load(open("fattree.js")))

can_my_network_handle_the_workload(100, g)


print_energy(g)

#Utiliza o algoritimo de Djisktra para a escolha do melhor caminho
length,path=nx.bidirectional_dijkstra(g,"H1","H6")

print "O menor caminho com base no weigth eh ", (path)

# altera a capacidade de todos os switches para 10
#power_efficiency(g)

#print "O menor caminho com base no weigth eh ", (path)
     
#Faz a plotagem do grafo   
#nx.draw_networkx(g, node_size=800,)
#plt.title ("Fattree Energy Topology")
#pos=nx.shell_layout(g) # Posicao de todos os nodes
#plt.show()


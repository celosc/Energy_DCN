'''Consumo de energia da rede baseado em:
1) Mahadevan, Priya, et al. "A power benchmarking framework for network devices." 
NETWORKING 2009. Springer Berlin Heidelberg, 2009. 795-808.
2) Wang, Xiaodong, et al. "Carpo: Correlation-aware power optimization in data center networks." 
INFOCOM, 2012 Proceedings IEEE. IEEE, 2012.
10 Mbps = 0,15 W/h
100 Mbps = 0,3W/h
1 Gbps = 1W/h  
Switch de 48 portas 70W/h


Topologia Fattree baseado em A Scalable Commodity Data Center Network Architecture" by Al-Fares,
Loukissas and Vahdat
k = number of ports per switch = number of pods
    number core switches =  (k/2)^2
    number of edge switches per pod = k / 2
    number of agg switches per pod = k / 2
    number of hosts attached to each edge switch = k / 2
    number of hosts per pod = (k/2)^2
    total number of hosts  = k^3 / 4
'''
#from networkx.readwrite import json_graph
import networkx as nx
import argparse
from datetime import datetime
#import json
#import matplotlib.pyplot as plt

#def power_efficiency(g): #Esboco do metodo para alteracao das velocidade das portas 
#    for ed in g.edge.iteritems():
#        for n in ed[1].iteritems():
#            n[1][0]['capacity'] = 10
    
    #print "\n DEPOIS DE MUDAR A CAPACIDADE "
#    print_energy(g)

def print_paths(g):
    #Mapeamento dos caminhos
    source = "H1"
    target = "H6"
#Utiliza o algoritimo de Djisktra para a escolha do melhor caminho
    length, path = nx.bidirectional_dijkstra(g, source, target)
    #print "O menor caminho com base no weigth eh ", (path)
#Cria a lista de todos os camihos possiveis para alcancar o destino
#for paths in nx.all_simple_paths(g, source="H1", target="H6"):
#    all_paths = paths
#    print(all_paths)
#Cria uma lista de TODOS os camihos possiveis de uma origem para alcancar um destino
    paths = nx.all_simple_paths(g, source, target) 
    #print "\nLista de todos os caminhos ", (list(paths))
    #print paths
#Excessao para o caso do caminho nao ser encontrado
    try:
        path = nx.shortest_path(g, source, target)
    except:
        path = None
    if None == path:
        print "No route found!"

def print_energy(g): #Funcao que verifica o consumo de energia
    '''
        Define o consumo dos switches com base no tipo de equipamento (Access, Aggregation, Core) e as
        portas e seu consumo pela velocidade do link
    '''
    
    # Variavel que armazena a energia total consumida por todos os switches
    energy_sw = 0
      
    for n in g.nodes():  # para cada nodo do grafo
        if g.node[n]["type"] == 'switch':  # verifica se eh do tipo switch
            if g.node[n]["status"] == 'on':  # se for do tipo switch, verifica se esta ligado
                
                # se estiver ligado, verifica o tipo e atribui o consumo do chassi
                layer_sw = g.node[n]['layer'] == "access" and 60.0 or g.node[n]['layer'] == "aggregation" and 140.0 or 150.0
                
                # variavel que guarda o acumulado de consumo das portas do sw
                total_portas = 0
                
                # para cada sw, procura a capacidade de cada porta
                for link in g.edges(data=True):
                    #print link
                    link_consumption = link[2]['link'] == 100 and 2.5 or link[2]['link'] == 1000 and 3.5 or 5.0
                    if (link[0][0] == 'S') and (link[1][0] == 'S') or (link[0][0] == 'S') and (link[1][0] == 'H'):
                        total_portas += link_consumption
                
                # energia total para o switch
                energy_sw += layer_sw
                
                #print " -----> node: {} | total node energy: {}".format(n,layer_sw)
    # Verifica as portas existentes nos switches da topologia e atribui o consumo para elas

    print "\nO consumo dos switches eh: ", energy_sw, "W/h\n"
    print "O consumo das portas eh: ", total_portas, "W/h\n"
    print "O consumo total da topologia eh: ", energy_sw + total_portas, "W/h\n"



def bw_edge_capacity(edge, graph):
    
        #Recebe uma aresta da rede, olha para os nodos e pega a MENOR capacidade entre eles
    
    # armazena os nodos que estao a esquerda e direita da aresta
    node_left = edge[0]
    node_right = edge[1]

    #print "esquerda: {} | direita: {}".format(node_left, node_right)
    
    node_left_cap = get_port_bw(node_left, edge)
    node_right_cap = get_port_bw(node_right, edge)

    #print "cap esquerda: {} | cap direita {}".format(node_left_cap, node_right_cap)

    smallest = 0
    
    if node_left_cap < node_right_cap:
        smallest = node_left_cap
    elif node_left_cap > node_right_cap:
        smallest  = node_right_cap
    else:
        smallest = node_right_cap
    
    #print "esquerda: {} | direita: {} | menor: {} | edge: {}".format(node_left, node_right, smallest, edge)

    return smallest

def get_port_bw(node, edge):  
        
        return edge[2]['link']
    

def list_ports_node(edge, graph): #teste de captura de portas de origem
    
    source_node = edge[0]
    destination_node = edge[1]
    
    port_source_node = get_port_nr(source_node, edge)
    port_destination_node = get_port_nr_dst(destination_node, edge)
    print "source node: {} | source port: {} ".format(source_node, port_source_node)
    print "source node: {} | destination port: {} ".format(destination_node, port_destination_node)
    
def get_port_nr(node, edge):  
        
        return edge[2]['src_port']
    
def get_port_nr_dst(node, edge):  
        
        return edge[2]['dst_port']    
    
def print_source_ports_nodes(graph):

    
    for edge in graph.edges(data=True):  # para cada link, verifica se atende a capacidade
        ports_nodes = list_ports_node(edge, graph)

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

   
def mk_topo(pods, bw):
    num_hosts         = (pods ** 3)/4
    num_agg_switches  = pods * pods
    num_core_switches = (pods * pods)/4

    hosts = [('H' + str(i), {'type':'host', 'port':'on'})
             for i in range (1, num_hosts + 1)]

    core_switches = [('S' + str(i), {'type':'switch','layer':'core', 'status':'on'})
                       for i in range(1,num_core_switches + 1)]

    agg_switches = [('S' + str(i), {'type':'switch','layer':'aggregation', 'status':'on'})
                    for i in range(num_core_switches + 1,num_core_switches + num_agg_switches+ 1)]

    g = nx.DiGraph()
    g.add_nodes_from(hosts)
    g.add_nodes_from(core_switches)
    g.add_nodes_from(agg_switches)
    #print g.node

    host_offset = 0
    for pod in range(pods):
        core_offset = 0
        for sw in range(pods/2):
            switch = agg_switches[(pod*pods) + sw][0]
            #print "agg_switches", switch
            # Connect to core switches with aggregation switches
            for port in range(pods/2):
                core_switch = core_switches[core_offset][0]
                g.add_edge(switch,core_switch,
                           {'src_port':port,'dst_port':pod,'link':10000,'cost':1})
                g.add_edge(core_switch,switch,
                           {'src_port':pod,'dst_port':port,'link':10000,'cost':1})
                core_offset += 1
                #print g.edge
            # Connect to aggregate switches in same pod
            for port in range(pods/2,pods):
                lower_switch = agg_switches[(pod*pods) + port][0]
                #print "acc_switches", lower_switch
                g.add_edge(switch,lower_switch,
                           {'src_port':port,'dst_port':sw,'link':1000,'cost':1})
                g.add_edge(lower_switch,switch,
                           {'src_port':sw,'dst_port':port,'link':1000,'cost':1})
                #print g.edge
        for sw in range(pods/2,pods):
            switch = agg_switches[(pod*pods) + sw][0]
            # Connect to hosts
            for port in range(pods/2,pods): # First k/2 pods connect to upper layer
                host = hosts[host_offset][0]
                # All hosts connect on port 0
                g.add_edge(switch,host,
                           {'src_port':port,'dst_port':0,'link':100,'cost':1})
                g.add_edge(host,switch,
                           {'src_port':0,'dst_port':port,'link':100,'cost':1})
                host_offset += 1
    
    #print g.edge
    #print g.nodes(data=True)
    #for path in nx.all_simple_paths(g, source="H3", target="H4"):
        #print(path)
    return g

def parse_args(): #Metodo que define os argumentos que sao usados no simulador, como por exemplo o numero de pods
    parser = argparse.ArgumentParser()
    parser.add_argument('-p','--pods',type=int,action='store',dest='pods',
                        default=4,
                        help='number of pods (parameter k in the paper)')
    parser.add_argument('-b','--bandwidth',type=str,action='store',dest='bw',
                        default='1Gbps',
                        help='bandwidth of each link')
    parser.add_argument('-o', '--out', action='store',dest='output',
                        default=None,
                        help='file root to write to')

    return parser.parse_args(
                             )
def print_pods_information():
    pods = 50
#k = number of ports per switch = number of pods
    print "number core switches =", (pods * pods) / 4
    print "number aggregation switches =", pods * pods
    print "number of edge switches per pod =", pods / 2
    print "number of agg switches per pod =", pods / 2
    print "number of hosts attached to each edge switch = ", pods / 2
    print "number of hosts per pod =", (pods / 2) ** 2
    print "total number of hosts  =", (pods ** 3) / 4
    
#print_pods_information()

args = parse_args()
g = mk_topo(args.pods,args.bw)

#Retorna as conexoes do nodo "S1"
#print g.edges(nbunch="S1", data=True)

print print_source_ports_nodes(g)

print can_my_network_handle_the_workload(100, g)

start_time = datetime.now()

print_energy(g)

print_paths(g)

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
     
#Faz a plotagem do grafo   
#nx.draw_networkx(g, node_size=800,)
#plt.title ("Fattree Energy Topology")
#pos=nx.shell_layout(g) # Posicao de todos os nodes
#plt.show()

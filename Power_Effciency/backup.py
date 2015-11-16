energy_layer_sw = 0
for l in g.nodes(data=True):
    layer_sw = l[2]['layer'] == "access" and 60.0 or l[2]['layer'] == "aggregation" and 140.0 or 150.0
    energy_layer_sw += layer_sw
        
    #Verifica as portas existentes nos switches da topologia e atribui o consumo para elas   
total_portas = 0
for e in g.edges(data=True):
    cost = e[2]['capacity'] == 10 and 1.5 or e[2]['capacity'] == 100 and 2.5 or 5.0
    if (e[0][0] == 'S'):
        total_portas += cost
    if (e[1][0] == 'S'):
        total_portas += cost
total_energy = energy_layer_sw + total_portas
print "O consumo dos switches eh: ", energy_layer_sw, "W/h"
print "O consumo das portas eh: ", total_portas, "W/h"
print "O consumo total da topologia eh: ",total_energy,  "W/h"




energy_sw = 0
for n in g.nodes():  # See that hosts are assigned addresses
    if g.node[n]["type"] == 'switch':
        #print "Switch {}, Layer = {}".format(n, g.node[n]['layer'])
        layer_sw = g.node[n]['layer'] == "access" and 60.0 or g.node[n]['layer'] == "aggregation" and 140.0 or 150.0
        energy_sw += layer_sw
    print energy_sw
    
    
    #print "Nodes do grafo: {}".format(g.nodes())  # Lista os nodos
#print "graph nodes: {}".format(g.nodes("id"))  # Lists nodes
#print "graph links: {}".format(g.edges())  #  Shows link info
#print "Todas as informacoes dos links do grafo: {}".format(g.edges(data=True))  #  Shows link info



'''
for n in g.nodes():  # See that hosts are assigned addresses
    if g.node[n]["type"] == 'host':
        print "Host {}, IP = {}, MAC = {}".format(n, g.node[n]['ip'], g.node[n]['mac']) 
'''
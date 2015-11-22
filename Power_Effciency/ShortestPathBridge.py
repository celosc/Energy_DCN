""" This file contains an example of centralized computation and configuration
    of shortest path based bridging. In particular we compute forwarding tables
    for all switches given static topology information where the tables contain
    destination MAC addresses and the forwarding is based on shortest distance.

    Step 1: Determine which hosts are connected to which switches and save that
            information.

    Steps 2: Compute all the shortest paths from switches to a given destination switch.
            (a) Create a copy of the network without any hosts
            (b) Use NetworkX algorithm to compute all shortest paths

    Step 3: Create MAC to port forwarding table for each switch
            (a) Based on Switch to Switch forwarding from step 2
            (b) Based on Directly connected hosts
"""
import networkx as nx
from networkx.readwrite import json_graph
import json


def computeL2FwdTables(g):
    """ Given a network described by the graph g returns a dictionary of forwarding
     tables indexed by switch name. Each forwarding table is itself a dictionary
     indexed by a destination MAC address.
    """
    # Figure out which nodes are hosts or switches
    nodes = g.nodes()
    #print "Nodes", nodes
    hosts = [n for n in nodes if g.node[n]['type'] == 'host']
    #print "Hosts", hosts
    switches = [n for n in nodes if g.node[n]['type'] == 'switch']
    #print "switches", switches
    
    # Create the switch to host mapping, i.e., lists of hosts associated with
    # switches
    switch_host_map = {}
    for s in switches:
        switch_host_map[s] = []
    for h in hosts:
        hedges = g.edges(h)
        #print hedges
        if len(hedges) != 1:
            raise Exception("Hosts must be connected to only one switch in this model")
        other = hedges[0][1]  # Should be the other side of the link
        if not other in switches:
            raise Exception("Hosts must be connected only with a switch in this model")
        switch_host_map[other].append(h)  #Okay add the host to the switch map
        #print "switch map: ", switch_host_map

    # Get switch only subgraph and compute all the shortest paths with NetworkX
    g_switches = g.subgraph(switches)
    # compute all the shortest paths, result is a dictionary index by two nodes
    # and returning a list of nodes. From this we can get the next hop link to
    # any destination switch
    spaths = nx.shortest_path(g_switches, weight='weight')

    # Compute next hop port forwarding table for switches
    next_hop_port = {}
    for s_src in switches:
        for s_dst in switches:
            if s_src != s_dst:
                path = spaths[s_src][s_dst]
                next_hop = path[1]  # Get the next hop along path from src to dst
                port = g_switches.get_edge_data(s_src,next_hop)["ports"][s_src]
                next_hop_port[(s_src, s_dst)] = port

    # Create MAC based forwarding table for each switch from previous table
    # and direct switch to host links
    mac_fwd_table = {}
    for s_src in switches:
        mac_fwd_table[s_src] = {}  # Initialize forwarding table for each source switch
        for s_dst in switches:
            if s_src != s_dst:
                for h in switch_host_map[s_dst]:
                    h_mac = g.node[h]['mac']
                    mac_fwd_table[s_src][h_mac] = next_hop_port[(s_src, s_dst)]
            else:  # Host is directly connected to the switch
                for h in switch_host_map[s_dst]:
                    port = g.get_edge_data(s_src,h)["ports"][s_src]
                    h_mac = g.node[h]['mac']
                    mac_fwd_table[s_src][h_mac] = port
    return mac_fwd_table

if __name__ == '__main__':
    g = json_graph.node_link_graph(json.load(open("fattree.js")))
    fwdTable = computeL2FwdTables(g)
    for s in fwdTable.keys():
        print "Switch {} forwarding table:".format(s)
        print fwdTable[s]
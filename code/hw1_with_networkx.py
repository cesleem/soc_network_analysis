# see http://networkx.lanl.gov/ for a tutorial on NetworkX
import networkx as nx

# your GML file
filename = 'data/LadaFacebookAnon.gml'

# read in the graph using networkX
G = nx.read_gml(filename,relabel=True)

# check out the functions number_of_nodes, number_of_edges,
# connected_component_subgraphs, degree_centrality,number_connected_components
# to answer the hw 1 questions about your network

# number of nodes:
# num_nodes = G.number_of_nodes()
# print 'number of nodes: ' + str(num_nodes)

# # number_of_edges:
# num_edges = G.number_of_edges()
# print 'number of edges: ' + str(num_edges)

# # connected_component_subgraphs:
# num_connected_component_subgraphs = sorted(nx.connected_component_subgraphs(G), key = len, reverse=True) #list(nx.connected_component_subgraphs(G))
# print 'size of largest connected component: ' + str(len(num_connected_component_subgraphs[0]))

# degree_centrality
# deg_centrality = nx.degree_centrality(G)
# max_deg_centrality = max(deg_centrality, key=deg_centrality.get)
# print 'degree centrality: ' + str(deg_centrality[max_deg_centrality])

#maximum degree:
degrees = G.degree()
max_degree = max(degrees, key=degrees.get)
print 'maximum degree: ' + str(degrees[max_degree])
print degrees


# # number_connected_components
# num_connected_components = nx.number_connected_components(G)
# print 'number of connected components: ' + str(num_connected_components)
import igraph 
import random

how_many_graphs = 20000
max_nodes = 1000
max_edges = 10000
delete_edges_perc = 0.1  # Delete 10% of nodes!

for i in range(how_many_graphs):
    num_nodes = random.randint(1, max_nodes)
    num_edges = random.randint(1, max_edges)

    # Generate random graph
    graph = igraph.Graph(directed=True)
    graph.add_vertices(num_nodes)
    edges = [
        random.choices(range(num_nodes), k=2) 
        for _ in range(num_edges)
    ]
    graph.add_edges(edges)

    # delete nodes
    del_list = random.choices(range(num_edges), k= int(num_edges*delete_edges_perc))
    graph.delete_edges(del_list)










""" Submission for Part-1 of Module-1 """
# Setup Constants
EX_GRAPH0 = dict() #{0 : set(1,2), 1: set(), 2: set()}
EX_GRAPH0[0] = set([1,2])
EX_GRAPH0[1] = set([])
EX_GRAPH0[2] = set([])

EX_GRAPH1 = dict()
EX_GRAPH1[0] = set([1, 4, 5])
EX_GRAPH1[1] = set([2, 6])
EX_GRAPH1[2] = set([3])
EX_GRAPH1[3] = set([0])
EX_GRAPH1[4] = set([1])
EX_GRAPH1[5] = set([2])
EX_GRAPH1[6] = set([])

EX_GRAPH2 = dict()
EX_GRAPH2[0] = set([1, 4, 5])
EX_GRAPH2[1] = set([2, 6])
EX_GRAPH2[2] = set([3, 7])
EX_GRAPH2[3] = set([7])
EX_GRAPH2[4] = set([1])
EX_GRAPH2[5] = set([2])
EX_GRAPH2[6] = set([])
EX_GRAPH2[7] = set([3])
EX_GRAPH2[8] = set([1, 2])
EX_GRAPH2[9] = set([0, 3, 4, 5, 6, 7])

def make_complete_graph(num_nodes):
    """ 
    Takes the number of nodes num_nodes and returns a dictionary 
    corresponding to a complete directed graph with the specified 
    number of nodes. (self-loops are not allowed)
    The nodes of the graph should be numbered 0 to num_nodes - 1 
    when num_nodes is positive. Otherwise, the function returns a 
    dictionary corresponding to the empty graph. 
    """
    node_list = [num for num in range (0, num_nodes)]
    digraph = dict()

    for node in node_list:
        digraph[node] = set(cNode for cNode in node_list if cNode != node)
                
    return digraph

def compute_in_degrees(digraph):
    """
    Takes a directed graph (a dictionary), computes the 
    in-degrees for the nodes in the graph. It returns a 
    dictionary with the same set of keys (nodes) as 
    digraph whose corresponding values are the number 
    of edges whose head matches a particular node.
    """    
    
    in_degrees = dict()

    for (node, edges) in digraph.items():
        if node not in in_degrees:
            in_degrees[node] = 0
        for edge in edges:
            if edge in in_degrees:
                in_degrees[edge] += 1
            else:
                in_degrees[edge] = 1

    return in_degrees

def in_degree_distribution(digraph):
    """
    Takes a directed graph digraph (a dictionary), computes the 
    unnormalized distribution of the in-degrees of the graph. 
    The function should return a dictionary whose keys correspond
    to in-degrees of nodes in the graph. The value associated with
    each particular in-degree is the number of nodes with that 
    in-degree. In-degrees with no corresponding nodes in the graph
    are not included in the dictionary.
    """    
    
    in_degrees = compute_in_degrees(digraph)
    in_degree_dist = dict()

    for in_degree in in_degrees.values():
        if in_degree not in in_degree_dist: 
            in_degree_dist[in_degree] = 1
        else:
            in_degree_dist[in_degree] += 1

    return in_degree_dist

"""
File w/ utility functions and some
global variables used for testing.
"""

import urllib2

# Setup Constants
EX_GRAPH0 = dict()
EX_GRAPH0 = {
             0: set([1,2]),
             1: set([]),
             2: set([])
            }

EX_GRAPH1 = dict()
EX_GRAPH1 = {
             0: set([1, 4, 5]),
             1: set([2, 6]),
             2: set([3]),
             3: set([0]),
             4: set([1]),
             5: set([2]),
             6: set([]) 
            }

EX_GRAPH2 = {
             0: set([1, 4, 5]),
             1: set([2, 6]),
             2: set([3, 7]),
             3: set([7]),
             4: set([1]),
             5: set([2]),
             6: set([]),
             7: set([3]),
             8: set([1, 2]),
             9: set([0, 3, 4, 5, 6, 7])              
            }

def copy_graph(graph):
    """
    Make a copy of a graph
    """
    new_graph = {}
    for node in graph:
        new_graph[node] = set(graph[node])
    return new_graph

def delete_node(ugraph, node):
    """
    Delete a node from an undirected graph
    """
    neighbors = ugraph[node]
    ugraph.pop(node)
    for neighbor in neighbors:
        ugraph[neighbor].remove(node)

def count_num_of_edges(graph):
    """
    Count the number of edges
    in an undirected graph
    """
    num_of_edges = 0
    for edges in graph.values():
        num_of_edges += len(edges)

    return (num_of_edges/2)

def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph
    
    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]
    
    print "Loaded graph with", len(graph_lines), "nodes"
    
    answer_graph = {}
    out_degrees = 0
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:            
            answer_graph[node].add(int(neighbor))
        out_degrees += (len(answer_graph[node]))

    print ("Avg out degree: " + str(float(out_degrees)/len(answer_graph)))

    return answer_graph

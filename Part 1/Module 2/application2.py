import utility
import random
import project1
import project2
import upa
import matplotlib.pyplot as plt
import numpy as np
import time
from collections import defaultdict

GRAPH_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_rf7.txt"

CN_GRAPH  = dict()
ER_GRAPH  = dict()
UPA_GRAPH = dict()

def exec_module(graph, module):
    start = time.clock()
    module(graph)
    stop = time.clock()
    return stop - start

def er_graph(n, p):
    nodes = [num for num in range(n)]
    
    num_of_edges = 0
    graph = dict()
    for node_i in range(n):
        for node_j in range(n):
            if (node_i != node_j ) and (random.random() < p):
                if node_i not in graph:
                    graph[node_i] = set([])
                if node_j not in graph:
                    graph[node_j] = set([])
                graph[node_i].add(node_j)
                graph[node_j].add(node_i)                 

    print ("Created graph w/ " + str(n) + " nodes and " +
           str(utility.count_num_of_edges(graph)) + " edges!")
    return graph

def upa_graph(total_nodes, min_nodes):
    graph = project1.make_complete_graph(min_nodes)
    upa_trial = upa.UPATrial(min_nodes)

    for node in range(min_nodes, total_nodes):
        neighbors = upa_trial.run_trial(min_nodes)
        graph[node] = neighbors
        for neighbor in neighbors:
            graph[neighbor].add(node)

    #print ("# of edges in UPA Graph -> " + str(utility.count_num_of_edges(graph)))
    return graph

def random_order(graph):
    nodes = graph.keys()
    return random.sample(nodes, len(nodes))

def make_graphs():
    global CN_GRAPH, ER_GRAPH, UPA_GRAPH
    CN_GRAPH  = utility.load_graph(GRAPH_URL)    
    ER_GRAPH  = er_graph(1239, 0.002)    
    UPA_GRAPH = upa_graph(1239, 2)    

def test_resilient(resilience):
    '''
    test if the graph is resilient, that is:
    if the size of the largest cc is within 25% of its original value,
        after 20% nodes removed
    '''
    return resilience[int((len(resilience)-1)*0.2)]>((len(resilience)-1)-(len(resilience)-1)*0.25)

def question1and2():
    global CN_GRAPH, ER_GRAPH, UPA_GRAPH
    attacked_cn  = project2.compute_resilience(CN_GRAPH, random_order(CN_GRAPH))
    attacked_er  = project2.compute_resilience(ER_GRAPH, random_order(ER_GRAPH))    
    attacked_upa = project2.compute_resilience(UPA_GRAPH, random_order(UPA_GRAPH))   

    plt.plot(attacked_cn, 'b-', label='Computer Graph')
    plt.plot(attacked_er, 'g-', label='ER graph [p=0.002]')
    plt.plot(attacked_upa, 'r-', label='UPA graph [m=2]')
    plt.legend(loc='upper right')

    plt.title('Resilience of networks under a random attack');
    plt.xlabel('# nodes removed')
    plt.ylabel('Largest connected component')
    plt.show()
    plt.close

    print test_resilient(attacked_cn)
    print test_resilient(attacked_er)
    print test_resilient(attacked_upa)

def time_algorithms():
    slow_times = []
    fast_times = []

    for n in range (10, 1000, 10):
        graph = upa_graph(n, 5)        
        slow_times.append(exec_module(graph, targeted_order))
        fast_times.append(exec_module(graph, fast_targeted_order))
        
    #print ("Targeted Order run time -> " + str(slow_times))
    #print ("Fast Targeted Order run time -> " + str(fast_times))
    return slow_times, fast_times

def targeted_order(ugraph):
    """
    Compute a targeted attack order consisting
    of nodes of maximal degree
    
    Returns:
    A list of nodes
    """
    # copy the graph
    new_graph = utility.copy_graph(ugraph)
    
    order = []    
    while len(new_graph) > 0:
        max_degree = -1
        for node in new_graph:
            if len(new_graph[node]) > max_degree:
                max_degree = len(new_graph[node])
                max_degree_node = node
        
        neighbors = new_graph[max_degree_node]
        new_graph.pop(max_degree_node)
        for neighbor in neighbors:
            new_graph[neighbor].remove(max_degree_node)

        order.append(max_degree_node)
    return order

def fast_targeted_order(ugraph):
    graph = utility.copy_graph(ugraph)
    
    degree_set = defaultdict(set)

    for node in graph.keys():            
        degree_set[len(graph[node])].add(node)

    idx = 0
    order = []
    for k in reversed(range(len(graph)-1)) :
        while len(degree_set[k]) != 0:
            node = degree_set[k].pop()
            neighbors = graph[node]
            for neighbor in neighbors:
                d = len(graph[neighbor])
                degree_set[d].discard(neighbor)
                degree_set[d-1].add(neighbor)

            order.append(node)
            utility.delete_node(graph, node)
            
    return order;

def question3():
    time_slow, time_fast = time_algorithms()

    x = np.arange(10, 1000, 10)
    plt.plot(x, time_slow, 'b-', label='targeted_order')
    plt.plot(x, time_fast, 'r-', label='fast_targeted_order')

    plt.legend(loc='upper right')

    plt.title('Comparison of targeted_order() and fast_targeted_order()');
    plt.xlabel('# of nodes')
    plt.ylabel('Running Time')
    plt.show()

def question4and5():
    make_graphs()    
    
    attacked_cn  = project2.compute_resilience(CN_GRAPH, fast_targeted_order(CN_GRAPH))
    attacked_er  = project2.compute_resilience(ER_GRAPH, fast_targeted_order(ER_GRAPH))    
    attacked_upa = project2.compute_resilience(UPA_GRAPH, fast_targeted_order(UPA_GRAPH))   
    

    plt.plot(attacked_cn, 'b-', label='Computer Graph')
    plt.plot(attacked_er, 'g-', label='ER graph [p=0.002]')
    plt.plot(attacked_upa, 'r-', label='UPA graph [m=2]')
    plt.legend(loc='upper right')

    plt.title('Resilience of networks under a (fast) targeted attack');
    plt.xlabel('# nodes removed')
    plt.ylabel('Largest connected component')
    plt.show()
    plt.close

    print test_resilient(attacked_cn)
    print test_resilient(attacked_er)
    print test_resilient(attacked_upa)    

if __name__ == "__main__":
    make_graphs()    
    question1and2()
    question3()
    question4and5()
   
    

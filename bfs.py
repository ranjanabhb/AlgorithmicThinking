""" Homework submission of Module-2 """
# Setup Constants
EX_GRAPH0 = dict()
EX_GRAPH0 = {
             0: set([1,2]),
             1: set([]),
             2: set([])
            }

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

from collections import deque

def remove_node_from_graph(ugraph, node):
    """
    For each node in ugraph, if node is in
    from the neighbors list; remove it .
    
    Removes node from ugraph.
    """
    for edges in ugraph.values():
        if node in edges:
            edges.remove(node)      

    ugraph.pop(node)

def bfs_visited(ugraph, start_node):
    """
    Takes an undirected graph "ugraph" and a node "start_node"
    and returns a set consisting of all the nodes that are visited
    by doing BFS on ugraph, starting at start_node
    """
    visited = set()
    visited.add(start_node)
    queue = deque()
    queue.append(start_node)

    while len(queue) > 0:        
        node = queue[0]
        print ("Working w/ node: " + str(node))
        queue.popleft()
        for neighbor in ugraph[node]:
            print ("\tVisiting neighbor: " + str(neighbor))
            if neighbor not in visited:
                print ("\t\tFound new neighbor: " + str(neighbor))
                visited.add(neighbor)
                queue.append(neighbor)

    print ("Nodes visited from " + str(start_node) + ": " + str(visited))
    return visited

def cc_visited(ugraph):
    """
    Takes the undirected graph ugraph and returns a list of sets,
    where each set consists of all the nodes (and nothing else)
    in a connected component, and there is exactly one set in the
    list for each connected component in ugraph and nothing else.
    """
    remaining_nodes = set(ugraph.keys())
    connected_component = list()

    print (remaining_nodes)
    
    while len(remaining_nodes) > 0:
        node = remaining_nodes.pop()
        remaining_nodes.add(node)        
        visited = bfs_visited(ugraph, node)
        connected_component.append(visited)
        remaining_nodes.difference_update(set(visited))        

    return connected_component            

def largest_cc_size(ugraph):
    """
    Takes the undirected graph ugraph and returns the size (an integer)
    of the largest connected component in ugraph
    """
    connected_components = cc_visited(ugraph)
    if len(connected_components) == 0:
        return 0
    else:
        return max([len(cc_size) for cc_size in connected_components])    
    
def compute_resilience(ugraph, attack_order):
    """
    Takes the undirected graph ugraph, a list of nodes attack_order
    and iterates through the nodes in attack_order. For each node in
    the list, the function removes the given node and its edges from
    the graph and then computes the size of the largest connected
    component for the resulting graph.
    
    The function should return a list whose k+1th entry is the size
    of the largest connected component in the graph after the removal
    of the first k nodes in attack_order. The first entry (indexed by zero)
    is the size of the largest connected component in the original graph.
    """

    resilience = list()
    resilience.append(largest_cc_size(ugraph))

    #resilience.append([largest_cc_size(ugraph.pop(node)) for node in attack_order])

    for node in attack_order:
        remove_node_from_graph(ugraph, node)
        resilience.append(largest_cc_size(ugraph))

    return resilience
    
if __name__ == "__main__":
    #print (bfs_visited(EX_GRAPH2, 0))
    #print (cc_visited(EX_GRAPH2))
    #print (largest_cc_size(EX_GRAPH2))
    print (compute_resilience(EX_GRAPH2, [2, 3, 6]))


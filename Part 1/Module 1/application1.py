"""
Imports physics citation graph 
"""

# general imports
import urllib2
import part1_module1_project as project
import plotter

# Set timeout for CodeSkulptor if necessary
#import codeskulptor
#codeskulptor.set_timeout(20)


###################################
# Code for loading citation graph

CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"

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

def normalize_graph(nodes,
                    indegree_distribution):
    """
    This function will take the indegree distribution
    of the citation graph and then normalize it.
    """
    normalized_distribution = dict()
    
    for (indegree, num_of_nodes) in indegree_distribution.items():
        #print (indegree, num_of_nodes)        
        normalized_distribution[indegree] = float(num_of_nodes)/nodes

    return normalized_distribution
    
def verify_normalized_distribution(normalized_graph):
    total = 0
    for (indegree, normalized_value) in normalized_graph.items():
        total += normalized_value

    print ("\nNormalized Value: " + str(total))


def run():
    citation_graph = load_graph(CITATION_URL)

    print (len(citation_graph))

    print(project.in_degree_distribution(citation_graph))
    normalized_distribution = normalize_graph(len(citation_graph),
                                              project.in_degree_distribution(citation_graph))

    print(len(normalized_distribution.keys()))
    print(len(normalized_distribution.values()))

    x = normalized_distribution.keys()
    y = normalized_distribution.values()
    print(len(x))
    print(len(y))

    x.pop(0)
    y.pop(0)

    plotter.plot(x, y)

    verify_normalized_distribution(normalized_distribution)

if __name__ == "__main__":
    run()




import jsonpickle
import networkx as nx

def load_challenge(number,data_path = 'graph_data/'):
    file_path = data_path+'graph'+str(number)+'.json'
    try:
        with open(file_path,'rb') as f:
            challenge = jsonpickle.decode(f.read())
        # Now just refresh the NetworkX challenge objects
        challenge.social_graph = nx.DiGraph(challenge.social_graph)
        challenge.concept_graph = nx.DiGraph(challenge.concept_graph)
        return challenge
    except IOError:
        print "Unable to open challenge %d"%number
        return None
        
def save_challenge(challenge,data_path = 'graph_data/'):
    ''' Saves a particular challenge object to disk'''
    try:
        file_path = data_path+"graph"+str(challenge.number)+'.json'
        pickled = jsonpickle.encode(challenge)
        with open(file_path,'wb') as f:
            f.write(pickled)
    except IOError:
        print 'Error: Unable to save challenge file!'
    
def apply_graph_metric_to_nodes(graph,function):
    ''' Applies a given network function to graph nodes to save on 
        later computation.
        Can take any function as long as that function takes in a networkx graph
        and outputs a dictionary of values keyed on the networkx nodes.
    '''
    # we'll use the function name as the key in the node's data
    func_name = function.__name__
    node_output=function(graph)
    nx.set_node_attributes(graph,func_name,node_output)    
    
def load_user_stats_into_concept_graph(challenge):
    ''' Given a particular challenge, finds some user stats and preloads them as
        keys on the concept graph
    '''
    stats = [nx.betweenness_centrality,
              nx.in_degree_centrality,
              nx.out_degree_centrality,
              nx.degree_centrality,
              nx.DiGraph.out_degree,
              nx.DiGraph.in_degree,
              nx.DiGraph.degree
             ]
    for func in stats:
        nx.set_node_attributes(challenge.social_graph,func.__name__,func(challenge.social_graph))
    
    for node in challenge.concept_graph.nodes_iter():
        user_id =  challenge.concept_graph.node[node]['creator']
        user = challenge.social_graph.node[user_id]
        for key,val in user.items():
            challenge.concept_graph.node[node]['u_'+key]=val    
    
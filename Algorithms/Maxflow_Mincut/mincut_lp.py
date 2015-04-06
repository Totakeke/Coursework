import networkx as nx
import pulp as plp
import sys

def main(argv):
    global inputpath
    global source
    global sink
    if len(sys.argv) != 4:
        print "Usage: python <source_file> <path_of_input_data_file> <source_node> <sink_node> "
        sys.exit()
    else:
        inputpath = sys.argv[1]
        source = int(sys.argv[2])
        sink = int(sys.argv[3])

if __name__ == "__main__":
    main(sys.argv)
    
#read in the gml file and convert it into a directed graph
G = nx.read_gml(inputpath)
H = nx.DiGraph(G)

#define the LP Problem
mincut = plp.LpProblem("MinCut", plp.LpMinimize)

#define each node to be a variable. This is equivalent to the Pi value in the notes.
node_vars = plp.LpVariable.dicts("Node",H.nodes(),0,1,plp.LpInteger)

#define each weight to be a variable, based on the edges that exist. This is equivalent to the Wij value in the notes.
weight_vars = plp.LpVariable.dicts("Weight",H.edges(),0,1,plp.LpInteger)

#define the objective function of the LP. As all capacities equal to one, it doesn't need to be explicitly stated. 
mincut += plp.lpSum(weight_vars[q] for q in H.edges())

#iterate over all edges as there is one constraint function for each edge that exist.
for e in H.edges_iter():
    mincut += node_vars[e[1]] - node_vars[e[0]] <= weight_vars[(e[0],e[1])]
    
#set the last constraint where the source and sink has to be different sets
mincut += node_vars[sink] - node_vars[source] == 1

#solve and print the optimal objective value
mincut.solve()
print plp.value(mincut.objective)




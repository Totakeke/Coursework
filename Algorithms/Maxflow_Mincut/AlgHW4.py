import networkx as nx
import sys

def main(argv):
    global inputpath
    global source
    global target
    if len(sys.argv) != 4:
        print "Usage: python <source_file> <path_of_input_data_file> <source_node> <sink_node> "
        sys.exit()
    else:
        inputpath = sys.argv[1]
        source = int(sys.argv[2])
        target = int(sys.argv[3])

if __name__ == "__main__":
    main(sys.argv)


#G=nx.read_gml("C:\Users\Justin\Documents\karate (1)\karate.gml")
G=nx.read_gml(inputpath)
for u in G.edges():
    G[u[0]][u[1]]['capacity']=1.0

maxflow1= nx.maximum_flow_value(G,source,target)
mincut1 = nx.minimum_cut_value(G,source,target)


#H=nx.read_gml("C:\Users\Justin\Downloads\power\power.gml")
#for u in H.edges():
#    H[u[0]][u[1]]['capacity']=1.0

#maxflow2 = nx.maximum_flow_value(H,2553,4458)
#mincut2 = nx.minimum_cut_value(H,2553,4458)

#print maxflow1, mincut1, maxflow2, mincut2
print maxflow1, mincut1
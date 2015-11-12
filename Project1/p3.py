import networkx as nx
import csv
import scipy as sp
import scipy.stats as st
import matplotlib.pyplot as plt
import numpy as np
import random
import math
import sys
import csv
def loadEdgeList(anomymizedEdges):
    G = nx.DiGraph()
    UG = nx.Graph()
    with open(anomymizedEdges,'rb') as file:
        content = csv.reader(file)
        for row in content:
            G.add_edge(row[0],row[1])
    UG = G.to_undirected()

    f = open('res.txt','wb')
    f.writelines( 'Average Local Clustering : {0}\n'.format(str(nx.average_clustering(UG)))) 

    f.writelines( 'Global Clustering: {0}\n'.format(str(nx.transitivity(G)))) 



    js = max([i for i in nx.algorithms.link_prediction.jaccard_coefficient(UG)], key = lambda x:x[2])
    f.writelines(  '\nNodes with max Jaccard Similarity : {0} {1}\n'.format(str(js[0]),str(js[1])))
    f.writelines( 'Page Rank Centrality:')
    pageRank = sorted(nx.pagerank_numpy(G).items(),key=lambda x:x[1])

    for i in pageRank[-10:]:
        f.writelines(  '{0}       {1}\n'.format(i[0],i[1]))
    f.writelines(  'Eigenvector Centrality:')
    eigenVector = sorted(nx.centrality.eigenvector_centrality(G).items(),key=lambda x:x[1] )
    for i in eigenVector[-10:]:
        f.writelines(  '{0}       {1}\n'.format(i[0],i[1]))
    f.writelines(  'Degree Centrality:')
    degreeCentrality = sorted(nx.centrality.in_degree_centrality(G).items(),key=lambda x:x[1])
    for i in degreeCentrality[-10:]:
        f.writelines(  '{0}       {1}\n'.format(i[0],i[1]))

    f.writelines(  'Rank correlation between Pagerank Centrality and Eigenvector Centrality: {0}'.format(str(st.spearmanr([i[1] for i in pageRank],[i[1] for i in eigenVector])[0])))

    f.writelines(  'Rank correlation between Pagerank Centrality and Degree Centrality: {0}'.format( str(st.spearmanr([i[1] for i in pageRank],[i[1] for i in degreeCentrality])[0])))

    f.writelines(  'Rank correlation between Degree Centrality and Eigenvector Centrality: {0}'.format(str(st.spearmanr([i[1] for i in degreeCentrality],[i[1] for i in eigenVector])[0])))

    js = max([i for i in nx.algorithms.link_prediction.jaccard_coefficient(UG)], key = lambda x:x[2])
    f.writelines(  '\nNodes with max Jaccard Similarity : {0} {1}\n'.format(str(js[0]),str(js[1])))
    
    f.close()
 


#loadEdgeList('anonymizededges_1000.csv')

try:
    if(len(sys.argv) != 2):
        print 'Usage \'p3.py filename\''
        sys.exit(-1)
    else:
        loadEdgeList(sys.argv[1])
except:
    print ''
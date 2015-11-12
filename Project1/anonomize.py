
import csv
def anonomize(file,sample):
    edges = []
    nodeDict = {}
    anonomizedEdges = []    

    if sample:
        with open(file,'r') as datafile:
            content = csv.reader(datafile)    
            total_nodes = 0
            children = 0
            for i in content:
                total_nodes += 1
                children += len(i)

            #sampling by number of children
            samplesize = children/total_nodes

    with open(file,'r') as datafile:
        anonomizedCount = 1
        content = csv.reader(datafile)    
        for row in content:
            node = row[0].strip()
            if not nodeDict.has_key(node):
                nodeDict[node] = anonomizedCount
                anonomizedCount += 1
            if sample : n = samplesize
            else: n = len(row)
            for i in row[1:n]:
                edges.append([node,i])                
                if not nodeDict.has_key(i):
                    nodeDict[i] = anonomizedCount
                    anonomizedCount += 1
                anonomizedEdges.append([nodeDict[node],nodeDict[i]])
            if sample:                 
                if len(nodeDict.items())>=1000: break
     
    with open('edges.csv','wb') as edgeFile:
        writer = csv.writer(edgeFile, quoting=csv.QUOTE_ALL)
        writer.writerows(edges)  
    
    with open('anonomizededges.csv','wb') as edgeFile:
        writer = csv.writer(edgeFile, quoting=csv.QUOTE_ALL)
        writer.writerows(anonomizedEdges)     
        
    with open('nodes.csv','wb') as edgeFile:
        writer = csv.writer(edgeFile, quoting=csv.QUOTE_ALL)
        writer.writerows(nodeDict.items())           

anonomize('output5_AY.csv',False)
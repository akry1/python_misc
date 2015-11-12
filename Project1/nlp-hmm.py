import pandas as pd

def trainfilepd(path):
    content  = pd.read_table(path, dtype=str,header=None,delimiter='/',names=list('AB'))

    words = list(content['A'].str.strip())
    tags = list(content['B'].str.strip())
    
    #sentences = ' '.join(words).split(' ### ')
    #sentences[0] = sentences[0].replace('### ','')
    #sentences[-1] = sentences[-1].replace(' ###','')

    #tagsSequences = ' '.join(alltags).split(' ### ')
    #tagsSequences[0] = tagsSequences[0].replace('### ','')
    #tagsSequences[-1] = tagsSequences[-1].replace(' ###','')

    def transitionProbs():
        bigrams = {}
        for i in range(len(tags)-1):
            bigrams[(tags[i],tags[i+1])] = bigrams.get((tags[i],tags[i+1]),0)+1
        return { i: float(j)/tags.count(i[0]) for i,j in bigrams.items()}

    def ObservationProbs():
        content['C'] = 1
        bigrams = content.groupby(['B','A'], as_index=True)['C'].sum().to_dict()
        return { i: float(j)/tags.count(i[0]) for i,j in bigrams.items()}
    
    return transitionProbs(), ObservationProbs()



def trainfile(path):
    content = list(open(path))

    words = []
    tags = []
    observations = {}

    for i in content:
        splits = i.replace('\n','').split('/')
        words.append(splits[0])
        tags.append(splits[1])
        observations[(splits[1],splits[0])] = observations.get((splits[1],splits[0]),0)+1

    transitions = {}
    for i in range(len(tags)-1):
        transitions[(tags[i],tags[i+1])] = transitions.get((tags[i],tags[i+1]),0)+1
    transitionProbs = { i: float(j)/(tags.count(i[0])) for i,j in transitions.items()}
    observationProbs = { i: float(j)/(tags.count(i[0])) for i,j in observations.items()}

    return transitionProbs, observationProbs, set(tags)


def testfile(path):
    content = list(open(path))
    words = ['###']
    tags = ['###']
    sentences = []
    generatedtags = []
    tagsequence = []

    for i in content[1:]:        
        splits = i.replace('\n','').split('/')
        words.append(splits[0])
        tags.append(splits[1])
        if splits[0]=='###' and splits[1]=='###':
            generatedtags.extend(Viterbi(words))
            sentences.append(words)
            tagsequence.extend(tags)
            words = ['###']
            tags = ['###']
    
    count = 0
    total = len(tagsequence)
    for i in range(total):
        if generatedtags[i]!=tagsequence[i]:
            count +=1
    print 'Error Rate is {0}'.format(float(count)/total)

        
    #print sentences
    #print '============================='
    #print tagsequence




def Viterbi(sentence):
    v= {}
    bp = {}
    p = {}
    unknownProb = 1.0/(10**8+len(tags))
    for i in range(len(sentence)):            
        np = {}
        for j in tags:            
            if i==0:
                v[(i,j)] = transitionProbs.get((sentence[i],j),unknownProb)* observationProbs.get((j,sentence[i]),unknownProb)
                bp[(i,j)] = j
                p[j] = [j]
            else:            
                v[(i,j)], maxstate = max([ (v[(i-1,k)]*transitionProbs.get((j,k),unknownProb)*observationProbs.get((j,sentence[i]),unknownProb),k) \
                                           for k in tags], key=lambda x:x[0])
                bp[(i,j)] = maxstate
                np[j]= p[maxstate]+[j]
        if i!=0:
            p = np

    finalProb,finalState = max( [ (v[(len(sentence)-1,s)],s) for s in tags], key=lambda x:x[0])

    stateSequence = [finalState]
    for i in range(1,len(sentence)):
        stateSequence.append(bp[(len(sentence)-i,stateSequence[i-1])])
    stateSequence.reverse()
    return stateSequence
    #return p[finalState]

transitionProbs, observationProbs, tags = trainfile('F:\Skydrive\ASU\NLP\entrain.txt')

testfile('F:\Skydrive\ASU\NLP\entest.txt')
#trainfilepd('F:\Skydrive\ASU\NLP\entrain.txt')

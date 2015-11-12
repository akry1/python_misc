import MapReduce
import sys

mr = MapReduce.MapReduce()

# Part 2
def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[1]
    value = record
    mr.emit_intermediate(key, value)

# Part 3
def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total=[]
    #for v in list_of_values:


    total.extend([ list_of_values[v]+list_of_values[j] for v in range(0, len(list_of_values)-1) for j in range(v+1,len(list_of_values)) if list_of_values[v][0]=='order' and list_of_values[j][0]=='line_item'])
    for i in total:
        mr.emit(i)

# Part 4
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)

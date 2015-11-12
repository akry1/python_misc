import MapReduce
import sys

mr = MapReduce.MapReduce()

# Part 2
def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[1][:-10]
    mr.emit_intermediate(key, 1)

# Part 3
def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    mr.emit((key))

# Part 4
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
import MapReduce
import sys

mr = MapReduce.MapReduce()

# Part 2
def mapper(record):
    # key: document identifier
    # value: document contents
    key = tuple(sorted(record))
    mr.emit_intermediate(key, 1)

# Part 3
def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    if len(list_of_values) !=2:
      mr.emit((key[0], key[1]))
      mr.emit((key[1], key[0]))

# Part 4
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
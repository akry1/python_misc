import MapReduce
import sys

mr = MapReduce.MapReduce()

# Part 2
def mapper(record):
    # key: document identifier
    # value: document contents
    if record[0]=='a':
        key = record[1]
    else:
        key = record[2]
    mr.emit_intermediate(key, record)

# Part 3
def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total = []
    for v in list_of_values:
      total.append(v)
    mr.emit((key, list(set(total))))

# Part 4
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
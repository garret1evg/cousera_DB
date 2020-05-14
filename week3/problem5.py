import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    string = record[1]
    string = string[:-10]
    #emit trimm string   
    mr.emit_intermediate(string, 1);
def reducer(key, list_of_values):
	mr.emit(key)			
	

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)

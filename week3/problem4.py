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
    key = record[0]
    friend = record[1]
    #emit main relationship    
    mr.emit_intermediate(key, record);
    #emit friend relationship to check non-sym
    mr.emit_intermediate(friend, record);
def reducer(key, list_of_values):
    	# key: word
    	# value: book
	for v in list_of_values:
		nonRel=[v[1],v[0]]
		if nonRel not in list_of_values:
			if v[0] == key:
				mr.emit((v[0],v[1]))
			else:
				mr.emit((v[1],v[0]))			
	

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)

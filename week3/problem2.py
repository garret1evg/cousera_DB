import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    identifier = record[1]	
    
    mr.emit_intermediate(identifier, record)

def reducer(key, list_of_values):
	#print key
   	#print list_of_values
	order = []
	for value in list_of_values:
		if(value[0] == 'order'):
			order = value	
		else:
			merged = order + value			
			mr.emit(merged)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)

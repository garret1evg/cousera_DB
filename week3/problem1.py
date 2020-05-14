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
    value = record[1]
    words = value.split()
    #print record
    #print key
    #print words	
    for w in words:
      mr.emit_intermediate(w, key)

def reducer(key, list_of_values):
    	# key: word
    	# value: book
   	unique_books=[]
	for v in list_of_values:
		if v not in unique_books:
			unique_books.append(v)
	
	mr.emit((key, unique_books))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)

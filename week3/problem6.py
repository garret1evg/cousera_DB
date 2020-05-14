import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    for k in range(5):
        if record[0] == 'a':
            indexes = (record[1], k)
        else:
            indexes = (k, record[2])
        mr.emit_intermediate(indexes, record)
def reducer(key, list_of_values):
    row = [0] * 5
    column = [0] * 5
    for x in list_of_values:
        matrix = x[0]
        i = x[1]
        j = x[2]
        value = x[3]
        target = row if matrix == 'a' else column
        target[j if matrix == 'a' else i] = value
    result = 0
    for k in range(5):
        result += row[k] * column[k]
    if result != 0:
        mr.emit(key + (result,))


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)

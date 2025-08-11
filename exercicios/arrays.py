import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    ar = numpy.array(arr, float)
    return ar[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
print(type(result))

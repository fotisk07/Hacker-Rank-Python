import numpy

n, m = [int(i) for i in input().strip().split()]
A = numpy.array([[int(i) for i in input().strip().split()] for j in range(n)])
print(numpy.max( numpy.min(A,1) ))

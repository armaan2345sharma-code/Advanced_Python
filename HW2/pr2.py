#finding max
from functools import reduce
l=[1,5,7,8,9,10,56,98,80]
m=reduce(max,l)
print(m)
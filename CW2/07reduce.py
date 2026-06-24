from functools import reduce 
sum=lambda a,b: a+b
l=[25,67,88,99,10]
val=reduce(sum,l)
print(val)
def square(num):
    k=num*num
    return k
#Method 1
m=[1,2,56,89]
l2=[]
for item in m:
    l2.append(square(item))
print(l2)
#Method 2
print(list(map(square,m)))
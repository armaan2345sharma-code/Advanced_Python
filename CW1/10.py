a=[1,2,3,4,5,6,8,9,7,]
#b=[]
#for item in a:
    #if item%2==0:
       # b.append(item)
#print(b)
list1=[item for item in a if item%2==0]#list comprehension 
print(list1)
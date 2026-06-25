def divisible_5(num):
    if num%5==0:
        return True
    else:
        return False
l1=[5,6,7,8,9,10,16,20]
print(list(filter(divisible_5,l1)))
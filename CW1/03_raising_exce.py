def increment(num):
    try:
        return  int(num)+1
    except:
        raise ValueError("Not work ")
    
a= increment('dfkj')
print(a)
    
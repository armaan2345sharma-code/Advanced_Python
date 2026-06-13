try:
    i=int(input("Enter a number: "))
    c=1/i
    print(c)
except Exception as e:
    print (e)
else:#Else block will execute if there is no exception
    print("No error occurred.")
    exit()
finally:
    print("we are done")
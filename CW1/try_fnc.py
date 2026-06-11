while(True):
    print("Enter q to quit")
    a=input("enter a number ")
    if a=='q':
        break
    try:
        a=int(a)
        if a>6:
            print("You entered a correct number")
    except Exception as e:
        print("Your input is error result",e)
print("Thanks for playing ")




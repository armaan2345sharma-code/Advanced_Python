try:
    a=int(input("Enter a number:"))
    c=1/a
    print(c)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter a valid number.")
print("thanks for using the program")


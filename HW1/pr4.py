try:
    a=int(input("Enter a numinator: "))
    b=int(input("Enter a denominator: "))
    result=a/b
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Denominator cannot be zero.")
finally:
    print("Program execution is completed")
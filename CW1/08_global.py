a=65#global var
def func():
    global a
    print(f"print a in func: {a}")
    a=10#local var
    print(f"print a in func after assignment: {a}")
func()
print(f"print a in global scope: {a}")
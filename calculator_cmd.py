import sys

def add(a,b): return a+b
def subtract(a,b): return a-b
def multiply(a,b): return a*b
def divide(a,b):
    if b==0:
        return "Error: Cannot divide by zeror"
    return a/b



if len(sys.argv) != 4:
    print("Usage:")
    print("python main.py <add/sub/mul/div> <num1> <num2>")
    sys.exit()


operation = sys.argv[1]
num1 = float(sys.argv[2])
num2 = float(sys.argv[3])

if operation == "add":
    result = add(num1,num2)
elif operation=="sub":
    result = subtract(num1, num2)
elif operation == "mul":
    result = multiply(num1, num2)
elif operation == "div":
    result = divide(num1, num2)
else: 
    result = "Invailid operation"

print("Result: ",result)
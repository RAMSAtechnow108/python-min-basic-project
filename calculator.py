def add(a, b):
    return a + b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b == 0:
        return "please denominatore should be positive"
    return a/b

while True:
    print("--------------------Calculator------------------")
    print("1. Add | 2. Subtract | 3. Multipy | 4.Divide | 5.Exit")
    choice = input("Choose: ")

    if choice == "5":
        print("Exiting...")
        break

    if choice not in ["1", "2", "3","4"]:
        print("Wrong choice! please try again.")
        continue

    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("Error: Bro, Please enter number only.")
        continue

    if choice == "1":
        print(f"The addition of {a} and {b} is: ",add(a,b))
    elif choice == "2":
        print(f"The subtracting form {a} to {b} is: ",subtract(a,b))
    elif choice =="3":
        print(f"The multiplication of {a} and {b} is: ",multiply(a,b))
    elif choice =="4":
        print(f"The division of {a} and {b} is: ",divide(a,b))

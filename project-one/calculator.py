# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
# conflict testing

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: division by zero"
    return a / b

def main():
    print("Select operation: + / - / * / /")
    op = input("Operation: ")
    a = float(input("First number: "))
    b = float(input("Second number: "))

    if op == "+":
        print(add(a, b))
    elif op == "-":
        print(subtract(a, b))
    elif op == "*":
        print(multiply(a, b))
    elif op == "/":
        print(divide(a, b))
    else:
        print("Unknown operation")

main()

# calculator.py

from datetime import datetime, time

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


# conflict testing
def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: division by zero - new note to error message"
    return a / b

def goHomeSooner():
    now = datetime.now()
    if now.weekday() == 4 and now.time() >= time(14, 0):
        print("Go home!")
        exit(0)
    else:
        print("Work more...!")

def main():
    print("Select operation: + / - / * / /")
    op = input("Operation: ")
    #a = float(input("First number: "))
    #b = float(input("Second number: "))

    if op == "+":
        print(add(a, b))
    elif op == "-":
        print(subtract(a, b))
    elif op == "*":
        print(multiply(a, b))
    elif op == "/":
        print(divide(a, b))
    else:
        goHomeSooner()


main()

def add (val1,val2):
    return val1+val2

def multiply (val1, val2):
    return val1*val2

def subtract (val1, val2):
    return val1-val2

def divide (val1,val2):
    val1/val2

operations ={
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

num1 = int(input("Enter the first number:"))
for symbol in operations:
    print(symbol)
operator = input("pick an operator:")

num2 = int(input("Enter the second number:"))


calculation_function = operations[operator]
answer = calculation_function (num1, num2)
print(f"the answer of {num1}{operator}{num2} = {answer} ")
    
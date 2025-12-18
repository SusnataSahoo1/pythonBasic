number1 = input ("Enter the first number ")
number2 = input ("Enter the second number ")

def add(number1, number2):
    return int(number1) + int(number2)

resultAdd = add(number1, number2)
print("Addition :",resultAdd)

def subtract(number1, number2):
    return int(number1) - int(number2)
resultSub = subtract(number1, number2)

print("Subtraction :",resultSub)

def multiply(number1, number2):
    return int(number1) * int(number2)
resultMulti = multiply(number1, number2)

print("Multiplication :",resultMulti)

def divide(number1, number2):
    return int(number1) / int(number2)
resultDiv = divide(number1, number2)
print("Division :",resultDiv)
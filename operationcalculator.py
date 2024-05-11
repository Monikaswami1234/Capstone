def add(a, b):
    return a + b
def subtract(a, b):
    return a - b 
def multiply(a, b):
    return a * b 
def division(a, b):
    if b == 0:
        return "Error! Division by Zero"
    else:
        return a / b

print("Select operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Division")

choice = input("Enter choice(1,2,3,4)")

if choice in ('1', '2', '3', '4'):
    number1 = float(input("Enter first number:"))
    number2 = float(input("Enter second number:"))

    if choice == '1':
        print("Result: ", add(number1, number2))
    elif choice == '2':
        print("Result: ", subtract(number1, number2))
    elif choice == '3':
        print("Result: ", multiply(number1, number2))
    elif choice == '4':
        print("Result: ", division(number1, number2))
    else:
        print("Invalid number")
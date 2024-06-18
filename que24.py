#24. Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result. 
def simple_calculator():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter an operator (+, -, *, /): ").strip()

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
            return
    else:
        print("Invalid operator. Please enter one of +, -, *, /.")
        return

    print(f"The result of {num1} {operator} {num2} is: {result}")

simple_calculator()

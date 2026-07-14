from langchain.tools import tool
from rich import print


@tool
def calculator(expression : str):
    """
    This function helps in performing basic arithmetic operation
    and it supports operators : +,-,//,/,*
    and input should be in format : "15 + 17"
    """

    values = expression.split()
    try:
        num1 = int(values[0])
        operation = values[1]
        num2 = int(values[2])

    except Exception:
        return f"You have enter invalid expression, Example input is : '15 + 27'"
        

    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '//':
        if num2 != 0:
            return num1//num2
        else:
            return f"Division by zero is not possible."
    elif operation == '*':
        return num1*num2
    elif operation == '/':
        if num2 != 0:
            return num1/num2
        else:
            return f"Division by zero is not possible."
            
    else:
        return f"Unsupported Operator, Supported Operators are [+,-,*,/,//]"
    
print(calculator.invoke("10 + 20"))

print(calculator.invoke("10 - 5"))

print(calculator.invoke("10 * 6"))

print(calculator.invoke("10 / 2"))

print(calculator.invoke("10 // 3"))

print(calculator.invoke("10 % 3"))

print(calculator.invoke("hello world"))
print(calculator.invoke("10 +"))
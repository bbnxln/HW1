expression = str(input("Введи строку в польской нотации, разделяя каждый символ пробелом"))

def sum(x, y): return x + y
def subtraction(x, y): return x - y
def multiplication(x, y): return x * y
def division(x, y): return x / y if y != 0 else float('inf')

def rpn(expression):
    stack = []
    operators = {
        '+': sum,
        '-': subtraction,
        '*': multiplication,
        '/': division
    }

    tokens = expression.split()

    for token in tokens:
        if token in operators:
            if len(stack) < 2:
                raise ValueError("Недостаточно операндов для оператора")
            y = stack.pop()
            x = stack.pop()
            result = operators[token](x, y)
            stack.append(result)
        else:
            stack.append(float(token))

    if len(stack) != 1: 
        raise ValueError("Неправильное выражение")
    return stack[0]

result = rpn(expression)
print(f"Результат выражения '{expression}': {result}")
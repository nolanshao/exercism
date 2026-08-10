def isoperation(symbol):
    return symbol in "plus minus multiplied divided"

def isnumber(a):
    try:
        int(a)
        return True
    except ValueError:
        return False

def operation(symbol, a, b):
    A = int(a)
    B = int(b)
    if symbol == 'plus':
        return A + B
    elif symbol == 'minus':
        return A - B
    elif symbol == 'multiplied':
        return A * B
    elif symbol == 'divided':
        return A / B

def answer(question):
    question = question.strip('?')
    tokens = question.split(' ')
    equation = []
    for t in tokens:
        if t != 'What' and t != 'is' and t != 'by':
            equation.append(t)
            
    for i, c in enumerate(equation):
        if i % 2 == 0:
            if not isnumber(c):
                raise ValueError("syntax error")
        else:
            if isnumber(c):
                raise ValueError("syntax error")
            if not isoperation(c):
                raise ValueError("unknown operation")

    if len(equation) == 1:
        return int(equation[0])
    elif len(equation) == 0 or len(equation) == 2:
        raise ValueError("syntax error")
    else:
        total = equation[0]
        for i in range(1, len(equation), 2):
            total = operation(equation[i], total, equation[i + 1])
        return total
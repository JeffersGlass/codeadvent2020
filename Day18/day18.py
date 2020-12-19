import re
import logging

def isInt(num):
    try:
        _ = int(num)
    except ValueError:
        return False
    return True

def findInnerParens(equation):
    pattern = re.compile(r'\([^\(\)]*\)')
    return re.search(pattern, equation)

#Evaluate an equation string with no parentheses, a la part 1, where precedence is left to right
def evalLeftToRight(equation):
    pattern = re.compile(r'(\d+)\s*([+*]+)\s*(\d+)')
    s = re.search(pattern, equation)

    if s == None: #If there is no second number set to find, we're done evaluating
        return int(equation)

    first, op, second = s.group(1,2,3)
    if op == '+':
        result = int(first) + int(second)
    elif op == '*':
        result = int(first) * int(second)
    else:
        raise ValueError(f"Unknown operations {op}")
    
    return evalLeftToRight(str(result) + equation[s.span(0)[1]:])

#Evaluate an equation string with no parentheses a la part 2, where multiplication takes precedence over addition:
def evalWithPrecedence(equation):
    logging.debug(f"Evaluating-with-precedence the equation {equation}")
    multPattern = re.compile(r'(\d+)\s*[*]+\s*(\d+)')
    s = re.search(multPattern, equation)
    if s == None:
        logging.debug(f"No multiplications found in {equation}, moving on to addition")
        addPattern = re.compile(r'(\d+)\s*[\+]+\s*(\d+)')
        s = re.search(addPattern, equation)
        if s == None:
            logging.debug(f"No additions or multiplications found in {equation}")
            return int(equation.replace("(",'').replace(')',''))
        first, second = s.group(1, 2)
        result = int(first) + int(second)
        return evalWithPrecedence(equation[:s.span(0)[0]:] + str(result) + equation[s.span(0)[1]:])
    else:
        first, second = s.group(1,2)
        result = int(first) * int(second)
        return evalWithPrecedence(equation[:s.span(0)[0]:] + str(result) + equation[s.span(0)[1]:])

def doStep(equation, evalFunc):
    logging.debug(f"Running one step on equation {equation}")
    inner = findInnerParens(equation)
    if inner == None:
        logging.debug(f"Equation contains smaller parentheticals, evaluating left to right")
        return evalFunc(equation)
    else:
        innerExpression = inner.group(0)[1:-1]
        innerValue = evalFunc(innerExpression)
        logging.debug(f"Found smallest parenthetical to be {innerExpression}, which has value {innerValue}")
        
        innerSpan = inner.span()
        newEquation = equation[:innerSpan[0]] + str(innerValue) + equation[innerSpan[1]:]
        logging.debug(f"New equation to be evaluated is {newEquation}")
        return newEquation

def resolve(equation, evalFunc):
    while not isInt(equation):
        equation = doStep(equation, evalFunc)

    return equation
       

if __name__ == '__main__':
    logging.basicConfig(level = logging.DEBUG)

    with open('inputtest.txt', 'r') as infile:
        data = [line.strip() for line in infile]
        
    #print(f"Solution to part 1 is: {sum([resolve(line, evalLeftToRight) for line in data])}")

    line = data[0]
    print(line)
    print(resolve(line, evalWithPrecedence))
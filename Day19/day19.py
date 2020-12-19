import re
from itertools import product
import logging

def getNumsInRule(rule):
    return {int(r) for r in rule.split(" ") if r != "|"}

def canEvaluate(rule, knownRules):
    return getNumsInRule(rule).issubset(knownRules)

def generateNewCombinations(comboString):
    possibilities = [rules[int(r)] for r in comboString.strip(" ").split(" ")]
    logging.debug(f"Generating combinations of {possibilities}")
    results = {''.join([letter for letter in smallList]) for smallList in list(product(*possibilities))}
    logging.debug(f"Combinations are: {results}")
    
    return results

def evalRule(rule):
    logging.debug(f"Evaluating rule {r}:{rules[r]}")
    subsets = rules[r].split("|")
    combos = generateNewCombinations(subsets[0])

    for i in range(1, len(subsets)):
        combos = combos.union(generateNewCombinations(subsets[i]))

    logging.debug(f"Result was {combos}]")
    return(combos)

if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)

    with open('input.txt', 'r') as infile:
        #With each rule on a new line,
        #Create a dictionary with rulenumbers as keys and rules as values
        ruleList, messageList = ''.join([line for line in infile]).split("\n\n")
        rules = {int(line.split(':')[0]) : line.split(':')[1].strip(" \n\"") for line in ruleList.split("\n")}
        messageList = messageList.split('\n')

    logging.debug(f"Initial Rules: {[str(r) + ':' + str(rules[r]) for r in rules]}")

    #Initialize our list of rules that we know with the ones that are only letters
    pattern = re.compile(r'[a-z]+')
    knownRules = {num for num in rules if re.fullmatch(pattern, rules[num]) is not None}
    for k in knownRules:
        rules[k] = {rules[k]} #Turn our pre-determined rules into lists of length 1
    logging.debug(f"Known starting Rules: {knownRules}")

    while knownRules != set(range(len(rules))):
        for r in rules:
            if r not in knownRules and canEvaluate(rules[r], knownRules):
                rules[r] = evalRule(r)
                knownRules.add(r)
                #logging.info(f"Rule {r} is now: {rules[r]}")

    print(f"Solution to part 1: {len([mes for mes in messageList if mes in rules[0]])}")


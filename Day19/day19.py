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

    #Part 1:

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

    while len(knownRules) != len(rules):
        for r in rules:
            if r not in knownRules and canEvaluate(rules[r], knownRules):
                rules[r] = evalRule(r)
                knownRules.add(r)
                logging.info(f"Rule {r} solved; now know {len(knownRules)} rules of {len(rules)}")

    print(f"Solution to part 1: {len([mes for mes in messageList if mes in rules[0]])}")

    #Part 2:
    logging.getLogger().setLevel(logging.INFO)

    with open('inputPart2.txt', 'r') as infile:
        #With each rule on a new line,
        #Create a dictionary with rulenumbers as keys and rules as values
        ruleList, messageList = ''.join([line for line in infile]).split("\n\n")
        rules = {int(line.split(':')[0]) : line.split(':')[1].strip(" \n\"") for line in ruleList.split("\n")}
        messageList = messageList.split('\n')

    #Initialize our list of rules that we know with the ones that are only letters
    pattern = re.compile(r'[a-z]+')
    knownRules = {num for num in rules if re.fullmatch(pattern, rules[num]) is not None}
    for k in knownRules:
        rules[k] = {rules[k]} #Turn our pre-determined rules into lists of length 1
    logging.debug(f"Known starting Rules: {knownRules}")

    #Initialize a list of recursive rules, which contain themself:
    #TODO would be good to do this programmatially...
    recursiveRules = {8, 42}
    logging.debug(f"Recursive rules: {recursiveRules}")

    while len(knownRules) != len(rules) - len(recursiveRules) - 1:
        for r in rules:
            if r not in knownRules and canEvaluate(rules[r], knownRules):
                rules[r] = evalRule(r)
                knownRules.add(r)
                logging.info(f"Rule {r} solved; now know {len(knownRules)} rules of {len(rules)-len(recursiveRules)-1} non-recursive, nonzero rules")

    #Rule 0 is is "8 11", so any valid entry must start with a member of rule 42, all of which are of length 8, as are all members of rule 31
    #Snippets which obey rule 8 are either a member of rule 42, or multiple copies of that answer
    #Snippets which obey rule 11 start with a (x>=1) member of rule 42 and end with (x>=1) member of rule 31
    #So valid messages will be of the form:
    #   (1 or more members of rule 42)(X members of rule 42)(X members of rule 31)
    #Conveniently, all messages have lengths which are a multiple of 8!
    #Note: there is no overlap between the valid rules of rule 42 and rule 31

    def isValidPart2(message):
        chunkSize = 8
        bites = [message[i:i+chunkSize] for i in range(0, len(message), chunkSize)]
        valid42s = 0
        for n in range(len(bites)):
            if bites[n] in rules[42]: valid42s += 1
            else: break
        valid31s = 0
        for n in range(len(bites)-1, -1, -1):
            if bites[n] in rules[31]: valid31s += 1
            else: break
        logging.debug(f"{bites}, leading 42s:{valid42s}, trailing 31s:{valid31s}")
        if (valid42s + valid31s == len(bites)) and(valid42s > valid31s) and (valid42s >= 2) and valid31s > 0:
            logging.debug(f"{bites} is Valid")
            return True
        else:
            logging.debug(f"{bites} is Invalid")
            return False

    print(f"Solution to part 2:{len([mes for mes in messageList if isValidPart2(mes)])}")


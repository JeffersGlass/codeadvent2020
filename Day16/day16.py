#Part 1
import re
import logging

with open('input.txt', 'r') as infile:
    fields, myTicket, tickets = ''.join([line for line in infile if 'ticket' not in line]).split("\n\n")

pattern = re.compile(r'([0-9]+)-([0-9]+)')
spans = re.findall(pattern, fields)
ticketNums = ''.join([line for line in tickets]).replace('\n',',').split(',')

minimum = min([int(s[0]) for s in spans])
maximum = max([int(s[1]) for s in spans])

print(f"Solution to part 1 is: {sum([int(t) for t in ticketNums if int(t) < minimum or int(t) > maximum])}")

#Part 2

logging.getLogger().setLevel(logging.INFO)

ticketLists = [t.split(',') for t in tickets.split('\n')]
validTickets = [t for t in ticketLists if all([minimum <= int(n) <= maximum for n in t])]

fieldPairs = [(f.split(': ')[0], f.split(': ')[1]) for f in fields.split('\n')]
numFields = len(fieldPairs)
fieldRules = dict()
for fp in fieldPairs:
    span1 = re.findall(pattern, fp[1])[0]
    span2 = re.findall(pattern, fp[1])[1]
    set1 = set(range(int(span1[0]), int(span1[1])+1))
    set2 = set(range(int(span2[0]), int(span2[1])+1))
    set1.update(set2)
    #rules specifies the allowable value in each field; possible positions (pos pos) is the places this named field could be
    fieldRules[fp[0]] = {'rules': set1, 'pospos': set(range(numFields))}

#Eliminante the potential positions from each label, given each ticket's fields
for vt in validTickets:
    logging.debug(f"Examining ticket {vt}")
    for i, num in enumerate(vt):
        num = int(num)
        logging.debug(f"Examining the number {num} in position {i}")
        #For any rules that num can't be a part of, remove i from possible positions of that rule
        for fr in fieldRules:
            if num not in fieldRules[fr]['rules']:
                #logging.debug(f"{num} is not in rules for {fr}")
                fieldRules[fr]['pospos'].discard(i)

#Sort through the possible positions for each rule, and single out positions that can only be one
#possible position, until all rules have a definitive position
finalPositions = dict()

for _ in range(numFields):
    singlePossibility = [f for f in fieldRules if len(fieldRules[f]['pospos']) == 1][0]
    position = list(fieldRules[singlePossibility]['pospos'])[0]
    finalPositions[singlePossibility] = position
    for rule in fieldRules:
        fieldRules[rule]['pospos'].discard(position)

myTicket = myTicket.split(',')

product = 1

for field in finalPositions:
    if field[:9] == 'departure':
        logging.info(f"Field {field} matches description; value is {finalPositions[field]}")
        product *= int(myTicket[finalPositions[field]])

print(f"Solution to part 2 is: {product}")
#Part 1
import re

with open('input.txt', 'r') as infile:
    fields, _, tickets = ''.join([line for line in infile if 'ticket' not in line]).split("\n\n")

pattern = re.compile(r'([0-9]+)-([0-9]+)')
spans = re.findall(pattern, fields)
tickets = ''.join([line for line in tickets]).replace('\n',',').split(',')

minimum = min([int(s[0]) for s in spans])
maximum = max([int(s[1]) for s in spans])

print(sum([int(t) for t in tickets if int(t) < minimum or int(t) > maximum]))
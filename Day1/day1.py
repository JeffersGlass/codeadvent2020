file = 'input.txt'

data = list()

with open('input.txt', 'r') as infile:
    for line in infile:
        data.append(line.strip('\n').strip('\r'))

print(data)
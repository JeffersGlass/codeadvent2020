def isValid(low, high, letter, password):
    return low <= password.count(letter) <= high

def isValidLine(line):
    contents = line.split(' ')
    lowbound, highbound = [int(x) for x in contents[0].split('-')]
    letter = contents[1].strip(":")
    password = contents[2].strip("\n")
    return isValid(lowbound, highbound, letter, password)


with open('input.txt', 'r') as infile:
    data = [line for line in infile]

print (len([line for line in data if isValidLine(line)]))
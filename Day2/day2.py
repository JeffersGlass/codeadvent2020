def isValid_Sled(low, high, letter, password):
    return low <= password.count(letter) <= high

#The 'first', 'second' inputs are given as 1-indexed values per the problem statement
def isValid_Toboggan(first, second, letter, password):
    return (password[first-1] == letter) ^ (password[second-1] == letter)

def isValidLine(line, func):
    contents = line.split(' ')
    lowbound, highbound = [int(x) for x in contents[0].split('-')]
    letter = contents[1].strip(":")
    password = contents[2].strip("\n")
    return func(lowbound, highbound, letter, password)

with open('input.txt', 'r') as infile:
    data = [line for line in infile]

print ("The solution to part 1 is: " + str(len([line for line in data if isValidLine(line, isValid_Sled)])))
print ("The solution to part 2 is: " + str(len([line for line in data if isValidLine(line, isValid_Toboggan)])))
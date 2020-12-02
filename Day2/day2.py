def isValid_Sled(low, high, letter, password):
    return low <= password.count(letter) <= high

def isValidLine(line, func):
    contents = line.split(' ')
    lowbound, highbound = [int(x) for x in contents[0].split('-')]
    letter = contents[1].strip(":")
    password = contents[2].strip("\n")
    return func(lowbound, highbound, letter, password)

#While the problem statements/input give input with '1-indexed' values, this function takes '0-indexed' values
def isValid_Toboggan(first, second, letter, password):
    return (password[first] == letter) ^ (password[second] == letter)


with open('input.txt', 'r') as infile:
    data = [line for line in infile]

print ("The solution to part 1 is: " + str(len([line for line in data if isValidLine(line, isValid_Sled)])))
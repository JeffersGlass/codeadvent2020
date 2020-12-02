def isValid(low, high, letter, password):
    return low <= password.count(letter) <= high

with open('input.txt', 'r') as infile:
    data = [line for line in infile]

sum = 0
contents = data[4].split(' ')
print(contents)
lowbound, highbound = [int(x) for x in contents[0].split('-')]
print (f"{lowbound} {highbound}")
letter = contents[1].strip(":")
print(letter)
password = contents[2].strip("\n")
print(password)
print (isValid(lowbound, highbound, letter, password))
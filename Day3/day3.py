with open('input.txt', 'r') as infile:
    data = [line.strip('\n') for line in infile]

#Solution in one line:
print (len([line for line in enumerate(data) if line[1][(line[0]*3) % len(line[1])] == '#']))

#More verbose solution with the same method:
e = enumerate(data)

total = 0
lineLength = len(data[0])

for line in e:
    charpos = (line[0]*3) % lineLength
    if (line[1][charpos] == '#'): total += 1

print(f"The answer to part 1 is: {total}")
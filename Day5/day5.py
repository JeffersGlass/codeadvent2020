#Day 5 Part 1:
with open('input.txt', 'r') as infile:
    data = ['0b' + line.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1').strip() for line in infile]

#Cast all all data as integers to confirm parsing was correct
data = [int(d, 2) for d in data]
print(f"Solution to part 1 is {max(data)}")

#Day5 Part 2:

print(f"Solution to part 2 is {[mine for mine in range(min(data), max(data)+1) if mine not in data]}")


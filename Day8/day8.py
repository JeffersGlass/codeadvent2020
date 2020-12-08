data = list()

with open('input.txt', 'r') as infile:
    for line in infile:
        inst, val = line.split(' ')[0], int(line.split(' ')[1])
        data.append((inst, val))
    

accumulator = 0
head = 0
seenInstructions = set()

while head not in seenInstructions:
    seenInstructions.add(head)
    print(f"Processing instruction @ {head}: {data[head][0]},{data[head][1]}")
    if data[head][0] == 'nop':
        head += 1
    elif data[head][0] == 'acc':
        accumulator += data[head][1]
        head += 1
    elif data[head][0] == 'jmp':
        head += data[head][1]


print(accumulator)


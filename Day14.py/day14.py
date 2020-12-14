import re

def applyMask(mask, num):
    onesMask =      int(''.join([('1' if m == '1' else '0')for m in mask ]), 2)
    zeroesMask =    int(''.join([('0' if m == '0' else '1')for m in mask ]), 2)
    num = num | onesMask
    num = num & zeroesMask
    return num

if __name__ == '__main__':

    with open('input.txt', 'r') as infile:
        data = [line.strip() for line in infile]

    #part1
    mask = '0'
    memory = dict()

    for line in data:
        if 'mask' in line:
            mask = line.split(' = ')[1]
        else:
            pattern = r'\[([0-9]+)\] = ([0-9]+)'
            m = re.search(pattern, line)
            address = int(m.group(1))
            value = int(m.group(2))
            memory[address] = applyMask(mask, value)

    print(f"Solution to part 1 is: {sum(memory.values())}")

    
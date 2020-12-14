with open('inputtest.txt', 'r') as infile:
    data = [line.strip() for line in infile]

def applyMask(mask, num):
    onesMask =      int(''.join([('1' if m == '1' else '0')for m in mask ]), 2)
    zeroesMask =    int(''.join([('0' if m == '0' else '1')for m in mask ]), 2)
    num = num | onesMask
    num = num & zeroesMask
    return num

    
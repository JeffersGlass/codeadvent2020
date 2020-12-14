import re
import logging


def applyMask(mask, num):
    onesMask =      int(''.join([('1' if m == '1' else '0')for m in mask ]), 2)
    zeroesMask =    int(''.join([('0' if m == '0' else '1')for m in mask ]), 2)
    num = num | onesMask
    num = num & zeroesMask
    return num

def getMaskedAddresses(mask, address):
    logging.debug(f"Original address is {address}")
    #A '1' in the mask sets that bit of the address to 1
    onesMask =      int(''.join([('1' if m == '1' else '0')for m in mask ]), 2)
    address |= onesMask

    logging.debug(f"Address with ones masked is:\n{str(bin(address)[2:]).zfill(36)} ({address})")

    addressList = list()

    #An 'X' in the mask leaves that bit floating
    positions = list(re.finditer(r'X', mask))                     #Positions of all the X's in the mask
    xCount = len(positions)                                       #How many X's are there?
    perms = [bin(x)[2:].zfill(xCount) for x in range(2**xCount)]  #2^x permutations of 0, 1
    for perm in perms:                                            #For each permutation of 1's and zeros:
        logging.debug(f"Working on permutation {perm}")
        newAddress = str(bin(address)[2:]).zfill(36)              #Copy original address
        for pos in range(len(positions)):                         #For each position:  
            xPos = positions[pos].start()                         #Get the location of the 'X' we're working on
            newAddress = newAddress[0:xPos] + perm[pos] + newAddress[xPos+1:] #Replace it with 1 or 0, from the permutation
        logging.debug(f"Result is {newAddress} ({int(newAddress, 2)})")
        addressList.append(int(newAddress, 2))                    #add this address to the list

    return addressList

if __name__ == '__main__':

    with open('input.txt', 'r') as infile:
        data = [line.strip() for line in infile]

    #Part1
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

    #Part 2

    #Can we use a naive approach of just adding all all possible memory locations to a dict?
    locations = 0
    with open('input.txt', 'r') as infile:
        for line in infile:
            if 'mask' in line:
                locations += 2**line.count('X')
    
    print(f"Final memory locations for part 2: {locations}") #16912 - sure

    mask = '0'
    memory = dict()
    logging.basicConfig(level=logging.INFO)

    with open('input.txt', 'r') as infile:
        data = [line.strip() for line in infile]

    for line in data:
        if 'mask' in line:
            mask = line.split(' = ')[1]
            logging.debug(f"Mask is now {mask}")
        else:
            pattern = r'\[([0-9]+)\] = ([0-9]+)'
            m = re.search(pattern, line)
            givenAddress = int(m.group(1))
            value = int(m.group(2))
            addresses = getMaskedAddresses(mask, givenAddress)
            for a in addresses:
                memory[a] = value
    
    print(f"Solution to part 2 is: {sum(memory.values())}")


    
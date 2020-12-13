#Part 1:
with open('input.txt', 'r') as infile:
    target = int(infile.readline())
    busses = [int(num) for num in infile.readline().split(',') if 'x' not in num]

def nextTime(target, bus):
    runningTotal = bus
    while runningTotal <= target:
        runningTotal += bus
    return (runningTotal - target)

nextTimes =[nextTime(target, b) for b in busses]
minTime = min(nextTimes)
print(f"Solution to part 1: {minTime * busses[nextTimes.index(minTime)]}")

#Part 2:
from math import prod, lcm

with open('input.txt', 'r') as infile:
    _ = infile.readline()
    busses = [e for e in enumerate(infile.readline().split(',')) if 'x' not in e[1]]

busses = [{'pos':b[0], 'value':int(b[1])} for b in busses]
busses = sorted(busses, key=lambda x: x['pos'])

#For a given prime A, a second prime P, and a residue R,
#Find the num N such that 0 <= N < P and (N*A)+R === 0 (mod P)

def findLeastSuccess(given, prime, residue):
    for i in range(prime):
        if ((i*given)+residue) % prime == 0:
            return i*given

    return -1

number = findLeastSuccess(busses[0]['value'], busses[1]['value'], busses[1]['pos'])
addend = lcm(busses[0]['value'],busses[1]['value'])

for b in busses[2:]:
    #print(f"Adding {b['value']} at position {b['pos']} to the mix makes our value ", end ="")
    while (number+b['pos']) % b['value'] != 0:
        number += addend
    addend = lcm(addend, b['value'])
    #print(f"{number} and our addend {addend}")

print(f"Solution to part 2: {number}")

















'''    

#Given the arithmetic sequences Ax + b and Cy + D,
#Find the smallest number the two sequences have in common
def findCommonInSequence(A, B, C, D):
    for i in range(C):
        if ((C*i + D - B)/A).is_integer():
            return C*i + D

    return -1

#print(findCommonInSequence(busses[1]['value'], findLeastSuccess(busses[0]['value'],busses[1]['value'], busses[1]['pos']), busses[2]['value'], findLeastSuccess(busses[0]['value'],busses[2]['value'],busses[2]['pos'])))

def findSolution3(given):
    common = findCommonInSequence(given[1]['value'], findLeastSuccess(given[0]['value'],given[1]['value'], given[1]['pos']), given[2]['value'], findLeastSuccess(given[0]['value'],given[2]['value'],given[2]['pos']))
    return common * given[0]['value']

#print(findSolution3(busses))
#print (findCommonInSequence(5,1,7,0))

'''
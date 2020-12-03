import itertools
from math import prod

with open('testinput.txt', 'r') as infile:
    data = [line.strip('\n') for line in infile]

#Solution in one line:
print ("The answer to part 1 is: " + str(len([line for line in enumerate(data) if line[1][(line[0]*3) % len(line[1])] == '#'])))

#More verbose solution with the same method:
e = enumerate(data)

total = 0
lineLength = len(data[0])

for line in e:
    charpos = (line[0]*3) % lineLength
    if (line[1][charpos] == '#'): total += 1

print(f"The answer to part 1 is: {total}")



#Solution to part 2 in few lines using list comprehensions:

def getSlopeTrees(slope, over, down):
    return len([line for line in enumerate(slope) if (line[0] % down == 0) and ((line[0]*over)/down).is_integer() and (line[1][int((line[0]*over)/down) % len(line[1])] == '#')])

testSteps = [(1,1),(3,1),(5,1),(7,1),(1,2)]
print (f"The answer to part 2 is : {prod([getSlopeTrees(data, *t) for t in testSteps])}")



#A functions that was useful in troubleshooting some list indexing issues:
'''
def getSlopeTreesVerbose(slope, over, down):
    total = 0
    for line in enumerate(slope):

        print(line, end = "\t")

        readThisLine = (line[0] % down == 0)
        print(f"Line[0] mod Down is 0: {readThisLine}", end = "\t")

        treePosition = ((line[0]*over)/down) % len(line[1])
        print(f"Looking at position: {treePosition}", end = "\t")
        
        if treePosition.is_integer(): 
            treePosition = int(treePosition)

            lineHasTree = (line[1][treePosition] == '#')
            print(f"Is tree? {lineHasTree}")
            
            if readThisLine and lineHasTree: total = total + 1
        else:
            print("")
    return total
'''

#Print the intermediate results of testing our various setups:
'''
for t in testSteps:
    print (f"For test Right {t[0]}, down {t[1]}, we hit {getSlopeTrees(data, *t)} trees")
'''

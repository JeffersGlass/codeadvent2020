import sys
sys.path.append("..")
from usefulDecorators import *

#Creates a dictionary where keys are colors of bag (string) and the values are a set of the 
#colors of bag which directly contain the key color
def createBagList():
    bagList = dict()

    with open('input.txt', 'r') as infile:
        for line in infile:
        #Split input line container colored and contained colors
            container, contains = line.split(' bags contain ')
            #This line is a hack that assumes all numbers are single digit, which they appear to be??
            contains = [c.strip('\n. ').replace(' bags', '').replace(' bag', '')[2:] for c in contains.split(',') if 'no other bags' not in c]
            #print(f"{container}\t\t{contains}")
            for color in contains:
                if color not in bagList:
                    bagList[color] = {container}
                else:
                    bagList[color].add(container)

    return bagList        


#@sayFunction
def findParentColors(color, bagList):
    if color not in bagList:
        return set()
    else:
        retVal = bagList[color]
        return retVal.union(*[findParentColors(c, bagList) for c in bagList[color]])

def createContainedList():
    baseList = dict()

    with open('input.txt', 'r') as infile:
        for line in infile:
            container, contains = line.split(' bags contain ')
            #This line is a hack that assumes all numbers are single digit, which they appear to be??
            contains = [c.strip('\n. ').replace(' bags', '').replace(' bag', '') for c in contains.split(',') if 'no other bags' not in c]
            contains = [(int(c[0]), c[2:]) for c in contains]
            baseList[container] = contains
    return baseList

def findTotalBags(color, bagList):
    if color not in bagList:
        raise ValueError(f"{color} is not in the list of keys of baglist")
    else:
        if len(bagList[color]) == 0: return 1
        else: return sum([c[0] * findTotalBags(c[1], bagList) for c in bagList[color]]) + 1


if __name__ == '__main__':    
    #Solution to part 1
    print(f"Solution to part 1: {len(findParentColors('shiny gold', createBagList()))}")
    
    #Solution to part 2
    print(f"Solution to part 2: {findTotalBags('shiny gold', createContainedList())-1}")


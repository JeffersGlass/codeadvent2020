import sys
sys.path.append("..")
from usefulDecorators import *

#A dictionary where keys are colors of bag (string) and the values are a set of the 
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



if __name__ == '__main__':

    #Solution to part 1
    f = findParentColors('shiny gold', createBagList())
    print(f"Solution to part 1: {len(f)} \n")


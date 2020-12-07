import sys
sys.path.append("..")
from usefulDecorators import *

#A dictionary where keys are colors of bag (string) and the values are a set of the 
#colors of bag which directly contain the key color

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

    examined = set()
    toExamine = set(bagList[firstBag])
    found = set()
    topLevel = 0

    while(True):

        #print(f"Start of loop: {examined}\t{toExamine}\t{found}")
        print("Seen {:<3} colors, will check {:<3} colors this loop".format(len(examined), len(toExamine)))

        for e in toExamine:
            #print(f"Examining containers of {e}")
            if e not in bagList: 
                #print(f"Found color {container} which has no containers, assuming it is top-level")
                examined.add(container)
                continue
            for container in bagList[e]:                    
                if (container not in toExamine and container not in examined):
                    found.add(container)
                    #print(f"Color {e} has new container {container}, adding to 'found'")
        
        #print("Found {:<3} new colors this loop".format(len(found)))
        examined = examined.union(toExamine)

        #print(f"Just before check: {examined}\t{toExamine}\t{found}")
        #input("Hit enter to continue")
        if len(found) == 0: return examined

        toExamine = found.copy()
        found = set()


@sayFunction
def findParentColors(color):
    if color not in bagList:
        return set()
    else:
        retVal = bagList[color]
        return retVal.union(*[findParentColors(c) for c in bagList[color]])
    


if __name__ == '__main__':

    f = findParentColors('shiny gold')
    print(f)
    print(f"Solution to part 1: {len(f)} \n")


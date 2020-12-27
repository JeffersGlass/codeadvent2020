from operator import add
from itertools import permutations
import logging
from functools import cache
import sys
sys.path.append("..")
from function_timing import *

def doStep(state):
    nextState = set()
    #determine radius/of tiles to check
    radius = maxRadius(state)
    logging.debug(f"Max radius for this step is {radius}")
    for h in hexesInRadius(radius+1):
        blackNeighbors = len([n for n in getNeighbors(h) if n in state])
        if h in state: #   if it's black, apply black rules to see if it stays black
            logging.debug(f"Hex {h} is black and has {blackNeighbors} black neighbors")
            if 1 <= blackNeighbors <= 2: nextState.add(h) 
        else:
            logging.debug(f"Hex {h} is white and has {blackNeighbors} black neighbors")
            if blackNeighbors == 2: nextState.add(h)       #   if it's white, apply white ruls to see it it turns black
        logging.debug(f"Next State is now: {nextState}")
    return nextState

def maxRadius(state):
    return max(max([abs(s[0]) for s in state]), max([abs(s[1]) for s in state]), max([abs(s[2]) for s in state]))

@cache
def hexesInRadius(radius):
    hexes = set()
    for x in range(-radius, radius+1):
        for y in range(max(-radius, -x-radius), min(radius, -x+radius)+1):
            z = -x-y
            hexes.add((x,y,z))
    return hexes

@cache
def getNeighbors(position):
    return [tuple(map(add, position, p)) for p in permutations([0,-1,1])]

@timer
def runNumDays(state, numDays):
    for d in range(1,100+1):
        state = doStep(state)
        print(f"After {d} days, there are {len(state)} black tiles")


if __name__ == '__main__':

    #Part 1
    #region
    with open('input.txt', 'r') as infile:
        instructions = [line.strip() for line in infile]

    blackTiles = set()

    dirs = {
        'e':    (1,-1,0),
        'ne':   (1,0,-1),
        'nw':   (0,1,-1),
        'w':    (-1,1,0),
        'sw':   (-1,0,1),
        'se':   (0,-1,1)
    }

    for inst in instructions:
        pos = [0,0,0]
        while len(inst) > 0:
            if inst[0] in ['e','w']:
                direction = dirs[inst[0]]
                inst = inst[1:]
            else:
                direction = dirs[inst[0:2]]
                inst = inst[2:]
            pos = list(map(add, pos, direction))

        pos = tuple(pos)

        if pos not in blackTiles: blackTiles.add(pos)
        else: blackTiles.remove(pos)

    print(f"Solution to part 1: {len(blackTiles)}")
    #endregion
        
    #Part 2
    logging.basicConfig(level=logging.INFO)
    logging.debug(f"Black tiles at beginning: {blackTiles}")
    runNumDays(blackTiles, 100)
        
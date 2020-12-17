import logging
cells = set()

with open('input.txt', 'r') as infile:
    for rowNum, line in enumerate(infile):
        for colNum, state in enumerate(line):
            if state == '#': cells.add((rowNum, colNum, 0))

def getExtents(cellSet):
    xExtents = (min([c[0] for c in cellSet]), max([c[0] for c in cellSet]))
    yExtents = (min([c[1] for c in cellSet]), max([c[1] for c in cellSet]))
    zExtents = (min([c[2] for c in cellSet]), max([c[2] for c in cellSet]))
    return (xExtents, yExtents, zExtents)

def getLiveNeighbors(cellSet, position):
    sum = 0
    for x in [-1,0,1]:
        for y in [-1,0,1]:
            for z in [-1, 0, 1]:
                logging.debug(f'Examining position {position[0]+x},{position[1]+y},{position[2]+z}')
                if (not (x==0 and y==0 and z==0)) and ((position[0]+x,position[1]+y,position[2]+z) in cellSet): 
                    sum += 1
                    logging.debug(f'Live neighbor found')
    return sum

def doStep(cellSet):
    newState = set()
    extents = getExtents(cellSet)
    
    for x in range(extents[0][0]-1, extents[0][1]+2):
        for y in range(extents[1][0]-1, extents[1][1]+2):
            for z in range(extents[2][0]-1, extents[2][1]+2):
                n = getLiveNeighbors(cellSet, (x,y,z))
                if ((x,y,z) in cellSet): #Cell is currently live
                    if (2 <= n <= 3): newState.add((x,y,z))
                else: #Cell is currently dead
                    if (n == 3): newState.add((x,y,z))

    return newState


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)

    print(cells)
    for i in range(6):
        print(f"Starting step {i+1}")
        cells = doStep(cells)

    print(len(cells))
import logging

def getExtents3D(cellSet):
    xExtents = (min([c[0] for c in cellSet]), max([c[0] for c in cellSet]))
    yExtents = (min([c[1] for c in cellSet]), max([c[1] for c in cellSet]))
    zExtents = (min([c[2] for c in cellSet]), max([c[2] for c in cellSet]))
    return (xExtents, yExtents, zExtents)

def getExtents4D(cellSet):
    xExtents = (min([c[0] for c in cellSet]), max([c[0] for c in cellSet]))
    yExtents = (min([c[1] for c in cellSet]), max([c[1] for c in cellSet]))
    zExtents = (min([c[2] for c in cellSet]), max([c[2] for c in cellSet]))
    wExtents = (min([c[3] for c in cellSet]), max([c[3] for c in cellSet]))
    return (xExtents, yExtents, zExtents, wExtents)

def getLiveNeighbors3D(cellSet, position):
    sum = 0
    for x in [-1,0,1]:
        for y in [-1,0,1]:
            for z in [-1, 0, 1]:
                logging.debug(f'Examining position {position[0]+x},{position[1]+y},{position[2]+z}')
                if (not (x==0 and y==0 and z==0)) and ((position[0]+x,position[1]+y,position[2]+z) in cellSet): 
                    sum += 1
                    logging.debug(f'Live neighbor found')
    return sum

def getLiveNeighbors4D(cellSet, position):
    sum = 0
    for x in [-1,0,1]:
        for y in [-1,0,1]:
            for z in [-1, 0, 1]:
                for w in [-1,0,1]:
                    logging.debug(f'Examining position {position[0]+x},{position[1]+y},{position[2]+z}')
                    if (not (x==0 and y==0 and z==0 and w==0)) and ((position[0]+x,position[1]+y,position[2]+z, position[3]+w) in cellSet): 
                        sum += 1
                        logging.debug(f'Live neighbor found')
    return sum

def doStep3D(cellSet):
    newState = set()
    extents = getExtents3D(cellSet)
    
    for x in range(extents[0][0]-1, extents[0][1]+2):
        for y in range(extents[1][0]-1, extents[1][1]+2):
            for z in range(extents[2][0]-1, extents[2][1]+2):
                n = getLiveNeighbors3D(cellSet, (x,y,z))
                if ((x,y,z) in cellSet): #Cell is currently live
                    if (2 <= n <= 3): newState.add((x,y,z))
                else: #Cell is currently dead
                    if (n == 3): newState.add((x,y,z))

    return newState

def doStep4D(cellSet):
    newState = set()
    extents = getExtents4D(cellSet)
    
    for x in range(extents[0][0]-1, extents[0][1]+2):
        for y in range(extents[1][0]-1, extents[1][1]+2):
            for z in range(extents[2][0]-1, extents[2][1]+2):
                for w in range(extents[3][0]-1, extents[3][1]+2):
                    n = getLiveNeighbors4D(cellSet, (x,y,z,w))
                    if ((x,y,z,w) in cellSet): #Cell is currently live
                        if (2 <= n <= 3): newState.add((x,y,z,w))
                    else: #Cell is currently dead
                        if (n == 3): newState.add((x,y,z,w))

    return newState


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)

    #Part 1:
    cells = set()

    with open('input.txt', 'r') as infile:
        for rowNum, line in enumerate(infile):
            for colNum, state in enumerate(line):
                if state == '#': cells.add((rowNum, colNum, 0))

    
    for i in range(6):
        logging.info(f"Starting step {i+1}")
        cells = doStep3D(cells)

    print(f"Solution to part 1 is: {len(cells)}")

    #Part 2:
    cells = set()

    with open('input.txt', 'r') as infile:
        for rowNum, line in enumerate(infile):
            for colNum, state in enumerate(line):
                if state == '#': cells.add((rowNum, colNum, 0, 0))

    for i in range(6):
        logging.info(f"Starting step {i+1}")
        cells = doStep4D(cells)

    print(f"Solution to part 2 is: {len(cells)}")
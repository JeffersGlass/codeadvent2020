from copy import deepcopy

def printSeatingLayout(layout):
    for row in range(layout['numRows']):
        for column in range(layout['numCols']):
            print(layout[(row, column)], end = "")
        print("")

def iterate(layout, neighborfunc, tolerance):
    newLayout = dict()
    newLayout['numRows'], newLayout['numCols'] = layout['numRows'], layout['numCols']
    for row in range(layout['numRows']):
        for column in range(layout['numCols']):
            currentSeat = layout[(row, column)]
            if currentSeat == '.':
                newLayout[(row, column)] = '.'
            else:
                neighbors = neighborfunc(layout, row, column)
                if currentSeat == 'L':
                    if neighbors == 0: newLayout[(row, column)] = '#'
                    else: newLayout[(row, column)] = 'L'
                elif currentSeat == '#':
                    if neighbors >= tolerance: newLayout[(row, column)] = 'L'
                    else: newLayout[(row, column)] = '#'
    
    return newLayout

def iterateUntilStable(layout, neighborfunc, tolerance):
    oldLayout = deepcopy(layout)
    seats = iterate(layout, neighborfunc, tolerance)

    while(oldLayout != seats):
        oldLayout = deepcopy(seats)
        seats = iterate(seats, neighborfunc, tolerance)
    return seats

def getImmediateNeighbors(layout, row, column):
    neighbors = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not(i == 0 and j == 0):
                neighbors += (1 if layout.get((row+i, column+j), '.') == '#' else 0)
    return neighbors

def getVisibleNeighbors(layout, row, column):
    neighbors = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i==0 and j==0):
                pos = (row+i, column+j)
                while layout.get(pos, 'L') == '.':
                    pos = (pos[0]+i, pos[1]+j)
                if layout.get(pos) == '#':
                    neighbors += 1
    return neighbors

def seatsFilled(layout):
    return sum([(1 if layout[row, column] == '#' else 0) for row in range(layout['numRows']) for column in range(layout['numCols'])])

if __name__ == '__main__':
    inputSeats = dict()

    row = 0
    column = 0

    with open('input.txt', 'r') as infile:
        for line in infile:
            column = 0
            for seat in line:
                inputSeats[(row, column)] = line[column]
                column +=1
            row += 1

        inputSeats['numRows'] = row
        inputSeats['numCols'] = column
    
    #Part 1:
    seats = deepcopy(inputSeats)
    print(f"Solution to part 1 is: {seatsFilled(iterateUntilStable(seats, getImmediateNeighbors, 4))}")
    

    #Part 2
    seats = deepcopy(inputSeats)
    print(f"Solution to part 2 is: {seatsFilled(iterateUntilStable(seats, getVisibleNeighbors, 5))}")
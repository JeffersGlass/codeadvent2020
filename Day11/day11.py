from copy import deepcopy

seats = dict()

row = 0
column = 0

with open('input.txt', 'r') as infile:
    for line in infile:
        column = 0
        for seat in line:
            seats[(row, column)] = line[column]
            column +=1
        row += 1

    seats['numRows'] = row
    seats['numCols'] = column

def printSeatingLayout(layout):
    for row in range(layout['numRows']):
        for column in range(layout['numCols']):
            print(layout[(row, column)], end = "")
        print("")

def iterate(layout):
    newLayout = dict()
    newLayout['numRows'], newLayout['numCols'] = layout['numRows'], layout['numCols']
    for row in range(layout['numRows']):
        for column in range(layout['numCols']):
            currentSeat = layout[(row, column)]
            if currentSeat == '.':
                newLayout[(row, column)] = '.'
            else:
                neighbors = getImmediateNeighbors(layout, row, column)
                if currentSeat == 'L':
                    if neighbors == 0: newLayout[(row, column)] = '#'
                    else: newLayout[(row, column)] = 'L'
                elif currentSeat == '#':
                    if neighbors >= 4+1: newLayout[(row, column)] = 'L'
                    else: newLayout[(row, column)] = '#'
    
    return newLayout

def getImmediateNeighbors(layout, row, column):
    neighbors = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            neighbors += (1 if layout.get((row+i, column+j), '.') == '#' else 0)
    return neighbors


def seatsFilled(layout):
    return sum([(1 if layout[row, column] == '#' else 0) for row in range(layout['numRows']) for column in range(layout['numCols'])])


if __name__ == '__main__':
    oldLayout = deepcopy(seats)
    seats = iterate(seats)
    while(oldLayout != seats):
        oldLayout = deepcopy(seats)
        seats = iterate(seats)
    print(f"Solution to part 1 is: {seatsFilled(seats)}")
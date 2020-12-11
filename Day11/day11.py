seats = dict()

row = 0
column = 0

with open('inputtest.txt', 'r') as infile:
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
    
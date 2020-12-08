from sys import exit

inputData = list()

with open('input.txt', 'r') as infile:
    for line in infile:
        inst, val = line.split(' ')[0], int(line.split(' ')[1])
        inputData.append([inst, val])

#Returns a tuple of (Did the loop terminate?, accumulator value at exit)    
def accumulatorValueBeforeLoop(data):

    workingData = [[d[0], d[1]] for d in data]
    accumulator = 0
    head = 0
    seenInstructions = set()

    
    while head not in seenInstructions:
        seenInstructions.add(head)

        #Added to detect the instruction-past-end-of-data requirement for Part 2
        if head == len(workingData):
            return accumulator, True
        
        
        #print(f"Processing instruction @ {head}: {workingData[head][0]},{workingData[head][1]}")
        if workingData[head][0] == 'nop':
            head += 1
        elif workingData[head][0] == 'acc':
            accumulator += data[head][1]
            head += 1
        elif workingData[head][0] == 'jmp':
            head += data[head][1]

    return accumulator, False

#Swaps the given position (pos) nop to jmp or jmp to nop as applicable;
#Returns (accumulator value, True if program terminated by running off the end, false if it loops)
def solveWithSwaps(baseData, pos):
    if baseData[pos][0] in ('jmp', 'nop'):
        testData = [[d[0], d[1]] for d in baseData] #Breaks the input list appart to pass by value instead of by reference
        

        if testData[pos][0] == 'jmp':
            testData[pos][0] = 'nop'
        elif testData[pos][0] == 'nop':
            testData[pos][0] = 'jmp'
        else:
            raise ValueError(f"Unknown instruction {testData[pos][0]}")

        #print(f"Running test with position {pos} changed to {testData[pos][0]} ", end = "")

        result = accumulatorValueBeforeLoop(testData)
        return result
    else:
        return (0, False)

if __name__ == '__main__':
    print(f"Solution to part 1 is: {accumulatorValueBeforeLoop(inputData)[0]}")
    for i in range(len(inputData)):
        result = solveWithSwaps(inputData, i)
        if result[1] == True: print(f"Solution to part 2 is: {result[0]}")
import logging
from sys import exit

def doStep(dataList):
    lastNum = dataList[-1]
    if lastNum not in dataList[:-1]:
        logging.debug(f"{lastNum} is new, adding a 0 to end of list")
        dataList.append(0)
    else:
        lastSpot = max([i for i, num in enumerate(dataList[:-1]) if num == lastNum])
        newNum = len(dataList) - lastSpot - 1
        logging.debug(f"We have seen {lastNum} before at position {lastSpot}; curent position is {len(data)}; adding {newNum} to list")
        dataList.append(newNum)
    return dataList

def doStepDict(dataDict):
    lastNum = dataDict['lastNum']
    if lastNum not in dataDict: #First time we've seen this number:
        logging.debug(f"{lastNum} is new, adding a 0 to end of list")
        dataDict[lastNum] = dataDict['lastPos']
        dataDict['lastNum'] = 0    
    else:
        #Last time we've seen the new number was at index lastSpot:
        lastSpot = dataDict[lastNum] 

        #The new last number in the list should be the different between the "end" of the list and the last time we saw that number
        dataDict['lastNum'] = dataDict['lastPos'] - lastSpot

        #The most recent time we saw that number is the current position
        dataDict[lastNum] = dataDict['lastPos']
        logging.debug(f"We have seen {lastNum} before at position {lastSpot}; curent position is {dataDict['lastPos']}; adding {dataDict['lastNum']} to list")

    dataDict['lastPos'] = dataDict['lastPos'] + 1
    return(dataDict)

    

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    #Part 1:

    with open('input.txt', 'r') as infile:
        data = [int(d) for d in infile.readline().split(',')]

    while(len(data) != 2020):
        doStep(data)

    print(data[-1])

    #Part 2:
    logging.getLogger().setLevel(logging.INFO)

    with open('input.txt', 'r') as infile:
        line = infile.readline().split(',')
        data = {int(num): i for i, num in enumerate(line[:-1])}
        data['lastNum'] = int(line[-1])
        data['lastPos'] = len(line) - 1

    print(data)

    #while(data['lastPos'] < 2020 -1):
    #    print(doStepDict(data)['lastNum'])

    while data['lastPos'] < 30_000_000 - 1:
        doStepDict(data)
    print(f"{data['lastNum']}")

    

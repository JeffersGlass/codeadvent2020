def getFirstNonSum(lookback, data):
    for i in range(lookback, len(data)):
        if not any(
            [((data[i] - summand in data[i-lookback:i]) and \
            (summand != data[i]/2))
            for summand in data[i-lookback:i]] \
        ): return data[i]

def findListSumTo(target, data):
    startNum = 0
    length = 1

    while(True):
        value = sum(data[startNum:startNum+length])
        if value == target:
            return data[startNum:startNum+length]
        elif value > target:
            startNum += 1
            length = 1
        else:
            length += 1        


if __name__ == '__main__':

    with open('input.txt', 'r') as infile:
        data = [int(line) for line in infile]

    invalidNum = getFirstNonSum(25, data)
    print(f"Solution to part 1 is: {invalidNum}")

    sumList = findListSumTo(invalidNum, data)
    print(f"Solution to part 2 is:  {max(sumList) + min(sumList)}")
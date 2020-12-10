from functools import lru_cache

with open('input.txt', 'r') as infile:
    data = [int(line) for line in infile]
    data += [0] + [max(data)+3]

@lru_cache
def findPathsTo(num):
    if num == 0:
        return 1
    else:
        runningTotal = 0
        if num-1 in data: runningTotal += findPathsTo(num-1)
        if num-2 in data: runningTotal += findPathsTo(num-2)
        if num-3 in data: runningTotal += findPathsTo(num-3)
        return runningTotal


if __name__ == '__main__':

    oneGaps = [d for d in data if d+1 in data]
    threeGaps = [d for d in data if (d+1 not in data and d+2 not in data and d+3 in data)]
    print(f"Solution to part 1 is: {len(oneGaps) * len(threeGaps)}")

    myCharger = max(data)
    print(f"Paths to {myCharger}: {findPathsTo(myCharger)}")

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
        for i in [1,2,3]:
            if num-i in data: runningTotal += findPathsTo(num-i)
        return runningTotal


if __name__ == '__main__':

    oneGaps = [d for d in data if d+1 in data]
    threeGaps = [d for d in data if (d+1 not in data and d+2 not in data and d+3 in data)]
    print(f"Solution to part 1 is: {len(oneGaps) * len(threeGaps)}")

    print(f"Solution to part 2 is:: {findPathsTo(max(data))}")

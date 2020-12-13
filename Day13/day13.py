#Part 1:
with open('input.txt', 'r') as infile:
    target = int(infile.readline())
    busses = [int(num) for num in infile.readline().split(',') if 'x' not in num]

def nextTime(target, bus):
    runningTotal = bus
    while runningTotal <= target:
        runningTotal += bus
    return (runningTotal - target)

nextTimes =[nextTime(target, b) for b in busses]
minTime = min(nextTimes)
print(f"Solution to part 1: {minTime * busses[nextTimes.index(minTime)]}")
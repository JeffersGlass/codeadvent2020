from sys import exit

# Day 6, Part 1
letters = 'abcdefghijklmnopqrstuvwxyz'

with open('input.txt', 'r') as infile:
    data = ''.join([line for line in infile]).split('\n\n')

print(f"The solution to part 1 is: {sum([(1 if letter in group else 0) for letter in letters for group in data])}")

# Day 6 Part 2

with open('input.txt', 'r') as infile:
    data = ''.join([line for line in infile]).split('\n\n')

data = [group.split('\n') for group in data]

#First solution
print(f"The solution to part 2 is: {sum([sum([(1 if all([letter in form for form in group]) else 0) for letter in letters]) for group in data])}")

#Second Solution
def letterInAllForms(letter, group):
    return all([letter in form for form in group])

result = 0
for group in data:
    groupScore = sum([(1 if letterInAllForms(letter, group) else 0) for letter in letters])
    result += groupScore
print(f"The solution to part 2 is: {result}")


#Third Solution
result = 0

for group in data:
    groupList = list()
    for form in group:
        groupList.append([(1 if letter in form else 0) for letter in letters])

    scoreList = [1 for i in range(26)]    

    runningTotal = 0

    for i in range(26):
        for g in groupList:
            scoreList[i] *= g[i]
        runningTotal += scoreList[i]
    result += runningTotal

print(f"The solution to part 2 is: {result}")

    

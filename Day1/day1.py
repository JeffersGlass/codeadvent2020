from sys import exit

file = 'input.txt'

data = list()

with open(file, 'r') as infile:
    for line in infile:
        data.append(int(line.strip('\n').strip('\r')))

for i in range(len(data)):
    for j in range(i, len(data)):
        if data[i] + data[j] == 2020:
            print(f"Found that {data[i]} and {data[j]} sum to 2020; their product is {data[i]*data[j]}")
            exit()

print ("Finished loop, no pairs found that sum to 2020")
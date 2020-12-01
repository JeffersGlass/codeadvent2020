import sys
sys.path.append("..")
from function_timing import *

file = 'input.txt'

@timer
def naiveFind():
    data = list()

    with open(file, 'r') as infile:
        for line in infile:
            data.append(int(line.strip('\n').strip('\r')))

    for i in range(len(data)):
        for j in range(i, len(data)):
            if data[i] + data[j] == 2020:
                success(data[i], data[j])
                return

    print ("Finished loop, no pairs found that sum to 2020")

@timer
def dictFind():

    seen = dict()

    with open(file, 'r') as infile:
        for line in infile:
            num = int(line)
            complement = 2020-num
            if complement in seen:
                success(num, complement)
                return
            seen[num] = True

    print ("Finished loop, no pairs found that sum to 2020")



def success(first, second):
    print(f"Found that {first} and {second} sum to 2020; their product is {first*second}")

if __name__ == '__main__':
    #naiveFind()
    dictFind()
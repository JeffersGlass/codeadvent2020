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

@timer
def naiveProduct():

    data = list()

    with open(file, 'r') as infile:
        for line in infile:
            data.append(int(line.strip('\n').strip('\r')))

    for i in range(len(data)):
        for j in range(i, len(data)):
            for k in range(j, len(data)):
                if data[i] + data[j] + data[k] == 2020:
                    success(data[i], data[j], data[k])


def success(*args):
    """Prints a statement to the console that the numbers given as arguments sum to 2020 and prints their product
    """

    print("Found that ", end = "")
    product = 1
    for i in range(len(args)):
        print(f"{args[i]}", end = "")
        if i < len(args)-1: print(" and ", end = "")
        product *= args[i]
    print (f" sum to 2020; their product is: {product}")

    #Original implemenetation of this function that accepted only two arguments:
    #print(f"Found that {first} and {second} sum to 2020; their product is {first*second}")

if __name__ == '__main__':
    #For the solution to Day 1 part 1, run either of the following two functions:
    #naiveFind()
    #dictFind()

    #For the solution to Day 1 part 2, run the following function:
    naiveProduct()
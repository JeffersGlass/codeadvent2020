fileName = 'input.txt'

#Check whether any turns in the input file are not 90-degree increments
with open(fileName, 'r') as infile:
    nonNinetyTurns = [line for line in infile if line[0] in ['L','R'] and line.strip()[1:] not in ['90','180','270']]
    if len(nonNinetyTurns) > 0:
        raise ValueError(f"One or more turns is not an increment of 90 degrees; algorithm may give incorrect answers. {nonNinetyTurns}")

dirs = {'N':(0,-1), 'E':(1,0), 'W':(-1,0), 'S':(0,1)}

#Part 1:

location = [0,0]
direction = list(dirs['E'])

with open(fileName, 'r') as infile:
    for line in infile:
        if line[0] in dirs:
            location = [a+b for a,b in zip(location, [d*int(line[1:]) for d in dirs[line[0]]])]
        elif line.strip() in ['R90', 'L270']:
            direction = [-1*direction[1], direction[0]]
        elif line.strip() in ['L90', 'R270']:
            direction = [direction[1], -1*direction[0]]
        elif line.strip() in ['R180', 'L180']:
            direction = [-1*direction[0], -1*direction[1]]
        elif line[0] == 'F':
            location = [a+b for a,b in zip(location, [d*int(line[1:]) for d in direction])]
        else:
            raise ValueError(f"Unknown command {line}")
        #input(f"Line {line.strip()} lead to location: {location}")

print(f"Solution to part 1: {abs(location[0])+abs(location[1])}")

#Part 2:

location = [0,0]
waypoint = [10,-1]
direction = list(dirs['E'])

with open(fileName, 'r') as infile:
    for line in infile:
        if line[0] in dirs:
            waypoint = [a+b for a,b in zip(waypoint, [d*int(line[1:]) for d in dirs[line[0]]])]
        elif line.strip() in ['R90', 'L270']:
            waypoint = [-1*waypoint[1], waypoint[0]]
        elif line.strip() in ['L90', 'R270']:
            waypoint = [waypoint[1], -1*waypoint[0]]
        elif line.strip() in ['R180', 'L180']:
            waypoint = [-1*waypoint[0], -1*waypoint[1]]
        elif line[0] == 'F':
            location = [a+b for a,b in zip(location, [w*int(line[1:]) for w in waypoint])]
        else:
            raise ValueError(f"Unknown command {line}")
        #input(f"Line {line.strip()} lead to location: {location}. Waypoint is {waypoint}.")

print(location)
print(f"Solution to part 2: {abs(location[0])+abs(location[1])}")
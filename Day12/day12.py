#Check whether any turns in the input file are not 90-degree increments
with open('input.txt', 'r') as infile:
    nonNinetyTurns = [line for line in infile if line[0] in ['L','R'] and line.strip()[1:] not in ['90','180','270']]
    if len(nonNinetyTurns) > 0:
        raise ValueError(f"One ore more turns is not an increment of 90 degrees; algorithm may give incorrect answers. {nonNinetyTurns}")

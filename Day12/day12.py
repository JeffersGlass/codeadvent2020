with open('input.txt', 'r') as infile:
    print([line for line in infile if line[0] in ['L','R'] and line.strip()[1:] not in ['90','180','270']])
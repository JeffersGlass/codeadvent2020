from operator import add

if __name__ == '__main__':

    with open('input.txt', 'r') as infile:
        instructions = [line.strip() for line in infile]

    blackTiles = set()

    dirs = {
        'e':    (1,-1,0),
        'ne':   (1,0,-1),
        'nw':   (0,1,-1),
        'w':    (-1,1,0),
        'sw':   (-1,0,1),
        'se':   (0,-1,1)
    }

    for inst in instructions:
        pos = [0,0,0]
        while len(inst) > 0:
            if inst[0] in ['e','w']:
                direction = dirs[inst[0]]
                inst = inst[1:]
            else:
                direction = dirs[inst[0:2]]
                inst = inst[2:]
            pos = list(map(add, pos, direction))

        pos = tuple(pos)

        if pos not in blackTiles: blackTiles.add(pos)
        else: blackTiles.remove(pos)

    print(f"Solution to part 1: {len(blackTiles)}")
        
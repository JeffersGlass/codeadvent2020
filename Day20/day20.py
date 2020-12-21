def tilify(tileString):
    """Return a tile-formatted dictionary from a properly formatting input string

    Args:
        tileString (str): An 11-line string; 
        
        the first line is of the format
        Tile [Number]:

        The remaning lines consist of 10 characters which are either . or #, possibly followed by a new line
    Returns:
        A dictionary with keys/valules:
            "ID"    Number of the tiles ID
            "edges" Dictionary with keys 0, 1, 2, 3, corresponding to  "top", "right", "bottom", and "left"
                Values are numbers, which are equivalent to the binary value of each side
                of the given tile, with . being 0 and # being 1
            "minified" Set containing the values of the 4 edges, or each edge's "binRev" value
            (binary digits reversed), whichever is smaller
    """
    lines = tileString.split('\n')

    retDict = dict()
    retDict['ID'] = int(lines[0].split(' ')[1][:-1])

    retDict['edges'] = {
        0 : imageLineToNum(lines[1].strip()), #top edge
        1 : imageLineToNum(''.join([line[-1] for line in lines])), #right edge
        2 : imageLineToNum(lines[-1].strip()), #bottom edge
        3 : imageLineToNum(''.join([line[0] for line in lines])) #left edge
    }

    retDict['minified'] = {min(x, revBin(x)) for x in retDict['edges'].values()}

    return retDict

def findCorners(tileList):
    allSides = [item for t in tileList for item in t['minified']]
    corners = list()
    for t in tileList:
        nonMatched = 0
        for e in t['minified']:
            edgeCount = allSides.count(e)
            if edgeCount == 1: nonMatched += 1
        if nonMatched == 2: corners.append(t)
    return(corners)


def imageLineToNum(line):
    #region
    """Turns one line of 10 symbols into its representation as a number, taking . as 0 and # as 1 in binary

    Args:
        line (string): The string of . and # to be transformed

    Returns:
        int: The result of the transformation
    """
    #endregion

    return sum([2**i for i, digit in enumerate(line[::-1]) if digit == "#"])

def revBin(num):
    #region
    """Returns the value of a base 10 number with its binary digits reversed

    Args:
        num (int): Number to have its digits reversed

    Returns:
        int: the given number with its binary digits reversed
    """
    #endregion
    return int('{:010b}'.format(num)[::-1], 2)

if __name__ == '__main__':
    from math import prod 

    with open('input.txt', 'r') as infile:
        tileData = ''.join([line for line in infile]).split('\n\n')
    
    tiles = [tilify(t) for t in tileData]
    for c in findCorners(tiles):
        print(c)
    print(f"Solution to Part 1 is: {prod([c['ID'] for c in findCorners(tiles)])}")
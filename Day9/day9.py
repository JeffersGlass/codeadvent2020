def getFirstNonSum(lookback, data):
    for i in range(lookback, len(data)):
        if not any(
            [((data[i] - summand in data[i-lookback:i]) and \
            (summand != data[i]/2))
            for summand in data[i-lookback:i]] \
        ): return data[i]

if __name__ == '__main__':

    with open('input.txt', 'r') as infile:
        data = [int(line) for line in infile]

    print(getFirstNonSum(25, data))
from math import prod
import logging

def playRound(deck1, deck2):
    top1, top2 = deck1[0], deck2[0]
    if top1 > top2:
        logging.debug(f"Player 1 wins because {top1} > {top2}")
        deck1 = deck1[1:] + [top1] + [top2]
        deck2 = deck2[1:]
    else:
        logging.debug(f"Player 2 wins because {top1} < {top2}")
        deck1 = deck1[1:]
        deck2 = deck2[1:] + [top2] + [top1]
    return deck1, deck2

def score(deck):
    if len(deck) > 0: return sum([((i+1) * num) for i, num in enumerate(deck[::-1])])
    return 0

if __name__ == '__main__':
    #Part 1:
    logging.basicConfig(level=logging.INFO)

    with open('input.txt', 'r') as infile:
        player1, player2 = ''.join([line for line in infile]).split('\n\n')
        player1 = [int(x) for x in player1.split('\n')[1:]]
        player2 = [int(x) for x in player2.split('\n')[1:]]

    roundNum = 0
    while len(player1) > 0 and len(player2) > 0:
        player1, player2 = playRound(player1, player2)
        roundNum += 1
        logging.debug(f"After round {roundNum}, the decks are: \nPlayer 1:\n{player1}\nPlayer 2:\n{player2}")
        logging.debug("")

    print(f"This game took {roundNum} rounds to finish")
    print(f"Solution to part 1 is: {max(score(player1), score(player2))}")
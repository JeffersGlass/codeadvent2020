from math import prod
from copy import deepcopy
import logging
#from functools import cache

def playRoundPart1(deck1, deck2):
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

def playRoundPart2(deck1, deck2):
    top1, top2 = deck1[0], deck2[0]
    results = None
    if (len(deck1) - 1 >= top1) and (len(deck2) - 1) >= top2:
        logging.info(f"Playing subgame with decks {deepcopy(deck1[1:top1+1]), deepcopy(deck2[1:top2+1])}")
        results = playGame(deepcopy(deck1[1:top1+1]), deepcopy(deck2[1:top2+1]), playRoundPart2)
    if (results != None):
        if len(results[1]) == 0:  #player 1 won the subgame
            logging.debug(f"Player 1 has won the subgame")
            deck1 = deck1[1:] + [top1] + [top2]
            deck2 = deck2[1:]
        elif len(results[0]) == 0: #player 2 has won the subgame
            logging.debug(f"Player 2 has won the subgame")
            deck1 = deck1[1:]
            deck2 = deck2[1:] + [top2] + [top1]
    else:
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

def hashGame(deck1, deck2):
    return ((tuple([d for d in deck1]), tuple([d for d in deck2])))

def playGame(deck1, deck2, roundfunc):
    logging.debug(f"Playing game with decks\n{deck1}\n{deck2}")
    gameStates = set()
    gameStates.add(hashGame(deck1, deck2))

    roundNum = 0
    while len(deck1) > 0 and len(deck2) > 0:
        #logging.debug(f"Gamestates have been {gameStates}")
        deck1, deck2 = roundfunc(deck1, deck2)
        roundNum += 1
        logging.debug(f"After round {roundNum}, the decks are: \nPlayer 1:{deck1}\nPlayer 2:{deck2}")
        if hashGame(deck1, deck2) in gameStates:
            return ([1],[])
        else:
            gameStates.add(hashGame(deck1, deck2))
        logging.debug("-----")
        if logging.getLogger().level == logging.DEBUG: x = input("")
    logging.info(f"Results of game: {deck1},{deck2}")

    return(deck1, deck2)


if __name__ == '__main__':
    #Part 1:
    logging.basicConfig(level=logging.INFO)

    with open('input.txt', 'r') as infile:
        player1, player2 = ''.join([line for line in infile]).split('\n\n')
        player1 = [int(x) for x in player1.split('\n')[1:]]
        player2 = [int(x) for x in player2.split('\n')[1:]]

    player1, player2 = playGame(player1, player2, playRoundPart1)
    print(f"Solution to part 1 is: {max(score(player1), score(player2))}")

    #part2
    logging.getLogger().setLevel(logging.INFO)
    with open('input.txt', 'r') as infile:
        player1, player2 = ''.join([line for line in infile]).split('\n\n')
        player1 = [int(x) for x in player1.split('\n')[1:]]
        player2 = [int(x) for x in player2.split('\n')[1:]]

    player1, player2 = playGame(player1, player2, playRoundPart2)
    print(f"Solution to part 2 is: {max(score(player1), score(player2))}")

    #[10, 3, 18, 17, 36, 22, 32, 20, 16, 2, 30, 14, 45, 41, 25, 19, 33, 26, 13, 9, 12, 7, 8, 4, 43, 15, 38, 5, 50, 34, 39, 31, 48, 29, 49, 24, 42, 1, 47, 40, 35, 23, 44, 37, 28, 21, 46, 11, 27, 6],
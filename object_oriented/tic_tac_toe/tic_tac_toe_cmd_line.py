import copy, sys
from tic_tac_toe_game import Game

def get_move(game):                                 # get next move for X from user
    while True:
        move = int(input('# '))
        if not 1 <= move <= 9:
            raise Exception(f'user input of {move} is not in range [1 .. 9]')
        break
    return move

def run():
    game = Game()
    game.board.print_play_keys()                               # display how to specify moves as numbers
    print()
    while True:
        game.print()
        print()
        while True:
            try:
                move = get_move(game)               # get move from user
                print()
                msg, _ = game.play(move)            # record move on new copy of board
                game.print()
                print()
                if msg is not None:
                    print(msg)
                    print()
                    return
            except Exception as e:
                print(e)
                continue

run()
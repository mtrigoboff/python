import copy, statistics as stats, sys

class Board:

    # indices of rows, columns and diagonals
    rows_cols_diags = [[6, 7, 8], [3, 4, 5], [0, 1, 2],     # rows
                       [6, 3, 0], [7, 4, 1], [8, 5, 2],     # columns
                       [6, 4, 2], [8, 4, 0]]                # diagonals

    def __init__(self):                                     # initial board setup
        self.squares = [' '] * 9
        self.lines = [[self.squares[index] for index in line] for line in self.rows_cols_diags]

    @staticmethod
    def print_play_keys():                                  # print chart of play keys
        print('keys for moves')
        print(' 7 | 8 | 9 ')
        print('---+---+---')
        print(' 4 | 5 | 6 ')
        print('---+---+---')
        print(' 1 | 2 | 3 ')

    def print(self):                                        # print current state of this board
        print(f' {self.squares[6]} | {self.squares[7]} | {self.squares[8]} ')
        print('---+---+---')
        print(f' {self.squares[3]} | {self.squares[4]} | {self.squares[5]} ')
        print('---+---+---')
        print(f' {self.squares[0]} | {self.squares[1]} | {self.squares[2]} ')

    def is_full(self):                                      # are the board squares completely full
        return self.squares.count(' ') == 0

    def square(self, n):                                    # the value of a particular square
        return self.squares[n - 1]

    def score(self, player):                                # arbitrary "score" for a board
        line_scores = [line.count(player) for line in self.lines]
        return stats.mean(line_scores)

    def play(self, player, square):                         # play a particular square
        self.squares[square - 1] = player
        self.lines = [[self.squares[index] for index in rcd_line] for rcd_line in self.rows_cols_diags]
        return self

    def empty_square_indices(self):                         # list of indices of all empty squares
        return [i for i in range(9) if self.squares[i] == ' ']

    def win(self, player):                                  # is there a winning line for a player
        wins = [line for line in self.lines if line.count(player) == 3]
        return wins != []

    def could_win(self, player):                            # is there a line where player could win
        for i in range(8):
            line = self.lines[i]
            if line.count(player) == 2 and line.count(' ') == 1:
                return self.rows_cols_diags[i][line.index(' ')] + 1
        return -1

def get_move(board):                                        # get next move for X from user
    while True:
        try:
            move = int(input('# '))
            if not 1 <= move <= 9:
                raise Exception(f'user input of {move} is not in range [1 .. 9]')
            elif board.square(move) != ' ':
                raise Exception(f'square {move} is already occupied')
            break
        except Exception as e:
            print(e)
            continue
    print()
    return move

def end_if_win(board, player):                              # print board and exit if player wins
    if board.win(player):
        board.print()
        print()
        print(f'{player} wins!')
        print()
        sys.exit(0)

def end_if_board_full(board):                               # print board and exit if board is full
    if not board.empty_square_indices():
        board.print()
        print()
        print('game over - no win')
        print()
        sys.exit(0)

def run():
    board = Board()
    Board.print_play_keys()                                 # display how to specify moves as numbers
    print()
    while True:
        board.print()
        print()
        move = get_move(board)                              # get move from user
        board2 = copy.deepcopy(board)
        board2.play('X', move)                              # record move on new copy of board
        end_if_win(board2, 'X')                             # end if X wins
        end_if_board_full(board2)                           # end if board is full
        brd2_O_win = board2.could_win('O')                  # is there a move for O to win
        if brd2_O_win != -1:
            board2.play('O', brd2_O_win)                    # O makes winning move
            end_if_win(board2, 'O')                         # end because O wins as a result of move
        brd2_blk_move = board2.could_win('X')               # is there a move for X to win
        if brd2_blk_move != -1:
            board2.play('O', brd2_blk_move)                 # block winning move for X
            end_if_win(board2, 'O')                         # end if O wins
            end_if_board_full(board2)                       # end if board is full
            board = board2                                  # set up for next time through loop
        else:
            next_boards = [copy.deepcopy(board2).play('O', i + 1) for i in board2.empty_square_indices()]
            for brd in next_boards:
                end_if_win(brd, 'O')                        # end if O wins on this move
            # collect scores for all possible next boards, set next board to one with highest score
            next_board_scores = [board.score('O') for board in next_boards]
            board = next_boards[next_board_scores.index(max(next_board_scores))]

run()
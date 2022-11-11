import copy, enum, statistics as stats, sys

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

    def score(self, player):                                # arbitrary score for a board
        line_scores = [line.count(player) for line in self.lines]
        return stats.mean(line_scores)

    def play(self, player, square):                         # play a particular square
        self.squares[square] = player
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
                return self.rows_cols_diags[i][line.index(' ')]
        return -1

class Game:
    X_wins = 'X wins!'
    O_wins = 'O wins!'
    board_full = 'game over - draw'

    def __init__(self):
        self.board = Board()

    def print(self):
        self.board.print()

    # returns [message about why game is over, move that O made]
    def play(self, move):
        if self.board.squares[move - 1] != ' ':
            raise Exception(f'square {move} is already occupied')
        board2 = copy.deepcopy(self.board)
        board2.play('X', move - 1)                          # record move on new copy of board
        if board2.win('X'):
            self.board = board2
            return [Game.X_wins, None]                      # end if X wins
        if not board2.empty_square_indices():
            self.board = board2
            return [Game.board_full, None]                  # end if board is full
        brd2_O_win = board2.could_win('O')                  # is there a move for O to win
        if brd2_O_win != -1:
            board2.play('O', brd2_O_win)                    # O makes winning move
            self.board = board2
            return [Game.O_wins, brd2_O_win + 1]
        brd2_blk_move = board2.could_win('X')               # is there a move for X to win
        if brd2_blk_move != -1:
            board2.play('O', brd2_blk_move)                 # block winning move for X
            if board2.win('O'):                             # end if O wins
                self.board = board2
                return [Game.O_wins, brd2_blk_move + 1]
            if not board2.empty_square_indices():           # end if board is full
                self.board = board2
                return [Game.board_full, None]
            self.board = board2
            return [None, brd2_blk_move + 1]
        else:
            # list element: [index of board move, board]
            next_boards = [[i, copy.deepcopy(board2).play('O', i)] for i in board2.empty_square_indices()]
            for nb in next_boards:
                if nb[1].win('O'):                          # end if O wins
                    self.board = nb[1]
                    return [Game.O_wins, nb[0] + 1]
            # collect scores for all possible next boards, set next board to one with highest score
            next_board_scores = [item[1].score('O') for item in next_boards]
            # pick next board with highest score
            item = next_boards[next_board_scores.index(max(next_board_scores))]
            self.board = item[1]
            return [None, item[0] + 1]
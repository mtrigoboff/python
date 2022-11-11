import sys, time, turtle as t
from tic_tac_toe_game import Game

wn_size = 512
wn_margin = 60
turtle_size = 2
board_size = wn_size - 2 * wn_margin
line1_coord = wn_margin + board_size / 3
line2_coord = wn_margin + 2 * board_size / 3

class Square:
    size = (board_size - 2 * turtle_size) / 3
    margin = size / 6

    def __init__(self, bot_left_x, bot_left_y):
        self.bot_left_x = bot_left_x
        self.bot_left_y = bot_left_y
        self.marked = False

    def hit(self, x, y):
        return self.bot_left_x < x < self.bot_left_x + Square.size and \
               self.bot_left_y < y < self.bot_left_y + Square.size

    def mark(self, player):
        t.width(6)
        t.penup()
        if player == 'X':
            t.goto(self.bot_left_x + self.margin, self.bot_left_y + self.margin)
            t.pendown()
            t.goto(self.bot_left_x + self.size - self.margin,
                   self.bot_left_y + self.size - self.margin)
            t.penup()
            t.goto(self.bot_left_x + self.size - self.margin,
                   self.bot_left_y + self.margin)
            t.pendown()
            t.goto(self.bot_left_x + self.margin,
                   self.bot_left_y + self.size - self.margin)
        else:
            t.goto(self.bot_left_x + self.size / 2,
                   self.bot_left_y + self.margin)
            t.pendown()
            t.circle((self.size - 2 * self.margin) / 2)
        self.marked = True

    # def paint(self):
    #     t.penup()
    #     t.color('red')
    #     t.fillcolor('green')
    #     t.begin_fill()
    #     t.goto(self.bot_left_x,                 self.bot_left_y)
    #     t.pendown()
    #     t.goto(self.bot_left_x + Square.size,   self.bot_left_y)
    #     t.goto(self.bot_left_x + Square.size,   self.bot_left_y + Square.size)
    #     t.goto(self.bot_left_x,                 self.bot_left_y + Square.size)
    #     t.goto(self.bot_left_x,                 self.bot_left_y)
    #     t.penup()
    #     t.end_fill()

squares = [Square(wn_margin, wn_margin),
           Square(line1_coord - turtle_size / 2,        wn_margin),
           Square(line2_coord - turtle_size / 2,        wn_margin),
           Square(wn_margin,                            line1_coord - turtle_size / 2),
           Square(line1_coord - turtle_size / 2,        line1_coord - turtle_size / 2),
           Square(line2_coord - turtle_size / 2,        line1_coord - turtle_size / 2),
           Square(wn_margin,                            line2_coord - turtle_size / 2),
           Square(line1_coord - turtle_size / 2,        line2_coord - turtle_size / 2),
           Square(line2_coord - turtle_size / 2,        line2_coord - turtle_size / 2),
           ]

def draw_board():
    t.penup()

    t.goto(wn_margin, line1_coord - turtle_size / 2)  # bottom horizontal
    t.pendown()
    t.goto(wn_size - wn_margin, line1_coord - turtle_size / 2)
    t.penup()

    t.goto(wn_margin, line2_coord - turtle_size / 2)  # bottom horizontal
    t.pendown()
    t.goto(wn_size - wn_margin, line2_coord - turtle_size / 2)
    t.penup()

    t.goto(line1_coord - turtle_size / 2, wn_margin)  # left vertical
    t.pendown()
    t.goto(line1_coord - turtle_size / 2, wn_size - wn_margin)
    t.penup()

    t.goto(line2_coord - turtle_size / 2, wn_margin)  # right vertical
    t.pendown()
    t.goto(line2_coord - turtle_size / 2, wn_size - wn_margin)
    t.penup()

def open_window():
    t.title('CS 160 - Tic Tac Toe')

    t.setup(wn_size, wn_size, 0, 0)  # window size, turtle initial position

    # set window coordinates of bottom-left corner to 0,0
    t.setworldcoordinates(0, 0, wn_size, wn_size)

    t.hideturtle()
    t.penup()
    t.speed('fastest')
    t.bgcolor('papaya whip')
    t.width(turtle_size)
    t.color('black')

    # t.speed('slowest')
    # for square in squares:
    #     square.paint()

    draw_board()

game = Game()
done = False

def click_fn(x, y):
    global done

    if not done:
        for i in range(len(squares)):
            if squares[i].hit(x, y) and not squares[i].marked:
                squares[i].mark('X')
                # time.sleep(1)                   # make it seem like code is "thinking"
                msg, O_move = game.play(i + 1)
                if O_move is not None:
                    squares[O_move - 1].mark('O')
                    # print(f'O move: {O_move}')
                if msg is not None:
                    done = True
                    print(msg)
                return

open_window()

t.listen()
t.onkey(sys.exit, 'Escape')

t.onscreenclick(click_fn)  # function to call when screen is clicked

t.mainloop()
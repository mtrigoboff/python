import turtle as t

# colors coded as strings using names from the Turtle Graphics Colors page
dot_color = 'yellow green'
line_color = 'firebrick3'

# window properties
t.title(f'CS 160 - Coordinate Click')
t.bgcolor('pale goldenrod')

# set up window coordinates: 0,0 is bottom-left corner
width = 520
height = 320
t.setup(width, height, 0, 0)
t.setworldcoordinates(0, 0, width, height)

# pen properties
# (turtle starts out pointed horizontally to the right)
t.shape('turtle')
t.speed('slowest')                  # set turtle speed to slowest
t.width(3)                          # set pen width
t.color(line_color)

# initial pen position
t.penup()                           # don't draw while positioning
t.goto(width / 2, height / 2)       # set position

t.pendown()
print(f'init:  {int(width / 2):3}, {int(height / 2):3}')

# function to handle mouse clicks in window
def clickFn(x, y):
    print(f'click: {int(x):3}, {int(y):3}')
    t.goto(x, y)

# tell turtle graphics window to call clickFn()
# whenever mouse is clicked in window
t.onscreenclick(clickFn)

# function to handle escape key
def quitFn():
    quit()

t.listen()                          # tell window to listen to keyboard

# tell window to call quitFn when Escape key is hit
t.onkey(quitFn, 'Escape')

t.mainloop()                        # keep window open and responsive
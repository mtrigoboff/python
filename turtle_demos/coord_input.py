import turtle as t

title = 'CS 160 - Coordinate Input'
divider = '-------------------------'

# colors coded as strings using names from the Turtle Graphics Colors page
line_color = 'firebrick3'
bg_color = 'pale goldenrod'

# window properties
t.title(title)
t.bgcolor(bg_color)

# set up window coordinates: 0,0 is bottom-left corner
width = 520
height = 320
t.setup(width, height, 0, 0)
t.setworldcoordinates(0, 0, width, height)

# pen properties
# (turtle starts out pointed horizontally to the right)
t.shape('turtle')                       # set cursor shape to turtle
t.speed('slowest')                      # set turtle speed to slowest
t.width(3)                              # set pen width
t.color(line_color)

# initial pen position
t.penup()                               # don't draw while positioning
t.hideturtle()
turtleX = width / 2
turtleY = height / 2
t.setheading(90)
t.goto(turtleX, turtleY)                # set position

t.pendown()
t.showturtle()

print(title)
print(divider)

while True:

    x = input('input x coordinate: ')   # get x as string
    x = int(x)                          # convert x to number

    if x < 0:                           # stop if x is negative
        break

    y = input('input y coordinate: ')   # get y as string
    y = int(y)                          # convert y to number

    print('moving to ', x, y)           # print new position
    print(divider)                      # print divider

    t.goto(x, y)                        # move turtle to x and y

print(divider)
print('Click turtle graphics window to exit.')

t.exitonclick()                         # keep window open until mouse click
import math, turtle as t

# colors coded as strings using names from the Turtle Graphics Colors page
dot_color = 'yellow green'
line_color = 'firebrick3'

# window properties
t.title(f'CS 160 - Turtle Chase')
t.bgcolor('pale goldenrod')

# set up window coordinates: 0,0 is bottom-left corner
width = 520
height = 320
t.setup(width, height, 0, 0)
t.setworldcoordinates(0, 0, width, height)

# pen properties
# (turtle starts out pointed horizontally to the right)
t.shape('turtle')               # set cursor shape to turtle
t.speed(0.51)                   # set turtle speed to slowest
t.width(4)                      # set pen width
t.color(line_color)

# initial turtle position
t.penup()                       # don't draw while positioning
t.hideturtle()
t.setheading(90)                # pointing up
turtleX = width / 2
turtleY = height / 2
t.setpos(turtleX, turtleY)		# set position

t.penup()
t.showturtle()

def clickFn(x, y):
    global turtleX, turtleY

    if x == turtleX:        # avoid divide by zero
        if y > turtleY:
            heading = 90
        else:
            heading = 270
    else:
        yDiff = y - turtleY
        xDiff = x - turtleX
        tan = yDiff / xDiff
        # print(f'xDiff: {xDiff}, yDiff: {yDiff}, tan = {tan:.2f} ', sep='')
        heading = math.degrees(math.atan((y - turtleY) / (x - turtleX)))
        if xDiff < 0:
            heading = (heading + 180) % 360
    # print(f'heading = {heading:.2f}')
    t.setheading(heading)
    t.goto(x, y)
    turtleX = x
    turtleY = y

t.onscreenclick(clickFn)
t.mainloop()                    # run turtle window
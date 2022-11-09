import math, turtle as t

# colors coded as strings using names from the Turtle Graphics Colors page
dot_color = 'yellow green'
line_color = 'firebrick3'

# window properties
t.title(f'CS 160 - Coordinate Input')
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

# initial pen position
t.penup()                       # don't draw while positioning
t.hideturtle()
turtleX = width / 2
turtleY = height / 2
t.setheading(90)
t.setpos(turtleX, turtleY)		# set position

t.penup()
t.showturtle()
print('ready')
while (True):
    heading = float(input('heading: '))
    t.setheading(heading)

t.exitonclick()                  # keep window open until mouse click
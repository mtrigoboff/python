import turtle as t

# import pdb; pdb.set_trace()		        # start debugger

red_color = 'firebrick2'
green_color = 'chartreuse3'
blue_color = 'dodger blue'

title = 'CS 160 - Coordinate Input (Colors)'
divider = '-------------------------'

def setup_window():
    # colors coded as strings using names from the Turtle Graphics Colors page
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
    t.color('gray63')

    # initial pen position
    t.penup()                               # don't draw while positioning
    t.hideturtle()
    turtleX = width / 2
    turtleY = height / 2
    t.setheading(90)
    t.goto(turtleX, turtleY)                # set position

setup_window()

t.pendown()
t.showturtle()

print(title)
print(divider)

while True:

    input_color = input('red, green, blue, or stop: ')
    if input_color == 'red':
        line_color = red_color
    elif input_color == 'green':
        line_color = green_color
    elif input_color == 'blue':
        line_color = blue_color
    elif input_color == 'stop':
        break
    else:
        continue

    coords = input('input x, y coordinates: ')
    x_coord, y_coord = coords.split()
    x = int(x_coord)                    # convert x to number
    y = int(y_coord)                    # convert y to number

    print('moving to ', x, y)           # print new position
    print(divider)                      # print divider

    t.color(line_color)
    t.goto(x, y)                        # move turtle to x and y

print(divider)
print('Click turtle graphics window to exit.')

t.exitonclick()                         # keep window open until mouse click
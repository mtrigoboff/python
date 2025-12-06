import turtle as t

# window parameters
wnWidth = 840
wnHeight = 800

# set up turtle graphics window
def setup():
	t.title('CS 160 - Fractal Turtle Tree')
	
	t.setup(wnWidth, wnHeight, 0, 0)  # window size, turtle initial position
	
	# set window coordinates of bottom-left corner to 0,0
	t.setworldcoordinates(0, 0, wnWidth, wnHeight)
	
	t.bgcolor('LightBlue1')

	t.speed('fastest')
	t.penup()

# lawn parameters
lawnColor = 'light green'
lawnHeight = 100
lawnTweak = 10                          # needed to cover entire window width

def drawLawn():
	t.color(lawnColor)
	t.pencolor(lawnColor)
	t.fillcolor(lawnColor)
	t.begin_fill()
	t.goto(-lawnTweak, -lawnTweak)
	t.pendown()
	t.setheading(90)
	t.forward(lawnHeight)
	t.right(90)
	t.forward(wnWidth + lawnTweak)
	t.right(90)
	t.forward(lawnHeight)
	t.right(90)
	t.forward(wnWidth + lawnTweak)
	t.end_fill()
	t.penup()

# tree parameters
shorten = 0.75
narrow = 0.66
angle = 24
greener = 1.14
stopLgth = 30
initialPenWidth = 32

def drawBranch(xCoord, yCoord, lgth, heading, penWidth, penColor):
	t.pencolor(penColor)
	t.setheading(heading)
	t.width(penWidth)
	t.goto(xCoord, yCoord)

	t.pendown()
	t.forward(lgth)
	t.penup()
	
	if lgth >= stopLgth:
		penColor = [penColor[0], min(penColor[1] * greener, 1), penColor[2]]
		branchEndCoords = t.position()
		drawBranch(branchEndCoords[0], branchEndCoords[1],
		           lgth * shorten, heading + angle,
		           penWidth * narrow, penColor)
		drawBranch(branchEndCoords[0], branchEndCoords[1],
		           lgth * shorten, heading - angle,
		           penWidth * narrow, penColor)
	else:
		t.color(penColor)
		t.stamp()

setup()

drawLawn()

# draw sun
t.goto(60, wnHeight - 80)
t.dot(70, 'yellow')

# draw tree
t.shape('turtle')
drawBranch(wnWidth / 2 - initialPenWidth / 4, -10, 200, 90, initialPenWidth, [0.5, 0.35, 0])

# turtle climbs tree trunk
t.setheading(75)
t.goto(wnWidth / 2 - 11, -10)
t.speed('slowest')
t.goto(wnWidth / 2 - 11, 152)

t.exitonclick()
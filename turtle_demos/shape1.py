import turtle as t

# window
window_title = 'CS 160 - Shape 1'
window_width = 300
window_height = 300

def setup(wnTitle, wnWidth, wnHeight):
	# window properties
	t.title(wnTitle)
	t.setup(wnWidth, wnHeight, 0, 0)	# window size, turtle initial position

	# set window coordinates of bottom-left corner to 0,0
	t.setworldcoordinates(0, 0, wnWidth, wnHeight)

	# pen properties (turtle starts out pointed horizontally to the right)
	t.speed('slowest')              # other possibilities: fastest, fast, normal, slow

# colors coded as strings using names from the Turtle Graphics Colors page
fill_color = 'yellow green'
line_color = 'firebrick3'
bg_color = 'pale goldenrod'

setup(window_title, window_width, window_height)

# set up shape
t.color(line_color)					# set pen color
t.fillcolor(fill_color)
t.width(4)  						# set pen width
line_lgth = 100

t.bgcolor(bg_color)
t.penup()
t.goto(window_width / 2, window_height * 0.82)
t.setheading(90)					# point straight up
t.pendown()

# draw shape
t.begin_fill()                      # shape drawn below this will be filled
vertex_angle = 72

# draw shape
t.right(126)
t.forward(line_lgth)
t.right(vertex_angle)
t.forward(line_lgth)
t.right(vertex_angle)
t.forward(line_lgth)
t.right(vertex_angle)
t.forward(line_lgth)
t.right(vertex_angle)
t.forward(line_lgth)
t.right(vertex_angle)

t.end_fill()                        # fill drawn shape with fill_color

t.exitonclick()						# keep window open until mouse click
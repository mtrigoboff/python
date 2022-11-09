# demonstrates writing text into turtle window

import random, sys, turtle as t

# window width and height
wn_width = 520
wn_height = 400

# code that sets up the turtle graphics window
def setup():
	t.title('CS 160 - Write Demo')
	
	t.setup(wn_width, wn_height, 0, 0)  # window size, turtle initial position
	
	# set window coordinates of bottom-left corner to 0,0
	t.setworldcoordinates(0, 0, wn_width, wn_height)
	
	t.hideturtle()
	t.penup()
	t.speed('fastest')
	
	t.bgcolor('bisque')

# global variables
click_number = 0
colors = ['red', 'yellow', 'green', 'blue', 'violet', 'black', 'white']

# called when screen is clicked
def screen_click_fn(x, y):
	global click_number		# needed because we are modifying this global variable
	
	t.goto(x, y)
	t.color(random.choice(colors))
	click_number += 1
	t.write(f'Click {click_number}', False, 'center', ['Arial', 16, 'bold'])

setup()

t.onscreenclick(screen_click_fn)  	# function to call when screen is clicked

t.listen()
t.onkey(sys.exit, 'Escape')

t.mainloop()						# window will process user interface events
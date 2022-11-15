class Rectangle:
	def __init__(self, name, botLeftX, botLeftY, width, height, penWidth, color):
		self.name =				name
		self.botLeftX =			botLeftX
		self.botLeftY =			botLeftY
		self.width =			width
		self.height =			height
		self.penWidth =			penWidth
		self.color =			color

	def __str__(self):
		return f'{rect.name}, {rect.botLeftX}, {rect.botLeftY}, {rect.width}, {rect.height}, {rect.penWidth}, {rect.color}'

rectangles = [Rectangle('Rect1',  50,  50, 200, 120, 8, 'blue'),
              Rectangle('Rect2', 280, 310, 200, 120, 6, 'red'),
              Rectangle('Rect3', 500, 600, 220, 150, 8, 'green'),
			  Rectangle('Rect4',  50, 600, 200, 120, 4, 'purple'),
              Rectangle('Rect5', 500,  50, 180, 100, 2, 'black')]

for rect in rectangles:
	print(rect)
print()
import os.path, sys

import tkinter as tk
from tkinter import ttk		# 'improved' tkinter widgets

from pcc.gui.items.button import Button
from pcc.gui.items.textfield import TextField
from pcc.gui.items.nosuchitemerror import NoSuchItemError
from pcc.gui.items.automate import automate

def newWindow(name, keypressFn=None, updateFn=None):
	"""
	Returns a new window object with specified ``name``, ``keypressFn``, and ``updateFn``.
	The second and third arguments are optional. See :ref:`wn_functions`.

	:param name: window name
	:type name: string
	:param keypressFn: keypress handler (see :ref:`wn_functions`)
	:type keypressFn: Python function
	:param updateFn: updates the user interface state (see :ref:`wn_functions`)
	:type updateFn: Python function
	:return: ``pcc.gui.Window`` instance
	"""
	return Window(name, keypressFn, updateFn)

class Window:
	"""
	A Python class that creates a window on the screen which can be populated
	with graphical user interface items like text fields and buttons.
	"""

	def setPosn(self, x, y):
		"""
		Sets the position of the window on the screen. The ``x`` and ``y`` arguments specify
		the position of the top-left corner of the window. The top-left corner of
		the screen is ``x == 0``, ``y == 0``. Larger values of ``x`` are to the *right*.
		Larger values of ``y`` are *lower*.

		:param x: x coordinate of top-left corner of window
		:type x: int
		:param y: y coordinate of top-left corner of window
		:type y: int
		:return: *nothing*
		"""
		self.wn.geometry('+{}+{}'.format(x, y))

	def setSize(self, width, height):
		"""
		Sets the size of the window on the screen.

		:param width: width of the window
		:type width: int
		:param height: heightof the window
		:type height: int
		:return: *nothing*
		"""
		self.wn.geometry('{}x{}'.format(width, height))

	def setResizable(self, widthResizable, heightResizable):
		"""
		Makes the width and/or the height of the window resizable.

		:param widthResizable: make the width of the window resizable
		:type widthResizable: Boolean
		:param heightResizable: make the height of the window resizable
		:type heightResizable: Boolean
		:return: *nothing*
		"""
		self.wn.resizable(widthResizable, heightResizable)

	def addButton(self, name, btnClickFn, sameRow=False, enabled=True):
		"""
		Adds a button to the window. Specify ``sameRow=True`` to add the button
		to the same row as the previously added window item.

		:param name: name of the button
		:type name: string
		:param btnClickFn: function to call when the button is clicked.
							The function argument will be the name of the button.
		:type btnClickFn: fn(string)
		:param sameRow: whether to add the button to the current row or the next row
		:type sameRow: Boolean
		:param enabled: whether the button is enabled or disabled (grayed out)
		:type enabled: Boolean
		:return: *nothing*
		"""
		btn = Button(self, name, btnClickFn, enabled)
		if not sameRow:
			self.currentRow = self.currentRow + 1
			self.currentCol = 0
		else:
			self.currentCol = self.currentCol + 1
		btn.grid(self.currentRow, self.currentCol)

	def addTextField(self, name, enabled=True):
		"""
		Adds a text field to the next row of the window.

		:param name: name of the text field
		:type name: string
		:param enabled: whether the text field will accept user input
		:type enabled: Boolean
		:return: *nothing*
		"""
		field = TextField(self, name)
		self.currentRow = self.currentRow + 1
		field.grid(self.currentRow)
		field.setEnabled(enabled)

	def getValue(self, name):
		"""
		Gets the value of the named window item.
		Can cause a ``NotImplentedError`` for item types that do not contain a value (e.g. button).
		Can cause a ``NoSuchItemError`` if ``name`` is not the name of an item.

		:param name: name of the window item
		:type name: string
		:return: value of the item
		:rtype: depends on item type; string for text field
		"""
		item = self.getItem(name)
		return item.getValue()

	def setValue(self, name, value):
		"""
		Sets the value of the named window item.
		Can cause a ``NotImplentedError`` for item types that do not contain a value (e.g. button).
		Can cause a ``NoSuchItemError`` if ``name`` is not the name of an item.

		:param name: name of the window item
		:type name: string
		:param value: value for the window item
		:type value: depends on item type
		:return: *nothing*
		"""
		item = self.getItem(name)
		item.setValue(value)

	def setEnabled(self, name, enabled):
		"""
		Sets the enabled state of the named window item.
		For instance, a button could be grayed out and unresponsive or normal-looking and active.
		Can cause a ``NotImplentedError`` for item types that do not support enabled/disabled states.
		Can cause a ``NoSuchItemError`` if ``name`` is not the name of an item.

		:param name: name of the window item
		:type name: string
		:param enabled: value for the window item
		:type enabled: Boolean
		:return: *nothing*
		"""
		item = self.getItem(name)
		item.setEnabled(enabled)

	def open(self):
		"""
		Opens the window.

		:return: *nothing*
		"""
		appDirPath = os.path.split(sys.argv[0])[0]
		if len(sys.argv) > 1:
			for argv in sys.argv[1:]:
				if len(argv) > 2 and argv[:2] == '<-':
					automateFilePath = os.path.join(appDirPath, argv[2:])
					if os.path.isfile(automateFilePath):
						self.openWindow = automate(self, automateFilePath)
						if self.updateFn is not None:
							self.updateFn()
		if self.openWindow:
			self.wn.mainloop()

	def close(self):
		"""
		Closes the window.

		:return: *nothing*
		"""
		if self.openWindow:
			self.wn.quit()

	def focusReturnKey(self):
		"""
		Call this from your ``myKeypressFn(key)`` function if you want the window item that currently has the focus to respond to the Return/Enter key. See :ref:`focus_and_return_key` and :ref:`wn_functions`.

		:return: *nothing*
		"""
		widget = self.wn.focus_get()

		# currently it only makes sense for buttons to respond
		if widget.widgetName == 'ttk::button':
			widget.invoke()

	# "private" members

	def __init__(self, title, keyPressFn=None, updateFn=None):
		self.wn = wn = tk.Tk()

		wn.protocol('WM_DELETE_WINDOW', self.close)
		wn.title(title)
		frame = ttk.Frame(wn, padding='12 12 12 12')
		frame.pack()

		if keyPressFn is not None:
			wn.bind_all('<KeyPress>', self.keyPressHandler)
			self.keyPressFn = keyPressFn

		self.updateFn = updateFn

		self.wn = wn
		self.frame = frame
		self.items = {}
		self.currentRow = 0
		self.currentCol = 0
		self.openWindow = True


	def keyPressHandler(self, event):
		ignoreKeySyms = ('App', 'Control_L', 'Control_R', 'Shift_L', 'Shift_R', 'Win_L', 'Win_R')
		# App is the context menu key

		if self.keyPressFn is not None and event.keysym not in ignoreKeySyms:
			self.keyPressFn(event.keysym)
		if self.updateFn is not None:
			self.updateFn()

	def getItem(self, name):
		try:
			item = self.items[name]
		except:
			raise NoSuchItemError(name)

		return item


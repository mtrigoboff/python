import tkinter as tk
from tkinter import ttk		# 'improved' tkinter widgets

from mlt.gui.items.item import Item

class TextField(Item):

	def __init__(self, window, name):
		super(TextField, self).__init__(window, name)
		self.label = ttk.Label(window.frame, text = name + ':')
		self.var = tk.StringVar()
		self.field = tk.Entry(window.frame, textvariable=self.var, state='normal')

	def grid(self, row, col=0):
		self.label.grid(row=row, column=col, sticky='e', padx=self.padding, pady=self.padding)
		self.field.grid(row=row, column=col+1, padx=self.padding, pady=self.padding)

	def getValue(self):
		return self.var.get()

	def setValue(self, value):
		return self.var.set(value)

	def setEnabled(self, enabled):
		if enabled:
			# self.label.state(['!disabled'])
			self.field.config(state='normal')
		else:
			# self.label.state(['disabled'])
			self.field.config(state='readonly')


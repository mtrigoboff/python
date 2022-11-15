import tkinter as tk
from tkinter import ttk		# 'improved' tkinter widgets

from pcc.gui.items.item import Item

class Button(Item):

	def __init__(self, window, name, btnClickFn=None, enabled=True):
		super(Button, self).__init__(window, name)
		if enabled:
			state = 'normal'
		else:
			state = 'disabled'
		self.btn = ttk.Button(window.frame, text=name, command=self.btnFn, state=state)
		self.btnClickFn = btnClickFn
		self.setEnabled(enabled)

	def btnFn(self):
		if self.btnClickFn is not None:
			self.btnClickFn(self.name)

	def setEnabled(self, enabled):
		if enabled:
			self.btn.state(['!disabled'])
		else:
			self.btn.state(['disabled'])

	def grid(self, row, col=0):
		self.btn.grid(row=row, column=col, padx=self.padding, pady=self.padding)


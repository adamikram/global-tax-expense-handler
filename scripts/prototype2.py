import tkinter as tk
import csv
from tkinter import messagebox
import os


class ListBox:
	def __init__(self,parent):
		self.parent = parent
		

		self.my_scrollbar = tk.Scrollbar(parent,orient=tk.VERTICAL)
		self.my_listbox = tk.Listbox(parent,yscrollcomman=self.my_scrollbar,height=50,width=50)		
		self.my_scrollbar.config(command=self.my_listbox.yview)		

	def render(self):
		self.my_listbox.pack()
		self.my_scrollbar.pack()



class program:
	def __init__(self):
		self.root = tk.Tk()
		self.root.title('Global Tax Statement Consolidator')

		expenseType_listbox = ListBox(self.root)
		expenseType_listbox.render()


	def start(self):
		self.root.mainloop()

if __name__ == "__main__":
	myProgram = program()
	myProgram.start()
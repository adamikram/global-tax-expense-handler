from tkinter import ttk
import tkinter as tk

class GfiWindow(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, *kwargs)



        self.tv = ttk.Treeview(self)
        self.tv['columns'] = ('Rank', 'Name', 'Badge')
        self.tv.column('#0', width=0, stretch=tk.NO)
        self.tv.column('Rank', anchor=tk.CENTER, width=80)
        self.tv.column('Name', anchor=tk.CENTER, width=80)
        self.tv.column('Badge', anchor=tk.CENTER, width=80)

        self.tv.heading('#0', text='', anchor=tk.CENTER)
        self.tv.heading('Rank', text='Id', anchor=tk.CENTER)
        self.tv.heading('Name', text='rank', anchor=tk.CENTER)
        self.tv.heading('Badge', text='Badge', anchor=tk.CENTER)
        #
        # self.tv.insert(parent='', index=0, iid=0, text='', values=('1', 'Vineet', 'Alpha'))
        # self.tv.insert(parent='', index=1, iid=1, text='', values=('2', 'Anil', 'Bravo'))
        # self.tv.insert(parent='', index=2, iid=2, text='', values=('3', 'Vinod', 'Charlie'))
        # self.tv.insert(parent='', index=3, iid=3, text='', values=('4', 'Vimal', 'Delta'))
        # self.tv.insert(parent='', index=4, iid=4, text='', values=('5', 'Manjeet', 'Echo'))
        self.tv.grid(column=0, row=0, sticky='NW')

    def make_columns(self):
        pass

    def populate_tree(self):
        pass

    def clear_tree(self):
        pass
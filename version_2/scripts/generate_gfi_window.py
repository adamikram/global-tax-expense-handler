from tkinter import ttk
import tkinter as tk
import pandas as pd

class Tree(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, *kwargs)
        self.grid_columnconfigure(0, weight=1)


        self.tv = ttk.Treeview(self)
        self.tv.grid(column=0, row=0, sticky='EW')

    def make_columns(self, columns):
        self.tv['columns'] = columns

        self.tv.column('#0', width=0, stretch=tk.NO)
        self.tv.heading('#0', text='', anchor=tk.CENTER)
        for column in columns:
            self.tv.column(column, anchor=tk.E, width=150, stretch=tk.NO)
            self.tv.heading(column, text=column, anchor=tk.CENTER)
        pass

    def populate_tree(self, rows):
        count = 0
        for row in rows:
            self.tv.insert(parent='', index=count, iid=count, values=row)
            count += 1

    def clear_tree(self):
        self.tv.delete(*self.tv.get_children())

class GfiView(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.statementTree = Tree(self)
        self.statementTree.make_columns(['SHeesh', 'bruh', 'ayyo'])
        self.statementTree.grid(column=0, row=0, sticky='we')

    def update_tree(self, df):
        # print(data.columns)

        # print(df.columns[0])
        columns = []
        for columnTitle in df.columns:
            columns.append(columnTitle)
        self.statementTree.make_columns(columns)

        self.statementTree.populate_tree(df.values.tolist())

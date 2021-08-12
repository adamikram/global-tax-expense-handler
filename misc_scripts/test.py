import tkinter as tk
from tkinter import Label
from tkinter import filedialog


root = tk.Tk()
my_label = tk.Label(root,text='root.filename').pack()
my_label.config(text=root.filename)

def getFile():
   root.filename = tk.filedialog.askopenfilename(initialdir="../all_data/script_data",title="Select A CSV Statement",filetypes=(("csv files", "*.csv"),("all files","*.*")))
   

my_button = tk.Button(root,text = 'Select File to Apply Word Bank',command = getFile).pack()





root.mainloop()

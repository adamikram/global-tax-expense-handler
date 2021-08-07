from tkinter import *
from tkinter import filedialog


root = Tk()

my_label = Label(root).pack()

def getFile():
   root.filename = filedialog.askopenfilename(initialdir="../all_data/script_data",title="Select A CSV Statement",filetypes=(("csv files", "*.csv"),("all files","*.*")))
   global my_label
   my_label.config(text=root.filename)




my_button = Button(root,text = 'Select File to Apply Word Bank',command = getFile).pack()


root.mainloop()

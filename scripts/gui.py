import tkinter as tk

# class labelList






window = tk.Tk()
programFrame = tk.Frame(master=window,bg="green")
programFrame.pack(fill=tk.BOTH,expand=True)

titleFrame = tk.Frame(master=programFrame,height=50, bg="blue")
titleFrame.pack(fill=tk.X,side=tk.TOP)

actionFrame = tk.Frame(master=programFrame,bg="yellow")
actionFrame.pack(fill=tk.BOTH,side=tk.TOP,expand=True)

titleLabel = tk.Label(master=titleFrame,text="Expense Consolidator")
titleLabel.pack(fill=tk.BOTH,side=tk.TOP,expand=True)

expenseTypeColumnTitle = tk.Label(master=actionFrame,text="Expense Types")
expenseTypeColumnTitle.grid(row=0,column=0)


window.mainloop()
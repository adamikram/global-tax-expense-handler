from classes import *
import tkinter as tk



class listBox(tk.Frame):
    def __init__(self,parent,*args,**kwargs):
        tk.Frame.__init__(self,parent,*args,**kwargs)

        self.scrollbar = tk.Scrollbar(self,orient=tk.VERTICAL)
        self.lb = tk.Listbox(self, yscrollcommand=self.scrollbar, height=50, width=40)
        self.scrollbar.config(command= self.lb.yview)
        self.scrollbar.pack(side= tk.RIGHT, fill=tk.Y)
        self.lb.pack(fill=tk.Y, expand=True)

    #can add a list using
    def addList(self,list):
        self.lb.delete(0,tk.END)
        self.lb.insert(tk.END, *list)

    # configure lb
    def config(self,**kwargs):
        self.lb.config(**kwargs)

class MainApplication(WordBank):
    def __init__(self,filePath):
        self.root = tk.Tk()

        # self.wordBank = WordBank(filePath)
        #
        # self.operatingExpense_Listbox = listBox(self.root)
        # self.operatingExpense_Listbox.pack()
        # self.operatingExpense_Listbox.addList(self.wordBank.get_operating_expenses())

        # ---- Operating Expense Column -----
        operatingExpenses_Label = tk.Label(self.root, text="Operating Expense", pady=10).grid(column=0, row=0, sticky="EW", padx = 5)
        operatingExpense_Listbox = listBox(self.root).grid(column=0, row=1, sticky="NS", padx = 5)
        addOperatingExpense_Button = tk.Button(text="Add Operating Expense").grid(column=0, row=2, sticky="EW",ipady = 10, pady = 5, padx = 5)
        removeOperating_Expense = tk.Button(text="Remove Operating Expense").grid(column=0, row=3, sticky="EW",ipady = 10, padx = 5)

        # ---- Expense Bank Column ----#
        expenseBank_Label = tk.Label(self.root,text="Expense Bank",pady=10).grid(column=1, row=0, sticky="EW", padx = 5)
        expenseBank_Listbox = listBox(self.root).grid(column=1, row=1, sticky="NS", padx = 5)
        addExpense_Button = tk.Button(text="Add Expense Keyword").grid(column=1, row=2, sticky="EW",ipady = 10, pady = 5, padx = 5)
        removeExpense_Button = tk.Button(text="Remove Expense Keyword").grid(column=1, row=3, sticky="EW",ipady = 10, padx = 5)

        # ---- Undefined Expenses Column ----
        undefinedExpense_Label = tk.Label(self.root,text="Undefined Expenses",pady=10).grid(column=2, row=0, sticky="EW", padx = 5)
        expenseBank_Listbox = listBox(self.root).grid(column=2, row=1, sticky="NS", padx = 5)
        fileSelect_Button = tk.Button(text="Choose File(s)").grid(column=2, row=2, sticky="EW",ipady = 10, pady = 5, padx = 5)
        consolidate_Button = tk.Button(text="Consolidate Expenses").grid(column=2, row=3, sticky="EW",ipady = 10, pady = 5, padx = 5)




        self.root.mainloop()

        pass


if __name__ == "__main__":
    wordBankPath = r'../data/newWordBank.csv'

    app = MainApplication(wordBankPath)
    pass

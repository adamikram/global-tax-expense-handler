from classes import *
import tkinter as tk
from tkinter import messagebox


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

class AddExpenseType():
    def __init__(self, parent):
        self.surface = tk.Toplevel(parent)

        self.expense_Label = tk.Label(self.surface, text='Operating Expense', padx=5, justify=tk.LEFT)
        self.code_Label = tk.Label(self.surface, text='Expense Code', padx=5, justify=tk.LEFT)

        self.expense_Label.grid(column=0, row=0, sticky='W',pady = 5)
        self.code_Label.grid(column=0, row=1, sticky='W', pady = 5)

        self.expense_Entry = tk.Entry(self.surface)
        self.code_Entry = tk.Entry(self.surface)

        self.expense_Entry.grid(column=1, row=0, sticky='E', pady = 5)
        self.code_Entry.grid(column=1, row=1, sticky='E', pady = 5)

        self.submit_Button = tk.Button(self.surface, text="Submit Operating Expense", command=self.get_entry_val)
        self.submit_Button.grid(column=0, row=2, columnspan=2, sticky='EW')

    def get_entry_val(self):
        newOperatingExpense = self.expense_Entry.get()
        newCode = self.code_Entry.get()

        print(newOperatingExpense.isspace())

        if newOperatingExpense.isspace() == True or newCode.isspace() == True:
            messagebox.showerror("Error", "Invalid Entry")

class WordbankView(tk.Frame):
    def __init__(self,wordbankPath,parent, *args, **kwargs):
        tk.Frame.__init__(self,parent,*args,**kwargs)
        self.wordbank = WordBank(wordbankPath)


        # ---- Operating Expense Column -----
        operatingExpenses_Label = tk.Label(self, text="Operating Expense", pady=10)
        operatingExpense_Listbox = listBox(self)
        addOperatingExpense_Button = tk.Button(self, text="Add Operating Expense", command=self.add_expense_type)
        removeOperating_Expense = tk.Button(self, text="Remove Operating Expense")

        operatingExpenses_Label.grid(column=0, row=0,sticky="EW", padx=5)
        operatingExpense_Listbox.grid(column=0, row=1, sticky="NS", padx=5)
        addOperatingExpense_Button.grid(column=0, row=2, sticky="EW", ipady=10, pady=5, padx=5)
        removeOperating_Expense.grid(column=0, row=3, sticky="EW", ipady=10, padx=5)

        operatingExpense_Listbox.addList(self.wordbank.get_operating_expenses())

        # ---- Expense Bank Column ----#
        expenseBank_Label = tk.Label(self, text="Expense Bank", pady=10)
        expenseBank_Listbox = listBox(self)
        addExpense_Button = tk.Button(self, text="Add Expense Keyword")
        removeExpense_Button = tk.Button(self, text="Remove Expense Keyword")

        expenseBank_Label.grid(column=1, row=0, sticky="EW", padx=5)
        expenseBank_Listbox.grid(column=1, row=1, sticky="NS", padx=5)
        addExpense_Button.grid(column=1, row=2, sticky="EW", ipady=10, pady=5,padx=5)
        removeExpense_Button.grid(column=1, row=3, sticky="EW", ipady=10, padx=5)

        # ---- Undefined Expenses Column ----
        undefinedExpense_Label = tk.Label(self, text="Undefined Expenses", pady=10)
        expenseBank_Listbox = listBox(self)
        fileSelect_Button = tk.Button(self,text="Choose File(s)")
        consolidate_Button = tk.Button(self,text="Consolidate Expenses")

        undefinedExpense_Label.grid(column=2, row=0, sticky="EW", padx=5)
        expenseBank_Listbox.grid(column=2, row=1, sticky="NS", padx=5)
        fileSelect_Button.grid(column=2, row=2, sticky="EW", ipady=10, pady=5,padx=5)
        consolidate_Button.grid(column=2, row=3, sticky="EW", ipady=10, pady=5, padx=5)

    def add_expense_type(self):
            allOperatingExpenses = self.wordbank.get_operating_expenses()
            # allCodes = self.wordbank.get

            AddExpenseType(self)
            # print('bruh')

from csv_parse import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import os

class listBox(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.lb = tk.Listbox(self, yscrollcommand=self.scrollbar, height=50, width=40, exportselection=False)
        self.scrollbar.config(command=self.lb.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.lb.pack(fill=tk.Y, expand=True)

    #can add a list using
    def add_list(self, new_list):
        self.lb.delete(0,tk.END)
        self.lb.insert(tk.END, *new_list)

    # configure lb
    def config(self,**kwargs):
        self.lb.config(**kwargs)

    # returns a list of the selection of the lb
    def get_selection(self):
        arr = []
        for index in self.lb.curselection():
            arr.append(self.lb.get(index))
        return arr
    #binds a command to single clicking lb
    def bind(self,func):
        self.lb.bind('<<ListboxSelect>>', func)

class AddExpenseType():
    def __init__(self, parent, wordbank, listbox):
        self.wordbank = wordbank
        self.lb = listbox

        self.parent = parent
        self.surface = tk.Toplevel(self.parent)
        self.surface.title("New Type")
        self.surface.grab_set()

        self.expense_Label = tk.Label(self.surface, text='Operating Expense', padx=5, justify=tk.LEFT)
        self.code_Label = tk.Label(self.surface, text='Expense Code', padx=5, justify=tk.LEFT)

        self.expense_Label.grid(column=0, row=0, sticky='W',pady = 5)
        self.code_Label.grid(column=0, row=1, sticky='W', pady = 5)

        self.expense_Entry = tk.Entry(self.surface)
        self.code_Entry = tk.Entry(self.surface)

        self.expense_Entry.grid(column=1, row=0, sticky='E', pady=5)
        self.code_Entry.grid(column=1, row=1, sticky='E', pady=5)

        self.submit_Button = tk.Button(self.surface, text="Submit Operating Expense", command=self.get_entry_val)
        self.submit_Button.grid(column=0, row=2, columnspan=2, sticky='EW')

    def get_entry_val(self):
        expenseTypeError = False
        expenseCodeError = False
        newOperatingExpense = self.expense_Entry.get()
        newCode = self.code_Entry.get()

        if newOperatingExpense == '' or newCode == '':
            tk.messagebox.showwarning('Error', 'Invalid Entry')
        else:
            allOperatingExpenses = self.wordbank.get_operating_expenses()
            for expenseType in allOperatingExpenses:
                if newOperatingExpense.lower() == expenseType.lower():
                    expenseTypeError = True

            if not newCode.isdigit():
                expenseCodeError = True
            else:
                allCodes = []
                for code in self.wordbank.get_all_codes():
                    allCodes.append(int(code))

                if int(newCode) in allCodes:
                    expenseCodeError = True

        if expenseTypeError is True and expenseCodeError is True:
            messagebox.showwarning('Error', 'Operating Expense and Code Invalid')
        elif expenseTypeError is True:
            messagebox.showwarning('Error', 'Operating Expense Invalid')
        elif expenseCodeError is True:
            messagebox.showwarning('Error', 'Code Invalid')
        else:
            self.wordbank.add_expense_type(newOperatingExpense, newCode)
            self.lb.add_list(self.wordbank.get_operating_expenses())

            #clear entries
            self.expense_Entry.delete(0, tk.END)
            self.code_Entry.delete(0, tk.END)
            self.surface.destroy()
class remove_expense_type:
    def __init__(self, parent, operating_expense, wordbank, listbox):
        self.wordbank = wordbank
        self.parent = parent
        self.listbox = listbox
        self.operating_expense = operating_expense
        self.surface = tk.Toplevel(self.parent)
        self.surface.grab_set()
        self.surface.title('Confirm')

        text = tk.Label(self.surface, text=f'Are You Sure You Want to Delete {operating_expense}?')
        text.grid(column=0, row=0, columnspan=2, sticky='NW', ipady= 8, ipadx=5)

        yes_button = tk.Button(self.surface, text="Yes", padx=5, pady=5, command=self.remove_operating_expense)
        yes_button.grid(column=0, row=1, sticky='EW')

        no_button = tk.Button(self.surface, text="No", padx=5, pady=5, command=self.surface.destroy)
        no_button.grid(column=1, row=1, sticky='EW')

    def remove_operating_expense(self):
        self.wordbank.remove_operating_expense(self.operating_expense)
        self.surface.destroy()
        self.listbox.add_list(self.wordbank.get_operating_expenses())

# add keyword window class
class AddKeyword:
    def __init__(self, parent, wordbank, operating_expense, listbox):
        self.root = tk.Toplevel(parent)
        self.root.title("Add Keyword")
        self.root.grab_set()
        self.operating_expense = operating_expense
        self.wordbank = wordbank
        self.lb = listbox


        small_font = ('Verdana', 15)
        text = tk.Label(self.root, text='Enter New Keyword:', padx=5, pady=10)
        text.grid(row=0, column=0, pady=5, padx=5)

        self.entry = tk.Entry(self.root, font=small_font)
        self.entry.grid(row=1, column=0, pady=5, padx=5)
        self.entry.bind('<Return>', self.add)
        self.entry.focus()

        enter_Button = tk.Button(self.root, text="Submit", pady=8, padx=5, command=self.add)
        enter_Button.grid(row=2, column=0, sticky='EW', pady=5, padx=5)

    def add(self, event):
        new_keyword = self.entry.get()

        if new_keyword != '':
            if self.wordbank.is_keyword(new_keyword):
                messagebox.showwarning('Error', 'Already in wordbank')
            else:
                self.entry.delete(0, tk.END)
                self.wordbank.add_keyword(self.operating_expense, new_keyword)
                newList = self.wordbank.get_word_bank(self.operating_expense)
                self.lb.add_list(newList)
                self.root.destroy()

# class that holds the wordbank view
class WordbankView(tk.Frame):
    def __init__(self, wordbankPath, parent, *args, **kwargs):
        tk.Frame.__init__(self,parent,*args,**kwargs)
        self.wordbank = WordBank(wordbankPath)
        self.parent = parent
        self.statementFilepath = ''

        # ---- Operating Expense Column -----
        operatingExpenses_Label = tk.Label(self, text="Operating Expense", pady=10)
        self.operatingExpense_Listbox = listBox(self)
        addOperatingExpense_Button = tk.Button(self, text="Add Operating Expense", command=self.add_expense_type)
        removeOperating_Expense = tk.Button(self, text="Remove Operating Expense", command=self.remove_expense_type)

        operatingExpenses_Label.grid(column=0, row=0,sticky="EW", padx=5)
        self.operatingExpense_Listbox.grid(column=0, row=1, sticky="NS", padx=5)
        addOperatingExpense_Button.grid(column=0, row=2, sticky="EW", ipady=10, pady=5, padx=5)
        removeOperating_Expense.grid(column=0, row=3, sticky="EW", ipady=10, padx=5)

        self.operatingExpense_Listbox.add_list(self.wordbank.get_operating_expenses())

        # ---- Expense Bank Column ----#
        self.expenseBank_Label = tk.Label(self, text="Expense Bank", pady=10)
        self.expenseBank_Listbox = listBox(self)
        addExpense_Button = tk.Button(self, text="Add Expense Keyword", command=self.add_keyword)
        removeExpense_Button = tk.Button(self, text="Remove Expense Keyword", command=self.remove_keyword)

        self.expenseBank_Label.grid(column=1, row=0, sticky="EW", padx=5)
        self.expenseBank_Listbox.grid(column=1, row=1, sticky="NS", padx=5)
        addExpense_Button.grid(column=1, row=2, sticky="EW", ipady=10, pady=5, padx=5)
        removeExpense_Button.grid(column=1, row=3, sticky="EW", ipady=10, padx=5)

        self.operatingExpense_Listbox.bind(self.populate_keywords)  # bind add_keywords to single click

        # # ---- Undefined Expenses Column ----
        undefinedExpense_Label = tk.Label(self, text="Undefined Expenses", pady=10)
        self.undefinedExpenseBank_Listbox = listBox(self)
        self.fileSelect_Button = tk.Button(self, text="Choose File", command=self.choose_file)
        consolidate_Button = tk.Button(self, text="Consolidate Expenses")
        #
        undefinedExpense_Label.grid(column=2, row=0, sticky="EW", padx=5)
        self.undefinedExpenseBank_Listbox.grid(column=2, row=1, sticky="NS", padx=5)
        self.fileSelect_Button.grid(column=2, row=2, sticky="EW", ipady=10, pady=5, padx=5)
        consolidate_Button.grid(column=2, row=3, sticky="EW", ipady=10, pady=5, padx=5)

# opens window to add an expense type
    def add_expense_type(self):
            addField = AddExpenseType(self,
                                      self.wordbank,
                                      self.operatingExpense_Listbox)
# opens confirmation screen to remove an expense type
    def remove_expense_type(self):
        try:
            operating_expense = self.operatingExpense_Listbox.get_selection()[0]
            remove_field = remove_expense_type(
                self,
                operating_expense,
                self.wordbank,
                self.operatingExpense_Listbox
            )
        except IndexError:
            messagebox.showwarning('Error', 'No Operating Expense Selected')

    def populate_keywords(self, event):
        cur_select = self.operatingExpense_Listbox.get_selection()[0]
        self.expenseBank_Label.config(text=f'Expense Bank - {cur_select}')
        key_dict = self.wordbank.get_word_bank(cur_select)
        self.expenseBank_Listbox.add_list(key_dict)

    def add_keyword(self):
        try:
            operating_expense = self.operatingExpense_Listbox.get_selection()[0]
            add = AddKeyword(self, self.wordbank, operating_expense, self.expenseBank_Listbox)

        except IndexError:
            messagebox.showwarning('Error', 'Nothing is selected')
    def remove_keyword(self):
        try:
            operating_expense = self.operatingExpense_Listbox.get_selection()[0]
            keyword = self.expenseBank_Listbox.get_selection()[0]

            self.wordbank.remove_keyword(operating_expense, keyword)
            self.expenseBank_Listbox.add_list(self.wordbank.get_word_bank(operating_expense))

        except IndexError:
            messagebox.showwarning('Error', 'Nothing is selected')

    def choose_file(self):
        self.statementFilepath = filedialog.askopenfilename(title="Select A CSV Statement",
                                                            filetypes=(("csv files", "*.csv"), ("all files","*.*")))
        if self.statementFilepath != '':
            self.fileSelect_Button.config(text=f'Choose File - {os.path.basename(self.statementFilepath)}')

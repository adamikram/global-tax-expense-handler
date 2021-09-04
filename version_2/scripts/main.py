from operating_expense_window import *
import tkinter as tk
from tkinter import ttk


class MainApplication():
    def __init__(self, word_bank_path):
        self.root = tk.Tk()
        self.root.title("Global Tax Expense Consolidator")
        self.statement = CsvStatement('')
        self.wordBank = WordBank(r'../data/newWordBank.csv')

        notebook = ttk.Notebook(self.root) # window manager
        wordbank_tab = tk.Frame(notebook)
        gfi_tab = tk.Frame(notebook)



        notebook.grid(column=0, row=0, sticky='ne')



        gfi_frame = GfiView(gfi_tab)
        gfi_frame.grid(column=0, row=0, sticky="EW")

        wordbankFrame = WordbankView(wordbank_tab, gfi_frame, self.wordBank, self.statement)

        notebook.add(wordbank_tab, text='Wordbank')
        notebook.add(gfi_tab, text='Generate GFI')

        wordbankFrame.pack()

        self.root.mainloop()



if __name__ == "__main__":
    wordBankPath = r'../data/newWordBank.csv'

    app = MainApplication(wordBankPath)
    pass

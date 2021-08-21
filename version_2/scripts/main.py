from operating_expense_window import *
import tkinter as tk










class MainApplication(WordBank):
    def __init__(self, word_bank_path):
        self.root = tk.Tk()
        WordbankView(word_bank_path, self.root).pack()





        self.root.mainloop()




if __name__ == "__main__":
    wordBankPath = r'../data/newWordBank.csv'

    app = MainApplication(wordBankPath)
    pass

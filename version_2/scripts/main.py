# Title: Tax Consolidator and .gfi generator
# Author: Adam Ikram

# class that takes in a csv file and parses it
import os
import pandas as pd

#parses csv files
class CsvParse:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)

    def get_headings(self):
        return self.df.columns

    def get_column(self,column):
        return self.df[column].tolist()
    def save(self,path):
        pass

class ExpenseType:
    def __init__(self, operating_expense, code, word_bank):
        self.operating_expense = operating_expense
        self.code = code
        self.wordBank = []
        self.expenses = []

    def add_keyword(self, keyword):
        self.wordBank.append(keyword)

    def remove_keyword(self,keyword):
        i = self.wordBank.index(keyword)
        del self.wordBank[i]

class WordBank(CsvParse):
    def __init__(self,path):
        CsvParse.__init__(self,path)
        self.expenseTypes = []
        self.populate_expense_types()

    def populate_expense_types(self):
        for column in self.get_headings():
            arr = self.get_column(column)
            code = arr[0]
            del arr[0]
            newType = ExpenseType(column, code, arr)
            self.expenseTypes.append(newType)





class MainProgram():
    def __init__(self,word_bank_path):
        self.wordBank = WordBank(word_bank_path)
        pass


wordBankPath = r'C:\Users\Ahmed\OneDrive\Desktop\global-tax-expense-handler\version_2\data\newWordBank.csv'


myProgram = MainProgram(wordBankPath)

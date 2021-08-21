# Title: Tax Consolidator and .gfi generator
# Author: Adam Ikram

# class that takes in a csv file and parses it
import os
import pandas as pd

#parses csv files
class CsvParse:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)
        self.df = self.df.fillna('')

    # gets the heading of a data frame
    def get_headings(self):
        return self.df.columns

    # gets the specified column of a data frame without blanks
    def get_column(self,column):
        # arr = self.df[column].fillna('')
        arr = self.df[column].tolist()
        while True:
            try:
                arr.remove('')
            except ValueError:
                break
        return arr
    def save(self,path):
        pass

class ExpenseType:
    def __init__(self, operating_expense, code, word_bank):
        self.operating_expense = operating_expense
        self.code = code
        self.wordBank = word_bank
        self.expenses = []

    def add_keyword(self, keyword):
        self.wordBank.append(keyword)

    def remove_keyword(self,keyword):
        i = self.wordBank.index(keyword)
        del self.wordBank[i]

    def is_code(self,code):
        if int(self.code) == code:
            return True
        else:
            False

    def is_operating_expense(self,operating_expense):
        if operating_expense.lower() == self.operating_expense.lower():
            return True
        else:
            False

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

    def get_operating_expenses(self):
        arr = []
        for expenseType in self.expenseTypes:
            if expenseType.operating_expense != "":
                arr.append(expenseType.operating_expense)
        return arr

    def remove_keyword(self,expenseType, value):
        for TYPE in self.expenseTypes:
            if TYPE.operatingExpense == expenseType:
                TYPE.remove_keyword(value)
                break

    def add_keyword(self,expenseType, value):
        for TYPE in self.expenseTypes:
            if TYPE.operatingExpense == expenseType:
                TYPE.remove_keyword(value)
                break

    def get_word_bank(self,expenseType):
        for TYPE in self.expenseTypes:
            if TYPE.operating_expense == expenseType:
                return TYPE.wordBank

    def get_code(self,expenseType):
        for TYPE in self.expenseTypes:
            if TYPE.operating_expense == expenseType:
                # print(type.code)
                return TYPE.code

    def is_code(self, code):
        for TYPE in self.expenseTypes:
            if TYPE.code == code:
                return True
        return False

    def is_operating_expense(self, operating_expense):
        for TYPE in self.expenseTypes:
            if TYPE.operating_expense == operating_expense:
                return True
        return False


if __name__ == "__main__":
    wordBankPath = r'../data/newWordBank.csv'
    wordbank = WordBank(wordBankPath)


    for expenseType in wordbank.get_operating_expenses():
        print(wordbank.get_word_bank(expenseType))

        pass
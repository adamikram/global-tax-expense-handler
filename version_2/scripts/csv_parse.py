# Title: Tax Consolidator and .gfi generator
# Author: Adam Ikram

# class that takes in a csv file and parses it
import os
import pandas as pd

#parses csv files
class CsvParse:
    def __init__(self, file_path, is_initital=True):
        if is_initital:
            self.parse(file_path)
    def parse(self, file_path):
        self.df = pd.read_csv(file_path)
        self.df = self.df.fillna('')

    # gets the heading of a data frame
    def get_headings(self):
        return self.df.columns

    # gets the specified column of a data frame without blanks
    def get_column(self,column, remove_blanks=True):
        # arr = self.df[column].fillna('')
        arr = self.df[column].tolist()
        if remove_blanks:
            while True:
                try:
                    arr.remove('')
                except ValueError:
                    break
            return arr
        else:
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

    def remove_keyword(self, keyword):
        i = self.wordBank.index(keyword)
        del self.wordBank[i]

    def is_code(self, code):
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
    def __init__(self, path):
        CsvParse.__init__(self, path)
        self.path = path
        self.expenseTypes = []
        self.populate_expense_types()

    def get_expenses(self, operating_expense):
        for oType in self.expenseTypes:
            if oType.operating_expense == operating_expense:
                print(oType.expenses)

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

    def get_all_codes(self):
        arr = []
        for expenseType in self.expenseTypes:
            if expenseType.code != "":
                arr.append(expenseType.code)
        return arr

    def remove_keyword(self, expense_type, value):
        for TYPE in self.expenseTypes:
            if TYPE.operating_expense == expense_type:
                TYPE.remove_keyword(value)
                break

    def add_keyword(self, expense_type, value):
        for TYPE in self.expenseTypes:
            if TYPE.operating_expense == expense_type:
                TYPE.add_keyword(value)
                break

    def get_word_bank(self, expense_type):
        for TYPE in self.expenseTypes:
            if TYPE.operating_expense == expense_type:
                return TYPE.wordBank

    def get_code(self, expense_type):
        for TYPE in self.expenseTypes:
            if TYPE.operating_expense == expense_type:
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

    def add_expense_type(self, operating_expense, code):
        newType = ExpenseType(operating_expense, code, [])
        self.expenseTypes.append(newType)

    def remove_operating_expense(self, operating_expense):
        count = 0
        for TYPE in self.expenseTypes:
            if TYPE.operating_expense == operating_expense:
                break
            count +=1
        del self.expenseTypes[count]

    def is_keyword(self, keyword):
        all_keywords = []

        for operating_expense in self.get_operating_expenses():
            for key in self.get_word_bank(operating_expense):
                all_keywords.append(key.lower())

        if keyword.lower() in all_keywords:
            return True
        else:
            return False


# class that parses statements
class CsvStatement(CsvParse):
    def __init__(self, path):
        CsvParse.__init__(self, path, False)

    def read(self, path):
        self.parse(path)
# file = r"C:\Users\adami\Documents\GitHub\global-tax-expense-handler\version_1\all_data\script_data\sample_statement.csv"
# myStatement = CsvStatement(file)
# print(myStatement.get_headings()[5])
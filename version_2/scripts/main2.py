import pandas as pd

wordbank = r"C:\Users\Ahmed\OneDrive\Desktop\global-tax-expense-handler\version_2\data\newWordBank.csv"
expense_schedule = r"C:\Users\Ahmed\OneDrive\Desktop\global-tax-expense-handler\version_2\data\Expense_Schedule.xlsx"

codesSheet = pd.read_excel(expense_schedule)
# print(codesSheet['Operating Expense'].tolist())
# print(codesSheet['Code'].tolist())

dict = {}

for index, row in codesSheet.iterrows():
    dict[row['Operating Expense']] = [row['Code']]

newdf = pd.DataFrame.from_dict(dict)

newdf.to_csv('newBank.csv',index=False)
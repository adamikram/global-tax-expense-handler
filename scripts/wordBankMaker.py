import csv
import os

expenseTypePath = r"C:\Users\Ahmed\OneDrive\Desktop\expenseTypes.txt"
sampleStatementPdfPath = r"C:\Users\Ahmed\OneDrive\Desktop\sample_statement.csv"
scriptsPath = r"C:\Users\Ahmed\OneDrive\Desktop\scripts"
# csvToRead = r"C:\Users\Ahmed\OneDrive\Desktop\scripts\expenseTypes_backup.csv")
csvToRead = r"C:\Users\Ahmed\OneDrive\Desktop\scripts\newCSV.csv"
allExpensesWords = r"C:\Users\Ahmed\OneDrive\Desktop\manged_cvs\managed.csv"

class expense_maker:
	def __init__(self):
		self.numOfExpenseType = 0
		self.expenseDict = {}
	def addExpenseType(self,type):
		self.expenseDict[type] = []
	def addExpense(self,type,expense):
		if expense != '':
			self.expenseDict[type].append(expense)
	def listExpenseTypes(self):
		expenseTypes = []
		for x in self.expenseDict.keys():
			expenseTypes.append(x)
		return expenseTypes
	def listAllExpenses(self):
		for expenseTypes in self.expenseDict.keys():
			print(f'{expenseTypes} : {self.expenseDict[expenseTypes]}')
	def clearDict(self):
		self.expenseDict.clear()
	def saveToFile(self,newFilePath,fileName):
		largestLen = self.largestExpenseList()
		fList = []
		firstRow = self.listExpenseTypes()
		fList.append(firstRow)
		
		for lineNum in range(largestLen):
			# print(lineNum+1)
			row = []

			for expenseType in fList[0]:
				# print(expenseType)
				if lineNum+1 <= len(self.expenseDict[expenseType]):
					row.append(self.expenseDict[expenseType][lineNum])
				else:
					row.append('')
			fList.append(row)

		for x in fList:
			pass
			# print(x)
		# flist.append(", ".join, self.expenseDict.keys())

		with open(os.path.join(newFilePath,fileName),"w+") as text_file:
			for line in fList:
				lineText = ', '.join(line)
				text_file.write(f'{lineText}\n')
			pass

	def readFile(self,path):
		self.clearDict()
		with open(path,mode='r') as csv_file:
			csv_reader = csv.reader(csv_file,delimiter=',')
			line_count = 0

			expenseTypesX  = []
			column = 0
			for row in csv_reader:
				if line_count == 0:
					for cell in row:
						self.addExpenseType(cell)
						expenseTypesX.append(cell)
				else:
					for expenseType in self.listExpenseTypes():
						
						self.addExpense(expenseType,row[column])						
						column += 1
					column = 0

				line_count+=1

	def largestExpenseList(self):
		largestListLen = 0
		for expenseType in self.expenseDict.keys():
			if len(self.expenseDict[expenseType]) > largestListLen:
				largestListLen = len(self.expenseDict[expenseType])
		return largestListLen

	def inputCatagoryColumnToCsv(self,catagoryList,path):		
		with open()
	def getCatagorylist(self,path,newStatementPath,newStatementName):		
		with open(path,mode='r') as csv_file:
			csv_reader = csv.reader(csv_file,delimiter=',')

			line_count = 0
			expenseTypeList = []
			payeeColumn = 0

			for row in csv_reader:
				if line_count == 0:
					payeeColumn= row.index("Payee" or "payee")
					line_count+=1
				else:
					# print(row[payeeColumn])
					exp = self.isValueInDict(row[payeeColumn].lower())
					print(f'{row[payeeColumn]} is {exp}')
					if exp != False:
						expenseTypeList.append(exp)
						# print(f'{row[payeeColumn]} is {exp}')
					else:
						expenseTypeList.append("Undefined")
		inputCatagoryColumnToCsv(expenseTypeList,os.path.join(newStatementPath,newStatementName))

	def isValueInDict(self,value):
		for key in self.expenseDict.keys():
			for expense in self.expenseDict[key]:
				if expense.lower() in value.lower():
					return key
		return False

		# for key in self.expenseDict.keys():
		# 	if value.lower() in self.expenseDict[key]:
		# 		return key
		# return False

def csv_ColumnRead(path,columnNum):
    lineArr = []
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:
            lineArr.append(row[columnNum])

        csv_file.close()
    return lineArr
def writeListToCsv(arr,xpath,name):
    with open(os.path.join(xpath,name),"w+") as text_file:
        for line in arr:
            lineText = ', '.join(line)
            text_file.write(f'{lineText}\n')
        pass

def csv_RowRead(path,rowNum):
	lineArr = []
	count = 0
	with open(path) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')

		for row in csv_reader:
			if count == rowNum:
				lineArr.append(row)
				break
			count +=1

		csv_file.close()
	return lineArr
expenses = expense_maker()
# for expenseType in csv_ColumnRead(expenseTypePath,0):
# 	expenses.addExpenseType(expenseType)


expenses.readFile(csvToRead) 

# expenses.getCatagorylist(sampleStatementPdfPath)
expenses.getCatagorylist(sampleStatementPdfPath,)












# expenses.listAllExpenses()
# print(expenses.isValueInDict('global tax'))

# expList = []
# for x in csv_ColumnRead(allExpensesWords,0):
# 	expList.append(x)
# count = 0
# while True:
# 	print(f'expense is {expList[count]}. ')
# 	count+=1
# 	userInput =  input("Input Expense Type and Expense seperated by a comma: ")
	
# 	if userInput != "":
#             userInput.split(", ")
	
# 	if userInput== "":
# 		print("passed")
# 	elif userInput[0] == "exit":
# 		break
# 	else:
# 		expenses.addExpense(userInput[0],userInput[1])

# 	# try:
# 	# 	expenses.addExpense(userInput[0],userInput[1])
# 	# except:
# 	# 	print("something went wrong")



# expenses.saveToFile(scriptsPhath,"newCSV.csv")

# expenses.listAllExpenses()
# print(expenses.largestExpenseList())

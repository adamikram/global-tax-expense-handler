from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
import csv

csv_wordbank = r"C:\Users\adami\Documents\GitHub\global-tax-expense-handler\version_2\data\savedCSVWordbank.csv"
script_data_path = r'C:\Users\Ahmed\OneDrive\Desktop\global-tax-expense-handler\all_data\script_data'
myTxtFile = r"C:\Users\Ahmed\OneDrive\Desktop\global-tax-expense-handler\all_data\script_data\managed.csv"

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
				lineText = ','.join(line)
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
						if not row[column].isspace():
							self.addExpense(expenseType,row[column])						
						column += 1
					column = 0
				line_count+= 1

	def largestExpenseList(self):
		largestListLen = 0
		for expenseType in self.expenseDict.keys():
			if len(self.expenseDict[expenseType]) > largestListLen:
				largestListLen = len(self.expenseDict[expenseType])
		return largestListLen

	def inputCatagoryColumnToCsv(self,column,statementPath,newPath):
		fileRowList = []
		with open(statementPath,'r') as csv_input:
			csv_reader_input = csv.reader(csv_input,delimiter=',')
			count = 0
			# print(column)
			for row in csv_reader_input:
				row.append(column[count])
				fileRowList.append(row)
				count +=1
		with open(newPath,'w') as csv_output:
			for row in fileRowList:
				csv_output.write(f"{','.join(row)}\n")

	def getCatagorylist(self,path,newStatementPath,newStatementName):		
		with open(path,mode='r') as csv_file:
			csv_reader = csv.reader(csv_file,delimiter=',')

			line_count = 0
			expenseTypeList = ['Expense Type']
			payeeColumn = 0
			undefinedExpenses = []

			for row in csv_reader:
				if line_count == 0:
					payeeColumn= row.index("Payee" or "payee")
					line_count+=1
				else:
					# print(row[payeeColumn])
					exp = self.isDictInValue(row[payeeColumn].lower())
					# print(f'{row[payeeColumn]} is {exp}')
					if exp != False:
						expenseTypeList.append(exp)
					else:
						expenseTypeList.append("Undefined")
						undefinedExpenses.append(row[payeeColumn])

		self.inputCatagoryColumnToCsv(expenseTypeList,path,os.path.join(newStatementPath,newStatementName))
		return undefinedExpenses
	def isDictInValue(self,value):
		for key in self.expenseDict.keys():
			for expense in self.expenseDict[key]:
				if expense.lower() in value.lower():
					return key
		return False

	def isValueInDict(self,value):
		for key in self.expenseDict.keys():
			for expense in self.expenseDict[key]:
				if expense.lower() == value.lower():
					return True
		return False
class expenseListbox():
	def __init__(self,surface):
		self.my_frame = Frame(surface) #underlying frame
		self.my_scrollbar = Scrollbar(self.my_frame,orient=VERTICAL) #scrollbar
		self.my_listbox = Listbox(self.my_frame,yscrollcomman=self.my_scrollbar,height=50,width=50,exportselection=False) #listbox
		self.my_scrollbar.config(command=self.my_listbox.yview)
		self.currentlySelected = ''
	def render(self):
		self.my_scrollbar.pack(side=RIGHT,fill=Y)
		self.my_frame.pack()
		self.my_listbox.pack()

	def addList(self,myList):
		for item in myList:
			self.my_listbox.insert(END,item)
	def bind(self,func):
		self.my_listbox.bind('<<ListboxSelect>>', func)
	def clear(self):
		self.my_listbox.delete(0,END)
	def getSelection(self):
		value = self.my_listbox.curselection()[0]
		return self.my_listbox.get(value)

#function for updating second listbox
def updateSecondLb(event):
	expensesListBox.clear()
	key = expenseTypeListBox.getSelection()
	expensesListBox.addList(myExpenses.expenseDict[key])
	expensesLabel.config(text=key)
	expenseTypeListBox.currentlySelected = key

def addExpenseType():
	newKey = expenseType_entry.get()
	
	if newKey in myExpenses.expenseDict.keys():
		messagebox.showinfo("Error","Type already in system")
	elif newKey != '' and newKey not in myExpenses.expenseDict.keys():
		myExpenses.addExpenseType(newKey)
		expenseTypeListBox.clear()
		expenseTypeListBox.addList(myExpenses.listExpenseTypes())
		expenseType_entry.delete(0,END)

		
def deleteExpenseType():
	keyToDelete = expenseTypeListBox.getSelection()
	if keyToDelete in myExpenses.listExpenseTypes():
		del myExpenses.expenseDict[keyToDelete]

	expensesListBox.clear()
	expenseTypeListBox.clear()
	expenseTypeListBox.addList(myExpenses.listExpenseTypes())

def addExpense_listbox():
	newExpense = expense_entry.get()
	try:
		curExpenseType = expenseTypeListBox.getSelection()
		print(curExpenseType)
		
		if myExpenses.isValueInDict(newExpense):
			messagebox.showinfo("Error","Value already in system")
		elif newExpense != '':
			myExpenses.addExpense(curExpenseType,newExpense)
		

		expensesListBox.clear()
		expensesListBox.addList(myExpenses.expenseDict[curExpenseType])
		expense_entry.delete(0,END)
	except IndexError:
		messagebox.showinfo("Error","Please Select an Expense Type")
	
	expense_entry.delete(0,END)

def deleteExpense():
	selection = expensesListBox.my_listbox.curselection()
	count = 0
	if selection:
		# print(expensesListBox.getSelection())
		for x in myExpenses.expenseDict[expenseTypeListBox.currentlySelected]:
			if x == expensesListBox.getSelection():
				del myExpenses.expenseDict[expenseTypeListBox.currentlySelected][count]
				# print(myExpenses.expenseDict[expenseTypeListBox.currentlySelected][x])
				break
			count+=1
	expensesListBox.my_listbox.delete(count)


def save():
	myExpenses.saveToFile(script_data_path,'savedCSVWordbank.csv')

def csv_ColumnRead(path,columnNum):
    lineArr = []
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:
            lineArr.append(row[columnNum])

        csv_file.close()
    return lineArr

myExpenses = expense_maker()
myExpenses.readFile(csv_wordbank)


root = Tk()
root.title('ListBox Class')
# root.geometry("400x400")



#expense types frame
expenseTypeFrame = Frame(root)
expenseTypeFrame.pack(side=LEFT)

#label for expense types
expenseTypeLabel = Label(expenseTypeFrame,text="Expense Types")
expenseTypeLabel.pack(side=TOP)

# button to delete a expense type
deleteExpenseType_button = Button(expenseTypeFrame,text='Delete Expense Type',command=deleteExpenseType)
deleteExpenseType_button.pack(side=BOTTOM)

#add expense type button
addExpenseType_button = Button(expenseTypeFrame,text='Add Expense Type',command=addExpenseType)
addExpenseType_button.pack(side=BOTTOM)

#entry to input expense type
expenseType_entry = Entry(expenseTypeFrame)
expenseType_entry.pack(side=BOTTOM)

#listbox for expense types
expenseTypeListBox = expenseListbox(expenseTypeFrame)
expenseTypeListBox.render()
expenseTypeListBox.addList(myExpenses.expenseDict.keys())



# #frame for unsorted expense list
# unsortedExpenseFrame = Frame(root)
# unsortedExpenseFrame.pack(side=LEFT)

# #label for unsorted expenseList
# unsortedExpenseLabel = Label(unsortedExpenseFrame,text='Unsorted List')
# unsortedExpenseLabel.pack(side=TOP)

# #unsorted listbox
# unsortedListbox = expenseListbox(unsortedExpenseFrame)
# unsortedListbox.render()
# unsortedListbox.addList(csv_ColumnRead(myTxtFile,0))




#frame for expenses
expensesFrame = Frame(root)
expensesFrame.pack(side=LEFT)

#expenses label
expensesLabel = Label(expensesFrame,text="Expenses")
expensesLabel.pack(side=TOP)
#expenses lb
expensesListBox = expenseListbox(expensesFrame)
expensesListBox.render()	
expenseTypeListBox.bind(updateSecondLb)

#save button
save_button = Button(expensesFrame,text='Save Word Bank',command=save)
save_button.pack(side=BOTTOM)

#delete expense button
delete_expense_button = Button(expensesFrame, text='Delete Expense', command=deleteExpense)
delete_expense_button.pack(side=BOTTOM)

#add expense button
add_expense = Button(expensesFrame,text='Add Expense',command=addExpense_listbox)
add_expense.pack(side=BOTTOM)

#entry to enter in
expense_entry = Entry(expensesFrame)
expense_entry.pack(side=BOTTOM)

#Undefined List
undefinedFrame = Frame(root)
undefinedFrame.pack(side = LEFT)

#label
undefinedLabel = Label(undefinedFrame,text="Undefined Expenses")
undefinedLabel.pack(side=TOP)

#undefined expenses listbox
undefinedListbox = expenseListbox(undefinedFrame)
undefinedListbox.render()





#function that handles choosing a file
root.filename=''
def chooseFile(label):
	root.filename = filedialog.askopenfilename(initialdir="../all_data/script_data",title="Select A CSV Statement",filetypes=(("csv files", "*.csv"),("all files","*.*")))
	print(root.filename)
	label.config(text = f'File to sort is:{root.filename}')

#choose statement csv to analyse
selectedFile = ''
fileLabel = Label(undefinedFrame,text='File to sort is: ')
statementFileChooser = Button(undefinedFrame,text='Choose File',command=lambda:chooseFile(fileLabel))
statementFileChooser.pack(side = BOTTOM)

#show which file is selected
fileLabel.pack(side=BOTTOM)


def addExpenseTypeColumn(file,label,listbox,expenses):
	if file != '':
		base = os.path.basename(file)
		base = base.split(".")[0]
		base = f'{base}_sorted.csv'
		undefinedExpenses = myExpenses.getCatagorylist(file,script_data_path,base)
		listbox.clear()
		listbox.add_list(undefinedExpenses)

		label.config(text='Sorted! Open in Excel to Create a Pivot Table',fg='green')
	else:
		messagebox.showinfo("Error", "Please Select A Valid CSV File")



#button  to analyse
sortButton = Button(undefinedFrame,text="Add Expense Type Column",command= lambda:addExpenseTypeColumn(root.filename,fileLabel,undefinedListbox,myExpenses))
sortButton.pack(side=BOTTOM)
root.mainloop()
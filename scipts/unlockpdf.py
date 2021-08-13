import PyPDF2
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


class button:
    def __init__(self, *args, **kwargs):
        self.myButton = tk.Button(*args, **kwargs)

    def render(self, **kwargs):
        self.myButton.grid(**kwargs)

    def configure(self, **kwargs):
        self.myButton.configure(**kwargs)

class pdfUnlocker():
    def __init__(self, pdfList='', dirPath=''):

        self.pdfList = pdfList
        self.dirPath = dirPath
        self.isData = False

    def addFileList(self, fileList):
        self.pdfList = fileList

    def addDir(self,dirPath):
        self.dirPath = dirPath

    def dataCheck(self):
        if self.pdfList == '' or self.dirPath == '':
            self.isData = False
            return False
        else:
            self.isData = True
            return True

    def pdfUnlock(self):
        if self.dataCheck() == True:
            fileList = self.pdfList
            newDir = self.dirPath

            blank_page = r'..\data\blank.pdf'
            # Open the files that have to be merged one by one

            for file in fileList:
                pdf1File = open(file, 'rb')
                blankPageFile = open(blank_page, 'rb')

                # Read the files that you have opened
                pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
                pdf2Reader = PyPDF2.PdfFileReader(blankPageFile)

                # Create a new PdfFileWriter object which represents a blank PDF document
                pdfWriter = PyPDF2.PdfFileWriter()

                # Loop through all the pagenumbers for the first document
                for pageNum in range(pdf1Reader.numPages):
                    pageObj = pdf1Reader.getPage(pageNum)
                    pdfWriter.addPage(pageObj)

                # Loop through all the pagenumbers for the second document
                for pageNum in range(pdf2Reader.numPages):
                    pageObj = pdf2Reader.getPage(pageNum)
                    pdfWriter.addPage(pageObj)

                # Now that you have copied all the pages in both the documents, write them into the a new document
                newPath = os.path.join(newDir,f'unlocked_{os.path.basename(file)}')
                pdfOutputFile = open(newPath, 'wb')
                pdfWriter.write(pdfOutputFile)
                print(f'Writing {newPath}')
                # Close all the files - Created as well as opened
                pdfOutputFile.close()
                pdf1File.close()
                blankPageFile.close()

class mainProgram(pdfUnlocker):
    def __init__(self, *args, **kwargs):
        self.root = tk.Tk()
        self.root.title('Unlock PDF')
        pdfUnlocker.__init__(self)

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)

        unlockButton = button(self.root, text='Unlock PDF', height=3, padx=50, state=tk.DISABLED,command=lambda:self.pdfUnlock())
        unlockButton.render(column=0, row=0, sticky="nwse", pady=10, padx=10)

        fileSelectButton = button(self.root, text='Choose PDF Files', height=3, padx=50,
                                  command=lambda: self.getFile("file", fileSelectButton, "Choose PDF Files",unlockButton))
        fileSelectButton.render(column=0, row=1, sticky="nwse", ipady=10, padx=10)

        destinationSelectionButton = button(self.root, text='Choose Destination',
                                            command=lambda: self.getFile("directory", destinationSelectionButton,"Choose Destination",unlockButton), height=3, padx=50)
        destinationSelectionButton.render(column=0, row=2, sticky="nwse", pady=10, padx=10)

        self.root.mainloop()



    def getFile(self, type, button, message,lockButton):
        if type == "directory":
            path_selected = filedialog.askdirectory(title="Select A Folder")
            button.configure(text=f"{message}\n{path_selected}")
            self.dirPath = path_selected
            # if self.dataCheck():
            #     self.lockButton(lockButton,True)
            # else:
            #     self.lockButton(lockButton,False)
        else:
            fileIsValid = True
            paths = filedialog.askopenfilenames(title="Select A File",filetypes=(("pdf files", "*.pdf"), ("all files", "*.*")))
            for file in paths:
                if not file.endswith('.pdf'):
                    tk.messagebox.showerror("Error", "Please Select PDF File(s) Only!")
                    fileIsValid = False
                    break
                else:
                    message += f'\n {file}'
                    self.pdfList = paths
            button.configure(text=message)
        print(f'The Folder is {self.dirPath} and the files are {self.pdfList}')
        print(self.dataCheck())
        if self.dataCheck():
            lockButton.configure(state=tk.NORMAL)
        else:
            lockButton.configure(state=tk.DISABLED)

myProgram = mainProgram()

#
# directory = r'C:\Users\Ahmed\OneDrive\Desktop\saud_statements\statements_pdf'
# newDir = r'C:\Users\Ahmed\OneDrive\Desktop\saud_statements\pdf_unlocked'
#
# blank_page = r"C:\Users\Ahmed\OneDrive\Desktop\saud_statements\blank-pages-deleted.pdf"
#
# # Open the files that have to be merged one by one
#
# def unlockPdf(lockedDir, lockedName,blankPath):
#     pdf1File = open(os.path.join(lockedDir,lockedName), 'rb')
#     blankPageFile = open(blankPath, 'rb')
#
#     # Read the files that you have opened
#     pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
#     pdf2Reader = PyPDF2.PdfFileReader(blankPageFile)
#
#     # Create a new PdfFileWriter object which represents a blank PDF document
#     pdfWriter = PyPDF2.PdfFileWriter()
#
#     # Loop through all the pagenumbers for the first document
#     for pageNum in range(pdf1Reader.numPages):
#         pageObj = pdf1Reader.getPage(pageNum)
#         pdfWriter.addPage(pageObj)
#
#     # Loop through all the pagenumbers for the second document
#     for pageNum in range(pdf2Reader.numPages):
#         pageObj = pdf2Reader.getPage(pageNum)
#         pdfWriter.addPage(pageObj)
#
#     # Now that you have copied all the pages in both the documents, write them into the a new document
#     pdfOutputFile = open(f'unlocked_{lockedName}', 'wb')
#     pdfWriter.write(pdfOutputFile)
#
#     # Close all the files - Created as well as opened
#     pdfOutputFile.close()
#     pdf1File.close()
#     blankPageFile.close()
#
#
# for file in os.listdir(directory):
#     unlockPdf(directory,file,blank_page)
#     print(f'{file} unlocked')
#
#

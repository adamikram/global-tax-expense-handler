import PyPDF2
import os

directory = r'C:\Users\Ahmed\OneDrive\Desktop\saud_statements\statements_pdf'
newDir = r'C:\Users\Ahmed\OneDrive\Desktop\saud_statements\pdf_unlocked'

blank_page = r"C:\Users\Ahmed\OneDrive\Desktop\saud_statements\blank-pages-deleted.pdf"

# Open the files that have to be merged one by one

def unlockPdf(lockedDir, lockedName,blankPath):
    pdf1File = open(os.path.join(lockedDir,lockedName), 'rb')
    blankPageFile = open(blankPath, 'rb')

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
    pdfOutputFile = open(f'unlocked_{lockedName}', 'wb')
    pdfWriter.write(pdfOutputFile)

    # Close all the files - Created as well as opened
    pdfOutputFile.close()
    pdf1File.close()
    blankPageFile.close()


for file in os.listdir(directory):
    unlockPdf(directory,file,blank_page)
    print(f'{file} unlocked')
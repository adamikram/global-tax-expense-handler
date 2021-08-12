import os
from PyPDF2 import PdfFileMerger, PdfFileReader

pdfDirectory = r'C:\Users\Samra\Desktop\testDir'
newFolder = r'C:\Users\Samra\Desktop\testMerged'


#merge file function
#takes input directory and name of merged file
def mergeFiles(directory,mergedFileName):
    newFileList = []
    pdfMerge = PdfFileMerger() #make pdf object

    print(f"Merging {directory} directory")
    
    #iterate through files in dir
    for file in os.listdir(pdfDirectory):
        print(file)
        if file.endswith('.pdf'):
            pdfMerge.append(PdfFileReader(os.path.join(directory,file)))
            print(f"merged {file}")
    
    #saving file
    print(f"Saving File as {mergedFileName}")
    pdfMerge.write(os.path.join(newFolder,mergedFileName))
    pdfMerge = PdfFileMerger()
    print(f"Saved as {mergedFileName}")




#iterate through a folder that contains folders that
#contain pdfs (merges files independantly)
##def mergeFolder(directory):
##    for folder in os.listdir(directory): #iterate through directory
##        print(folder) 
##        newDir = os.path.join(directory,folder) #join orginal path with foldername to get new path
##        print(newDir)
##        mergeFiles(newDir,os.path.join(newDir,f'{folder}.pdf')) #save the file in it's parent folder
##    

paths = []
def getPaths(directory):
    paths = []
    for folder in os.listdir(pdfDirectory):
        paths.append(os.path.join(directory,folder))
        
    return paths

paths = getPaths(pdfDirectory)

for i in paths:
    mergeFiles(i,os.path.join(i,r'merged.pdf'))

##for i in paths
##mergeFolder(pdfDirectory)
##mergeFiles(pdfDirectory,'merged.pdf')


from PyPDF2 import PdfFileMerger,PdfFileReader
import os

inputPath = r'C:\Users\Samra\Desktop\statements'
outputPath = r'C:\Users\Samra\Desktop\testMerged'


def mergeFiles(inputPath,outputPath,name,folder):
    merger = PdfFileMerger()
    for file in os.listdir(inputPath):
        print(f"merging {file} in {folder}")
        merger.append(PdfFileReader(os.path.join(inputPath,file)))
        
    merger.write(os.path.join(outputPath,name))

def mergeFiles_Folder(inputPath,outputPath):
    for folder in os.listdir(inputPath):
        subFolderPath = os.path.join(inputPath,folder)
        fileName = f'{folder}_merged.pdf'
        mergeFiles(subFolderPath,outputPath,fileName,folder)
        
mergeFiles_Folder(inputPath,outputPath)
    


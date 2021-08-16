import csv
import os

# path = r'C:\Users\Ahmed\OneDrive\Desktop\csv\csv\2019_merged.csv')
csvFolder = r'C:\Users\Ahmed\OneDrive\Desktop\manged_cvs'
# with open(path) as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             # print(f'Column names are {", ".join(row)}')

#             line_count += 1
#         else:
#             # print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[5]}.')
#             for i in range(5):
#                 print(row[i])
#             line_count += 1
#             break
#     print(f'Processed {line_count} lines.')

def getCsvLineList(path):
    lineArr = []
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:
            lineArr.append(row)

        csv_file.close()
    return lineArr


def appendLineList(master,toAppend):
    for row in toAppend:
        master.append(row)
    return master
def getPaths(filePath):
    pathList = []
    for filename in os.listdir(filePath):
        pathList.append(os.path.join(filePath,filename))
    return pathList

def join_csv_files(folderPaths):
    master = []

    
    for path in folderPaths:
        master= appendLineList(master,getCsvLineList(path))

    return master


def writeListToCsv(arr,xpath,name):
    with open(os.path.join(xpath,name),"w+") as text_file:
        for line in arr:
            lineText = ', '.join(line)
            text_file.write(f'{lineText}\n')
        pass


    # csv_merged_file = open(os.path.join(folderPath,name),"w")
    


    # csv_merged_file = open(os.path.join(xpath,name),'a')
    # csv_merged_file.close()

    # csv_merged_file.open(os.path.join(xpath,name),"w")

    # for line in arr:
    #     csv_merged_file.write(line)

    # csv_merged_file.close()



#make new directory:
# csv_merged_file = open(os.path.join(csvFolder,r'csv_merged.csv'),"x")



masterPathList = getPaths(csvFolder)
masterLineArr = []
masterLineArr = join_csv_files(masterPathList)

writeListToCsv(masterLineArr,csvFolder,r'managed.csv')
# print(getPaths(csvFolder))
# print(masterPathList)

# print(masterLineArr)
# print(masterLineArr)
# print(getCsvLineList(path)[0][5])

import pymongo 
import os
import pandas as pd
import numpy as np


connectionString = "mongodb+srv://adamikram:adamikram@expense-handler.i30se.mongodb.net/global-tax-database?retryWrites=true&w=majority"
wordbankfilename = 'newWordBank.csv'

client = pymongo.MongoClient(connectionString)  
for db in client.list_databases():  
    print(db['name'])  
    

db = client['expense_handler']
print(db.list_collection_names())
# sampledoc = [{"_id":"hello"},{"_id":"ayyo"}]

col = db['expense-handler']




# col.insert_many(sampledoc)

# with open('newWordBank.csv','r') as infile:
# 	for line in infile:
# 		print(line)
# df = pd.read_csv('newWordBank.csv')

# df.replace(np.nan,0)

# wordbankdict = []
# for bruh in df.columns:
	

# 	df[bruh] = df[bruh].replace(np.nan, 0)
# 	raw_list = df[bruh].tolist()

# 	code = df[bruh].tolist()[0]
# 	expense_type = bruh

# 	del raw_list[0]


# 	cleanedKeywords = []



# 	for key in raw_list:
# 		if key != 0:
# 			cleanedKeywords.append(key)

# 	wordbankdict.append({'_id':int(code),
# 						 'operating_expense': expense_type,
# 						 'wordbank':cleanedKeywords			
# 						})


# col.insert_many(wordbankdict)
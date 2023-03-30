#!/usr/bin/env python
# coding: utf-8

# In[40]:


import os,shutil

path = "E:/testingPath/"

file_name = os.listdir(path)

folders_names = ['powerBI_files','png_files','excel_files','pdf_files','csv_files']

for folder in folders_names:
    try:     
        if not os.path.exists(path+folder):
            os.makedirs(path+folder)
            print('files created')
        else:
             os.makedirs(path+folder)
    except:
          print ('something missing')
            
for file in file_name:
    if ".csv" in file and not os.path.exists(path + "csv_files/" + file):
        shutil.move(path + file, path + "csv_files/" + file)
    elif ".xlsx" in file and not os.path.exists(path + "excel_files/" + file):
        shutil.move(path + file, path + "excel_files/" + file)    
    elif ".pdf" in file and not os.path.exists(path + "pdf_files/" + file):
        shutil.move(path + file, path + "pdf_files/" + file)   
    elif ".pbix" in file and not os.path.exists(path + "powerBI_files/" + file):
        shutil.move(path + file, path + "powerBI_files/" + file) 
    elif ".png" in file and not os.path.exists(path + "png_files/" + file):
        shutil.move(path + file, path + "png_files/" + file)                 
            


# In[ ]:





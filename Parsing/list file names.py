import os
# change directory
os.chdir("Folder Path")
#File name like Monday-log-#1.txt in to the folser
for f in os.listdir():
    #split file name and extention
    file_name, file_ext =os.path.splitext(f)
    #split "-" to file name
    print(file_name.split())
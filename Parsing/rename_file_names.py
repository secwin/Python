# !! Important folder only contains file !!
#--> files name like Monday - log - #1.txt, Tuesday-log-#2.txt, z-b-1.py etc.
import os
# change directory
os.chdir("Folder Path")
#File name like Monday-log-#1.txt in to the folser
for f in os.listdir():
    #split file name and extention
    file_name, file_ext =os.path.splitext(f)

    f_date, f_type, f_num = file_name.split("-") #-->split file name with - each word

    f_num = f_num.strip() #--> remove whitespace
    #f_num = f_num.strip()[1:]#--> remove #
    f_num = f_num.strip()[1:].zfill(2)#--> remove # and add zero insted #

    #"{}-{}{}".format--> represent file format
    new_name = "{}-{}{}".format(f_num,f_date,file_ext)
    os.rename(f, new_name)  #rename files

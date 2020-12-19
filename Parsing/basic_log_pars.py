log=open("File Path")
lines=log.readlines()
for line in lines :
    #Pars log ->if each veraible split with space->Example Date is 3rd in the log from left to right: 01:08:39
    #pars second
    print(line.split()[3].split(":")[2])
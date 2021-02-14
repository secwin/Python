import wmi
import re
c = wmi.WMI ()

for process in c.Win32_Process ():

        print (process.ProcessId, process.Name, process.executablepath)
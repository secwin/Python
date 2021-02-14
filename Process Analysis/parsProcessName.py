import wmi
c = wmi.WMI ()
for process in c.Win32_Process ():
        if any(procstr in str(process.Name) for procstr in\
            ['Calculator','powershell']):
            print(process.Name)


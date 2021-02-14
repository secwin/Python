import wmi
check = 0
processes = wmi.WMI()
for process in processes.Win32_Process():
    if any(name in str(process.Name) for name in \
           ['Calculator', 'shell']):
        process.Terminate()
        check += 1
if check == 0:
    print("Not found!")

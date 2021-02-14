import re
import collections

logfile = open("!!Path of File", "r")
IP=[]
for line in logfile:

            ip = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
            if ip != None:
                IP.append(ip.group())

counter = collections.Counter(IP)
for count in counter.most_common(10):
    print(str(count[0]) + " number of request => " + str(count[1]) )

logfile.close()
import collections
logfile = open("!!Path of File!!", "r")
url=[]
for line in logfile:
    try:
        url.append(line[line.index("GET" or "POST")+4:line.index("HTTP/1.1")])
    except:
        pass
counter = collections.Counter(url)
for count in counter.most_common(10):
    print(str(count[0]) + "  number of request=> " + str(count[1]) )

logfile.close()
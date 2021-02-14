import re
from collections import Counter

reg200 = r'HTTP/1.\d" (200)'
reg404 = r'HTTP/1.\d" (404)'
with open("!!Path of File!!") as f:
        log = f.read()
        response404 = re.findall(reg404,log)
        status404 = Counter(response404)
        response200 = re.findall(reg200, log)
        status200 = Counter(response200)
        for a,b in status200.items():
            str(b)
        for c,d in status404.items():
            str(d)

        print("Percentage of successful requests =>", (b*100)/(b+d))


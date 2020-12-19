import requests
import json
import sched, time
#get data
data = {
    'query': 'get_recent',
    'selector': '100'
}

def run():
    #import json data
    response = requests.post('https://mb-api.abuse.ch/api/v1/', data=data)

    malwares = json.loads(response.content.decode("utf-8", "ignore"))


    for m in malwares["data"]:
        with open("E:\python\malware_name_hash.txt", "a+",encoding='utf-8', errors="ignore") as mn:
            mn.write(str(m['file_name'] +"  :  "+ m["md5_hash"]) + "\n")
            mn.close()
    #wait 60 sec
    time.sleep(60)
#execute code again
while True:
    run()

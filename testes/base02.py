import os

response = os.popen("nmap 10.240.13.5 -p 22,2225,2522 | grep open")
response = response.read().split(":")[0]
print("A porta SSH É: ", response)

import os
hostname = "10.240.76.139" #example
response = os.popen("snmpget -v2c -c'mk_Onl!ne' " + hostname + " 1.0.8802.1.1.2.1.3.4.0 ")
response1 = response.read().split(":")[1]

#response = os.system("snmpget -v2c -c'mk_Onl!ne' " + hostname + " 1.0.8802.1.1.2.1.3.4.0 ")


#and then check the response...
#print("response é: ", response)
print("response1 é: ", response1)

#print("a oid é: ", response)


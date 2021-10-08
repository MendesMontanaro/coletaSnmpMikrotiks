import os
hostname = "10.240.76.139" #example
response = os.system("snmpwalk -v2c -c'mk_Onl!ne' " + hostname + " 1.0.8802.1.1.2.1.3.4.0 ")


#and then check the response...
print(response)
print("a oid é: ", response)


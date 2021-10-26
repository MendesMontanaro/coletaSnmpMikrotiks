import os
import signal

iplist = []


def colect_list():
    with open("data/ips.txt", "r") as ip_temp:
        for row03 in ip_temp:
            iplist.append(row03.replace("\n", ""))


colect_list()

iplength = len(iplist)


def coleta():
    for line in range(0, iplength):
        signal.alarm(60)

        try:

            print("oi")
            print("Iniciando coleta no ip: " + iplist[line])

            response = os.system("snmpwalk -v2c -c'm_Onl!ne' " + iplist[line] + " 1.0.8802.1.1.2.1.3.4.0 ")
            response = response.read().split(":")[1]
            print(response)
            pass

        finally:
            signal.alarm(0)


coleta()

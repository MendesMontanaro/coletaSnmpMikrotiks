import signal
import logging
import os

logging.basicConfig(filename='logs.log', level=logging.DEBUG)

class TimeoutException(Exception):
    pass


def timeout_handler(signum, frame):
    raise TimeoutException

iplist = []
timelist = []

def colect_list():
    with open("data/ips.txt", "r") as ip_temp:
        for row03 in ip_temp:
            iplist.append(row03.replace("\n", ""))


colect_list()

iplength = len(iplist)

def config_mass():
    for line in range(0, iplength):
        signal.alarm(60)

        try:

            comment = "Iniciando coleta SNMP no equipamento: " + iplist[line]
            print(comment)

            response = os.popen("snmpget -v2c -c'mk_Onl!ne' " + iplist[line] + " 1.0.8802.1.1.2.1.3.4.0 ")
            response = response.read().split(":")[1]
            print(iplist[line], " - ", response)

        except Exception:
            print(iplist[line], " - ", "SNMP incorreto ou desabilitado")
            continue

        except KeyboardInterrupt:
            print("\n Parando ")

        finally:
            signal.alarm(0)


config_mass()

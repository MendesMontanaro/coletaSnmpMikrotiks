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

            comment = "Iniciando coleta da porta SSH no equipamento: " + iplist[line]
            print(comment)

            response = os.popen("nmap " + iplist[line] + " -p 22,2225,2522 | grep open")
            response = response.read().split(":")[0]
            print("A porta SSH É: ", response)


        except Exception:
            print(iplist[line], " - ", "SSH DESABILITADO")
            continue

        except KeyboardInterrupt:
            print("\n Parando ")

        finally:
            signal.alarm(0)


config_mass()

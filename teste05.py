import paramiko
from paramiko import SSHClient, SSHConfig, SSHException
import subprocess
import time
import re
import json
import sys
import datetime
from ftplib import FTP
import uuid
import signal
import requests

iplist = []
hostnamelist = []
devicelist = []
timelist = []
login = 'backup'
passwd = '@nl1n3Ba'
accessportFTP = 21


class TimeoutException(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutException

signal.signal(signal.SIGALRM, timeout_handler)

def colect_list():

    # COLETA DE LISTAS DE HOSTNAMES (CIDADES), DEVICES (DISPOSITIVOS), IPS(IPS PUBLICOS DOS CONCENTRADORES")
    with open("data/users.txt", "r") as users_temp:
        for row01 in users_temp:
            hostnamelist.append(row01.replace("\n", ""))

    with open("data/devices.txt", "r") as devices_temp:
        for row02 in devices_temp:
            devicelist.append(row02.replace("\n", ""))

    with open("data/ips.txt", "r") as ip_temp:
        for row03 in ip_temp:
            iplist.append(row03.replace("\n", ""))


colect_list()
# print(len(iplist))
# print(len(hostnamelist))
# print(len(devicelist))

iplength = len(iplist)
datatime = time.strftime("%Y-%m-%d")

def backup_mass():
    for line in range(0, iplength):
        signal.alarm(60)
        try:

            pass


        except Exception as e:
            errobackup = open("error_backups/errobackup" +datatime+ ".txt", "a+")
            errobackup.write("Erro no backup de ip - " +tempip+":" +str(e)+"\n")
            errobackup.close()
            signal.alarm(0)
            # print(e)
            continue

        except ValueError as e2:
            errobackup = open("error_backups/errobackup" +datatime+ ".txt", "a+")
            errobackup.write("Erro no backup de ip: " +tempip+": "+str(e2)+ "\n")
            errobackup.close()
            signal.alarm(0)
            continue

        except paramiko.ssh_exception.AuthenticationException as mikoerr2:
            errobackup = open("error_backups/errobackup" +datatime+ ".txt", "a+")
            errobackup.write("Erro no backup de ip: "+tempip+": " +str(mikoerr2)+"\n")
            # print(mikoerr2)
            errobackup.close()
            signal.alarm(0)
            continue

        except TimeoutException:
            errobackup = open("error_backups/errobackup" +datatime+ ".txt", "a+")
            errobackup.write("Erro no backup de ip: " +tempip+ ":Tempo de execução expirado.\n")
            errobackup.close()
            signal.alarm(0)
            continue

        finally:
            ssh.close()
            signal.alarm(0)


backup_mass()



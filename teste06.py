import time
import signal
import netmiko
import logging

logging.basicConfig(filename='login.log', level=logging.DEBUG)
logger = logging.getLogger('netmiko')

iplist = []
portlist = []
timelist = []
userlist = []
passlist = []
login = 'montanaro'
passwd = 'Am15171924'


class TimeoutException(Exception):
    pass


def timeout_handler(signum, frame):
    raise TimeoutException


signal.signal(signal.SIGALRM, timeout_handler)


def colect_list():
    # COLETA DE LISTAS DE HOSTNAMES (CIDADES), DEVICES (DISPOSITIVOS), IPS(IPS PUBLICOS DOS CONCENTRADORES")
    with open("data/users.txt", "r") as user_temp:
        for row1 in user_temp:
            userlist.append(row1.replace("\n", ""))

    with open("data/pass.txt", "r") as pass_temp:
        for row2 in pass_temp:
            passlist.append(row2.replace("\n", ""))

    with open("data/ips.txt", "r") as ip_temp:
        for row03 in ip_temp:
            iplist.append(row03.replace("\n", ""))

    with open("data/port.txt", "r") as port_temp:
        for row4 in port_temp:
            portlist.append(row4.replace("\n", ""))


colect_list()

print(len(iplist))
print(len(portlist))
print(len(userlist))
print(len(passlist))

iplength = len(iplist)
portlenght = len(portlist)
userlength = len(userlist)
passlength = len(passlist)
datatime = time.strftime("%Y-%m-%d")


# LOGICA DE COMO FAZER
#porta ip usuario senha

#for p, i in zip(porta, ip):
#  for user in usuario:
#    for sen in senha:
#      try:
#        p, i, user, sen
#      execp


def config_mass():
    for ipline, portline in zip(iplength, portlenght):
        signal.alarm(60)
        for user in userlist:
            for password in passlist:
                try:
                    print("IP: " + iplist[ipline] + " porta: " + portlist[portline])

                    pass
                    #print("config FINALIZADA NO IP ", iplist[line], " às ", datatime)


                #except Exception as e:  # Essa exceção irá tratar caso o script não consiga logar na porta 22
                    #arqconfig = open("erroconfig" + datatime + ".txt", "a+")
                    #arqconfig.write("Erro no login através da porta 22 no ip - :" + str(e) + "\n")
                    #arqconfig.close()
                    #signal.alarm(0)
                    #print(e)
                    #continue

                #except ValueError as e2:
                    #arqconfig = open("erroconfig" + datatime + ".txt", "a+")
                    #arqconfig.write("Erro na coinfig de ip: " + tempip + ": " + str(e2) + "\n")
                    #arqconfig.close()
                    #signal.alarm(0)
                    #continue

                #except netmiko.ssh_exception.AuthenticationException as mikoerr2:
                    #arqconfig = open("erroconfig" + datatime + ".txt", "a+")
                    #arqconfig.write("Erro na config de ip: " + tempip + ": " + str(mikoerr2) + "\n")
                    #arqconfig.close()
                    #signal.alarm(0)
                    #continue

                #except TimeoutException:
                    #arqconfig = open("erroconfig" + datatime + ".txt", "a+")
                    #arqconfig.write("Erro na config de ip: " + tempip + ":Tempo de execução expirado.\n")
                    #arqconfig.close()
                    #signal.alarm(0)
                    #continue

                except KeyboardInterrupt:
                    print("\n Parando ")

                finally:
                    signal.alarm(0)


config_mass()

import time
import signal
import netmiko
import logging
import paramiko

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

print("o arquivo tem: ", len(iplist), " ips")
print("o arquivo tem ", len(portlist), " portas")
print("o arquivo tem ", len(userlist), " usuarios")
print("o arquivo tem ", len(passlist), " senhas")

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
    for ipline, portline in zip(iplist, portlist):
        signal.alarm(60)
        for user in userlist:
            for password in passlist:
                try:
                    print("Vamos lá!\n")
                    print("IP: ", ipline, " porta: ", portline, "usuario: ", user, "senha: ", password)
                    host1 = {  # Enter Device information
                        "host": ipline,
                        "username": user,
                        "password": password,
                        "device_type": "mikrotik_routeros",
                        "global_delay_factor": 0.1,
                        "conn_timeout": 15,
                        "port": portline,
                        # Increase all sleeps by a factor of 1
                    }

                    net_connect = netmiko.Netmiko(**host1)
                    command1 = ["inter print"]  # Enter set of commands
                    print("Connected to:", net_connect.find_prompt())               # Display hostname
                    output = net_connect.send_config_set(command1, delay_factor=.5) # Run set of commands in order

                    print(output)
                    net_connect.disconnect()

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

                except netmiko.ssh_exception.NetmikoTimeoutException as mikoerr3:
                    print("Erro de login - exeption netmiko timeout mikoerr3")
                    print(mikoerr3)

                    continue

                except paramiko.ssh_exception.AuthenticationException as mikoerr4:
                    print("Erro de login - exeption paramiko mikoerr4")
                    print(mikoerr4)

                    continue

                except netmiko.ssh_exception.NetmikoAuthenticationException as mikoerr5:
                    print("Erro de login - exeption netmiko mikoerr5")
                    print(mikoerr5)

                    continue

                except paramiko.ssh_exception.SSHException as erro1:
                    print("erro de login - exeption paramiko erro")
                    print(erro1)

                    continue
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

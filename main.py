import time
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
# porta ip usuario senha

# for p, i in zip(porta, ip):
#  for user in usuario:
#    for sen in senha:
#      try:
#        p, i, user, sen
#      execp


# Indica se consegiu logar
Flag = False


def config_mass():
    # roda em cima dos IPs
    for ipline in iplist:
        # reseta a FLAG para um novo IP
        Flag = False

        # roda em cima das portas
        for portline in portlist:
            # se a Flag for verdadeira para o for
            if Flag == True: break

            # roda em cima dos usuários
            for user in userlist:
                # se a Flag for verdadeira para o for
                if Flag == True: break

                # roda em cima dos passwords
                for password in passlist:
                    # se a Flag for verdadeira para o for
                    if Flag == True: break

                    # Um tempinho só para acompanhar os prints
                    # Depois pode tirar essa linha
                    time.sleep(2)

                    print("\nVamos lá!")
                    print(" >> IP: ", ipline, " porta: ", portline, "usuario: ", user, "senha: ", password)

                    try:
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
                        command1 = ["/radius add address=191.7.212.14 comment=FreeRadius.online.net.br secret=0nl@dm00 service=login",
                                    "/user aaa set use-radius=yes",
                                    "/user add group=full name=noc password=Eqs8qMX5ZgEmRCtG",
                                    "/snmp community set [ find default=yes ] name=mk_Onl!ne",
                                    "/snmp set contact=noc@online.net.br enabled=yes trap-version=2",
                                    "/system ntp client set enabled=yes primary-ntp=10.240.150.50 secondary-ntp=200.160.0.8",
                                    "/system clock set time-zone-name=America/Fortaleza",
                                    "/ip service set telnet disabled=yes",
                                    "/ip service set ftp disabled=yes",
                                    '/ip service set ssh address="191.7.212.6/32,191.7.212.88/32,191.7.212.90/32,191.7.212.91/32,191.7.194.98/32,191.7.215.190/32,10.240.150.18/32" port=2225',
                                    "/ip service set api disabled=yes",
                                    "/ip service set winbox address=191.7.212.6/32,191.7.212.88/32,191.7.212.90/32,191.7.212.91/32",
                                    "/ip service set api-ssl disabled=yes",
                                    "/tool romon set enabled=yes secrets=mk_Onl!ne"]  # Enter set of commands
                        print("Connected to:", net_connect.find_prompt())  # Display hostname
                        output = net_connect.send_config_set(command1, delay_factor=.5)  # Run set of commands in order

                        print(output)
                        net_connect.disconnect()

                        # Se conseguir logar naquele IP, PORTA, USUARIO E SENHA
                        # TROCA O VALOR DA FLAG PARA TRUE
                        # INFORMANDO A TROCA DO IP
                        Flag = True

                        pass
                        # print("config FINALIZADA NO IP ", iplist[line], " às ", datatime)


                    # except Exception as e:  # Essa exceção irá tratar caso o script não consiga logar na porta 22
                    # arqconfig = open("erroconfig" + datatime + ".txt", "a+")
                    # arqconfig.write("Erro no login através da porta 22 no ip - :" + str(e) + "\n")
                    # arqconfig.close()
                    # signal.alarm(0)
                    # print(e)
                    # continue

                    except EOFError as eoferror:
                        print("Erro de EOFError ")
                        continue

                    except ValueError as e2:
                        print("Erro de ValueError ")
                        continue
                        # arqconfig = open("erroconfig" + datatime + ".txt", "a+")
                        # arqconfig.write("Erro na coinfig de ip: " + tempip + ": " + str(e2) + "\n")
                        # arqconfig.close()
                        # signal.alarm(0)
                        # continue

                    except netmiko.ssh_exception.NetmikoTimeoutException as mikoerr3:
                        print("Erro de login - exeption netmiko timeout mikoerr3")
                        # print(mikoerr3)
                        continue

                    except paramiko.ssh_exception.AuthenticationException as mikoerr4:
                        print("Erro de login - exeption paramiko mikoerr4")
                        # print(mikoerr4)
                        continue

                    except netmiko.ssh_exception.NetmikoAuthenticationException as mikoerr5:
                        print("Erro de login - exeption netmiko mikoerr5")
                        # print(mikoerr5)
                        continue

                    except paramiko.ssh_exception.SSHException as erro1:
                        print("erro de login - exeption paramiko erro")
                        # print(erro1)

                        continue
                    # except netmiko.ssh_exception.AuthenticationException as mikoerr2:
                    # arqconfig = open("erroconfig" + datatime + ".txt", "a+")
                    # arqconfig.write("Erro na config de ip: " + tempip + ": " + str(mikoerr2) + "\n")
                    # arqconfig.close()
                    # signal.alarm(0)
                    # continue

                    # except TimeoutException:
                    # arqconfig = open("erroconfig" + datatime + ".txt", "a+")
                    # arqconfig.write("Erro na config de ip: " + tempip + ":Tempo de execução expirado.\n")
                    # arqconfig.close()
                    # signal.alarm(0)
                    # continue

                    except KeyboardInterrupt:
                        print("\n Parando ")


config_mass()

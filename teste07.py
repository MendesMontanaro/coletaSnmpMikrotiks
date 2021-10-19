from netmiko import Netmiko
import logging
logging.basicConfig(filename="test.log", level=logging.DEBUG)   # It will log all reads and writes on the SSH channel
logger = logging.getLogger("netmiko")
host1 = {                                                       # Enter Device information
    "host": "10.240.149.2",
    "username": "montanaro.mendes",
    "password": "Am15171924",
    "device_type": "mikrotik_routeros",
    "global_delay_factor": 0.1,
    "conn_timeout": 15,
    "port": 222,
    # Increase all sleeps by a factor of 1
}

net_connect = Netmiko(**host1)
status = net_connect
print(status)

#command1 = ["inter print"]  # Enter set of commands
#print("Connected to:", net_connect.find_prompt())               # Display hostname
#output = net_connect.send_config_set(command1, delay_factor=.5) # Run set of commands in order

                                                                # Increase the sleeps for just send_command by a factor of 2
net_connect.disconnect()                                        # Disconnect from Session

#print(output)

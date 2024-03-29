from colorama import init
from termcolor import colored
from netmiko import ConnectHandler

init()
ip_address = ['192.168.64.145', '192.168.64.147', '192.168.64.148', '192.168.64.149', '192.168.64.144', '192.168.64.146', '192.168.64.150', '192.168.64.151']

def test_ospf():
    ospf_state = False
    connection = ConnectHandler(**router)
    neighbors = connection.send_command('sh ip ospf neighbor | count  FULL').split('= ')[1]
    if neighbors != 0:
        ospf_state = True
        print(f"Host: {colored(router['host'], 'green')}" + f" Neighbors Count: {colored(neighbors, 'blue')}")
    connection.disconnect()
    assert(ospf_state == True)
    
for ip in ip_address:
    router = {
        "host": ip,
        "use_keys": True,
        "username": 'cisco',
        "port": 22,
        "device_type": 'cisco_ios',
        "key_file": './id_rsa',
        "secret": 'c!sco'
    }
    test_ospf()
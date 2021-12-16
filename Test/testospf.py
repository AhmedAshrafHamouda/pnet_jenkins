from colorama import init
from termcolor import colored
from netmiko import ConnectHandler

init()
ip_address = ['192.168.64.130', '192.168.64.131', '192.168.64.132', '192.168.64.133', '192.168.64.134', '192.168.64.135', '192.168.64.136', '192.168.64.137']


def test_ospf():
    ospf_state = False
    connection = ConnectHandler(**router)
    neighbors = connection.send_command('sh ip ospf neighbor | count  FULL').split('= ')[1]
    print(f"Host: {colored(router['host'], 'green')}" + f" Neighbors Count: {colored(neighbors, 'blue')}")
    if neighbors != 0:
        ospf_state = True
    connection.disconnect()
    assert(ospf_state == True)
    
for ip in ip_address:
    router = {
        "host": ip,
        "use_keys": True,
        "username": 'cisco',
        "port": 22,
        "device_type": 'cisco_ios',
        "key_file": '/home/ubuntu/.ssh/id_rsa',
        "secret": 'c!sco'
    }
    test_ospf()
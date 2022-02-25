from colorama import init
from termcolor import colored
from netmiko import ConnectHandler

init()
ip_address = ['192.168.64.149', '192.168.64.144', '192.168.64.146', '192.168.64.150', '192.168.64.151']

def test_dhcp():
    dhcp_state = False
    connection = ConnectHandler(**router)
    dhcp = int(connection.send_command('sh ip dhcp pool | c Pool').split('= ')[1])
    if dhcp != 0:
        dhcp_state = True
        print(f"DHCP Is Enabled On Host: {colored(router['host'], 'green')}")
    connection.disconnect()
    assert(dhcp_state == True)
    connection.disconnect()
    
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
    test_dhcp()
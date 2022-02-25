from colorama import init
from termcolor import colored
from netmiko import ConnectHandler

init()
ip_address = ['192.168.64.133', '192.168.64.134', '192.168.64.135', '192.168.64.136', '192.168.64.137']

def test_dhcp():
    dhcp_state = False
    connection = ConnectHandler(**router)
    dhcp = int(connection.send_command('sh ip dhcp pool | c Pool').split('= ')[1])
    if dhcp != 0:
        dhcp_state = True
        print(f"DHCP Is Enabled On Host: {colored(router['host'], 'green')}")
    connection.disconnect()
    assert(dhcp_state == True)
    
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
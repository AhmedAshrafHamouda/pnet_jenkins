import subprocess

ip_address = ['192.168.64.130', '192.168.64.131', '192.168.64.132', '192.168.64.133', '192.168.64.134', '192.168.64.135', '192.168.64.136', '192.168.64.137']

for host in ip_address:
    res = subprocess.call(['ssh', host])
    if res == 0:
        print ("ping to", host, "OK")
    elif res == 2:
        print ("no response from", host)
    else:
        print ("ping to", host, "failed!")
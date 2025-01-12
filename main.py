import subprocess
from net_statement import NetStatement
from hashing import Hashing

hex_string = "31bbb6d1b27329df0008"
hex_string = "31bb96623fff3f010007"

byte_values = bytes.fromhex(hex_string)
print(byte_values)

netif = NetStatement()
hsa = Hashing()
status, data = hsa.do_hash(byte_values)

command = ['ip', '-brief', 'link']
result = subprocess.check_output(command, text=True)
# subprocess.run(command)
# res = result.split('\n\n')
print(result)
# result = " "
# result ="lo               UNKNOWN        00:00:00:00:00:00 <LOOPBACK,UP,LOWER_UP>\n"
print(netif.decode_interface_statement(result))
print(netif.get_number_of_interface())
print(netif.get_all_interface_statement())
res = netif.get_interface_statement_at(2)
print("res")
print(res)

dev = netif.get_device_name(res)
sts = netif.get_connection_status(res)
mode = netif.get_connection_mode(res)
mac = netif.get_mac_address(res)
# # print(isinstance(res, str))

print(dev)
print(sts)
print(mode)
print(mac)



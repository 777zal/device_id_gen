import subprocess
from net_statement import NetSentence
from hashing import Hashing
from composer import Composer 

command = ['adb', 'devices']
result = subprocess.check_output(command, text=True)
print(result)
command = ['adb', 'shell', 'ip', '-brief', 'link']
result = subprocess.check_output(command, text=True)
print(result)

cp = Composer("31")
cp.setup_target_path("build.prop")
cp.set_new_field_name("ro.deviceid")
print("composing message")
id = cp.compose_id("B6D1B27329DF", "0008")
cp.insert_id_to_config_file(id)

# hex_string = "31bbb6d1b27329df0008"
# hex_string = "31bb96623fff3f010007"

# byte_values = bytes.fromhex(hex_string)
# print(byte_values)

netif = NetSentence()
hsa = Hashing()
# status, data = hsa.do_hash(byte_values)
# print(data)
command = ['ip', '-brief', 'link']
result = subprocess.check_output(command, text=True)
# subprocess.run(command)
# res = result.split('\n\n')
print(result)
# result = " "
# result ="lo               UNKNOWN        00:00:00:00:00:00 <LOOPBACK,UP,LOWER_UP>\n"
print(netif.decode_interface_sentence(result))
print(netif.get_number_of_interface())
print(netif.get_all_interface_sentence())
res = netif.get_interface_sentence_at(2)
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

print(netif.get_sentence_by_device_name("wlp4s0"))
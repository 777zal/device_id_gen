# import cityhash  
from hashing import Hashing
hex_string = "31bbb6d1b27329df0008"
hex_string = "31bb96623fff3f010007"
# hex_string = "48656c6c6f2c20576f72"
# byte_array = bytearray.fromhex(hex_string)
# result_string = byte_array.decode('utf-8', 'ignore')
byte_values = bytes.fromhex(hex_string)
print(byte_values)

hsa = Hashing()
status, data = hsa.do_hash(byte_values)
print(status)
print(data)


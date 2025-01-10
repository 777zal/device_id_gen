import cityhash  
import hashing as hs
hex_string = "31bbb6d1b27329df0008"
hex_string = "31bb96623fff3f010007"
# hex_string = "48656c6c6f2c20576f72"
# byte_array = bytearray.fromhex(hex_string)
# result_string = byte_array.decode('utf-8', 'ignore')
byte_values = bytes.fromhex(hex_string)
print(byte_values)

hsa = hs.Hashing()
print(hsa.hash(byte_values))
hash_value_32 = cityhash.CityHash32(byte_values)
# hash_value_64 = cityhash.CityHash64(data) 
print(f"CityHash32: {hash_value_32}")  
print(f"CitiHash32: {hex(hash_value_32)}")
# Compute a 128-bit hash 
# hash_value_128 = cityhash.CityHash128(data) 
# print(f"CityHash128: {hash_value_128}")


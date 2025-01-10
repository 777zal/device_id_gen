from cityhash import CityHash32

class Hashing:
    def __init__(self):
        print("Set Hash Class")
        
    def __check_input(self, input:bytearray):
        if len(input) > 10:
            return False
        return True

    def __convert_int32_to_list(self, input:int):
        result_list = []
        str_val = str(input)
        # bytes_val = input.to_bytes(1, 'big')
        byte_val = input.to_bytes(4, 'big')
        print(isinstance(byte_val, bytes))
        print(byte_val)
        # hex_string = hex(input)
        # print(hex_string)
        # byte_array =bytes.fromhex(hex_string)
        # print((byte_array))
        

    def hash(self, input:bytearray):
        status  = self.__check_input(input)
        self.__convert_int32_to_list(CityHash32(input))
         
            

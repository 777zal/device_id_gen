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
        str_val = f'{input:0x}' # convert integer to hex in string format
        for i in range (0,len(str_val),2):
            result_list.append(''.join([str_val[i],str_val[i+1]]))
        return result_list
        
    # def __shift_bytes(self, input:bytearray):
    #     result_list = []
    #     data_len = len(input)
    #     for i in range(0, data_len):
    #         print(i)
    #         result_list.append(input[(data_len-1)-i])
    #     return result_list

    def do_hash(self, input:bytearray):
        status  = self.__check_input(input)
        return status, self.__convert_int32_to_list(CityHash32(input))         
            

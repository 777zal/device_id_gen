from hashing import Hashing

class Composer:

    ############################################################
    # Pre Hash :
    # Header -> 1 byte 
    # 0xBB -> 1 byte
    # MAC Address -> 6 bytes
    # Sequence number -> 2 byte
    # res = Hash(Header, 0xBB, 6 bytes of MAC, Sequence Number)
    # ID = (Header, BB, 4 bytes of res, sequence number)
    #############################################################
    __mHeader = ""
    __identifier = "BB"
    __target_field_name = ""
    __mList = []
    __mHash = Hashing()
    __mPath = ""
    __id_field_name = ""

    def __init__(self, header_text:str):
        self.__mHeader = header_text
        print("Initiate Composer")

    def __convert_to_hexstring(self, input:bytearray):
        msg = ""
        for i in input:
            msg += i.hex()
        return msg

    def __convert_config_file_as_list(self, path:str):
        with open(path, 'r') as fh:
            for line in fh:
                self.__mList.append((line))

    def __get_field_at_line(self, msg:str) -> str:
        arr = msg.split('=')
        if len(arr) == 2:
            return arr[0]
        return 0

    def __get_content_at_line(self, msg:str) -> str:
        arr = msg.split('=')
        if len(arr) == 2:
            return arr[1]
        return 0

    def __get_number_of_config_lines(self) -> int:
        return len(self.__mList)

    def __get_row_by_keyword(self, msg:str) -> int:
        length = self.__get_number_of_config_lines()
        print(length)
        for i in range (0, length):
            if self.__get_field_at_line(self.__mList[i]) == msg or \
               self.__get_content_at_line(self.__mList[i]) == msg: 
                return i            
        return 0

    def compose_id(self, mac:str, sequence:str) -> str:
        result = []
        msg = ""
        msg += self.__mHeader + self.__identifier + mac + sequence
    
        status, hash_value = self.__mHash.do_hash(bytes.fromhex(msg))
        result.append(bytes.fromhex(self.__mHeader))
        result.append(bytes.fromhex(self.__identifier))
        for i in hash_value:           
            result.append(bytes.fromhex(i))
        res = bytes.fromhex(sequence)
        for i in res:
            result.append(i.to_bytes(1, 'big'))
        msg_out = self.__convert_to_hexstring(result)
        return msg_out 

    def setup_target_path(self, path:str, new_field:str):
        self.__mPath = path
        self.__id_field_name = new_field
        self.__convert_config_file_as_list(path)
        

    def insert_id_to_config_file(self, device_id:str):
        row = self.__get_row_by_keyword(self.__id_field_name)
        new_id = '\n'+self.__id_field_name+'='+device_id
        self.__mList.append(new_id)
        s = ''.join(self.__mList)
        print(s)
        file1 = open(self.__mPath, "w")
        file1.write(s)
        file1.close()
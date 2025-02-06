from hashing import Hashing

class Composer:

    ############################################
    # Pre Hash :
    # Header -> 1 byte 
    # 0xBB -> 1 byte
    # MAC Address -> 6 bytes
    # Sequence number -> 2 byte
    # res = Hash(Header, 0xBB, 6 bytes of MAC, Sequence Number)
    # ID = (Header, BB, 4 bytes of res, sequence number)
    ##########################
    __mHeader = ""
    __identifier = "BB"
    __mHash = Hashing()

    def __init__(self, header_text:str):
        self.__mHeader = header_text
        print("Initiate Composer")

    def __convert_to_hexstring(self, input:bytearray):
        msg = ""
        for i in input:
            msg += i.hex()
        return msg

    def compose_message(self, mac:str, sequence:str) -> str:
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



import subprocess

class NetSentence:
    
    __iface   = []
    __isValid = False
    __number_of_interface = 0

    def __init__(self):
        print("Network sentence Created")

    def __get_interface_list(self, input:str) -> list:
        text_list = input.split('\n')
        return text_list
    
    def __sentence_is_not_empty(self, input:str) -> bool:
        temp = self.__get_interface_list(input)        
        if len(temp) == 1:
            return False
        return True
    
    def __slice_interface_sentence(self, input:str) -> list:
        text = []
        temp = input.split(' ')
        for i in range (0, len(temp)):
            if temp[i]:
               text.append(temp[i])
        return text

    def decode_interface_sentence(self, input:str) -> bool:
        self.__isValid = False
        if not self.__sentence_is_not_empty(input):
            return False
        self.__iface = self.__get_interface_list(input)
        self.__isValid = True
        self.__number_of_interface = len(self.__get_interface_list(input))-1
        return True
        
    def get_number_of_interface(self) -> int:
        if not self.__isValid:
            return 0
        return self.__number_of_interface
    
    def get_all_interface_sentence(self) -> list:
        if not self.__isValid:
            return " "
        return self.__iface
    
    def get_interface_sentence_at(self, number:int) -> str:
        if not self.__isValid or number > self.__number_of_interface:
            return "empty"
        return self.__iface[number]
        
    def get_device_name(self, sentence:str) -> str:
        if not self.__isValid :
            return "empty"
        text = self.__slice_interface_sentence(sentence)
        return text[0]
    
    def get_connection_status(self, sentence:str) -> str:
        if not self.__isValid :
            return "empty"
        text = self.__slice_interface_sentence(sentence)
        return text[1]
    
    def get_mac_address(self, sentence:str) -> list:
        if not self.__isValid :
            return "empty"
        text = self.__slice_interface_sentence(sentence)
        return text[2].split(':')

    def get_connection_mode(self, sentence:str) -> str:
        if not self.__isValid :
            return "empty"
        text = self.__slice_interface_sentence(sentence)
        return text[3]
    
    def get_sentence_by_device_name(self, name:str) -> str:
        if self.__number_of_interface == 0:
            return "empty"
        for i in range (0, self.__number_of_interface):
            if(self.get_device_name(self.__iface[i]) == name):
                return self.__iface[i]
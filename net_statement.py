import subprocess

class NetStatement:
    
    __iface   = []
    __isValid = False
    __number_of_interface = 0

    def __init__(self):
        print("Network Statement Created")

    def __get_interface_list(self, input:str):
        text_list = input.split('\n')
        return text_list
    
    def __statement_is_not_empty(self, input:str):
        temp = self.__get_interface_list(input)        
        if len(temp) == 1:
            return False
        return True
    
    def __slice_interface_statement(self, input:str):
        text = []
        temp = input.split(' ')
        for i in range (0, len(temp)):
            if temp[i]:
               text.append(temp[i])
        return text

    def decode_interface_statement(self, input:str):
        self.__isValid = False
        if not self.__statement_is_not_empty(input):
            return False
        self.__iface = self.__get_interface_list(input)
        self.__isValid = True
        self.__number_of_interface = len(self.__get_interface_list(input))-1
        return True
        
    def get_number_of_interface(self):
        if not self.__isValid:
            return 0
        return self.__number_of_interface
    
    def get_all_interface_statement(self):
        if not self.__isValid:
            return " "
        return self.__iface
    
    def get_interface_statement_at(self, number:int):
        if not self.__isValid or number > self.__number_of_interface:
            return "empty"
        return self.__iface[number]
        
    def get_device_name(self, statement:str):
        if not self.__isValid :
            return "empty"
        text = self.__slice_interface_statement(statement)
        return text[0]
    
    def get_connection_status(self, statement:str):
        if not self.__isValid :
            return "empty"
        text = self.__slice_interface_statement(statement)
        return text[1]
    
    def get_mac_address(self, statement:str) -> list:
        if not self.__isValid :
            return "empty"
        text = self.__slice_interface_statement(statement)
        return text[2].split(':')

    def get_connection_mode(self, statement:str):
        if not self.__isValid :
            return "empty"
        text = self.__slice_interface_statement(statement)
        return text[3]
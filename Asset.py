"""
File: Asset.py
Description: <A brief description of this Python module.>
Author: Krish Sanjaybhai Bhadani
ID: 110429045
Username: bhaks003
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class asset:
    def __init__(self, name, description, encrypted = False):
        self.__name = name
        self.__description = description
        self.__encrypted = encrypted

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def encrypt(self):
        if self.__encrypted == False:
            self.__encrypted = True
            print(f"{self.__name} is encrypted.")
        else:
            print(f"{self.__name} is already encrypted.")

    def decrypt(self):
        if self.__encrypted == True:
            self.__encrypted = False
            print(f"{self.__name} is decrypted.")
        else:
            print(f"{self.__name} is already decrypted.")
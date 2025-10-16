"""
File: Asset.py
Description: Creates a digital asset with name, description and encryption state and also can change the state which is either encrypted or decrypted.
Author: Krish Sanjaybhai Bhadani
ID: 110429045
Username: bhaks003
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class asset:
    """
    This class contains the information about a digital asset such Security key, data spike, crypto token etc.
    with their description and state which is based on boolean expression
    but by default state be in decrypted if users need to change they cAN when creating the asset or after creating by using the method
    """
    def __init__(self, name, description, encrypted = False):
        self.__name = name
        self.__description = description
        self.__encrypted = encrypted

    # using getters in here might be usefull in get the info other classes and also data prevention.
    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_encrypted(self):
        return self.__encrypted

    # this method encrypts the asset based on expression
    def encrypt(self):
        if self.__encrypted == False:
            self.__encrypted = True
            print(f"{self.__name} is encrypted.")
        else:
            print(f"{self.__name} is already encrypted.")

    # this method decrypts the asset based on expression
    def decrypt(self):
        if self.__encrypted == True:
            self.__encrypted = False
            print(f"{self.__name} is decrypted.")
        else:
            print(f"{self.__name} is already decrypted.")

    # it is string conversion method in orde the display the name, description and encrypted if it is ortherwise it will show nothing.
    def __str__(self):
        if self.__encrypted == True:
            return f"{self.__name}: {self.__description} [Encrypted]"
        else:
            return f"{self.__name}: {self.__description}"


# a1 = asset("CrytoToken", "Used to acquire or repair rigs. ")
# print(a1)
# a1.encrypt()
# print(a1)
# a1.decrypt()
# print(a1)
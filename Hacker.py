"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: Krish Sanjaybhai Bhadani
ID: 110429045
Username: bhaks003
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Rig import Rig
from Asset import asset

class Hacker:
    def __init__(self, name):
        self.__name = name
        self.__inventory  = [asset("CryptoToken", "Used to acquire or repair rigs.")]
        self.__rig = False
        self.__trace_level = 0

    def get_trace_level(self):
        return self.__trace_level

    def is_exposed(self):
        if self.__trace_level > 6:
            return True
        return False

    def acquire_rig(self, rig_name):
        has_asset = False

        for item in self.__inventory:
            if item.get_name() == "CryptoToken":
                has_asset = True

        if has_asset:
            for item in self.__inventory:
                if item.get_name() == "CryptoToken":
                    self.__inventory.remove(item)
                    self.__rig = Rig(rig_name)
                    print(f"{self.__name} has acquired a rig {rig_name}")
        else:
            print(f"{self.__name} does not have CryptoToken to acquire a {rig_name}")

    def add_trace(self, amount):
        if amount <= 0 >= 10:
            print(f"{self.__name} needs to put postive number and until 10 in order to add trace")

        self.__trace_level += amount
        print(f"{self.__name} traced increased to  level: {str(self.__trace_level)}")

        if self.is_exposed():
            print(f"{self.__name} has exposed. Some actions may be blocked until it is reduced")

    def __str__(self):
        invetory_item = []
        for items in self.__inventory:
            invetory_item.append(items.get_name())

        rig_name = "No Rig"
        if self.__rig != False:
            rig_name = self.__rig.get_name()

        return f"{self.__name} | Rig: {rig_name} | Inventory: {invetory_item}"



# h1 = Hacker("TestHacker")
# print(h1)
# h1.add_trace(2)
# h1.add_trace(5)
# print(h1)
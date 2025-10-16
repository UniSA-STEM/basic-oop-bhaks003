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

    def __str__(self):
        invetory_item = []
        for items in self.__inventory:
            invetory_item.append(items.get_name())

        rig_name = "No Rig"
        if self.__rig != False:
            rig_name = self.__rig.get_name()

        return f"{self.__name} | Rig: {rig_name} | Inventory: {invetory_item} "


# h1 = Hacker("TestHacker")
# print(h1)

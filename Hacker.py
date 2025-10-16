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
        if amount <= 0  or amount > 10:
            print(f"{self.__name} needs to put postive number and until 10 in order to add trace")
            return

        self.__trace_level += amount
        print(f"{self.__name} traced increased to  level: {str(self.__trace_level)}")

        if self.is_exposed():
            print(f"{self.__name} has exposed. Some actions may be blocked until it is reduced")

    def reduce_trace(self, amount):
        if amount <=0  or amount > 10:
            print(f"{self.__name} needs to put postive number and until 10 in order to add trace")
            return

        self.__trace_level -= amount
        if self.__trace_level < 0:
            self.__trace_level = 0
        print(f"{self.__name} traced decreased to  level: {str(self.__trace_level)}")

        if not self.is_exposed():
            print(f"{self.__name} is no longer exposed")

    def launch_data_spike(self, target_rig):
        # this one will block if the hacker is exposed too much by trace level
        if self.is_exposed():
            print(f"{self.__name} is exposed and cannot launch attacks right now.")
            return

        # this one will check that if a hacker has a rig in order to launch data spike or not
        if self.__rig == False:
            print(f"{self.__name} does not have a rig to launch data spike.")

        # looking for a data spike in target's rig storage
        spike = False
        storage = self.__rig.get_storage()
        for item in storage:
            if item.get_name() == "Data Spike":
                spike = item

        if spike == False:
            print(f"{self.__name} does not have a data spike.")
            return

        # using the data spike and attacking
        storage.remove(spike)
        target_rig.take_hit()
        self.add_trace(1)
        print(f"{self.__name} launched a data spike at {target_rig.get_name()}")


    def __str__(self):
        invetory_item = []
        for items in self.__inventory:
            invetory_item.append(items.get_name())

        rig_name = "No Rig"
        if self.__rig != False:
            rig_name = self.__rig.get_name()

        return f"{self.__name} | Rig: {rig_name} | Trace Level: {self.__trace_level} | Inventory: {invetory_item}"


# h1 = Hacker("TestHacker")
# print(h1)
# h1.add_trace(2)
# h1.add_trace(5)
# print(h1)
# h1.reduce_trace(4)
# h1.reduce_trace(22)
# print(h1)
"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: Krish Sanjaybhai Bhadani
ID: 110429045
Username: bhaks003
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Asset import asset

class Rig:
    def __init__(self, name):
        self.__name = name
        self.__damage = 0
        self.__broken = False
        self.__storage = [asset("Data Spike", "Used in battles"), asset("Data Spike", "Used in battles"), asset("Encrypted Drive", "Used for extraction", True)]
        self.__upgrade_level = 0

    def get_name(self):
        return self.__name

    def get_storage(self):
        return self.__storage

    def repair(self):
        if self.__damage > 0 or self.__broken:
            self.__damage = 0
            self.__broken = False
            print(f"{self.__name} has been repaired to pristine condition")
        else:
            print(f"{self.__name} is already in pristine condition doesn't need to be repaired")

    def upgrade(self):
        self.__upgrade_level = self.__upgrade_level + 1
        print(f"{self.__name} has been upgraded to {self.__upgrade_level} level")

    def take_hit(self):
        self.__damage = self.__damage + 1
        print(f"{self.__name} has taken a hit. Current damage: {self.__damage}")

        if self.__damage >= 2 + self.__upgrade_level:
            self.broken = True
            print(f"{self.__name} has been broken. It needs a repair.")


# r1 = Rig("Rig test")
# r1.repair()
# r1.upgrade()
# r1.take_hit()
# r1.take_hit()
# r1.take_hit()
# r1.take_hit()
# r1.repair()
# r1.take_hit()
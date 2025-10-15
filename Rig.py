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

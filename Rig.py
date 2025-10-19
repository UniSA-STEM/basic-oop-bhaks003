"""
File: Rig.py
Description: A classes which represents a rig with name, damage_coutner, condtion, upgrade_level, And Stored Asset
Author: Krish Sanjaybhai Bhadani
ID: 110429045
Username: bhaks003
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Asset import asset
import random


"""
this class represent a rig (computer) which at first has 
2 Data Spike 
and 
1 Removeable Drive when Created
"""

class Rig:
    def __init__(self, name):
        self.__name = name
        self.__damage = 0
        self.__broken = False
        self.__storage = [asset("Data Spike", "Used in battles."), asset("Data Spike", "Used in battles."), asset("Removable Drive", "Found in rigs and used for extraction.")]
        self.__upgrade_level = 0

    # Using Getter to use the information in other classes
    def get_name(self):
        return self.__name

    def get_storage(self):
        return self.__storage

    def is_broken(self):
        return self.__broken

    """This method repair the rig and counters work on the upgrade level if it is level 0 it has capacity to withstand 2 hits and 
    after  that it will display repair message. 
    While level 1 ship can take 3 hit and so it goes on based on level"""
    def repair(self):
        if self.__damage > 0 or self.__broken:
            self.__damage = 0
            self.__broken = False
            print(f"{self.__name} has been repaired to pristine condition")
        else:
            print(f"{self.__name} is already in pristine condition doesn't need to be repaired")

    # this method upgrades the rig
    def upgrade(self):
        self.__upgrade_level = self.__upgrade_level + 1
        print(f"{self.__name} has been upgraded to {self.__upgrade_level} level")

    # this method takes hit from data spikes when it reaches itn repairing capacity it will show the message to repair as well. and also there is a damange counter as well
    def take_hit(self):
        self.__damage = self.__damage + 1
        print(f"{self.__name} has taken a hit. Current damage: {self.__damage}")

        if self.__damage >= 2 + self.__upgrade_level:
            self.__broken = True
            print(f"{self.__name} has been broken. It needs a repair.")

    # in this methof by the the help of random choice it will choose a asset from the given asset desc and will add in to storage as well
    def generate_asset(self):
        assets_list = [asset("CryptoToken", "Used to acquire or repair ship"), asset("Data Spike", "Used in battles."), asset("Removable Drive", "Found in rigs and used for extraction."), asset("Security Chip", "Used to encrypt or decrypt assets."), asset("Hardware Patch", "Used to upgrade rigs.")]
        new_asset = random.choice(assets_list)
        self.__storage.append(new_asset)
        print(f"{self.__name} has generated a new asset {new_asset}.")


    def store_asset(self, asset_name):
        if asset_name.get_encrypted():
            print(f"{asset_name} is encrypted and cannot be stored until decrypted.")
        else:
            self.__storage.append(asset_name)
            print(f"{asset_name} is stored in {self.__name}")

 # This method above and below are developed in order to transfer between rig storage and hacker's
 # inventory. but there is a catch it can only transfer the asset when it is decrypted
 # if hacker wants to transfer he needs to decrypt the encrypted asset.

    def release_asset(self, asset_name):
        for asset in self.__storage:
            if asset.get_name()  ==  asset_name.get_name():
                if asset.get_encrypted():
                    print(f"{asset.get_name()} is encrypted. you to decrypt in order to transfer it.")
                else:
                    self.__storage.remove(asset)
                    print(f"Releasing {asset.get_name()}. from {self.__name}")
                return
        print(f"{asset_name} is not in storage of  {self.__name}.")

    # This is shown the condition of rig based on the boolean exprerssion which is broken or not
    def get_condition(self):
        if self.__broken:
            return f"Broken  (Level {self.__upgrade_level})"
        else:
            return f"Pristine (Level {self.__upgrade_level})"

    # string conversion method to maker user friendly readable understsadning
    def __str__(self):
        asset_name = []
        for asset in self.__storage:
            asset_name.append(asset.get_name())
        return f"Rig: {self.__name} | Condition: {self.get_condition()} | Asset: {asset_name}"



# r1 = Rig("Rig test")
# # a1 = asset("Security Chip", "Used to encrypt or decrypt assets", True)
# # a2 = asset("Hardware Patch", "Used to upgrade rigs")
# # r1.repair()
# # r1.upgrade()
# # r1.take_hit()
# # r1.take_hit()
# # r1.take_hit()
# # r1.take_hit()
# # r1.repair()
# # r1.take_hit()
# # r1.generate_asset()
# # r1.generate_asset()
# # for item in r1.get_storage():
# #     print(item)
# # print(80*"#")
# # r1.store_asset(a1)
# # r1.store_asset(a2)
# # for item in r1.get_storage():
# #     print(item)
# # print(80*"#")
# # r1.release_asset(a1)
# # r1.release_asset(a2)
# # for item in r1.get_storage():
# #     print(item)
# # r1.get_condition()
# # r1.take_hit()
# # r1.take_hit()
# # r1.get_condition()
# # r1.take_hit()
# # r1.repair()
# # r1.get_condition()
# print(r1)
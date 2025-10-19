"""
File: Hacker.py
Description: Creates a hacker class which has function like acquire rig, store and retrieve asset, encrypt and decrypt asset and upgrade rigs.
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

    # using getter in here to information in other clases
    def get_trace_level(self):
        return self.__trace_level

    def is_exposed(self):
        if self.__trace_level > 6:
            return True
        return False

    # this method willl acquire a rig with the help Crypto Token if found one
    def acquire_rig(self, rig_name):
        has_asset = False
        for item in self.__inventory:
            if item.get_name() == "CryptoToken":
                has_asset = True
        if has_asset:
            for item in list(self.__inventory):
                if item.get_name() == "CryptoToken":
                    self.__inventory.remove(item)
                    self.__rig = Rig(rig_name)
                    print(f"{self.__name} has acquired a rig {rig_name}")
                    return True
        else:
            print(f"{self.__name} does not have CryptoToken to acquire a {rig_name}")
            return False

    # this method is just like leaving a footprint behind if too many footprint are visible hacker might not be able to use full potential
    def add_trace(self, amount):
        if amount <= 0  or amount > 10:
            print(f"{self.__name} needs to put postive number and until 10 in order to add trace")
            return
        self.__trace_level += amount
        print(f"{self.__name} traced increased to  level: {str(self.__trace_level)}")
        if self.is_exposed():
            print(f"{self.__name} has exposed. Some actions may be blocked until it is reduced")

    # in here it will reduce the footprint caused by an attack to stay low
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

    """
    launch_data_spike method attacks the target rig but at first it will self check whether it is exposed by trace_level or not, 
    then will check it was a rig 
    and after that it will search for a data spike in the storage if it is found it will launch at target_rig 
    in terms of leasving damage the target will take_hit and a add trace_level on own and will remove the spike from storage
    """
    def launch_data_spike(self, target_rig):
        # this one will block if the hacker is exposed too much by trace level
        if self.is_exposed():
            print(f"{self.__name} is exposed and cannot launch attacks right now.")
            return False
        # this one will check that if a hacker has a rig in order to launch data spike or not
        if self.__rig == False:
            print(f"{self.__name} does not have a rig to launch data spike.")
            return False
        # looking for a data spike in target's rig storage
        spike = False
        storage = self.__rig.get_storage()
        for item in storage:
            if item.get_name() == "Data Spike":
                spike = item
        if spike == False:
            print(f"{self.__name} does not have a data spike.")
            return False
        # using the data spike and attacking
        storage.remove(spike)
        target_rig.take_hit()
        self.add_trace(1)
        print(f"{self.__name} launched a data spike at {target_rig.get_name()}")
        return True

    """
    this extraction method uses logic if rig is broken it will move further, attacker must have rig, 
    it should be completly broken and also should contain removable drive 
    after drive is found then only it will transfer the asset to inventory
    """
    def extract_data_spike(self, target_rig):
        if self.__rig == False:
            print(f"{self.__name} does not have a rig to extract assets.")
            return False
        # determing if the target rig is broken or not
        if target_rig.is_broken() == False:
            print(f"{self.__name} is not broken cannot extract assets.")
            return False
        attacker_storage = self.__rig.get_storage()
        # finding removable drive in attackers storage
        drive = False
        for drive in attacker_storage:
            if drive.get_name() == "Removable Drive" and drive.get_encrypted() == False:
                drive = drive
        if drive == False:
            print(f"{self.__name} does not have a drive to extract assets.")
            return False
        # taking the drive away from target
        attacker_storage.remove(drive)
        moved = 0 #moving the decrypted assest from the target's storage
        for item in list(target_rig.get_storage()):
            if item.get_encrypted() == False:
                self.__inventory.append(item)
                target_rig.get_storage().remove(item)
                moved += 1
        print(f"{self.__name} extracted {moved}  decrypted assets from {target_rig.get_name()}")
        return True

    # this method is developed if check in  inventory  and storage if it has a security chip
    def has_security_chip(self):
        for item in self.__inventory:
            if item.get_name() == "Security Chip" and item.get_encrypted() == False:
                return True
        if self.__rig != False:
            for item in self.__rig.get_storage():
                if item.get_name() == "Security Chip" and item.get_encrypted() == False:
                    return True
        return False

    # encrypy_inventory method to encrypt the asset inside the inventory in order to secure the asset
    def encrypt_inventory(self, asset_name):
        for item in self.__inventory:
            if item.get_name() == asset_name:
                if not self.has_security_chip():
                    print(f"Encryption rquires a security chip in order to encrypt.")
                    return False
                if item.get_encrypted():
                    print(f"{asset_name} us already encrypted.")
                    return False
                item.encrypt()
                print(f"{asset_name} in inventory is encrypted.")
                return True
        print(f"{asset_name} found in inventory.")
        return False

    # this methods come in hand when user's want to trasnfer the asset as transferring only works it is encrypted
    def decrypt_inventory(self, asset_name):
        for item in self.__inventory:
            if item.get_name() == asset_name:
                if not self.has_security_chip():
                    print(f"Decryption rquires a security chip in order to decrypt.")
                    return False
                if not item.get_encrypted():
                    print(f"{asset_name} us already decrypted.")
                    return False
                item.decrypt()
                print(f"{asset_name} in inventory is decrypted.")
                return True
        print(f"{asset_name} is not found in inventory.")
        return False

    # this is will encrypt the asset inside the rig and needs security chip to encrypt
    def encrypt_rig(self, asset_name):
        if self.__rig == False:
            print(f"{self.__name} does not have a rig to encrypt.")
            return False
        storage = self.__rig.get_storage()
        for asset in storage:
            if asset.get_name() == asset_name:
                if not self.has_security_chip():
                    print(f"Encryption rquires a security chip in order to encrypt.")
                    return False
                if asset.get_encrypted():
                    print(f"{asset_name}  already encrypted.")
                    return False
                asset.encrypt()
                print(f"{asset_name} in rig is encrypted.")
                return True
        print(f"{asset_name} is not found in rig.")
        return False

    # this is will decrypt the asset inside the rig but it should have a secuirty chip
    def decrypt_rig(self, asset_name):
        if self.__rig == False:
            print(f"{self.__name} does not have a rig to decrypt.")
            return False
        storage = self.__rig.get_storage()
        for item in storage:
            if item.get_name() == asset_name:
                if not self.has_security_chip():
                    print(f"Decryption rquires a security chip in order to decrypt.")
                    return False
                if not item.get_encrypted():
                    print(f"{asset_name} already decrypted.")
                    return False
                item.decrypt()
                print(f"{asset_name} in rig is decrypted.")
                return True
        print(f"{asset_name} is not found in rig.")
        return False

    # this will upgrade the rig it is has a hardware patch otherwise it will decline
    def upgrade_rig(self):
        if self.__rig == False:
            print(f"{self.__name} does not have a rig to upgrade.")
            return False
        for asset in list(self.__inventory):
            if asset.get_name() == "Hardware Patch" and asset.get_encrypted() == False:
                self.__inventory.remove(asset)
                self.__rig.upgrade()
                print(f"{self.__name} has upgraded {self.__rig.get_name()} successfully.")
                return True
        print(f"{self.__name} doesn't have a Hardware patch to uprage the rig")
        return False

    # this is scan the asset name in inventory if found it will remove from the inventory
    def scan_inventory(self, asset_name):
        for item in self.__inventory:
            if item.get_name() == asset_name:
                self.__inventory.remove(item)
                print(f"{self.__name} has removed {item.get_name()} from inventory.")
                return item
        print(f"{asset_name} not in inventory.")
        return False

    # this method is used to transfer the asset from the from hacket's inventory to rig' storage
    def store_asset(self, asset_name):
        if self.__rig == False:
            print(f"{self.__name} does not have a rig to store.")
            return False
        if asset_name is not True:
            for item in list(self.__inventory):
                if item.get_name() == asset_name:
                    if item.get_encrypted():
                        print(f"{asset_name} is encrypted and cannot be store until decrypted.")
                        return False
                    self.__rig.store_asset(item)
                    self.__inventory.remove(item)
                    print(f"{self.__name} has store {asset_name} in {self.__rig.get_name()}.")
                    return True
            print(f"{asset_name} not in inventory.")
            return False

    # this is method in order to transfer between the storage and inventory well this one specifically removes the asset from storage of rig and add it into the hacker's inventory
    def retrieve_asset(self, asset_name):
        if self.__rig == False:
            print(f"{self.__name} does not have a rig to retrieve.")
            return False
        storage = self.__rig.get_storage()
        if asset_name != "":
            for asset in list(storage):
                if asset.get_name() == asset_name:
                    if asset.get_encrypted():
                        print(f"{asset_name} is encrypted and cannot be retrieved.")
                        return False
                    storage.remove(asset)
                    self.__inventory.append(asset)
                    print(f"{asset_name} in retrieved from {self.__rig.get_name()}.")
                    return True
            print(f"{asset_name} not found in inventory.")
            return False
        for item in list(storage):
            if not item.get_encrypted():
                storage.remove(item)
                self.__inventory.append(item)
        print(f"All decrypted assets retrieved from {self.__rig.get_name()}")
        return True

    # adding string conversion method
    def __str__(self):
        invetory_item = []
        for items in self.__inventory:
            invetory_item.append(items.get_name())
        rig_name = "No Rig"
        if self.__rig != False:
            rig_name = self.__rig.get_name()

        return f"{self.__name} | Rig: {rig_name} | Trace Level: {self.__trace_level} | Inventory: {invetory_item}"


# h1 = Hacker("TestHacker")
# t1 = Rig("Target 1")
# print(h1)
# h1.add_trace(2)
# h1.add_trace(5)
# print(h1)
# h1.reduce_trace(4)
# h1.reduce_trace(22)
# print(h1)
# h1.acquire_rig("NoRigggg")
# print(h1)
# h1.launch_data_spike(t1)
# h1.launch_data_spike(t1)
# print(h1)
# h1.extract_data_spike(t1)
# print(h1)
# h1.encrypt_inventory("Data Spike")
# h1.decrypt_inventory("Data Spike")
# h1.encrypt_rig(t1)
# h1.decrypt_rig(t1)
# h1.scan_inventory("Data Spike")
# h1.store_asset("Data Spike")
# h1.retrieve_asset("Data Spike")
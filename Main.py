"""
File: main.py
Description: <A brief description of this Python module.>
Author: Krish Sanjaybhai Bhadani
ID: 110429045
Username: bhaks003
This is my own work as defined by the University's Academic Misconduct Policy.
"""


from Hacker import Hacker
from Asset import asset
from Rig import Rig

def print_head(title):
    print()
    print(85*'-')
    print(20*"-",title,20*"-")
    print(85*'-')

def test_acquire_and_upgrade_rig():
    # Setup
    print_head("Creating Hackers, rigs and few assets")
    # assigning hacker
    hacker_1 = Hacker("JackSparrow")
    hacker_2 = Hacker("Neon")

    # hacker acquiring rig
    hacker_1.acquire_rig("TheBlackPearl")
    hacker_2.acquire_rig("TheBlackSuit")

    # creating a seperate rig to use in battles
    Rig_1 =  Rig("TheBlackPearl")
    Rig_2 = Rig("TheBlackSuit")

    print(hacker_1)
    print(hacker_2)
    print(Rig_1)

    # storing and transfering invertory to storage
    print_head("Storing and Retrieving Assets")
    # to retrieve asset from the attacker rig
    hacker_1.retrieve_asset("Removable Drive")
    hacker_1.store_asset("Removable Drive")
    print(hacker_1)

    # test incudes about encrpytion and decrption as trying without a security chip
    print_head("Trying encryption with out security chip")
    hacker_1.retrieve_asset("Data Spike") #getting one into inventory to attempt encryptiomn
    hacker_1.encrypt_inventory("Data Spike") # expected to be fail no chip found
    hacker_1.decrypt_inventory("Data Spike") # expected output would be it is already decrypyted

    # now we will try on encrypt ands decrypt in the rig without a chip
    hacker_1.store_asset("Data Spike")
    hacker_1.encrypt_rig("Data Spike")
    hacker_1.decrypt_rig("Data Spike")

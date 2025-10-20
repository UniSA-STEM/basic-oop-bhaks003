"""
File: main.py
Description: Instantiating Hacker, Rig, Asset class and testing functionality which includes demonstration of upgrading, repair, extracting, encrypting , decrypting, transferring and many more.
Author: Krish Sanjaybhai Bhadani
ID: 110429045
Username: bhaks003
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from traceback import print_tb

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

    # upgrading the rig without the Hardware pathc
    print_head("Uprading the RIG (no Hardware Patch)")
    hacker_1.upgrade_rig() #missing hardware patch message would appear

    # demonstration on repair would work
    print_head("Repair Demo (rig will take some hit and then get repaired as well)")
    Rig_2.take_hit()
    Rig_2.take_hit()
    print("Before Repair", Rig_2)
    Rig_2.repair()
    print("After Repair", Rig_2)


    # battle and trace extraction
    print_head("Battling, trae level and extraction ")
    hacker_1.launch_data_spike(Rig_1)
    hacker_1.add_trace(2)

    # breaking the target so that exrtaction can be done
    Rig_1.take_hit() #might be wondering why even after attacking must making sure even it add and totals all the hit
    print("before Launching", hacker_1)


    # extraction ofn asset from the target if broken but attacker should have a removable drive in order to do the extraction
    hacker_1.extract_data_spike(Rig_1)
    print("After Extracting", hacker_1)
    print("After Extracting", Rig_1)

    # attacking while high trace level
    print_head("Attacking while trace level is high")
    for level in range(10):
        hacker_1.add_trace(1)
    hacker_1.launch_data_spike(Rig_1)
    print(hacker_1)

    # upgrading without a rig
    print_head("Testing to upradge without a rig")
    no_rig = Hacker("RigNOooo")
    no_rig.upgrade_rig()
    print(no_rig)

    # final updates
    print_head("Final States of each")
    print(hacker_1)
    print(hacker_2)
    print(Rig_2)
    print(Rig_1)

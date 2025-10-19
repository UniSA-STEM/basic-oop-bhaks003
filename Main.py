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
    print_head("Creating Hackers, rigs and few assets")
    hacker_1 = Hacker("JackSparrow")
    hacker_2 = Hacker("Neon")

    hacker_1.acquire_rig("TheBlackPearl")
    hacker_2.acquire_rig("TheBlackSuit")

    Rig_1 =  Rig("TheBlackPearl")
    Rig_2 = Rig("TheBlackSuit")

    print(hacker_1)
    print(hacker_2)
    print(Rig_1)

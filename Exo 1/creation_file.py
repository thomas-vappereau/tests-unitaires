# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 11:12:17 2024

CREATION FILE

@author: VAPPEREAU
"""

def create_file():
    with open("bonjour.txt", "w") as file:
        file.write("Bonjour")

create_file()
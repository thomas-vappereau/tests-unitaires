# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 11:33:43 2024

@author: VAPPEREAU
"""
import os
import pytest

@pytest.fixture
def creation_file():
    file = open("test.txt", "w")
    file.write("Bonjour monde")
    file.close()
    file = open("test.txt", "r")
    
    yield file
    
    file.close()
    os.remove("test.txt")
    

def test_file_is_empty(creation_file):
    content = creation_file.read()
    assert content != "", "Le fichier est vide"
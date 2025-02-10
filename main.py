from config import ALPHA, CARACTER, arr
import random
import os
import time

def clean_terminal():
    time.sleep(3)
    os.system("cls")

def size(arr, n):
    count = 0

    while count < n:
        arr.append(" ") 
        count += 1
    return arr


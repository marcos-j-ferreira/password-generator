from config import ALPHA, CARACTER, NUMBER, arr
import random
import os
import time

def clean_terminal():
    time.sleep(2)
    os.system("cls")

def insert_all(n):
    c = 0
    while c < n:
        c += 1
        for i in range( n // 2):
            c += 1
            l = random.choice(ALPHA)
            arr.append(l)
       
        nu = random.choice(NUMBER)
        arr.append(nu)

        ca = random.choice(CARACTER)
        arr.append(ca)
    return arr

def insert_letter(n):
    arr.extend(random.choice(ALPHA) for _ in range(n))
    return arr
 
def insert_number(n):
    arr.extend(random.choice(NUMBER)for _ in range(n))
    return arr

def insert_especial(n):
    arr.extend(random.choice(CARACTER)for _ in range(n))
    return arr

def string(c):

    n = c
    lista = insert_all(n)
    new_list = "".join([str(x) for x in lista])
    return new_list
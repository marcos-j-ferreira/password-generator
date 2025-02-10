from config import ALPHA, CARACTER, arr
import random
import os


def size(arr, n):
    count = 0

    while count < n:
        arr.append(" ") 
        count += 1
    return arr


a = size(arr, 5)


print(a)



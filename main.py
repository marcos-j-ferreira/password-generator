from config import ALPHA, CARACTER, NUMBER, arr
import random
import os
import time

def clean_terminal():
    #time.sleep(2)
    os.system("cls")

def loading_screen(duration=2):
    print("Gerando sua senha", end="")
    for _ in range(duration * 3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print() 

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

def string(lista):

    new_list = "".join([str(x) for x in lista])
    return new_list

def main():
    cc = 0
    nn = 10

    while cc < 2:
        clean_terminal()

        print("\n -- Gere sua senha -- \n")

        options = {
            "t": input("Qaul Tamanho da sua Senha: "),
            "l": input("Você quer que tenha letras? (y/x): "),
            "n": input("Você quer que tenha números? (y/x): "),
            "c": input("Você quer que tenha caractere especial? (y/x): ")
        }

        nn = options["t"]

        clean_terminal()
        loading_screen()

        number = int(nn)

        d = number // 3

        if options["l"] == "y":
            insert_letter(d + 1)
        if options["n"] == "y":
            insert_number(d + 1)
        if options["c"] == "y":
            insert_especial(d - 1)

        cc += 2

    password = string(arr)
    print("Sua senha gerada: ", password)

main()

import show
import numpy as np
import Jatek
from state import State



def jatek():
    tabla = np.array([[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]])
    print("Kezdo allapot: ")
    show.show(tabla)
    print("1. round")
    print("Gep lepese: ")
    show.show(tabla)
    lepes(tabla, 1)

def play():
    hanyadik = int(input('Hanyadik jatekos szeretnél lenni {1,2}? '))
    strat = int(input('Válassz strategiat! 1: azonos, 2: telites '))
    tabla = np.array([[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]])
    print("Kezdo allapot: ")
    show.show(tabla)
    i = 1
    if hanyadik == 1:
        Jatek.lepes(tabla, i)
        State.computer_step(tabla, strat)
        print("Gép lépése: ")
        show.show(tabla)
        i += 1
    else:
        State.computer_step(tabla, strat)
        print("Gép lépése: ")
        show.show(tabla)
        Jatek.lepes(tabla, i)
        i += 1



if __name__ == "__main__":
    play()
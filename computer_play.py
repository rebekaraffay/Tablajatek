import show
import numpy as np
import Jatek
import random
import json


def check(tabla, strat):
    """
        True: még megy tovább a játék.
        False: vége van, valaki nyert.
    """
    if Jatek.van_sor(tabla) or Jatek.van_oszlop(tabla) or Jatek.azonos_sor_oszlop(tabla):
        if strat == 1:
            show.show(tabla, "A gep nyert")
        if strat == 2:
            show.show(tabla, "On nyert")
        return False
    elif -1 not in tabla:
        if strat == 1:
            show.show(tabla, "On nyert")
        if strat == 2:
            show.show(tabla, "A gep nyert")
        return False
    return True


# Hibaosztályok

class Error(Exception):
    pass

class SorOutOfRange(Error):
    pass

class OszlopOutOfRange(Error):
    pass

class ErtekOutOfRange(Error):
    pass

class NotEmpty(Error):
    pass


def jatekos_lep(tabla, strat, hanyadik, i):
    '''
        A felhasználótól elkérjük, hogy hova szeretne rakni, majd annak az értékét.
        Ezután a gép "tükrözi" a lépését.
    '''
    # felhasznalo lepese
    # helyes lepest hajtott-e vegre

    while True:
        try:
            sor_index = int(input('A sor indexe {1,2,3}: ')) - 1
            if sor_index not in range(0, 3):
                raise SorOutOfRange
            oszlop_index = int(input('Az oszlop indexe {1,2,3}: ')) - 1
            if oszlop_index not in range(0, 3):
                raise OszlopOutOfRange
            elif tabla[sor_index][oszlop_index] != -1:
                raise NotEmpty
            break
        except SorOutOfRange:
            print("A sor indexének {1,2,3}-belinek kell lennie, próbálja újra.")
        except OszlopOutOfRange:
            print("Az oszlop indexének {1,2,3}-belinek kell lennie, próbálja újra.")
        except NotEmpty:
            print("Csak üres mezőbe írhat, próbálja újra.")

    while True:
        try:
            ertek = str(input('Az ertek {x,o}: '))
            if ertek not in ['x', 'o']:
                raise ErtekOutOfRange
            break
        except ErtekOutOfRange:
            print("Az értéknek {o, x}nek kell lennie.")

    ertek =Jatek.value_changer(ertek)

    tabla[sor_index][oszlop_index] =ertek
    if hanyadik == 1:
        print(i, ". round:")
        i = i+1
    print("Felhasznalo lepese: ")
    show.show(tabla)

    if check(tabla,strat):
        if hanyadik == 2:
            print(i, ".round")
            i = i+1
            print("A gep lepese: ")
        tabla = computer_step(tabla, strat)
        if check(tabla, strat):
            jatekos_lep(tabla, strat, hanyadik, i)
    else:
        return None



def computer_step(tabla, strategy):
    '''
    1-es stratégia, ha azonosra törekszik mit lépjen a gép.
    2-es, ha teli táblára.
    Kész szótárból szedi ki a lépéseket. (ELtároltuk, hogy egy adott csúcsból hova érdemes lépni
    a különböző stratégiák esetén.
    '''

    with open("nyero_lepesek.json", "r") as read_file:
        strat_1 = json.load(read_file)

    with open("veszto_lepesek.json", "r") as read_file:
        strat_2 = json.load(read_file)

    if strategy == 1:
        #index = random.randint(0, len(strat_1[tabla])-1)
        step = strat_1[str(tabla)][0]
        print("haha", step, type(step))
    else:
        #index = random.randint(0, len(strat_2[tabla])-1)
        step = strat_2[str(tabla)][0]
        print("hihi", step, type(step))

    step = step.replace("[ ", "[")
    print("alma", step)
    step = step.replace("]", "")  # elhagyjuk a fölösleges elemeket
    step = step.replace("[", "")
    step = step.split("\n")
    for i in range(len(step)):
        step[i] = step[i].replace("  ", " ").split(" ")
    del step[1][0]
    del step[2][0]
    for i in range(3):
        for j in range(3):
            step[i][j] = int(step[i][j])

    step = np.array(step)
    show.show(step)
    return step

def final_game():

    while True:
        try:
            hanyadik = int(input('Hanyadik jatekos szeretnél lenni {1,2}? '))
            if hanyadik not in range(0,2):
                raise ErtekOutOfRange
            strat = int(input('Válassz strategiat! 1: telítés, 2: azonos '))
            if strat not in range(0,2):
                raise ErtekOutOfRange
            break
        except ErtekOutOfRange:
            print("Az értéknek 1-nek vagy 2-nek kell lennie.")

    tabla = np.array([[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]])
    print("Kezdo allapot: ")
    show.show(tabla)
    if hanyadik == 1:
        jatekos_lep(tabla, strat, hanyadik, 1)
    else:
        print("1. round")
        print("A gep lepese: ")
        tabla = computer_step(tabla, strat)
        jatekos_lep(tabla, strat, hanyadik, 2)

if __name__ == "__main__":
    final_game()
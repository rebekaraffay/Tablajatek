import show
import numpy as np
import Jatek
import random
import json

def check():
    pass        # todo


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


def jatekos_lep(tabla):
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

    ertek = Jatek.value_changer(ertek)

    tabla[sor_index][oszlop_index] = ertek

    print("Felhasznalo lepese: ")
    show.show(tabla)

    # todo: check


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
        #index = random.randint (0, len(strat_2[tabla])-1)
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

    np.array(step)
    print(step[0])
    step = [np.reshape([j for j in step[i]], (3, 3)) for i in range(len(step))]

    show.show(step)
    tabla = step
    return tabla


def play():
    hanyadik = int(input('Hanyadik jatekos szeretnél lenni {1,2}? '))
    strat = int(input('Válassz strategiat! 1: telítés, 2: azonos '))        # így lesz a gépnek beadott stratégia jó
    tabla = np.array([[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]])
    print("Kezdo allapot: ")
    show.show(tabla)
    i = 1
    if hanyadik == 1:
        print(i, ". round:")
        jatekos_lep(tabla)
        print(type(tabla))
        print("jatekos lepese utan a tabla: ", tabla)
        computer_step(tabla, strat)
        tabla = computer_step(tabla, strat)
        print("gép lepese utan a tabla: ", tabla)
        print("Gép lépése: ")
        i += 1



if __name__ == "__main__":
    play()
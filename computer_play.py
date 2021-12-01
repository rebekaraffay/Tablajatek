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
            show.show(tabla, "A gép nyert")
        if strat == 2:
            show.show(tabla, "Gratulálunk, Ön nyert!")
        return False
    elif -1 not in tabla:
        if strat == 1:
            show.show(tabla, "Gratulálunk, Ön nyert!")
        if strat == 2:
            show.show(tabla, "A gép nyert")
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
        Ellenőrizzük közben, hogy helyes válaszokat írt-e be.
        Ezután a gép "tükrözi" a lépését.
    '''
    # Hova szeretne lépni a felhasználó
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
    # Mit szeretne lépni a felhasználó
    while True:
        try:
            ertek = str(input('Az ertek {x,o}: '))
            if ertek not in ['x', 'o']:
                raise ErtekOutOfRange
            break
        except ErtekOutOfRange:
            print("Az értéknek {o, x}nek kell lennie.")
    # {0,1}-nek kezeli az algoritmus, de {o,x}-et mutat mindig a tábla (0=o, 1 = x).
    ertek = Jatek.value_changer(ertek)
    # megváltoztatjuk a táblát a felhasználó lépésére, megmutatjuk az állást
    tabla[sor_index][oszlop_index] =ertek
    if hanyadik == 1:
        print(i, ". round:")
        i = i+1
    print("Felhasznalo lepese: ")
    show.show(tabla)
    # ellenőrizzük, hogy vége van-e a játéknak
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


def get_different_index(parent: np.ndarray, child: np.ndarray):
    '''
        Megadja, hogy melyik mezőre léptek a gyerekben.
    '''
    difference = parent - child
    for i in range(3):
        for j in range(3):
            if difference[i][j] != 0:
                return i,j

def opposite_step(child: np.ndarray, parent:np.array, i: int, j: int):
    '''
        Ha egy szülőnek van vesztes gyereke, akkor azt elkerülvén a gyerekbe lépés ellentettjét hajtuk végre.
        Már elkértük az új lépés mezőjének indexeit a get_different_index() fv-nyel.
    '''
    if child[i][j] == 0:
        parent[i][j] = 1
    else:
        parent[i][j] = 0
    return parent

def convert_to_nparray(child: str):
    '''
        A jsonban csak stringként tudjuk tárolni az adatokat, viszont nekünk np.array kell és elég problémás az
        átalakítása.
        Ezt biztosan lehetett volna okosabban, kevésbé rizikósan megoldani, nekünk nem sikerült.
        Eltávolítunk minden fölösleges karaktert és megpróbáljuk jól splitelni, hogy minden
        a megfelelő helyre kerüljön.
    '''
    child = child.replace("[ ", "[")
    child = child.replace("]", "")  # elhagyjuk a fölösleges elemeket
    child = child.replace("[", "")
    child = child.split("\n")
    for i in range(len(child)):
        child[i] = child[i].replace("  ", " ").split(" ")
    del child[1][0]
    del child[2][0]
    for i in range(3):
        for j in range(3):
            child[i][j] = int(child[i][j])

    step = np.array(child)
    return step

def computer_step(tabla, strategy):
    '''
        1-es stratégia, ha azonosra törekszik mit lépjen a gép.
        2-es, ha teli táblára.
        Kész szótárból szedi ki a lépéseket. (ELtároltuk, hogy egy adott csúcsból hova érdemes lépni
        a különböző stratégiák esetén.
        A 2-esnél nagyon rosszul működik a nyertes / vesztes gyerekek számának arányán alapuló stratégia,
        ezért kicsit rásegítettünk. Nem ismerte fel azokat a helyzeteket, amikor már csak 1 lépés hiányzott a
        biztos veszteséghez, ezért azoknál külön meghatározzuk a lépéseit. Ha egy csúcsnak van vesztes gyereke,
        azokat eltároltuk egy újabb szótárban. Ha több van, akkor is csak egyet tudunk megúszni, ezért az elsőt
        elrontjuk úgy, hogy pont az ellenkezőjét lépjük.
    '''
    # szótárak beolvasása jsonból
    with open("nyero_lepesek.json", "r") as read_file:
        strat_1 = json.load(read_file)

    with open("veszto_lepesek.json", "r") as read_file:
        strat_2 = json.load(read_file)

    with open("azonos_esetben_vesztok.json", "r") as read_file:
        dict_loser_children = json.load(read_file)

    if strategy == 1:
        index = random.randint(0, len(strat_1[str(tabla)])-1)
        step = strat_1[str(tabla)][index]


    elif dict_loser_children[str(tabla)] != []: # ha 1 lépésre vagyunk vesztéstől
        index = random.randint(0, len(dict_loser_children[str(tabla)]) - 1)
        child = dict_loser_children[str(tabla)][index] # ha több van, akkor mindegy, csak egyet tudunk kivédeni
        child = convert_to_nparray(child)             # most már np.array
        i, j = get_different_index(tabla, child)
        step = opposite_step(child, tabla, i, j) # ellenkező lépés végrehajtása, mint amivel instant veszítene
        show.show(step)
        return step

    else:
        index = random.randint(0, len(strat_2[str(tabla)])-1)
        step = strat_2[str(tabla)][index]

    step = step.replace("[ ", "[")
    step = step.replace("]", "")  # elhagyjuk a fölösleges elemeket
    step = step.replace("[", "")
    step = step.split("\n")
    for i in range(len(step)):
        step[i] = step[i].replace("  ", " ").split(" ")
    del step[1][0]
    del step[2][0]
    print("korte", step)
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
            if hanyadik not in range(1,3):
                raise ErtekOutOfRange
            strat = int(input('Válassz strategiat! 1: telítés, 2: azonos '))
            if strat not in range(1,3):
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
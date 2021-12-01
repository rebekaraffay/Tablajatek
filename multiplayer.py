import show
import numpy as np
import Jatek

# ket jatekosra varians, egy gepnel ketten tudjak jatszani

# Hibaosztályok:

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


def check(tabla, strat):
    """
        True: még megy tovább a játék.
        False: vége van, valaki nyert.
    """
    if Jatek.van_sor(tabla) or Jatek.van_oszlop(tabla) or Jatek.azonos_sor_oszlop(tabla): #ha teljesulnek a nyeresi feltetelek
        if strat == 2:
            show.show(tabla, title="Az elso jatekos nyert")
            return False
        else:
            show.show(tabla, title="A masodik jatekos nyert")
            return False
    elif -1 not in tabla:
        if strat == 2:
            show.show(tabla, title="A masodik jatekos nyert")
            return False
        else:
            show.show(tabla, title="Az elso jatekos nyert")
            return False
    # ha nem teljesulnek a nyeresi feltetelek:
    return True


def jatekos_lep(tabla, strat, i):
    """A felhasználótól elkérjük, hogy hova szeretne rakni, majd annak az értékét.
            Ellenőrizzük, hogy helyes lepes-e, vege van-e."""

    # elso felhasznalo lepese
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
    tabla[sor_index][oszlop_index] = ertek # a jatekos lep

    if i % 2 == 1:
        print(i // 2 + 1, ". round")
        print("Elso jatekos lepese: ")

        show.show(tabla)

        if check(tabla, strat):  # ha nem nyert, akkor lephet a kovetkezo
            jatekos_lep(tabla, strat, i+1)
    else:
        print("Masodik jatekos lepese: ")

        show.show(tabla)

        if check(tabla, strat):  # ha nem nyert, akkor lephet a kovetkezo
            jatekos_lep(tabla, strat, i+1)

    return tabla


def multiplayer():
    while True:
        try:
            strat = int(input('Elso jatekos valassz strategiat! 1: telites, 2: azonos: ')) # helyes erteket adott-e meg
            if strat not in range(1,3):
                raise ErtekOutOfRange
            break
        except ErtekOutOfRange:
            print("Az értéknek 1-nek vagy 2-nek kell lennie.")

    tabla = np.array([[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]) # kezo allas
    print("Kezdő állapot: ")
    show.show(tabla)
    jatekos_lep(tabla, strat, 1)  # jatekosok lepnek, amig valamelyikuk nem nyer


if __name__ == "__main__":
    multiplayer()

import show
import numpy as np
import Jatek

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


def check(tabla, strat):
    """
        True: még megy tovább a játék.
        False: vége van, valaki nyert.
            1. nyert: Ha van csupa 0 vagy azonos sor / oszlop vagy
            2. nyert: Ha az előzőek nem teljesülnek és tele van az egész.
    """
    if strat == 1:  # 1-nek jó:
        van_nulla = (Jatek.van_sor(tabla) or Jatek.van_oszlop(tabla))
        if van_nulla:
            win = True
        else:
            win = Jatek.azonos_sor_oszlop(tabla)
        # 2. nyer:
        if -1 not in tabla and not(win):
            show.show(tabla, title="A masodik jatekos nyert")
            return False
        # 1. nyert
        elif win:
            show.show(tabla, title="Az elso jatekos nyert")
            return False
        # meg nincs vege
        else:
            return True
    if strat == 2:  # 2-nek jó:
        van_nulla = (Jatek.van_sor(tabla) or Jatek.van_oszlop(tabla))
        if van_nulla:
            win = True
        else:
            win = Jatek.azonos_sor_oszlop(tabla)
        # 2. nyer:
        if -1 not in tabla and not(win):
            show.show(tabla, title="Az elso jatekos nyert")
            return False
        # 1. nyert
        elif win:
            show.show(tabla, title="A masodik jatekos nyert")
            return False
        # meg nincs vege
        else:
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
            ertek = int(input('Az ertek {0,1}: '))
            if ertek not in range(0, 2):
                raise ErtekOutOfRange
            break
        except ErtekOutOfRange:
            print("Az értéknek {0,1}-belinek kell lennie.")

    tabla[sor_index][oszlop_index] = ertek  # beirtuk a jatekos altal megadott erteket a megfelelo helyre
    print(i, ". round")
    if i%2==1:
        print("Elso jatekos lepese: ")

        show.show(tabla)

        if check(tabla, strat):
            jatekos_lep(tabla, strat, i+1)
    else:
        print("Masodik jatekos lepese: ")

        show.show(tabla)

        if check(tabla, strat):
            jatekos_lep(tabla, strat, i+1)

    return tabla


def multiplayer():
    strat = int(input('Elso jatekos valassz strategiat! 1: azonos, 2: telites: '))
    tabla = np.array([[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]])
    print("Kezdo allapot: ")
    show.show(tabla)
    i = 1
    jatekos_lep(tabla, strat, i)


if __name__ == "__main__":
    multiplayer()

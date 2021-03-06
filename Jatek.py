import numpy as np
import show

# Ez annak a variansa, hogy a gep kezd es azonosra torekszik
# Itt mindig a gep nyer

def azonos_sor_oszlop(tabla):
    '''
        Eldönti, hogy van-e 2 egyforma teli oszlop vagy sor.
    '''
    for i in range(3):
        for j in range(3):
            if i != j:
                # ez a 2 sor teli egyforma-e?
                if np.array_equal(tabla[i], tabla[j]) and -1 not in tabla[i]:
                    return True
                # ez a 2 oszlop teli egyforma-e?
                if np.array_equal(tabla[:, i], tabla[:, j]) and -1 not in tabla[:, i]:
                    return True
    return False


def van_oszlop(tabla):
    '''
        Eldonti, hogy van-e csupa 0 oszlop.
    '''
    for i in range(3):
        van = True
        for j in range(3):
            if tabla[j][i] != 0:
                van = False
        if van:
            return True
    return False


def van_sor(tabla):
    '''
        Eldonti, hogy van-e csupa 0 sor.
    '''
    for i in range(3):
        van = True
        for j in range(3):
            if tabla[i][j] != 0:
                van = False
        if van:
            return True
    return False

def check(tabla):
    """
        True: még megy tovább a játék.
        False: vége van, valaki nyert.
            1. nyert: Ha van csupa 0 vagy azonos sor / oszlop vagy
            2. nyert: Ha az előzőek nem teljesülnek és tele van az egész.
    """
    if van_sor(tabla) or van_oszlop(tabla) or azonos_sor_oszlop(tabla):
        show.show(tabla, title="A gép nyert")
        return False

    elif -1 not in tabla:
        show.show(tabla, title="Gratulálunk, Ön nyert!")
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

def value_changer(value):
    """Atirjuk a beadott x/o-t 1/0-ra, hogy tudjunk vele dolgozni"""
    if value == 'x':
        return 1
    if value == 'o':
        return 0

def lepes(tabla, i):
    '''
        A felhasználótól elkérjük, hogy hova szeretne rakni, majd annak az értékét.
        Ezután a gép "tükrözi" a lépését.
    '''
    # felhasznalo lepese
    # helyes lepest hajtott-e vegre
    while True:
        try:
            sor_index = int(input('A sor indexe {1,2,3}: '))-1
            if sor_index not in range(0,3):
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

    ertek = value_changer(ertek)

    tabla[sor_index][oszlop_index] = ertek # itt lep a felhasznalo

    print("A játékos lépése: ")
    show.show(tabla) # kiiratjuk a lepest

    # gep lepese
    if check(tabla):
        i = i + 1
        print(i, ". round:")
        if oszlop_index == 1:
            tabla[2 - sor_index][oszlop_index] = ertek  # tukrozzuk a jatekos lepeset
        else:
            tabla[sor_index][2 - oszlop_index] = ertek
        print("A gép lépése: ")
        show.show(tabla)
        if check(tabla): #megnezzuk, hogy nyert-e, ha nem, akkor ujra a jatekos jon
            lepes(tabla,i)
    else:
        return None


def jatek():
    tabla = np.array([[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]) #kezdo allas
    print("Kezdő állapot: ")
    show.show(tabla)
    tabla[1, 1] = 0 # a gep elso lepeset konkretan megadjuk
    print("1. round")
    print("A gép lépése: ")
    show.show(tabla)
    lepes(tabla, 1)


if __name__ == "__main__":
    jatek()



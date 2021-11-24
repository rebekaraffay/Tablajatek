"""3*3-as táblán játsza két személy, kétféle (0 vagy 1) jel bár-
melyikét írhatják a mezőkbe (nincs saját jel). Egyikük (előre
meg kell állapodni, hogy melyikük) nyer, ha van két  egyforma (teli)
sor vagy oszlop, vagy ha 3 darab 0 került egy vonalba. Ha kilenc
jel elhelyezése után egyik fenti feltétel sem  teljesül,
másikuk a győztes."""

import numpy as np
import show

#todo def valuechanger itt is, mert jobb lenne, ha x-et es o-t irna be a felhasznalo
#todo print jatekszabalyok az elejen

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
        van csupa 0 oszlop.
    '''
    for i in range(3):
        van = True
        for j in range(3):
            if tabla[j,i] != 0:
                van = False
        if van:
            return True
    return False

def van_sor(tabla):
    '''
        Van csupa 0 sor.
    '''
    for i in range(3):
        van = True
        for j in range(3):
            if tabla[i,j] != 0:
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
    # 1-nek jó:
    van_nulla = (van_sor(tabla) or van_oszlop(tabla))
    if van_nulla:
        win = True
    else:
        win = azonos_sor_oszlop(tabla)
    # 2. nyer:
    if -1 not in tabla and not(win):
        print("The player won.")
        return False
    # 1. nyert
    elif win:
        print("The computer won.")
        return False
    # meg nincs vege
    else:
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


def lepes(tabla):
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
            ertek = int(input('Az ertek {0,1}: '))
            if ertek not in range(0, 2):
                raise ErtekOutOfRange
            break
        except ErtekOutOfRange:
            print("Az értéknek {0,1}-belinek kell lennie.")

    tabla[sor_index][oszlop_index] = ertek

    print("Felhasznalo lepese: ")
    show.show(tabla)

    check(tabla)

    # gep lepese
    if check(tabla):
        if oszlop_index == 1:
            tabla[2 - sor_index][oszlop_index] = ertek
        else:
            tabla[sor_index][2 - oszlop_index] = ertek
        print("Gep lepese: ")
        show.show(tabla)
    return tabla


def jatek():
    tabla = np.array([[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]])
    print("Kezdo allapot: ")
    show.show(tabla)
    tabla[1, 1] = 0
    print("Gep lepese: ")
    show.show(tabla)
    i = 0
    while check(tabla):
        i = i+1
        print(i , ". round:")
        lepes(tabla)


if __name__ == "__main__":
    jatek()



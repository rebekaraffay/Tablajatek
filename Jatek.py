"""3*3-as táblán játsza két személy, kétféle (0 vagy 1) jel bár-
melyikét írhatják a mezőkbe (nincs saját jel). Egyikük (előre
meg kell állapodni, hogy melyikük) nyer, ha van két  egyforma (teli)
sor vagy oszlop, vagy ha 3 darab 0 került egy vonalba. Ha kilenc
jel elhelyezése után egyik fenti feltétel sem  teljesül,
másikuk a győztes."""

import numpy as np


def strat(tabla):
    '''URES MEZO JELE -1'''
    lista = [tabla[i, 0] == tabla[i, 2] for i in range(3)] + [tabla[0, 1] == tabla[2, 1]]
    index = lista.index(False)
    if index in range(3):
        if tabla[index, 0] == -1:
            tabla[index, 0] = tabla[index, 2]
        else:
            tabla[index, 2] = tabla[index, 0]
    else:
        if tabla[0, 1] == -1:
            tabla[0, 1] = tabla[2, 1]
        else:
            tabla[2, 1] = tabla[0, 1]

def azonos_sor_oszlop(tabla):
    for i in range(3):
        for j in range(3):
            if i != j:
                # ez a 2 sor teli egyforma-e?

                l = [np.where(tabla[i] == -1)]
                if np.array_equal(tabla[i], tabla[j]) and len(l)==0:
                    return True
                # ez a 2 oszlop teli egyforma-e?
                l = [np.where(tabla[:, i] == -1)]
                if np.array_equal(tabla[:, i], tabla[:, j]) and len(l)==0:
                    return True
    return False


def check(tabla):
    """
        True: még megy tovább a játék.
        False: vége van, valaki nyert.
    """
    l = [tabla[:, i] == np.array([0,0,0]) for i in range(3)] + [tabla[i, :] == np.array([0,0,0]) for i in range(3)]
    if np.any(l, where=True):
        win = True
    else:
        win = azonos_sor_oszlop(tabla)
    if not(np.any(tabla[:, :], where=-1)) and not(win):
        print("The second player won.")
        return False
    elif win:
        print("The first player won.")
        return False
    else:
        return True

def lepes(tabla):
    sor_index = input('A sor indexe: ')
    oszlop_index = input('Az oszlop indexe: ')
    ertek = input('Az ertek: ')
    tabla[int(sor_index)-1][int(oszlop_index)-1] = int(ertek)
    return tabla

def jatek():
    tabla = np.array([[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]])
    print(check(tabla))
    print(tabla)
    tabla[1, 1] = 0
    print(tabla)
    while check(tabla):
        lepes(tabla)
        check(tabla)
        if check(tabla):
            strat(tabla)
        check(tabla)




if __name__ == "__main__":
    jatek()
"""3*3-as táblán játsza két személy, kétféle (0 vagy 1) jel bár-
melyikét írhatják a mezőkbe (nincs saját jel). Egyikük (előre
meg kell állapodni, hogy melyikük) nyer, ha van két  egyforma (teli)
sor vagy oszlop, vagy ha 3 darab 0 került egy vonalba. Ha kilenc
jel elhelyezése után egyik fenti feltétel sem  teljesül,
másikuk a győztes."""

import numpy as np

def azonos_sor_oszlop(tabla):
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
    for i in range(3):
        van = True
        for j in range(3):
            if tabla[j,i] != 0:
                van = False
        if van:
            return True
    return False

def van_sor(tabla):
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
    """

    van_nulla= (van_sor(tabla) or van_oszlop(tabla))
    print(van_nulla, "nullak")


    if van_nulla:
        win = True
    else:
        win = azonos_sor_oszlop(tabla)

    print(win, "win")
    print(azonos_sor_oszlop(tabla), "azonosak")

    if -1 not in tabla and not(win):
        print("The second player won.")
        return False
    elif win:
        print("The first player won.")
        return False
    else:
        return True

def lepes(tabla):
    sor_index = int(input('A sor indexe: '))-1
    oszlop_index = int(input('Az oszlop indexe: '))-1
    ertek = int(input('Az ertek: '))
    tabla[sor_index][oszlop_index] = ertek
    print(tabla)
    check(tabla)
    if check(tabla):

        if oszlop_index==1:
            tabla[2-sor_index][oszlop_index] = ertek
        else:
            tabla[sor_index][2-oszlop_index] = ertek
        print(tabla)




    return tabla

def jatek():
    tabla = np.array([[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]])
    print(check(tabla))
    print(tabla)
    tabla[1, 1] = 0
    print(tabla)
    i = 0
    while check(tabla):
        print(i)
        i = i+1
        lepes(tabla)
        check(tabla)




if __name__ == "__main__":
    jatek()
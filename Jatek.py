"""3*3-as táblán játsza két személy, kétféle (0 vagy 1) jel bár-
melyikét írhatják a mezőkbe (nincs saját jel). Egyikük (előre
meg kell állapodni, hogy melyikük) nyer, ha van két  egyforma (teli)
sor vagy oszlop, vagy ha 3 darab 0 került egy vonalba. Ha kilenc
jel elhelyezése után egyik fenti feltétel sem  teljesül,
másikuk a győztes."""


def strat(tabla):
    '''URES MEZO JELE -1'''
    lista = [tabla[i, 0] == tabla[i, 2] for i in range(3)] + [tabla[0, 1] == tabla[2, 1]]
    index = lista.index('False')
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


def check(tabla):
    l = [tabla[:i] == 0 for i in range(3)] + [tabla[i:] == 0 for i in range(3)]
    if "True" in l:
        return True
    else:
        l = [tabla[:j] == tabla[:i] for i, j in range(3) if i != j and] + [tabla[j:] - tabla[i:] == 0 for i, j in
                                                                           range(3) if i != j]
        if "True" in l:
            return True
        else:
            return False


def jatek():
    tabla = np.array[[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
    print(tabla)
    tabla[1, 1] = 0
    print(tabla)
    while check != True:

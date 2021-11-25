import itertools as it
import time
import numpy as np
import Jatek
import networkx as nx


def nodes():
    """Megadja az osszes lehetseges tablaallast, most -1,1,0 ertekekkel es 3x3-as tablara"""
    a = it.product(range(-1, 2), repeat=9)  # az osszes lehetseges elem
    a = list(a)  # listaban
    a = [np.reshape([j for j in a[i]], (3, 3)) for i in range(len(a))]  # npmatrixok listajat adja vissza
    return a


def nyeromezo(tabla):
    """Nyero mezok annak, akinek az a celja, hogy vagy csupa 0 vagy ket azonos sor/oszlop legyen
    nyer = 1
    veszt = 0
    nem vegallapot = -1"""

    # a 0/azonosnak jo:
    van_nulla = (Jatek.van_sor(tabla) or Jatek.van_oszlop(tabla))
    if van_nulla:
        win = True
    else:
        win = Jatek.azonos_sor_oszlop(tabla)
    # veszto mezo
    if -1 not in tabla and not win:
        return True
    # nyero mezo
    elif win:
        return True

    else:  # se nem nyertes se nem vesztes
        return False


def elek(tabla):
    """egy mezonek az oseit adja vissza"""
    osok = []
    t = tabla.copy()
    for i in range(3):
        for j in range(3):
            if tabla[i][j] != -1:
                tabla[i][j] = -1
                if not nyeromezo(tabla):
                    osok.append((str(tabla), str(t)))  # t is kell, hogy ellista legyen. Igazabol majd stringesiteni kell, mert nxgraphnak csak olyan csucsa lehet
                tabla = t
    return osok


def ossz_el(lista):
    s = time.time()
    """Egy listaban szereplo osszes csucs oseit visszaadja"""
    ellista = [elek(lista[i]) for i in range(len(lista))]
    ellista = [item for sublist in ellista for item in sublist]
    print(ellista[:10])
    t = time.time()
    print(t-s)
    return ellista

if __name__ == "__main__":
    s = time.time()
    d = nx.DiGraph()
    d.add_edges_from(ossz_el(nodes()))
    t = time.time()
    print(t-s)
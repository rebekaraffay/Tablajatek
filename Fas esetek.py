import itertools as it
import numpy as np
import Jatek
import networkx as nx




def nodes():
    """Megadja az osszes lehetseges tablaallast, most -1,1,0 ertekekkel es 3x3-as tablara"""
    a = it.product(range(-1,2), repeat=9) #az osszes lehetseges elem
    a = list(a)  # listaban
    a = [np.reshape([j for j in a[i]], (3,3)) for i in range(len(a))] #npmatrixok listajat adja vissza
    return a
def nodes2():
    """Megadja az osszes lehetseges tablaallast, most -1,1,0 ertekekkel es 3x3-as tablara"""
    a = it.product(range(-1,2), repeat=9) #az osszes lehetseges elem
    a = list(a)  # listaban
    a = [str(np.reshape([j for j in a[i]], (3,3))) for i in range(len(a))] #npmatrixok listajat adja vissza
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
    if -1 not in tabla and not (win):
        print("Ajjaj, vesztettel!")
        return 0
    #nyero mezo
    elif win:
        print("Hurra, nyertel!")
        return 1

    else:
        print("ez egy nem nyertes sem vesztes mezo")
        return -1


def nyeromezok(lista):
    """nyeromezok annak, aki 0/azonos sorra/oszlopra torekedik"""
    nyerok = [lista[i] for i in range(len(lista)) if nyeromezo(lista[i]) == 1]
    return len(nyerok)

def vesztomezok(lista):
    """vesztomezok annak, aki 0/azonos sorra/oszlopra torekedik"""
    vesztok = [lista[i] for i in range(len(lista)) if nyeromezo(lista[i]) == 0]
    return len(vesztok)

def nemvegallapot(lista):
    """nem vegallapot, innen meg kell lepni"""
    nv = [lista[i] for i in range(len(lista)) if nyeromezo(lista[i]) == -1]
    return nv

def elek(tabla):
    """egy mezonek az oseit adja vissza"""
    osok = []
    t = tabla.copy()
    for i in range(3):
        for j in range(3):
            if tabla[i][j] != -1:
                tabla[i][j] = -1
                osok.append((str(tabla), str(t)) #t is kell, hogy ellista legyen. Igazabol majd stringesiteni kell, mert nxgraphnak csak olyan csucsa lehet
                tabla = t
    return osok

def ossz_el(lista):
    """Egy listaban szereplo osszes csucs oseit visszaadja"""
    ellista = [elek(lista[i]) for i in range(len(lista))]
    ellista = [item for sublist in ellista for item in sublist]
    return ellista

    #nxgraph kell innentol? Es amugy megnezni, hogy a nyerok osei kozott van-e csak nyerobe vezeto? Szoval lehet, hogy kellene egy
    #gyerek fuggveny is, nemcsak os? (De az kb ugyanaz, csak forditva


class Jatek:

    D = nx.DiGraph()
    D.add_edges_from(ossz_el(nodes())) #iranyitott graf, a csucsok a allasok



    def __init__(self, allapot):
        self.allapot = nyeromezo(self) #megmondja, hogy milyen, nyertes/vesztes/dontetlen



    #def lepes(self):


















    def nodes():
        """Megadja az osszes lehetseges tablaallast, most -1,1,0 ertekekkel es 3x3-as tablara"""
        a = it.product(range(-1, 2), repeat=9)  # az osszes lehetseges elem
        a = list(a)  # listaban
        a = [np.reshape([j for j in a[i]], (3, 3)) for i in range(len(a))]  # npmatrixok listajat adja vissza
        return a

    def elek(tabla):
        """egy mezonek az oseit adja vissza"""
        osok = []
        t = tabla.copy()
        for i in range(3):
            for j in range(3):
                if tabla[i][j] != -1:
                    tabla[i][j] = -1
                    osok.append((tabla, t)) #t is kell, hogy ellista legyen. Igazabol majd stringesiteni kell, mert nxgraphnak csak olyan csucsa lehet
                    tabla = t
        return osok

    def ossz_el(lista):
        """Egy listaban szereplo osszes csucs oseit visszaadja"""
        ellista = [elek(lista[i]) for i in range(len(lista))]
        ellista = [item for sublist in ellista for item in sublist]
        return ellista





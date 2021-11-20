import itertools as it
import numpy as np
import Jatek
import networkx as nx




def nodes():
    """Megadja az osszes lehetseges tablaallast, most -1,1,0 ertekekkel es 3x3-as tablara"""
    a = it.product(range(-1, 2), repeat=9) #az osszes lehetseges elem
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
    return nyerok

def vesztomezok(lista):
    """vesztomezok annak, aki 0/azonos sorra/oszlopra torekedik"""
    vesztok = [lista[i] for i in range(len(lista)) if nyeromezo(lista[i]) == 0]
    return vesztok

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
                osok.append((str(tabla), str(t))) #t is kell, hogy ellista legyen. Igazabol majd stringesiteni kell, mert nxgraphnak csak olyan csucsa lehet
                tabla = t
    return osok

def ossz_el(lista):
    """Egy listaban szereplo osszes csucs oseit visszaadja"""
    ellista = [elek(lista[i]) for i in range(len(lista))]
    ellista = [item for sublist in ellista for item in sublist]
    return ellista

    #nxgraph kell innentol? Es amugy megnezni, hogy a nyerok osei kozott van-e csak nyerobe vezeto? Szoval lehet, hogy kellene egy
    #gyerek fuggveny is, nemcsak os? (De az kb ugyanaz, csak forditva


class Csucsok:

    D = nx.DiGraph()
    D.add_edges_from(ossz_el(nodes())) #iranyitott graf, a csucsok a allasok

    def __init__(self, csucs):
        self.csucs = csucs

    def nyero_arany(self, gyerek):
        if nyeromezo(gyerek) == 1:
            return 1
        elif nyeromezo(gyerek) == 0:
            return 0
        else:
            global D
            nyerobe = 0
            vesztobe = 0
            nyerok = nyeromezok(nodes())
            for nyero in nyerok:
                if nx.has_path(D, str(gyerek), str(nyero)):
                    nyerobe += 1
            vesztok = vesztomezok(nodes())
            for veszto in vesztok:
                if nx.has_path(D, str(gyerek), str(veszto)):
                    vesztobe += 1
            if vesztobe == 0:
                return 1
            else:
                return nyerobe / vesztobe

    def gyerekek(self):
        """egy mezonek az gyerekeit adja vissza"""
        gyerekek = []
        t = self.csucs.copy()
        for i in range(3):
            for j in range(3):
                if t[i][j] == -1:
                    t[i][j] = 0
                    gyerekek.append(t)
                    t[i][j] = 1
                    gyerekek.append(t)
                    t = self.csucs.copy()
        return gyerekek

    def lepes(self):
        aranyok = [nyero_arany(gyerek) for gyerek in gyerekek(self.csucs)]
        max_index = np.argmax(aranyok)
        lepes = (gyerekek(self.csucs))[max_index]
        Jatek.check(lepes)
        Jatek.show(lepes)
        if Jatek.check(lepes):
            return lepes


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

def jatekos_lep(tabla):
    '''
            A felhasználótól elkérjük, hogy hova szeretne rakni, majd annak az értékét.
            Ellenőrizzük, hogy helyes lepes-e, vege van-e.
        '''
    # felhasznalo lepese
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

    print("Felhasznalo lepese: ")
    Jatek.show(tabla)
    Jatek.check(tabla)
    if Jatek.check(tabla):
        return tabla

def Strategia():
    # mi a jatekos celja?
    # ki kezd?

    #kezdoallapot
    tabla = np.array([[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]])
    print("Kezdo allapot: ")
    show(tabla)

    hanyadik = input("Hanyadik jatekos szeretnel lenni {1., 2.}?")
    if hanyadik == 1:
        i = 0
        while check(tabla):
            i = i + 1
            print(i, ". round:")
            jatekos_lep(tabla)
            allapot = Csucsok(jatekos_lep(tabla))
            allapot.lepes()




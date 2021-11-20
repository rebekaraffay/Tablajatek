import itertools as it
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
        return 0
    # nyero mezo
    elif win:
        return 1

    else:  # se nem nyertes se nem vesztes
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
                osok.append((str(tabla), str(t)))  # t is kell, hogy ellista legyen
                tabla = t
    return osok


def ossz_el(lista):
    """Egy listaban szereplo osszes csucs oseit visszaadja"""
    ellista = [elek(lista[i]) for i in range(len(lista))]
    ellista = [item for sublist in ellista for item in sublist]
    return ellista


class Csucsok:

    def __init__(self, csucs):
        self.csucs = csucs  # egy tablaallast lehet beadni neki

    def nyero_arany(self, gyerek):
        """milyen aranyban/valoszinuseggel lehet egy csucs gyerekeibol nyerni"""
        if nyeromezo(gyerek) == 1:  # ha a gyerek az egy nyertes csucs
            return 1
        elif nyeromezo(gyerek) == 0:  # ha vesztes
            return 0
        else:  # ha nem vegallapot a gyerek
            d = nx.DiGraph()
            d.add_edges_from(ossz_el(nodes()))  # iranyitott graf, a csucsok az allasok
            nyerobe = 0
            vesztobe = 0
            nyerok = nyeromezok(nodes())
            for nyero in nyerok:
                if nx.has_path(d, str(gyerek), str(nyero)):
                    nyerobe += 1
            vesztok = vesztomezok(nodes())
            for veszto in vesztok:
                if nx.has_path(d, str(gyerek), str(veszto)):
                    vesztobe += 1
            if vesztobe == 0:  # tehat ha a gyerekbol nem megy veszto csucsba ut, akkor nyeronek szamit
                return 1
            else:
                return nyerobe / vesztobe

    def gyerekek(self):
        """egy mezonek a gyerekeit adja vissza"""
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

    def lepes(self):  # abban az esetben, ha a csupa 0/ azonos sor/oszlopra torekedik a gep
        print("hello")
        sorrend = sorted(self.gyerekek(), key=self.nyero_arany)  # a nyeresi valoszinuseg szerint rendezem oket
        lepes = sorrend[0]
        Jatek.check(lepes)
        print(lepes)
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
    """A felhasználótól elkérjük, hogy hova szeretne rakni, majd annak az értékét.
            Ellenőrizzük, hogy helyes lepes-e, vege van-e."""

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
    print(tabla)
    Jatek.check(tabla)
    if Jatek.check(tabla):
        return tabla


def strategia():
    # mi a jatekos celja? most meg csak az lehet, hogy teliteni akarja a tablat
    # ki kezd?
    # kivel jatszik.. Az is kellene, hogy geppel vagy emberrel?

    while True:
        try:
            hanyadik = int(input("Hanyadik jatekos szeretnel lenni {1., 2.}? "))
            if hanyadik != 1 and hanyadik != 2:
                raise ErtekOutOfRange
            break

        except ErtekOutOfRange:
            print("1. vagy 2. jatekos lehetsz, {1, 2} ertekek kozul valassz ")

    while True:
        try:
            celadas = int(input("Valssz startegiat! 1: Azonos/ csupa 0 sor/oszlop letrehozasa, 2: Tabla telitese "))
            if celadas != 1 and celadas != 2:
                raise ErtekOutOfRange
            break
        except ErtekOutOfRange:
            print("1. vagy 2. strategiat valszthatod, {1, 2} ertekek kozul valassz ")

    if hanyadik == 1 and celadas == 2:
        tabla = np.array([[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]])
        print("Kezdo allapot: ")
        print(tabla)
        i = 1
        while Jatek.check(tabla):
            print(i, ". round:")
            i = i + 1
            jatekos_lep(tabla)
            allapot = Csucsok(jatekos_lep(tabla))  # ez itt nem igazan jo, raadasul nagyon hosszu ido...
            tabla = allapot.lepes()

    if hanyadik == 2 and celadas == 2:
        Jatek.jatek()

    # if hanyadik == 1 and celadas == 1:
        # erre egy megforditott nyeromezok fuggveny kell, de ennyi
    # if hanyadik ==2 and celadas == 1:
        # erre is csak az es kesz


if __name__ == "__main__":
    strategia()

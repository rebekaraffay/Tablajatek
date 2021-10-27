import itertools as it
import Jatek

def nodes():
    """Megadja az osszes lehetseges tablaallast"""
    a = it.product(range(-1,2), repeat=9) #az osszes lehetseges elem
    a = list(a)  # listaban
    a = [np.reshape([j for j in a[i]], (3,3)) for i in range(len(a) - 1)] #npmatrixok listajat adja vissza
    return a[0]

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
        win = azonos_sor_oszlop(tabla)
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
    nyerok = [lista[i] for i in range(len(lista)-1) if nyeromezo(lista[i])==1]
    return nyerok

def vesztomezok(lista):
    """vesztomezok annak, aki 0/azonos sorra/oszlopra torekedik"""
    vesztok = [lista[i] for i in range(len(lista)-1) if nyeromezo(lista[i])==0]
    return vesztok

def nemvegallapot(lista):
    """nem vegallapot, innen meg kell lepni"""
    nv = [lista[i] for i in range(len(lista)-1) if nyeromezo(lista[i])==-1]
    return nv

def elek(tabla):
    """egy mezonek az oseit adja vissza"""
    osok = []
    t = tabla.copy()
    for i in range(3):
        for j in range(3):
            if tabla[i,j] != -1:
                tabla[i,j]=-1
                osok.append(tabla)
                tabla = t
    return osok









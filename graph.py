import time

import numpy as np
from node import Node
from state import State
import itertools as it
from itertools import permutations



class Graph:
    def __init__(self):
        empty_table = np.full((3, 3), -1, dtype=int)
        self.root = Node(State(empty_table))
        self.root.set_parents([])
        self.levels = []                        # szintek elemeinek listáinak listája
        self.levels.append([self.root])
        self.generate_new_level([self.root])

        #graf generalasa szintenkent gyerekek lista, keresztelek, fv: 2 tabla kozott 1 kul van-e, minden szulo-gyerek kapcs
        #ha vmi nyero helyzet, akkor ures lista gyerekeknek, levelek ne lehessenek osok, esetleg szurt szinteket eltarolni

    def generate_new_level(self, last_level):
        # legyártjuk az összes lehetőséget, nem csomópontból, n. szinten n helyen van érték

        s = time.time()

        level = len(self.levels)
        temporary = [ [-1]*(9-level) + [0]*i + [1]*(level-i) for i in range(level+1)]
        perm = [set(permutations(temporary[i], 9)) for i in range(len(temporary))]

        t = time.time()

        np_tables = [np.reshape(table_list, (3, 3)) for set_element in perm for table_list in set_element]


        print("reshape nélkül",t-s)
        k = time.time()
        print("reshappel",k-s)

        return np_tables



    #todo: def is_sibling   # szintek között megfelelő élek behúzásához, hogy 1-e a különbség
    #todo: irányított élek behúzása szintek között (kiv ha az ős nyerő), 2x végig káne menni,
    #           hogy gyereke-e, azt eltárolni a nodeban, majd, 2. körben, hogy őse-e és azt is node-ban eltárolni
    #todo: kiszedni a nem kapcsolódó dolgokat (amik ősei nyertesek) -> nem teszem bele őket a következő tömbbe
    #todo: nyerő, vesztő mezők kigyűjtése





if __name__ == "__main__":
    a = Graph()
import time

import numpy as np
from node import Node
from state import State
#import itertools as it
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



    #todo: def is_parent   # szintek között megfelelő élek behúzásához, hogy 1-e a különbség
    #todo: irányított élek behúzása szintek között (kiv ha az ős nyerő), 2x végig káne menni,
    #           hogy gyereke-e, azt eltárolni a nodeban, majd, 2. körben, hogy őse-e és azt is node-ban eltárolni
    #todo: kiszedni a nem kapcsolódó dolgokat (amik ősei nyertesek) -> nem teszem bele őket a következő tömbbe
    #todo: nyerő, vesztő mezők kigyűjtése

    def is_parent(self, last_level, current_level):
        # Count occurrence of element '1 and 0' in each row and from that say if one is a parent of the other
        index_last = self.levels.index(last_level)  # how many elements are different from -1 (not empty)
        index_current = self.levels.index(current_level)
        if index_last == index_current - 1:
            indices_last = []
            indices_current = []
            parent = []
            for i in range(len(last_level)):
                count1 = np.count_nonzero(last_level[i] == 1, axis=1)  # how many elements are 1 in a matrix
                count0 = index_last-count1
                indices_last.append([last_level[i], count1, count0])
            for i in range(len(current_level)):
                count1 = np.count_nonzero(current_level[i] == 1, axis=1)
                count0 = index_current-count1
                indices_current.append([current_level[i], count1, count0])
            for i in range(len(indices_last)):
                for j in range(len(indices_current)):
                    if indices_last[i][1] == indices_current[j][1] and indices_last[i][2] == indices_current[j][2]-1:
                        parent.append((indices_last[i][0], indices_current[j][0]))
                    elif indices_last[i][1] == indices_current[j][1]-1 and indices_last[i][2] == indices_current[j][2]:
                        parent.append((indices_last[i][0], indices_current[j][0]))
            return parent














if __name__ == "__main__":
    a = Graph()
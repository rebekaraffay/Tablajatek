import time

import numpy as np
from node import Node
from state import State
#import itertools as it
from itertools import permutations
from typing import List


class Graph:
    def __init__(self):
        empty_table = np.full((3, 3), -1, dtype=int)
        self.root = Node(State(empty_table))
        self.root.set_parents([])
        self.levels = []                        # szintek elemeinek listáinak listája
        self.generate_graph()

        #graf generalasa szintenkent gyerekek lista, keresztelek, fv: 2 tabla kozott 1 kul van-e, minden szulo-gyerek kapcs
        #ha vmi nyero helyzet, akkor ures lista gyerekeknek, levelek ne lehessenek osok, esetleg szurt szinteket eltarolni

    def generate_graph(self):
        '''
        Az első szintet a gyökérből képzem, majd rekurzívan az előzőekből, amíg nem csak levélből áll egy szint.
        '''
        potty = time.perf_counter()
        self.levels.append([self.root])
        leafless_new_level = self.generate_new_level([self.root])
        while len(leafless_new_level) < 700:
            print(f"Generated new level, time elapsed from start: {time.perf_counter()-potty}")
            leafless_new_level = self.generate_new_level(leafless_new_level)
            print(len(leafless_new_level))
        print(f"Finished generation, time elapsed from start: {time.perf_counter() - potty}")

    def generate_new_level(self, leafless_current_level: List[Node]):
        '''
        Létrehozom egy új szint összes lehetséges csúcsát táblákként.
        Csúcsokat csinálok belőlük.
        Létrehozom az előző szinttel való éleket.
        Eltárolom a nem végállapotú szülős csúcsokat a gráf új szintjeként.
        A nem levél csúcsokat eltárolom a következő szint leafless_current listájának.
        '''
        ts = time.perf_counter()
        pot_new_lev_tab = self.potential_new_level_tables()
        ts2 = time.perf_counter()
        pot_new_lev_nodes = [Node(State(table)) for table in pot_new_lev_tab]
        ts3 = time.perf_counter()
        self.generate_edges(pot_new_lev_nodes, leafless_current_level)
        ts4 = time.perf_counter()
        new_level_nodes = [child for child in pot_new_lev_nodes if len(child.parents) > 0]
        self.levels.append(new_level_nodes)
        ts5 = time.perf_counter()
        leafless_new_level = [child for child in new_level_nodes if not child.is_leaf()]
        ts6 = time.perf_counter()
        print(f"generate pot. tabées {ts2-ts}")
        print(f"node-osítás {ts3-ts2}")
        print(f"setting edges {ts4-ts3}, {len(pot_new_lev_nodes)}, {len(leafless_current_level)}")
        print(f"kill unreal nodes {ts5-ts4}")
        print(f"select leaf nodes {ts6-ts5}")
        return leafless_new_level

    def potential_new_level_tables(self):   # todo: rename potenciális, ezek még nem csúcsok
        '''
        Létrehozza a következő szint lehetséges ccsúcsainak tábláit.
        '''

        level = len(self.levels)
        temporary = [[-1]*(9-level) + [0]*i + [1]*(level-i) for i in range(level+1)]
        perm = [set(permutations(temporary[i], 9)) for i in range(len(temporary))]

        np_tables = [np.reshape(table_list, (3, 3)) for set_element in perm for table_list in set_element]

        return np_tables

    def generate_edges(self, new_level: List[Node], last_level: List[Node]):    # todo: last levelben csak a nem leafek legyenek
        '''
        Létrehozza a 2 szint elemeinek children és parents listáját, amit a node classban kértünk.
        '''
        for child in new_level:
            parents = [parent for parent in last_level if State.is_relate(parent.state.table, child.state.table)]
            child.set_parents(parents)
        for parent in last_level:
            children = [child for child in new_level if State.is_relate(parent.state.table, child.state.table)]
            parent.set_children(children)




                    #todo el hozzaadasa
                    #todo szulo, gyerek listahoz hozzaadasa
                    #todo ha nem vegallapot az os, akkor eltárolni következő last_levelnek




    #todo: def is_parent   # szintek között megfelelő élek behúzásához, hogy 1-e a különbség
    #todo: irányított élek behúzása szintek között (kiv ha az ős nyerő), 2x végig káne menni,
    #           hogy gyereke-e, azt eltárolni a nodeban, majd, 2. körben, hogy őse-e és azt is node-ban eltárolni
    #todo: kiszedni a nem kapcsolódó dolgokat (amik ősei nyertesek) -> nem teszem bele őket a következő tömbbe
    #todo: nyerő, vesztő mezők kigyűjtése



    def is_parent2(self, last_level, current_level):
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
    print()
    # print(a.root.children[0].state.table)
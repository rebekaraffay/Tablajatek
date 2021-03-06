import time
import numpy as np
from node import Node
from state import State
from itertools import permutations
from typing import List
import json



class Graph:
    def __init__(self):
        empty_table = np.full((3, 3), -1, dtype=int)
        self.root = Node(State(empty_table))
        self.root.set_parents([])
        self.levels = []
        self.generate_graph()
        self.list_levels = None
        self.dict_children = None
        self.dict_parents = None
        self.dict_walks = None
        self.dict_loser_children = None
        self.save_datas()
        self.dict_walk()

    def save_datas(self):
        '''
            Csináljunk szótárakat, listát és majd azokat akarom elmenteni.
            A levelek listában a gráf szinjeinek csúcsait tárolom el.
            Szintén a self.levels segítségével végigjárom az összes csúcsot és elmentem a gyerekeket
            és szülőket 1-1 szótárba, ahol az adott csúcs a kulcs.
            Mindennek a np.array tábláját mentem el, a szótárakban stringesitve vannak a kulcsok es az ertekek is.
        '''
        self.list_levels = [[node.state.table for node in level] for level in self.levels]

        dict_children = {}
        for lev in self.levels:
            for node in lev:
                dict_children[str(node.state.table)] = [str(child.state.table) for child in node.children] \
                if node.children is not None else []
        self.dict_children = dict_children

        dict_parents = {}
        for lev in self.levels:
            for node in lev:
                dict_parents[str(node.state.table)] = [str(parent.state.table) for parent in node.parents] \
                if node.parents is not None else []
        self.dict_parents = dict_parents

        # amikor a gép telíteni szeretne, egy csúcsnak van-e olyan gyereke, ami teljesíti valameliyk záró feltételt
        dict_loser_children = {}
        for lev in self.levels:
            for node in lev:
                if node.children is not None:
                    dict_loser_children[str(node.state.table)] = [str(child.state.table) for child in node.children \
                                                                  if child.state.who_won() == 0]
                else:
                    if node.state.who_won() == 1:               #baj ha utolso lepesnel vagyunk
                        dict_loser_children[str(node.state.table)] = []

        self.dict_loser_children = dict_loser_children


        # Ellenőrzések
        table = self.levels[1][2].state.table
        print("A gráf 1. szintjének 2. eleme ", self.levels[1][2])
        # list_levels
        print("A levél lista első szintjének 2. eleme: ", self.list_levels[1][2])
        # dict_children
        print("A gyerekek tábláinak szótárából az első szint 2. csúcsának gyerekei: ", dict_children[str(table)])
        # dict_parents
        print("A szülők szótárból az első szint 2. elemének ősei (a gyökér) ", dict_parents[str(table)])


        return dict_loser_children

    def dict_walk(self):
        '''
            Azon szotar letrehozasa, amely megmondja, hogy egy csucsbol hany ut vezet nyero illetve veszto csucsba.
        '''
        dict_walks = {}
        for level in reversed(self.levels):
            for node in level:
                if node.state.who_won() == 0:
                    dict_walks[str(node.state.table)] = [1, 0]

                elif node.state.who_won() == 1:
                    dict_walks[str(node.state.table)] = [0, 1]
                else:
                    dict_walks[str(node.state.table)] = [sum([dict_walks[str(child.state.table)][0] \
                                                              for child in node.children])\
                if node.children is not None else 0, sum([dict_walks[str(child.state.table)][1] \
                                                          for child in node.children])\
                if node.children is not None else 0]
        self.dict_walks = dict_walks
        return dict_walks

    def generate_graph(self):
        '''
            A gráf elkészítése.
            Az első szintet a gyökérből képzem, majd rekurzívan az előzőekből, amíg nem csak levélből áll egy szint.
        '''
        start = time.perf_counter()
        self.levels.append([self.root])
        leafless_new_level = self.generate_new_level([self.root])
        while len(leafless_new_level) > 0:
        #for i in range(3):
            print(f"Generated new level, time elapsed from start: {time.perf_counter()-start}")
            leafless_new_level = self.generate_new_level(leafless_new_level)
            print(len(leafless_new_level))
        print(f"Finished generation, time elapsed from start: {time.perf_counter() - start}")

    def generate_new_level(self, leafless_current_level: List[Node]):
        '''
            Létrehozom egy új szint összes lehetséges csúcsát táblákként.
            Csúcsokat csinálok belőlük.
            Létrehozom az előző szinttel való éleket.
            Eltárolom a nem végállapotú szülős csúcsokat a gráf új szintjeként.
            A nem levél csúcsokat eltárolom a következő szint leafless_current listájának.
        '''
        # ts = time.perf_counter()
        pot_new_lev_tab = self.potential_new_level_tables()
        # ts2 = time.perf_counter()
        pot_new_lev_nodes = [Node(State(table)) for table in pot_new_lev_tab]
        # ts3 = time.perf_counter()
        self.generate_edges(pot_new_lev_nodes, leafless_current_level)
        # ts4 = time.perf_counter()
        new_level_nodes = [child for child in pot_new_lev_nodes if len(child.parents) > 0]
        self.levels.append(new_level_nodes)
        # ts5 = time.perf_counter()
        leafless_new_level = [child for child in new_level_nodes if not child.is_leaf()]
        # ts6 = time.perf_counter()
        # print(f"generate pot. tabées {ts2-ts}")
        # print(f"node-osítás {ts3-ts2}")
        # print(f"setting edges {ts4-ts3}, {len(pot_new_lev_nodes)}, {len(leafless_current_level)}")
        # print(f"kill unreal nodes {ts5-ts4}")
        # print(f"select leaf nodes {ts6-ts5}")
        return leafless_new_level

    def potential_new_level_tables(self):
        '''
            Létrehozza a következő szint lehetséges csúcsainak tábláit.
        '''

        level = len(self.levels)
        temporary = [[-1]*(9-level) + [0]*i + [1]*(level-i) for i in range(level+1)]
        perm = [set(permutations(temporary[i], 9)) for i in range(len(temporary))]

        np_tables = [np.reshape(table_list, (3, 3)) for set_element in perm for table_list in set_element]

        return np_tables

    def generate_edges(self, new_level: List[Node], last_level: List[Node]):
        '''
            Létrehozza a 2 szint elemeinek children és parents listáját, amit a node classban kértünk.
        '''
        for child in new_level:
            parents = [parent for parent in last_level if State.is_relate(parent.state.table, child.state.table)]
            child.set_parents(parents)
        for parent in last_level:
            children = [child for child in new_level if State.is_relate(parent.state.table, child.state.table)]
            parent.set_children(children)









#if __name__ == "__main__":
    #a = Graph()
    # print(a.root.children[0].state.table)

import time

import numpy as np
from node import Node
from state import State
#import itertools as it
from itertools import permutations
from typing import List
import random
import json


class Graph:
    def __init__(self):
        empty_table = np.full((3, 3), -1, dtype=int)
        self.root = Node(State(empty_table))
        self.root.set_parents([])
        self.levels = []                        # szintek elemeinek listáinak listája
        self.generate_graph()
        self.Dict_levels = None


    def dict_into_file(self, dict):
        pass
        # todo

    def set_dicts(self):
        '''
        Csináljunk szótárat és majd azt akarom elmenteni.
        '''
        Dict_levels = {}
        for i in range(len(self.levels)):
            Dict_levels[i] = self.levels[i]
        self.Dict_levels = Dict_levels

            #for j in range(len(self.levels[i])):
                #Dict_children[self.levels[i][j]] = self.levels[i][j].children

        #Dict_children = {}


        return Dict_levels  # Dict_children

        # todo: generate_edgesben rögtön beadni? (problémám, hogy hogy menjek végig az összes csúcon,
        #  a gyerekeinek listája benne van a node osztályban


    def generate_graph(self):
        '''
        Az első szintet a gyökérből képzem, majd rekurzívan az előzőekből, amíg nem csak levélből áll egy szint.
        '''
        start = time.perf_counter()
        self.levels.append([self.root])
        leafless_new_level = self.generate_new_level([self.root])
        #while len(leafless_new_level) > 0:
        for i in range(2):
            print(f"Generated new level, time elapsed from start: {time.perf_counter()-start}")
            leafless_new_level = self.generate_new_level(leafless_new_level)
            print(len(leafless_new_level))
        print(f"Finished generation, time elapsed from start: {time.perf_counter() - start}")

        # dictionaryk
        Dict_levels = self.set_dicts()
        mutat = [Dict_levels[1][i].state.table for i in range(len(Dict_levels[1]))]
        # mutat = [ Dict_children[1][i].state.table for i in range(len(Dict_children[1]))]
        print(mutat)

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
            # todo: direktbe megírni, hogy mik ezek a csúcsok
            # self.save_graph()
        for parent in last_level:
            children = [child for child in new_level if State.is_relate(parent.state.table, child.state.table)]
            parent.set_children(children)







if __name__ == "__main__":
    a = Graph()
    # print(a.root.children[0].state.table)
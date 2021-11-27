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
        self.save_datas()
        self.dict_walk()
        self.choose_this_children()


    def save_datas(self):
        '''
        Csináljunk szótárakat, listát és majd azokat akarom elmenteni.
        A levelek listában a gráf szinjeinek csúcsait tárolom el.
        Szintén a self.levels segítségével végigjárom az összes csúcsot és elmentem a gyerekeket
        és szülőket 1-1 szótárba, ahol az adott csúcs a kulcs.
        Mindennek a np.array tábláját mentem el, a szótárakban stringesitve vannak a kulcsok es az ertekek listeitve.
        '''
        self.list_levels = [[node.state.table for node in level] for level in self.levels]

        dict_children = {}
        for lev in self.levels:
            for node in lev:
                dict_children[str(node.state.table)] = [child.state.table.tolist() for child in node.children] \
                if node.children is not None else []
        self.dict_children = dict_children

        dict_parents = {}
        for lev in self.levels:
            for node in lev:
                dict_parents[str(node.state.table)] = [parent.state.table.tolist() for parent in node.parents] \
                if node.parents is not None else []
        self.dict_parents = dict_parents




        # Ellenőrzések
        table = self.levels[1][2].state.table
        print("A gráf 1. szintjének 2. eleme ", self.levels[1][2])
        # list_levels
        print("A levél lista első szintjének 2. eleme: ", self.list_levels[1][2])
        # dict_children
        print("A gyerekek tábláinak szótárából az első szint 2. csúcsának gyerekei: ", dict_children[str(table)])
        # dict_parents
        print("A szülők szótárból az első szint 2. elemének ősei (a gyökér) ", dict_parents[str(table)])


        return dict_parents, dict_children


    def dict_walk(self):
        """Azon szotar letrehozasa, amely megmondja, hogy egy csucsbol hany ut vezet nyero illetve veszto csucsba"""
        dict_walks = {}
        for level in reversed(self.levels):
            for node in level:
                if node.state.who_won() == 0:
                    dict_walks[str(node.state.table)] = [1, 0]

                elif node.state.who_won() == 1:
                    dict_walks[str(node.state.table)] = [0, 1]
                else:
                    dict_walks[str(node.state.table)] = [sum([dict_walks[str(child.state.table)][0] for child in node.children])\
                if node.children is not None else 0, sum([dict_walks[str(child.state.table)][1] for child in node.children])\
                if node.children is not None else 0]
        self.dict_walks = dict_walks
        return dict_walks

    def choose_this_children(self): #todo a filters resz biztos nem jo, hogyan kellene a maximalis alapjan kivalsztani? Es ugye lehet 0 is,szoval baj a 0-val osztas
    #todo ha ez kesz van, akkor mar csak a lepest/jatekot kell megirni

        with open("proba_seta_teljes.json", "r") as read_file:
            aranyok = json.load(read_file)

        with open("proba.json", "r") as read_file:
            gyerek = json.load(read_file)
        choose_dict = {}
        gyerek_szotar = gyerek[1]
        for key in gyerek_szotar.keys():
            if len(gyerek_szotar[key]) == 0:
                pass
            else:
                lehetoseg = []
                for i in range(len(gyerek_szotar[key])):
                    if aranyok[gyerek_szotar[key][i]][1] == 0:
                        lehetoseg.append(gyerek_szotar[key][i])
                        choose_dict[key] = lehetoseg
                        lehetoseg = []

                    else:
                        nyero = []
                        veszto = []
                        nyero_lepes = sorted(gyerek_szotar[key], key=lambda x: aranyok[x][0]/aranyok[x][1])
                        for i in range(len(nyero_lepes)):
                            if aranyok[nyero_lepes[0]][0]/aranyok[nyero_lepes[0]][1]  == aranyok[nyero_lepes[i]][0]/aranyok[nyero_lepes[i]][1]:
                                nyero.append(nyero_lepes[i])
                        veszto_lepes = sorted(gyerek_szotar[key], key=lambda x: aranyok[x][1]/aranyok[x][0])[0]
                        for i in range(len(nyero_lepes)):
                            if aranyok[veszto_lepes[0]][1]/aranyok[veszto_lepes[0]][0]  == aranyok[veszto_lepes[i]][1]/aranyok[veszto_lepes[i]][0]:
                                veszto.append(nyero_lepes[i])

                        choose_dict[key] = [nyero, veszto]



        return choose_dict






    def generate_graph(self):
        '''
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







#if __name__ == "__main__":
    #a = Graph()
    # print(a.root.children[0].state.table)

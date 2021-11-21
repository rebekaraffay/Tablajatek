import numpy as np
from node import Node
from state import State


class Graph:
    def __init__(self):
        empty_table = np.full((3, 3), -1, dtype=int)
        self.root = Node(State(empty_table))
        self.root.set_parents([])
        #graf generalasa szintenkent gyerekek lista, keresztelek, fv: 2 tabla kozott 1 kul van-e, minden szulo-gyerek kapcs
        #ha vmi nyero helyzet, akkor ures lista gyerekeknek, levelek ne lehessenek osok, esetleg szurt szinteket eltarolni


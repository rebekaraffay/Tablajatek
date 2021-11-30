import numpy as np
from win_state import WinState
import random
import json


class State:
    '''
        tabla allapottara vonatkozo fuggvenyek
    '''

    def __init__(self, table):
        self.table = table
        self.end = None         # todo: ha nem használjuk sehol, akkor töröljük, \
        # Dorka nem használta végül, nem tudja ki írta


    def equal_row_or_column(self):
        '''
            Eldönti, hogy van-e 2 egyforma teli oszlop vagy sor.
        '''
        for i in range(3):
            for j in range(3):
                if i != j:
                    # is this 2 row equal?
                    if np.array_equal(self.table[i], self.table[j]) and -1 not in self.table[i]:
                        return True
                    # is this 2 column equal?
                    if np.array_equal(self.table[:, i], self.table[:, j]) and -1 not in self.table[:, i]:
                        return True
        return False

    def full_zero_exist(self):
        # column
        for i in range(3):
            exist = True
            for j in range(3):
                if self.table[j, i] != 0:
                    exist = False
            if exist:
                return True
        # row
        for i in range(3):
            exist = True
            for j in range(3):
                if self.table[i, j] != 0:
                    exist = False
            if exist:
                return True
        return False

    def who_win(self):
        if self.equal_row_or_column() or self.full_zero_exist():
            return WinState.WIN_CONDITION_EXIST
        elif -1 not in self.table:
            return WinState.OVER_WITHOUT
        return WinState.UNDECIDED

    def who_won(self):
        if self.equal_row_or_column() or self.full_zero_exist():
            return 0
        elif -1 not in self.table:
            return 1
        return 2

    @staticmethod
    def is_relate(parent: np.ndarray, child: np.ndarray) -> bool:
        difference = parent - child
        return np.count_nonzero(difference) == 1

    def computer_step(self, strategy):
        '''
        1-es stratégia, ha azonosra törekszik mit lépjen a gép.
        2-es, ha teli táblára.
        Kész szótárból szedi ki a lépéseket. (ELtároltuk, hogy egy adott csúcsból hova érdemes lépni
        a különböző stratégiák esetén.
        '''
        # todo: most node megy be és tábla jön ki, attól függ, hogy milyen lesz a nagy program, hogy mit szeretnénk
        with open("nyero_lepesek.json", "r") as read_file:
            strat_1 = json.load(read_file)

        with open("veszto_lepesek.json", "r") as read_file:
            strat_2 = json.load(read_file)

        if strategy == 1:
            index = random.randint(0, len(strat_1[self.table])-1)
            step = strat_1[str(self.table)][index]
        else:
            index = random.randint (0, len(strat_2[self.table])-1)
            step = strat_2[str(self.table)][index]

        step = [step[i] for i in range(2,len(step)-2)]      # két szélső kihagyva []

        rows = step.split('\n')


        step = [np.reshape([j for j in step[i]], (3, 3)) for i in range(len(step))]
        return step
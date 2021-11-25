import numpy as np
from win_state import WinState


class State:
    '''
        tabla allapottara vonatkozo fuggvenyek
    '''

    def __init__(self, table):
        self.table = table
        self.end = None



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

    @staticmethod
    def is_relate(parent: np.ndarray, child: np.ndarray) -> bool:
        difference = parent - child
        return np.count_nonzero(difference) == 1

    def is_winner(self):
        '''
        Ha levél és nyerőállapot, vagy ha van olyan gyereke, amely nyerő állapot
        '''
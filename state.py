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
        '''
            Eldönti, hogy van-e teli 0-ás sor vagy oszlop.
        '''
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
        '''
            Eldönti egy csúcsról, hogy végállapot-e, és melyik stratégia szerint nyertes, vagy, hogy még lépni kell-e.
            A visszatérési értékek globális változók akartak lenni, ezt sajnos nem használtuk ki eléggé.
            (Az lett volna a cél, hogy ne kell azzal bajlódni, hogy éppen milyen stratégia van, és nehogy elírjuk,
            ha számmal térne vissza.)
        '''
        if self.equal_row_or_column() or self.full_zero_exist():
            return WinState.WIN_CONDITION_EXIST
        elif -1 not in self.table:
            return WinState.OVER_WITHOUT
        return WinState.UNDECIDED

    def who_won(self):
        '''
            Ugyanazt csinálja, mint a who_win() fv, csak -1,0,1 visszatérési értékekkel.
        '''
        if self.equal_row_or_column() or self.full_zero_exist():
            return 0
        elif -1 not in self.table:
            return 1
        return 2

    @staticmethod
    def is_relate(parent: np.ndarray, child: np.ndarray) -> bool:
        '''
            Eldönti 2 csúcsról, hogy szülő-gyerek kapcsoaltban vannak-e, vagyis pontosan 1 különbség van-e:
            mégpedig úgy, hogy a szülőben üres az a hely, a gyerekben pedig {0,1} van odaírva.
            Az nem fordulhat elő, hogy 1 mező különböző, de mind2 kitöltött, mert akkor egy szinten lennének
            és nem adnánk be őket egyszerre egynek a fv-nek.
        '''
        difference = parent - child
        return np.count_nonzero(difference) == 1

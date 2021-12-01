# todo: játékszabélyok leírása világosan az elején
# todo: readme-be dokumentáció valami minimális szinten

import computer_play as cp
import multiplayer as mp

class Error(Exception):
    pass
class ErtekOutOfRange(Error):
    pass


def special_amoba():

    while True:
        try:
            tipus = int(input("Egyedul vagy egy baratoddal szeretnel jatszani? Ha egyedul: 1, ha nem: 2: "))
            if tipus not in range(1,3):
                raise ErtekOutOfRange
            break
        except ErtekOutOfRange:
            print("Az értéknek 1-nek vagy 2-nek kell lennie.")

    if tipus == 1:
        cp.final_game()
    if tipus == 2:
        mp.multiplayer()


if __name__ == "__main__":
    special_amoba()


import computer_play as cp
import multiplayer as mp

# a Jatek
#Hibaosztalyok:

class Error(Exception):
    pass
class ErtekOutOfRange(Error):
    pass


def special_amoba():
    """A kesz jatek"""
    while True:
        try:
            tipus = int(input("Egyedül vagy egy barátoddal szeretnél játszani? Ha egyedül: 1, ha nem: 2: ")) #kivalasztja a jatekos, hogy melyik tipusu jatek fusson le
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

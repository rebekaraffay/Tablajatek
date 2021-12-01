# todo: játékszabélyok leírása világosan az elején
# todo: readme-be dokumentáció valami minimális szinten

import computer_play as cp
import multiplayer as mp

def special_amoba():
    tipus = int(input("Egyedul vagy egy baratoddal szeretnel jatszani? Ha egyedul: 1, ha nem: 2: "))
    if tipus == 1:
        cp.final_game()
    if tipus == 2:
        mp.multiplayer()


if __name__ == "__main__":
    special_amoba()

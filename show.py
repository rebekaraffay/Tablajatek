import matplotlib.pyplot as plt
import numpy as np
from matplotlib.table import Table

node = np.array(([1, 0, -1], [0, 0, 0], [-1, 1, -1]))  # probanak van itt


def show(node, title = None):
    """Kirajzolja a tablat, lehet neki cimet is adni"""
    board_show(node)
    if title != None:
        plt.title(title, size = 30, color = "red", y=0.4, pad=14)  # cim adatainak beallitasa
        return plt.show()
    plt.show() #kirajzolas


def board_show(node):
    fig, ax = plt.subplots()  # uj abra
    ax.set_axis_off()
    tb = Table(ax, bbox=[0, 0, 1, 1]) # table-t hasznalunk

    width, height = 1, 1

    def valuechanger(value):
        """1 = X es 0 = O"""  # 1-et x-re, 0-t o-ra valtoztat
        if value == 1:
            return "X"
        elif value == 0:
            return "O"

    # hozzaadjuk a cellakat
    for (i, j), val in np.ndenumerate(node):
        tb.add_cell(i, j, width, height, text=valuechanger(val),
                    loc='center', facecolor='white')  # cellakba szoveget is rakunk, ami -1/X/O, attol fuggoen, hogy a numpyarray tablaban mik voltak az ertekek

    # sor cimkek
    for (i, j), label in np.ndenumerate(node):
        tb.add_cell(i, -1, width, height, text=i + 1, loc='right',
                    edgecolor='none', facecolor='none')  # cimkek azok 1/2/3 ertekek
    # oszlop cimkek
    for (i, j), label in np.ndenumerate(node):
        tb.add_cell(-1, j, width, height / 2, text=j + 1, loc='center',
                    edgecolor='none', facecolor='none')  #1/2/3 erteket vesznek fel
    tb.set_fontsize(25)


    for (i, j), label in np.ndenumerate(node):
        if label == -1:
            tb[i, j].get_text().set_color('w')  # -1-nek a szinet feherre valtoztatjuk, igy nem fog latszani a palyan

    ax.add_table(tb)
    return fig


if __name__ == '__main__': #proba
    show(node)
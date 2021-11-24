import matplotlib.pyplot as plt
import numpy as np
from matplotlib.table import Table

node = np.array(([1, 0, -1], [0, 0, 0], [-1, 1, -1]))


def show(node):
    """Shows the board"""
    board_show(node)
    plt.show()


def board_show(node):
    fig, ax = plt.subplots()  # new figure
    ax.set_axis_off()
    tb = Table(ax, bbox=[0, 0, 1, 1])

    width, height = 1, 1

    def valuechanger(value):
        """1 means X and 0 means O"""  # function changes 1 to x and 0 to O, as we want to show the table as the real game
        if value == 1:
            return "X"
        elif value == 0:
            return "O"

    # Add cells
    for (i, j), val in np.ndenumerate(node):
        tb.add_cell(i, j, width, height, text=valuechanger(val),
                    loc='center', facecolor='white')  # adding cells with text inside them, which is -1/X/O

    # Row Labels...
    for (i, j), label in np.ndenumerate(node):
        tb.add_cell(i, -1, width, height, text=i + 1, loc='right',
                    edgecolor='none', facecolor='none')  # row labels are 1/2/3
    # Column Labels...
    for (i, j), label in np.ndenumerate(node):
        tb.add_cell(-1, j, width, height / 2, text=j + 1, loc='center',
                    edgecolor='none', facecolor='none')  #col labels are 1/2/3
    tb.set_fontsize(25)

    for (i, j), label in np.ndenumerate(node):
        if label == -1:
            tb[i, j].get_text().set_color('w')  # setting the color of -1 to white, so it wont show in the table

    ax.add_table(tb)
    return fig


if __name__ == '__main__':
    show(node)
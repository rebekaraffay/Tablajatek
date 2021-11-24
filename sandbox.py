from Fas_esetek import nodes

# Rebeka kódja az élekre, graph fájlban volt
def is_parent2(self, last_level, current_level):
    # Count occurrence of element '1 and 0' in each row and from that say if one is a parent of the other
    index_last = self.levels.index(last_level)  # how many elements are different from -1 (not empty)
    index_current = self.levels.index(current_level)
    if index_last == index_current - 1:
        indices_last = []
        indices_current = []
        parent = []
        for i in range(len(last_level)):
            count1 = np.count_nonzero(last_level[i] == 1, axis=1)  # how many elements are 1 in a matrix
            count0 = index_last - count1
            indices_last.append([last_level[i], count1, count0])
        for i in range(len(current_level)):
            count1 = np.count_nonzero(current_level[i] == 1, axis=1)
            count0 = index_current - count1
            indices_current.append([current_level[i], count1, count0])
        for i in range(len(indices_last)):
            for j in range(len(indices_current)):
                if indices_last[i][1] == indices_current[j][1] and indices_last[i][2] == indices_current[j][2] - 1:
                    parent.append((indices_last[i][0], indices_current[j][0]))
                elif indices_last[i][1] == indices_current[j][1] - 1 and indices_last[i][2] == indices_current[j][2]:
                    parent.append((indices_last[i][0], indices_current[j][0]))
        return parent


class A:
    def __init__(self, name):
        self._name = name
        self._age = -1
        self._lista = None

    def set_age(self, age):
        self._age = age

    def set_lista(self):
        self._lista = []
        print("set lista", self._lista)

    def greeting(self):
        print(f"hi, my name is {self._name}")
        if self._age > -1:
            print(f"and my age is {self._age}")


def main():
    nodes()
    nodes()
    nodes()


if __name__ == "__main__":
    main()

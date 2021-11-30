from Fas_esetek import nodes

# átalakíts majdnem jó:
step = [step[i] for i in range(2,len(step)-2)]      # két szélső kihagyva []
    step = str(step)
    step = step.replace("'", "")
    step = step.replace("]", "")                        # elhagyjuk a fölösleges elemeket
    step = step.replace("[", "")
    step = step.split("\n")
    for i in range(len(step)):
        step[i] = step[i].replace("  ", " ").split(" ")
        print("step: ", step)
    del step[1][0]
    del step[2][0]
    for i in range(3):
        for j in range(3):
            step[i][j] = int(step[i][j])

    np.array(step)


    step = [np.reshape([j for j in step[i]], (3, 3)) for i in range(len(step))]

# np. array-jé alakításhoz
temp = []
        sor = 0
        for i in range(len(step)):
            start_0 = 0
            while step[i] != "]":
                i+=1
            end_0 = i
            while step[i] != "[":
                i+=1
            start_1 = i
            while step[i] != "]":
                i+=1
            end_1 = i
            while step[i] != "[":
                i+=1
            start_2 = i
            while step[i] != "]":
                i+=1
            end_2 = i


# gyorsítás próbálkozás, fentről felépíteni a fát
    def generate_graph_test(self):
        '''
        Az első szintet a gyökérből képzem, majd rekurzívan az előzőekből, amíg nem csak levélből áll egy szint.
        '''
        potty = time.perf_counter()
        root_test = np.array([[-1, -1, 1], [-1, 0, -1], [1, -1, -1]])
        root_list = [-1, -1, 1, -1, 0, -1, 1, -1, -1]
        unfilled_list = [0, 1, 3, 5, 7, 8]
        children = self.generate_all_children_domi(root_list, unfilled_list)
        #for ch in children:
         #   print(ch)
        #children = self.generate_all_children(root_test)
        for i in range(100_000):
            #children = self.generate_all_children_domi(root_list, unfilled_list)

            children = self.generate_all_children(root_test)
#            self.choose_random_child(children)
        print(len(children))
        print(f"Finished generation, time elapsed from start: {time.perf_counter() - potty}")

    def generate_all_children_domi(self, parent_table_list, unfilled_index_list):
        children = []
        for ind in unfilled_index_list:
            fill_0 = parent_table_list.copy()
            fill_0[ind] = 0
            fill_1 = parent_table_list.copy()
            fill_1[ind] = 1
            children.append(fill_0)
            children.append(fill_1)
        children_tabs = [np.reshape(table_list, (3, 3)) for table_list in children]
        return children_tabs

    def generate_all_children(self, parent):
        children = []
        table = parent.copy()
        for i in range(3):
            for j in range(3):
                if table[i][j] == -1:
                    table[i][j] = 0
                    children.append(table)
                    table = parent.copy()
                    table[i][j] = 1
                    children.append(table)
                    table = parent.copy()
        return children

    def choose_random_child(self, children):
        random_index = random.randint(0, len(children)-1)
        return children[random_index]

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
                if indices_last[i][1] == indices_current[j][1] and indices_last[i][2] == indices_current[j][2] - 1:  #itt nem nezi meg, hogy jo helyen vannak-e
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

def nyeromezok(lista):
    """nyeromezok annak, aki 0/azonos sorra/oszlopra torekedik"""
    nyerok = [lista[i] for i in range(len(lista)) if nyeromezo(lista[i]) == 1]
    return nyerok


def vesztomezok(lista):
    """vesztomezok annak, aki 0/azonos sorra/oszlopra torekedik"""
    vesztok = [lista[i] for i in range(len(lista)) if nyeromezo(lista[i]) == 0]
    return vesztok


def nemvegallapot(lista):
    """nem vegallapot, innen meg kell lepni"""
    nv = [lista[i] for i in range(len(lista)) if nyeromezo(lista[i]) == -1]
    return nv



def arreq_in_list(myarr, list_arrays):
    return next((True for elem in list_arrays if np.array_equal(elem, myarr)), False)

class Csucsok:

    def __init__(self, csucs):
        self.csucs = csucs  # egy tablaallast lehet beadni neki

    def nyero_arany(self, gyerek):
        """milyen aranyban/valoszinuseggel lehet egy csucs gyerekeibol nyerni"""
        if nyeromezo(gyerek) == 1:  # ha a gyerek az egy nyertes csucs
            return 1
        elif nyeromezo(gyerek) == 0:  # ha vesztes
            return 0
        else:  # ha nem vegallapot a gyerek
            d = nx.DiGraph()
            d.add_edges_from(ossz_el(nodes()))  # iranyitott graf, a csucsok az allasok
            nyerobe = 0
            vesztobe = 0
            nyerok = nyeromezok(nodes())
            for nyero in nyerok:
                if nx.has_path(d, str(gyerek), str(nyero)):
                    nyerobe += 1
            vesztok = vesztomezok(nodes())
            for veszto in vesztok:
                if nx.has_path(d, str(gyerek), str(veszto)):
                    vesztobe += 1
            if vesztobe == 0:  # tehat ha a gyerekbol nem megy veszto csucsba ut, akkor nyeronek szamit
                return 1
            else:
                return nyerobe / vesztobe

    def gyerekek(self):
        """egy mezonek a gyerekeit adja vissza"""
        gyerekek = []
        t = self.csucs.copy()
        for i in range(3):
            for j in range(3):
                if t[i][j] == -1:
                    t[i][j] = 0
                    gyerekek.append(t)
                    t[i][j] = 1
                    gyerekek.append(t)
                    t = self.csucs.copy()
        return gyerekek

    def lepes(self):  # abban az esetben, ha a csupa 0/ azonos sor/oszlopra torekedik a gep
        print("hello")
        sorrend = sorted(self.gyerekek(), key=self.nyero_arany)  # a nyeresi valoszinuseg szerint rendezem oket
        lepes = sorrend[0]
        Jatek.check(lepes)
        print(lepes)
        if Jatek.check(lepes):
            return lepes


# Hibaosztályok
class Error(Exception):
    pass

class SorOutOfRange(Error):
    pass

class OszlopOutOfRange(Error):
    pass

class ErtekOutOfRange(Error):
    pass

class NotEmpty(Error):
    pass


def jatekos_lep(tabla):
    """A felhasználótól elkérjük, hogy hova szeretne rakni, majd annak az értékét.
            Ellenőrizzük, hogy helyes lepes-e, vege van-e."""

    # felhasznalo lepese
    # helyes lepest hajtott-e vegre
    while True:
        try:
            sor_index = int(input('A sor indexe {1,2,3}: ')) - 1
            if sor_index not in range(0, 3):
                raise SorOutOfRange
            oszlop_index = int(input('Az oszlop indexe {1,2,3}: ')) - 1
            if oszlop_index not in range(0, 3):
                raise OszlopOutOfRange
            elif tabla[sor_index][oszlop_index] != -1:
                raise NotEmpty
            break
        except SorOutOfRange:
            print("A sor indexének {1,2,3}-belinek kell lennie, próbálja újra.")
        except OszlopOutOfRange:
            print("Az oszlop indexének {1,2,3}-belinek kell lennie, próbálja újra.")
        except NotEmpty:
            print("Csak üres mezőbe írhat, próbálja újra.")

    while True:
        try:
            ertek = int(input('Az ertek {0,1}: '))
            if ertek not in range(0, 2):
                raise ErtekOutOfRange
            break
        except ErtekOutOfRange:
            print("Az értéknek {0,1}-belinek kell lennie.")

    tabla[sor_index][oszlop_index] = ertek  # beirtuk a jatekos altal megadott erteket a megfelelo helyre

    print("Felhasznalo lepese: ")
    print(tabla)
    Jatek.check(tabla)
    if Jatek.check(tabla):
        return tabla


def strategia():
    # mi a jatekos celja? most meg csak az lehet, hogy teliteni akarja a tablat
    # ki kezd?
    # kivel jatszik.. Az is kellene, hogy geppel vagy emberrel?

    while True:
        try:
            hanyadik = int(input("Hanyadik jatekos szeretnel lenni {1., 2.}? "))
            if hanyadik != 1 and hanyadik != 2:
                raise ErtekOutOfRange
            break

        except ErtekOutOfRange:
            print("1. vagy 2. jatekos lehetsz, {1, 2} ertekek kozul valassz ")

    while True:
        try:
            celadas = int(input("Valssz startegiat! 1: Azonos/ csupa 0 sor/oszlop letrehozasa, 2: Tabla telitese "))
            if celadas != 1 and celadas != 2:
                raise ErtekOutOfRange
            break
        except ErtekOutOfRange:
            print("1. vagy 2. strategiat valszthatod, {1, 2} ertekek kozul valassz ")

    if hanyadik == 1 and celadas == 2:
        tabla = np.array([[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]])
        print("Kezdo allapot: ")
        print(tabla)
        i = 1
        while Jatek.check(tabla):
            print(i, ". round:")
            i = i + 1
            jatekos_lep(tabla)
            allapot = Csucsok(jatekos_lep(tabla))  # ez itt nem igazan jo, raadasul nagyon hosszu ido...
            tabla = allapot.lepes()

    if hanyadik == 2 and celadas == 2:
        Jatek.jatek()

    # if hanyadik == 1 and celadas == 1:
        # erre egy megforditott nyeromezok fuggveny kell, de ennyi
    # if hanyadik == 2 and celadas == 1:
        # erre is csak az es kesz

# eredeti check tabla
# 1-nek jó:
    van_nulla = (van_sor(tabla) or van_oszlop(tabla))
    if van_nulla:
        win = True
    else:
        win = azonos_sor_oszlop(tabla)
    # 2. nyer:
    if -1 not in tabla and not win:
        print("The player won.")
        return False
    # 1. nyert
    elif win:
        show.show(tabla, title="THE COMPUTER HAS WON")
        return False
    # meg nincs vege
    else:
        return True



if __name__ == "__main__":
    main()


def dict_walks(self):
    dict_walks = {}
    for level in reversed(self.levels):
        for node in level:
            if node.state.who_win() == 0:
                dict_walks[str(node.state.table)] = [1, 0]
            elif node.state.who_win() == 1:
                dict_walks[str(node.state.table)] = [0, 1]
            else:
                dict_walks[str(node.state.table)] = [
                    sum([dict_walks[str(child.state.table)][0] for child in node.children]),
                    sum([dict_walks[str(child.state.table)][1] for child in node.children])]
    self.dict_walks = dict_walks
    return dict_walks
import json
import graph
import Fas_esetek
import networkx as nx

# todo: open dictionaris
# csak pl, hogy legyen mivel dolgoznod
d = {}  # üres szótár, ekvivalens: d = dict()
d["apple"] = 12
d["plum"] = 2
d[1]=4
d

#if __name__ == "__main__":
    #with open("proba_szoveg_kiiras.json", "w") as write_file:
        #json.dump(d, write_file)

#if __name__ == "__main__":
    #with open("proba_szoveg_kiiras.json", "r") as read_file:
        #data = json.load(read_file)
        #print(data.keys())



if __name__ == "__main__":
    #a = graph.Graph()
    #adat = a.set_dicts()
    #print(adat)
    #with open("proba_szoveg_kiiras_graf.json", "w") as write_file:
       # json.dump(adat, write_file)
    d = nx.DiGraph()
    d.add_edges_from(Fas_esetek.ossz_el(Fas_esetek.nodes()))
    with open("proba_szoveg_kiiras_graf.json", "w") as write_file:
        json.dump(adat, write_file)

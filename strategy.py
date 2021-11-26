import json
import graph

# if __name__ == "__main__":
    # a = graph.Graph()
    # adat = a.save_datas()
    # with open("proba_szoveg_kiiras_graf.json", "w") as write_file:
       # json.dump(adat, write_file)


if __name__ == "__main__":
    with open("proba_szoveg_kiiras_graf.json", "r") as read_file:
        data = json.load(read_file)
        print(len(data[0].keys()))
        print(len(data[1].keys()))

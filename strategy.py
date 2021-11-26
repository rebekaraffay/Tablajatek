import json
import graph


# if __name__ == "__main__":
  #  with open("proba_szoveg_kiiras_graf.json", "r") as read_file:
   #     data = json.load(read_file)
    #    print(len(data[0].keys()))
     #   print(len(data[1].keys()))


if __name__ == "__main__":
    b = graph.Graph()
    seta = b.dict_walks()

    with open("proba_seta.json", "w") as write_file:
        json.dump(seta, write_file)

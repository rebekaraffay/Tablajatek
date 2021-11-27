import json
import graph

# if __name__ == "__main__":
  #  with open("proba.json", "r") as read_file:
   #     data = json.load(read_file)
    #    print(len(data[0].keys()))
     #   print(len(data[1].keys()))

if __name__ == "__main__":
    q = graph.Graph().save_datas()
    with open("teljes_szulo_gyerek_szotarak.json", "w") as write_file:
        json.dump(q, write_file)

#if __name__ == "__main__":
    # p = graph.Graph().save_datas()
    # with open("proba.json", "w") as write_file:
        # json.dump(p, write_file)

#if __name__ == "__main__":
    #b = graph.Graph().dict_walk()
    #with open("proba_seta_teljes.json", "w") as write_file:
        #json.dump(b, write_file)
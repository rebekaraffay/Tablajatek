import json

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

if __name__ == "__main__":
    with open("proba_szoveg_kiiras.json", "r") as read_file:
        data = json.load(read_file)
        print(data.keys())
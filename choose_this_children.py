import json

def choose_this_children_veszto():
    """Ha az a strategia, hogy telitesre torekszik a gep, megmondja, hogy hova lepjen egy adott csucsbol, dictionary formaban""" # Jsonbe szeretnenk majd elmenteni, hogy egy csucsbol hova erdemes lepni

    with open("proba_seta_teljes.json", "r") as read_file:
        aranyok = json.load(read_file)

    with open("teljes_szulo_gyerek_szotarak.json", "r") as read_file:
        gyerek = json.load(read_file)

    choose_dict_veszto = {}
    gyerek_szotar = gyerek[1]

    for key in gyerek_szotar.keys():
        if len(gyerek_szotar[key]) == 0:
            pass
        else:
            lista = []
            for i in range(len(gyerek_szotar[key])):
                lista.append(aranyok[(gyerek_szotar[key][i])][0])
            if any(elem == 0 for elem in lista): # Ellenorizzuk, hogy egy csucs gyerekei kozott van-e olyan, amelybol nem vezet szamara vesztobe ut
                veszto = []
                veszto_lepes = sorted(gyerek_szotar[key], key=lambda x: aranyok[x][0]) #rendezzuk, igy a 0 ertekkel rendelkezo gyerekek lesznek elol
                for i in range(len(veszto_lepes)):
                    if aranyok[veszto_lepes[0]][0] == aranyok[veszto_lepes[i]][0]: #minden 0 ertekkel rendelkezo gyereket jo lepesnek tekintunk
                        veszto.append(veszto_lepes[i])
                choose_dict_veszto[key] = veszto

            else:
                veszto = []
                veszto_lepes = sorted(gyerek_szotar[key], key=lambda x: -(aranyok[x][1] / aranyok[x][0])) #ha nyero es veszto ut is megy ki egy csucsbol, akkor nyero/veszto arany szerint rendezzuk oket csokkeno sorrendbe
                for i in range(len(veszto_lepes)):
                    if aranyok[veszto_lepes[0]][1] / aranyok[veszto_lepes[0]][0] == aranyok[veszto_lepes[i]][1] / \
                            aranyok[veszto_lepes[i]][0]:
                        veszto.append(veszto_lepes[i]) #valasszuk ki a legjobb arannyal rendelkezoket
                choose_dict_veszto[key] = veszto
    return choose_dict_veszto

def choose_this_children_nyero():
    """Ha az a strategia, hogy csupa 0 vagy azonos sor/oszlop eloallitasara torekedik a gep, megmondja, hogy egy adott csucsbol hova lepjen a gep, dictionary formaban"""


    with open("proba_seta_teljes.json", "r") as read_file:
        aranyok = json.load(read_file)

    with open("teljes_szulo_gyerek_szotarak.json", "r") as read_file:
        gyerek = json.load(read_file)

    choose_dict_nyero = {}
    gyerek_szotar = gyerek[1]

    for key in gyerek_szotar.keys():
        if len(gyerek_szotar[key]) == 0:
            pass
        else:
            lista = []
            for i in range(len(gyerek_szotar[key])):
                lista.append(aranyok[(gyerek_szotar[key][i])][1])
            if any(elem == 0 for elem in lista): # Ellenorizzuk, hogy egy csucs gyerekei kozott van-e olyan, amelybol nem vezet szamara vesztobe ut
                nyero = []
                nyero_lepes = sorted(gyerek_szotar[key], key=lambda x: aranyok[x][1]) #rendezzuk, igy a 0 ertekkel rendelkezo gyerekek lesznek elol
                for i in range(len(nyero_lepes)):
                    if aranyok[nyero_lepes[0]][1] == aranyok[nyero_lepes[i]][1]: #minden 0 ertekkel rendelkezo gyereket jo lepesnek tekintunk
                        nyero.append(nyero_lepes[i])
                choose_dict_nyero[key] = nyero

            else:
                nyero = []
                nyero_lepes = sorted(gyerek_szotar[key], key=lambda x: -(aranyok[x][0]/aranyok[x][1])) #ha nyero es veszto ut is megy ki egy csucsbol, akkor nyero/veszto arany szerint rendezzuk oket csokkeno sorrendbe
                for i in range(len(nyero_lepes)):
                    if aranyok[nyero_lepes[0]][0]/aranyok[nyero_lepes[0]][1] == aranyok[nyero_lepes[i]][0]/aranyok[nyero_lepes[i]][1]: #valasszuk ki a legjobb arannyal rendelkezoket
                        nyero.append(nyero_lepes[i])
                choose_dict_nyero[key] = nyero
    return choose_dict_nyero

#if __name__ == "__main__":  #elmentjuk json file-ba
    #q = choose_this_children_nyero()
    #with open("nyero_lepesek.json", "w") as write_file:
        #json.dump(q, write_file)

if __name__ == "__main__": #elmentjuk json file-ba
    p = choose_this_children_veszto()
    with open("veszto_lepesek.json", "w") as write_file:
        json.dump(p, write_file)
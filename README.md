# Tablajáték
#### Játékszabály
    3*3-as táblán játsza két személy, 
    kétféle (o vagy x) jel bármelyikét írhatják a mezőkbe (nincs saját jel).
    Egyikük (előre meg kell állapodni, hogy melyikük) nyer,
    ha van két  egyforma (teli) sor vagy oszlop,
    vagy ha 3 darab 0 került egy vonalba. 
    Ha kilenc jel elhelyezése után egyik fenti feltétel sem  teljesül,
    másikuk a győztes.

#### Tartalom
###### Json fileok
    teljes_szulo_gyerek_szotarak.json: egy táblaálláshoz megmondja, hogy 
    oda honnan lehet eljutni és hova lehet lépni (1 hosszúak a lépések)
    kulcsok: állások
    értékek: szülők vagy gyerekek
    (2 szótár van egybe, az első a szülőket tartalmazza,
    a második a gyerekeket)
    proba_seta_teljes.json: egy táblaálláshoz megmondja, hogy belőle hány
    út vezet nyerő, illetve vesztő állásba 
    (nyerőnek mindig azt hívjuk, ha van azonos/csupa o sor/oszlop)
    kulcsok: állások
    értékek: utak száma
    nyero_lepesek.json: egy táblaálláshoz megmondja, hogy melyik 
    gyerekeibe a legérdemesebb lépni, az alapján, hogy 
    melyik gyerekeineknek a legjobb a nyerő és vesztő utak aránya
    kulcsok: állások
    értékek: legjobb lépések, abban az esetben, ha azonosakra törekszünk
    veszto_lepesek.json: egy táblaálláshoz megmondja, hogy melyik 
    gyerekeibe a legérdemesebb lépni, az alapján, hogy 
    melyik gyerekeineknek a legjobb a nyerő és vesztő utak aránya
    kulcsok: állások
    értékek: legjobb lépések, abban az esetben, ha telítésre törekszünk
    proba.json: egy táblaálláshoz megmondja, hogy 
    oda honnan lehet eljutni és hova lehet lépni (1 hosszúak a lépések)
    kulcsok: állások
    értékek: szülők vagy gyerekek, list formában
    (2 szótár van egybe, az első a szülőket tartalmazza,
    a második a gyerekeket)
###### Python fileok
    main_game.py: Maga a játék, ezt kell lefuttatni.
    Jatek.py: A játék azon verziója, ha a gép kezd és azonosakra törekszik
    computer_play.py: A játék azon verziója, ha a géppel játszik valaki
    multiplayer.py: A játék azon verziója, ha ketten szertnék játszani
    choose_this_children.py: nyero- és veszto_lepesek.json generálása
    Fas_esetek.py: Kezdetleges gráftervezés
    graph.py: Gráfosztály létrehozása
    node.py: Csúcsosztály létrehozása
    state.py: Egy állás állapotára vonatkozó osztály
    win_state: Osztály a nyerés eldöntésére
    show.py: Lépés kirajzolására függvények
    strategy.py: Json-ok generálása itt történt
    sandbox.py: Elvetett függvények
    
    
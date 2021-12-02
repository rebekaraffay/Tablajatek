# Táblajáték
#### Játékszabály
    3*3-as táblán játsza két személy, 
    kétféle (o vagy x) jel bármelyikét írhatják a mezőkbe, nincs saját jel.
    Egyikük (előre meg kell állapodni, hogy melyikük) nyer,
    ha van két egyforma (teli) sor vagy oszlop,
    vagy ha 3 darab o került egy vonalba. 
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
    azonos_esetben_vesztok.json: az állásokhoz megnézi, hogy van-e vesztő
    gyerekük, egy csúcs ebben az esetben akkor vesztő, ha azonos/o 
    oszlop/sor van benne
    kulcsok: állások
    értékek: vesztő gyerekek
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

####Stratégia és fejlesztési lehetőségek

    A játék tervezése abból indult ki, hogy észrevettük, ha a gép kezd és az a feladata, hogy azonos
    sort/oszlopot vagy csupa o sort/oszlopot létesítsen, akkor neki mindig van nyerő stratégiája.
    Ezt a külön esetet megírtuk a Jatek.py file-ban. Azt láttuk, ha a gép középre tesz egy o-t, majd 
    a továbbiakban tükrözi a játékos lépését, akkor mindig ő nyer.
    A többi játéktípusra nem találtunk ilyen egyszerűsítő stratégiát, így azokat a gráfos módszerrel
    írtuk meg. Minden táblaállás megfelel egy csúcsnak, éleket akkor húztunk be 2 csúcs között, ha 1
    lépésben elérhető az egyik a másikból. Természetesen irányított élként kezeltük az éleket. 
    A gráfot először networkx-es digráfnak szerettük volna megírni (Fas_esetek.py), de rájöttünk, hogy
    valójában gráf- és csúcsosztályokkal hatékonyabban tudunk dolgozni.
    Így létrehoztuk a graph.py, node.py és state.py által tartalmazott osztályokat. Ezeken belül
    írtuk meg a legtöbb függvényt, amelyek a játék alapját adják. Mivel kb 20000 csúcsunk van és 2 
    szint között van olyan, hogy kb 8000000 él létezését kell ellenőrizni, így a gráfokhoz tartozó főbb 
    szótárakat json fileokba kimentettük, mert a gráflétesítés futási idejét a 30-40 percről 15-18
    szűkítve sem optimális, hogy 1 játék előtt ennyit kelljen várni.
    Először olyan stratégián gondolkodtunk, hogy alulról kezdve végigcímkézzük a csúcsokat,
    mindegyikről eldöntjük, hogy nyerő-e vagy vesztő. Itt viszont minél magasabbra mentünk a gráfban,
    annál több ellentmondásos címkézésbe kerültünk. Szétbontottuk ezután aszerint, hogy ki kezd. Itt 
    a fő elv az lett volna, hogy ha a gép lép és ő tud nyerő mezőbe lépni, akkor a kezdeti csúcs 
    is nyerő, különben vesztő. Ha az ellenfél lép, akkor ha ő tud vesztőbe lépni, akkor vesztő a 
    kiinduló csúcs, különben nyerő.
    Az általunk választott stratégia végül a következő lett: Minden csúcsról megnézzük, hogy hány
    nyerőbe és hány vesztőbe érkező út indul ki belőle, és ezek arányát tekintettük. Tehát megnéztük,
    hogy egy csúcs melyik gyerekeinek a legjobb a nyerő/vesztő aránya (0 vesztő esetén,
    ezeket előre kiválasztottuk és nem néztünk arányt), és a legjobb ilyenbe léptünk.
    Ha a gép azonosakra törekszik, akkor ez a módszer jól működik. Ha telíteni szeretne, akkor némi
    problémákba futottunk. Első észrevételünk az volt, hogy ha a gép kapott egy állást, amelynek
    van az ellenfele számára nyerő gyereke, nem lépett úgy, hogy blokkolja a nyerést. Ezért ezt az
    esetet külön vettük és másik függvénnyel, szótárral megoldottuk, hogy jól lépjen. A második 
    probléma az volt, hogy ha a gép jött, akkor lépett olyan állásba is, hogy annak volt olyan 
    gyereke, ami nyerő volt az ellenfél számára. Erre is írtunk egy külön ágat és meg tudtuk oldani,
    hogy ha van más választása, akkor ne olyan állásra lépjen.
    
    A fejleszthetési lehetőségekbe tartozik az eredi tervünk (nyerő/vesztő címkézés) megvalósítása, 
    annak tökéletesítése.
    A szótárak kulcsainak és értékeinek másfajta elmentése, hogy amikor az értékekre szertnénk lépni,
    akkor könnyebben tudjuk ezeket numpyarray-jé alakítani.
    A játék PyGame-ba való áttétele, felhasználóbarátabb és szebb kivitelezése.
    
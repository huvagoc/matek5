# Követelmények – 5. osztályos matematika kvíz

Az alábbi követelmények alapján az alkalmazás teljes egészében újraépíthető.

---

## Technológia

- Egyetlen, önálló `.html` fájl – nincs külső függőség, nincs telepítés
- Vanilla HTML + CSS + JavaScript, keretrendszer nélkül
- Offline működés (internet-kapcsolat nem szükséges)
- Reszponzív: telefon és PC egyaránt
- Automatikus sötét mód (prefers-color-scheme)

---

## Általános kvíz-működés

- Minden kvíz 20 kérdésből áll
- Helyes válasz esetén automatikus továbblépés ~700 ms késleltetéssel (rövid zöld visszajelzés után)
- Helytelen válasz esetén piros hibaüzenet + „Következő" gomb jelenik meg
- Haladásjelző sáv és kérdésszámláló (pl. 7/20)
- Pontszám megjelenik a kérdések alatt
- Eredményképernyő a kvíz végén éremmel (🥇🥈🥉💪) és százalékkal
- Tizedes elválasztó: bevitelnél vessző és pont is elfogadott; megjelenítésben mindig vessző (magyar szabvány)
- Enter billentyűvel is beküldhető a válasz
- Mobilbarát: a virtuális billentyűzet megjelenésekor a kártya kompakt módra vált (`visualViewport` API)

---

## Beállítások (kezdőképernyő)

Hat témacsoportba rendezett feladatok, mindegyik önállóan ki-/bekapcsolható; minden csoportnál alcím is megjelenik:

| # | Azonosító | Megjelenített név | Alcím |
|---|-----------|-------------------|-------|
| 1 | `szamelm` | 🔢 Számelmélet és számfogalom | Helyiérték, kerekítés, oszthatóság, negatív számok |
| 2 | `muveletek` | ➕ Műveletek és algebrai gondolkodás | Alapműveletek, egyenletek, szöveges feladatok, arányosság |
| 3 | `tortek` | ½ Törtek és tizedes törtek | Törtek, tizedes törtek, műveletek |
| 4 | `geo` | 📐 Geometria | Kerület, terület, testek |
| 5 | `meres` | 📏 Mérés | Hosszúság, terület, térfogat, tömeg, idő |
| 6 | `stat` | 📊 Statisztika és valószínűség | Átlag, adatok értelmezése |

Legalább egy csoportnak mindig bekapcsolva kell maradnia. A kvíz kérdései arányosan keverednek a bekapcsolt csoportok között.

---

## 1. témacsoport – Számelmélet és számfogalom

### Kategóriák és feladattípusok

**Helyiérték** – többjegyű számok tízes, százas, ezres stb. helyiértéke; egy adott helyiértéken lévő számjegy meghatározása.

**Kerekítés** – adott szám kerekítése a megadott pontossággal (tízesre, százasra, ezresre).

**Oszthatóság** – oszthatósági szabályok (2, 3, 4, 5, 9, 10); prímszámok felismerése; megadott feltételnek megfelelő szám megtalálása.

**Negatív számok** – negatív egész számok összeadása és kivonása; számegyenesen való elhelyezés; összehasonlítás.

---

## 2. témacsoport – Műveletek és algebrai gondolkodás

### Kategóriák és feladattípusok

**Alapműveletek** – egész- és tizedes törtes összeadás, kivonás, szorzás, osztás; helyes műveleti sorrend (zárójelek).

**Egyenlet** – egyszerű egyismeretlenes egyenletek megoldása (x + a = b, a × x = b alakú).

**Szöveges feladatok** – sablon-alapú, egylépéses szöveges feladatok (ld. részletesen lent).

**Arányosság** – egyenes arányosság; egységár és mennyiség; arány felírása és alkalmazása.

### Szöveges feladatok sablonjai

Minden sablon 10 különböző megfogalmazást tartalmaz, véletlenszerűen kiválasztva. A nevek véletlenszerűek (magyar keresztnevek listájából).

1. **Út = sebesség × idő** – jármű/személy, sebesség és idő adott, keresett: km
2. **Sebesség = út ÷ idő** – megtett út és idő adott, keresett: km/h
3. **Idő = út ÷ sebesség** – távolság és sebesség adott, keresett: óra
4. **Vásárlás – összköltség** – n darab × egységár, keresett: Ft
5. **Vásárlás – visszajáró** – vételár és fizetett összeg adott, keresett: Ft
6. **Törtrész** – egész mennyiség fele/harmada/negyede/ötöde, keresett: db/fő/Ft/km stb.
7. **Kerület szöveges** – valós életbeli kontextus (kert, pálya, szoba), keresett: m vagy cm
8. **Terület szöveges** – valós életbeli kontextus (szoba, telek, szőnyeg), keresett: m² vagy cm²
9. **Életkori feladatok** – kapcsolattípusonként valós korhatárok (testvér, szülő, nagyszülő, tanár), keresett: évvel (korkülönbség)
10. **Egyenes arányosság** – egységár és mennyiség arány, keresett: Ft

Minden válasz egész szám vagy egyszerű tizedes. Feladatok egyértelműek és egyetlen számítási lépéssel megoldhatók.

---

## 3. témacsoport – Törtek és tizedes törtek

### Kategóriák és feladattípusok

**Törtek** – törtek összehasonlítása (közös nevezőre hozás); egyszerűsítés; összeadás és kivonás (azonos és különböző nevező); melyik a nagyobb tört.

**Tizedes törtek** – tizedes törtek összeadása, kivonása, szorzása egész számmal; tizedes tört és tört közötti átváltás.

### Megszorítások
- Nevezők: 2, 3, 4, 5, 6, 8, 10 (tantervi körön belül)
- Minden válasz egyszerűsített törtként vagy tizedes törtként adandó meg

---

## 4. témacsoport – Geometria

### Kategóriák és feladattípusok

**Kerület és síkterület** – négyzet, téglalap, egyenlő oldalú / egyenlő szárú / általános háromszög; mindkét irány: oldalakból számított eredmény és fordítva.

**Felület és térfogat (3D)** – téglatest és kocka felszíne (F) és térfogata (V); adott élekből számított eredmény és fordítva (adott F vagy V-ből a hiányzó él).

### Megjelenítés
- Síkidomoknál opcionális SVG-rajz kérdésenként be-/kikapcsolható (alapból kikapcsolt): ismeretlen érték zölddel és kérdőjellel jelezve, egyenlő oldalak tick markkal, derékszög-jelzők, terület-feladatoknál T-érték az alakzat belsejében; rajz mindig arányos
- 3D-testekhez cabinet (ferde axonometrikus) projekciójú SVG-rajz minden feladatnál; ismeretlen él zölddel jelezve

### Megszorítások
- Síkidomok oldalai: 2–20 cm, egész számok
- 3D-testek élei: 2–15 cm, egész számok
- Minden válasz egész szám

---

## 5. témacsoport – Mérés

### Kategóriák
- Hosszúság: mm, cm, dm, m, km
- Terület: mm², cm², dm², m², ha, km²
- Térfogat: ml, cl, dl, l, cm³, dm³, m³
- Tömeg: mg, g, dkg, kg, t
- Idő: mp, perc, óra, nap

### Feladatgenerálás
- A válasz mindig egész szám vagy legfeljebb 2 tizedesjegyű szám
- Forrásérték mindig „szép" szám (egész vagy egyszerű tizedes), tartomány: 1–5000
- Az `Idő` kategória kb. egyharmad akkora valószínűséggel kerül elő, mint a többi
- Kétirányú feladatok: kis→nagy és nagy→kis egyenlő arányban, véletlenszerűen
- ~15%-ban dupla ugrás (pl. mm→dm, kihagyva a cm-et)
- ~15%-ban tizedes vesszős válasz (.5, .25, .75 törtrész)
- Idő megjelenítése: vegyes formátum (pl. „1 óra 30 perc" az „1,5 óra" helyett)

---

## 6. témacsoport – Statisztika és valószínűség

### Kategóriák és feladattípusok

**Statisztika** – kis adatsor átlagának kiszámítása; adott átlagból hiányzó elem meghatározása; adatok értelmezése (melyik a legnagyobb/legkisebb, hány adat van egy intervallumban).

### Megszorítások
- Adatsorok elemszáma: 3–6
- Értékek: 1–100, egész számok
- Átlag minden esetben egész szám (generálás garantálja)

---

## PDF / Nyomtatás

- „Nyomtatás (PDF)" gomb a kezdőképernyőn
- 20 kérdéses feladatsort generál a bekapcsolt témakörök alapján
- Kétoszlopos elrendezés; szöveges feladatok teljes szélességben jelennek meg
- A fájlnév automatikusan tartalmazza a napot, órát, percet és másodpercet (pl. `Matek_07-14-32-05.pdf`)
- A nyomtatott oldal alján két QR-kód jelenik meg: Buy Me a Coffee és Revolut (csak nyomtatásban látható, képernyőn rejtett)
- A QR-kódok base64 formátumban ágyazva – internetkapcsolat nélkül is megjelennek

---

## Analitika

GoatCounter szkript beágyazva (konfigurálható URL).

---

## Támogatás

A kezdőképernyő alján két link jelenik meg:
- ☕ [Buy Me a Coffee](https://buymeacoffee.com/huvagoc)
- 💸 [Revolut](https://revolut.me/huvagoc)

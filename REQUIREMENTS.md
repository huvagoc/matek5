# REQUIREMENTS — Magyar Iskolai Kvíz / matek5

Technikai és funkcionális követelmények. Ez a dokumentum az aktuálisan megvalósított állapotot írja le.

---

## Architektúra

- **Egyetlen önálló fájl:** minden logika, stílus és adat egyetlen `index.html`-ben van — inline CSS, inline JS, nincsenek külső függőségek.
- **Offline-first:** futásidőben nincs hálózati hívás (kivéve a GoatCounter analytics scriptet, amely aszinkron töltődik és nem kritikus).
- **Build nélkül:** nincs npm, nincs bundler, nincs transpiler. Fejlesztéshez elegendő egy szövegszerkesztő.

---

## Képernyők

Az alkalmazás három képernyőből áll (`display:none` / `display:flex` váltással):

1. **Beállítások** (`#screen-settings`) — témakör-választó gombok, Kezdjük! gomb, Nyomtatás gomb, kódbeírós megoldáskereső, support linkek, licensz-szöveg.
2. **Kvíz** (`#screen-quiz`) — progress bar, kérdéskártya, beviteli mező, visszajelzés, Következő gomb.
3. **Eredmény** (`#screen-result`) — érem emoji, pont/20, százalék, Újra / Beállítások gombok.

---

## Témakörök és kategóriák

### Csoportok (`GROUPS`)

Minden csoportnak van `id`, `name`, `sub` és `cats` mezője.

| id | Neve | Kategóriák |
|---|---|---|
| `szamelm` | 🔢 Számelmélet és számfogalom | Helyiérték, Kerekítés, Oszthatóság, NegativSzam |
| `muveletek` | ➕ Műveletek és algebrai gondolkodás | Alapmuveletek, Egyenlet, Szöveges, Aranyossag |
| `tortek` | ½ Törtek és tizedes törtek | Tortek, TizedesTort |
| `geo` | 📐 Geometria | Kerület, Síkterület, Felület3D, Térfogat3D |
| `meres` | 📏 Mérés | Hosszúság, Terület, Térfogat, Tömeg, Idő |
| `stat` | 📊 Statisztika és valószínűség | Statisztika |

**Fontos:** a `Felület3D` és `Térfogat3D` nevek szándékosan tartalmaznak `3D` utótagot, hogy ne ütközzenek a `meres` csoport `Térfogat` kategóriájával (mértékegység-átváltás). Ezeket nem szabad átnevezni.

### Kategória-útvonalak (`buildQuiz`)

A `buildQuiz` minden kérdésnél egy véletlenszerűen kiválasztott kategóriatípust használ:

- **`conv`** (mértékegység-átváltás): `Hosszúság`, `Terület`, `Térfogat`, `Tömeg`, `Idő` — a `GEO_CATS`-ban és `ARITH_CATS`-ban nem szereplő aktív kategóriák.
- **`geo`**: `GEO_CATS`-ban lévő kategóriák (`Kerület`, `Síkterület`, `Felület3D`, `Térfogat3D`) — `GEO[cat]` generátorokon keresztül.
- **`arith`**: `ARITH_CATS`-ban lévő kategóriák — `ARITH_GENS[cat]` generátorokon keresztül.
- **`word`**: a `Szöveges` kategória — `makeWordEx()` generátoron keresztül; dupla súlyú (kétszer szerepel a pool-ban).

Az `Idő` kategória a conv-pool-ban 1/3 súlyú a többi kategóriához képest.

---

## Feladatgenerátorok

### Mértékegység-átváltás (conv)

- `CONV_UNITS`: az egységek belső értékei (`mm=1`, `cm=10`, stb.) minden dimenzióban.
- `SINGLE`/`DOUBLE`: szomszédos ill. kétlépéses pár-listák kategóriánként.
- `tryPair` / `tryPairDec`: egész ill. tizedes válaszú párok generálása.
- `makeConv(cats, dj, goUp, dec)`: összetett logika, amely több kategória között vált, ha az első próbálkozás sikertelen.
- Idő: a válasz vegyes formátumban jelenik meg, pl. `1 óra 30 perc`.

### Aritmetika (arith)

Minden `ARITH_CATS` kategóriának saját template-tömbje van:

| Kategória | Tartalom |
|---|---|
| `Helyiérték` | Helyiértékolvasás, szorzás 10-hatványaival |
| `Kerekítés` | Kerekítés tízesre/százasra/ezresre/tízezresre |
| `Oszthatóság` | Osztók száma, LNKO, LKT, prímvizsgálat-jellegű feladatok |
| `NegativSzam` | Összeadás/kivonás negatív számokkal, összehasonlítás, ellentett |
| `Alapmuveletek` | Összeadás, kivonás (nagy számok), szorzás, osztás, műveleti sorrend |
| `Egyenlet` | Egyismeretlenes egyenletek (`x + b = c`, `a·x + b = c`, stb.) |
| `Aranyossag` | Egyenes arányosság (ár, sebesség, csap, fordított arányosság) |
| `Tortek` | Egyszerűsítés, összehasonlítás, összeadás/kivonás különböző nevező, szorzás/osztás egésszel, vegyes számok; törtválasz-ellenőrzés (`isFrac`) |
| `TizedesTort` | Összeadás, kivonás, szorzás, osztás, kerekítés, tört→tizedes |
| `Statisztika` | Átlag, összeg adott átlagból, medián, terjedelem |

### Geometria (geo)

A `GEO[cat]` tömbök generátorfüggvényeket tartalmaznak. Minden generátor egy `geo(shape, given, ans, to, qLabel, viz)` objektumot ad vissza.

| Kategória | Tartalom |
|---|---|
| `Kerület` | Négyzet, téglalap, egyenlő oldalú háromszög, egyenlő szárú háromszög, általános háromszög — ismeretlen él keresése is |
| `Síkterület` | Négyzet, téglalap — terület és ismeretlen oldal |
| `Felület3D` | Téglatest felülete (`F = 2(ab+bc+ac)`), kocka felülete (`F = 6a²`) — ismeretlen él keresése is |
| `Térfogat3D` | Téglatest térfogata (`V = abc`), kocka térfogata (`V = a³`) — ismeretlen él keresése is |

SVG-vizualizáció minden geo-kérdésnél elérhető (toggle gombbal); a nyomtatott munkafüzetben mindig megjelenik.

### Szöveges feladatok (word)

`WORD_T` tömb, 10 sablon (template), mindegyikben 10 szövegváltozat. Nevek: `WN` lista (magyar keresztnevek). Témák: út-sebesség-idő, vásárlás (összköltség, visszajáró), törtrész, kerület szövegesen, korábbi összehasonlítás, egyenes arányosság.

---

## Véletlenszám-generálás és kódrendszer

- **PRNG:** xorshift32 (`_rng()`), `_seed` állapotváltozóval. Minden `randInt`, `randChoice`, `shuffle` ezen alapul.
- **Feladatlapkód** formátuma: `XXXXX-YY` (5 hex jegy: seed 20 bit; `-`; 2 hex jegy: aktív csoportok bitmaszk).
- `encodeWorksheetCode(seed, activeGroupsSet)` → kód string.
- `decodeWorksheetCode(code)` → `{seed, groups}` objektum, vagy `null`.
- A kód beírásával a megoldások bármikor visszakereshetők a `solveFromCode()` funkcióval.

---

## Válasz-ellenőrzés

- **Numerikus:** `parseNum()` (`.` és `,` is elfogadott tizedesjegyként); `Math.abs(user - correct) < 1e-9`.
- **Tört (`isFrac`):** `checkFracAnswer()` — három eredmény: `'exact'`, `'unsimplified'` (helyes, de nem egyszerűsített — pontot kap, de jelzést kap), `'wrong'`.
- **Automatikus továbblépés:** helyes válasznál 700 ms után automatikusan a következő kérdésre lép (kivéve ha az egyszerűsítésre figyelmezteti a tanulót).

---

## Nyomtatás / PDF

`printWorksheet()` menete:

1. Új véletlenszerű seed generálása → kód kódolása → `buildQuiz()`.
2. `#print-area` feltöltése: fejléc (cím, név/dátum/kód sor), 2 hasábos grid, 20 feladat, QR-kódok (base64, inline).
3. `document.title` = `Matek_DD-HH-MM-SS` (PDF fájlnévhez).
4. 300 ms várakozás, majd `window.print()`, végül a cím visszaállítása.

Geo-kérdéseknél a vizualizáció mindig megjelenik nyomtatásban. Szöveges és többsoros feladatok teljes szélességű (`wide`) cellában kerülnek a rácsba.

---

## Megjelenítés

- **Decimális formátum:** megjelenítés mindig vesszővel (`hf()` helper), bevitel `.` és `,` egyaránt elfogadott.
- **Keyboard compact mód:** `window.visualViewport` alapján, ha a látható magasság < 65% a képernyőhöz képest — `.kb` class a body-n, kompaktabb padding/fontméret.
- **Sötét mód:** `@media (prefers-color-scheme: dark)` — CSS változók átírásával.
- **Support linkek:** csak a beállítások képernyőn láthatók; nyomtatásban QR-kódként jelennek meg.

---

## Korlátok és ismert jellemzők

- Minden válasz egész szám, legfeljebb 2 tizedesjegyű szám, vagy tört (egyszerűsített alakban).
- Az `Idő` kategória ~1/3 súlyú a többi conv kategóriához képest (a kevert idő-megjelenítés miatt).
- Tört-feladatnál az egyszerűsítetlen, de helyes válasz pontot kap, de jelzést ad.
- Geo-kérdéseknél a vizualizáció alapból rejtett, a tanuló dönthet a megjelenítéséről.
- Legalább egy csoportnak aktívnak kell lennie (a UI ezt kényszeríti).

---

## Fájlstruktúra (egyetlen fájl belső sorrendje)

1. CSS (változók, layout, keyboard compact, sötét mód, nyomtatási stílusok)
2. HTML (beállítások képernyő, kvíz képernyő, eredmény képernyő, rejtett nyomtatási terület)
3. JS — adatok: `CONV_UNITS`, `SINGLE`, `DOUBLE`, PRNG, kódolás, `SVG` helpek, `GEO` generátorok, `WORD_T` sablonok, `GROUPS`, `ARITH_GENS`
4. JS — logika: `buildQuiz`, `renderQ`, `submitAnswer`, `nextQuestion`, `printWorksheet`, `solveFromCode`, keyboard-detect
5. A fájl végén (az `</script>` után): `Felület3D` és `Térfogat3D` generátorok + GoatCounter analytics script

---

## Tervezett fejlesztések (még nem valósult meg)

- **6. osztályos tantárgyak:** külön `index.html` fájlok, azonos architektúra.

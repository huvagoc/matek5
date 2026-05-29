# Átváltás-kvíz 🎓

Egy egyszerű, böngészőben futó kvíz alkalmazás **5. osztályos mértékegység-átváltáshoz**, magyar tantervnek megfelelően. Letöltés és telepítés nélkül használható – egyetlen `.html` fájl, amely bármilyen eszközön (telefon, tablet, PC) működik.

---

## Célja

A Magyar Nemzeti Alaptanterv 5. osztályos matematika anyagához igazodó, interaktív gyakorló eszköz mértékegység-átváltáshoz. A tanuló saját tempójában, játékos formában ismételheti az anyagot – bárhol, internetkapcsolat nélkül is.

---

## Funkciók

- **5 kategória:** Hosszúság, Terület, Térfogat, Tömeg, Idő
- **Kétirányú feladatok:** felváltva kis→nagy és nagy→kis átváltás
- **Dupla ugrás:** minden 4. kérdés egységet átugrós átváltás (pl. mm → dm)
- **Magyar tizedes vessző** a megjelenítésben (pl. `1,5 óra`), de pont is elfogadott bevitelnél
- **Vegyes időkijelzés:** tizedes órák helyett „1 óra 30 perc" formátum
- **Automatikus továbblépés** helyes válasz esetén (rövid visszajelzés után)
- **Mobilbarát elrendezés:** a virtuális billentyűzet megjelenésekor kompakt módra vált
- **Kategória-szűrő:** a beállítás képernyőn kiválasztható, melyik kategóriákból jelenjenek meg kérdések
- **Eredményképernyő** érem-visszajelzéssel (🥇🥈🥉💪)
- **Sötét mód** automatikusan, az eszköz beállítása alapján

---

## Telepítés / Használat

1. Töltsd le az `atvaltas_kviz.html` fájlt
2. Nyisd meg bármilyen böngészőben (Chrome, Safari, Firefox)
3. Opcionálisan: tedd fel a [Netlify Drop](https://app.netlify.com/drop) oldalra a folyamatos online elérhetőségért – húzd rá a fájlt, és azonnal kapsz egy nyilvános URL-t

---

## A projekt fejlődése – követelmények és promptok összefoglalója

A projekt Claude AI segítségével, iteratív fejlesztéssel készült. Az alábbiakban összefoglaljuk az egyes fejlesztési lépéseket.

---

### 1. lépés – Python szkript alapok

**Kérés:**
> „Van egy 5. osztályos gyerekem, aki magyar iskolában tanul mértékegység-átváltást (mm–dm, m–km, l–dm³, mm²–cm² stb.). Írj Python kódot, ami véletlenszerű feladatokat generál: SZÁM MÉRTÉKEGYSÉG – ??? CÉLMÉRTÉKEGYSÉG formában."

**Eredmény:**
- Python szkript, amely véletlenszerű átváltási feladatokat generál
- 5 kategória: Hosszúság, Terület, Térfogat, Tömeg, Idő
- Feladatlap és megoldókulcs nyomtatható formátumban
- Egész szám vagy egyszerű tizedes választ generál
- Parancssori kapcsolók: `--n`, `--answers`, `--seed`, `--cat`

---

### 2. lépés – Kvíz formátum, kategória-konfiguráció, dupla ugrás

**Kérés:**
> „Csak a kvíz formátumot tartsd meg, a többit dobd ki. Kódban legyen konfigurálható, hogy melyik kategóriák aktívak (kikommentezéssel). Minden 4. kérdés legyen dupla ugrás, pl. mm → dm."

**Eredmény:**
- Interaktív parancssori kvíz mód
- `ACTIVE_CATEGORIES` lista kikommentezéssel szűrhető
- `QUIZ_LENGTH` konfigurálható
- Minden 4. kérdés kétlépéses átváltás
- Helyes/helytelen visszajelzés, végeredmény

---

### 3. lépés – Kétirányú feladatok, magyar tizedes vessző, egységrendszer finomítás

**Kérés:**
> „Az 'a' (ár) mértékegységet vedd ki, a 'ha' maradhat m² és km² mellé. Legyen kétirányú: nagy→kis és kis→nagy is. Magyarországon tizedes vesszőt használunk, nem pontot."

**Eredmény:**
- `a` (ár) mértékegység eltávolítva
- Páros kérdések: nagy→kis (`↓`), páratlan kérdések: kis→nagy (`↑`)
- Megjelenítésben tizedes vessző; bevitelnél mindkettő elfogadott
- A helyes válasz visszajelzésnél is vesszős formátum

---

### 4. lépés – Webes alkalmazás (HTML)

**Kérés:**
> „Meg lehet ezt tenni elérhetővé telefonon és/vagy PC-n, hogy 'menet közben' is lehessen játszani?"

**Eredmény:**
- Önálló `.html` fájl, minden logika benne, internetet nem igényel
- Kategória-kapcsoló a beállítások képernyőn (koppintással)
- Haladásjelző sáv, visszajelzések, eredményképernyő érmekkel
- Sötét mód automatikus támogatás

---

### 5. lépés – UX finomhangolás (mobilbarátság)

**Kérések (egyszerre):**
> 1. Helyes válasz esetén automatikusan lépjen a következő kérdésre
> 2. Vesszőt és pontot is fogadjon el; csak vesszőt jelenítsen meg
> 3. Mobilon a virtuális billentyűzet miatt ne csússzon el az elrendezés
> 4. A fejléceket (Idő, kis→nagy stb.) el lehet hagyni az elrendezés tömörítéséhez

**Eredmény:**
- Helyes válasz esetén 700 ms után automatikus továbblépés
- Hibás válasznál „Következő" gomb jelenik meg
- `visualViewport` API alapú billentyűzet-detekció: `.kb` CSS osztály vált kompakt módba
- Kategória- és irány-feliratok eltávolítva

---

### 6. lépés – Időkategória finomítás

**Kérések (egyszerre):**
> 1. Az időfeladatok legyenek ritkábbak
> 2. Tizedes értékek helyett vegyes formátum: pl. „1 óra 30 perc" az „1,5 óra" helyett

**Eredmény:**
- Az `Idő` kategória kb. 1/3 akkora valószínűséggel kerül kiválasztásra (~8% a többi ~23%-ával szemben)
- `formatTimeSrc()` függvény: törtórákat „X óra Y perc" formában jeleníti meg
- Érintett egységpárok: `nap` → „X nap Y óra", `óra` → „X óra Y perc", `perc` → „X perc Y s"

---

## Technikai megjegyzések

- Keretrendszer nélküli, tiszta HTML/CSS/JS
- Külső függőség: nincs
- A véletlenszám-generátor garantálja, hogy a **válasz mindig egész szám**, a forrásérték legfeljebb 2 tizedes jegyű
- A kategóriák és az egységpárok a kódban egyszerűen bővíthetők

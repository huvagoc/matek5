# 🧮 Matek kvíz — 5. osztály

Böngészőalapú, offline-képes matematika kvízalkalmazás 5. osztályos tanulók számára.

**Élő:** https://huvagoc.github.io/matek5  
**Repo:** https://github.com/huvagoc/matek5

---

## Mi ez?

Egyetlen HTML-fájl, amely véletlenszerű matematika feladatokat generál az 5. osztályos tananyag hat témakörére. Nincs telepítés, nincs bejelentkezés — csak megnyitod és oldasz feladatokat.

A kvíz 20 kérdésből áll. A végén pontszámot és százalékot mutat. Visszajelzés minden kérdés után azonnal jelenik meg.

---

## Témakörök

| Csoport | Tartalma |
|---|---|
| 🔢 Számelmélet | Helyiérték, kerekítés, oszthatóság (LNKO/LKT), negatív számok |
| ➕ Műveletek | Alapműveletek, egyenletek, szöveges feladatok, arányosság |
| ½ Törtek | Törtek egyszerűsítése, összeadás/kivonás/szorzás/osztás; tizedes törtek |
| 📐 Geometria | Kerület, síkterület, testek felülete és térfogata (téglatest, kocka) |
| 📏 Mérés | Mértékegység-átváltás: hosszúság, terület, térfogat, tömeg, idő |
| 📊 Statisztika | Átlag, medián, terjedelem |

A témakörök be- és kikapcsolhatók a beállítások képernyőn.

---

## Nyomtatás / PDF-munkafüzet

A **Nyomtatás (PDF)** gomb 20 feladatot generál - az aktív témakörökben - nyomtatható formában, két hasábos elrendezésben. A lapon megjelenik egy rövid kód (pl. `A3F7B-3F`). Ezt a kódot beírva a kvíz főoldalán visszakapod a megoldásokat — így a tanár kézzel is ellenőrizhet.

---

## Technikai adatok

- Egyetlen `index.html` fájl — keretrendszer, npm vagy build eszköz nélkül
- Teljesen offline működik (nincs hálózati függőség futásidőben)
- Reszponzív: mobil és asztali képernyőn egyaránt használható
- Automatikus sötét mód (`prefers-color-scheme`)
- Seeded PRNG (xorshift32): minden nyomtatott feladatlap reprodukálható a kódja alapján
- Analytics: GoatCounter (privacy-friendly, nincs süti)

---

## Licensz

© 2026 Vágó Csaba — [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)  
Nem kereskedelmi célra szabadon felhasználható, a szerző megjelölésével.

---

## Támogatás

Ha hasznos volt, megköszönöm:  
☕ [buymeacoffee.com/huvagoc](https://buymeacoffee.com/huvagoc) · 💸 [revolut.me/huvagoc](https://revolut.me/huvagoc)  
✉️ Visszajelzés: matek-kviz@pm.me

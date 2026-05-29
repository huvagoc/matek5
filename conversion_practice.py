"""
Mértékegység-átváltó kvíz – 5. osztály
=======================================
Konfiguráció: kommenteld ki a nem kívánt kategóriákat az ACTIVE_CATEGORIES listában.
Futtatás: python conversion_practice.py
"""

import random
from fractions import Fraction

# ---------------------------------------------------------------------------
# CONFIG – kommenteld ki amit NEM akarsz
# ---------------------------------------------------------------------------

ACTIVE_CATEGORIES = [
    "Hosszúság",
    "Terület",
    "Térfogat",
    "Tömeg",
    "Idő",
]

QUIZ_LENGTH = 20   # hány kérdés legyen

# ---------------------------------------------------------------------------
# Unit maps
# ---------------------------------------------------------------------------

UNITS = {
    "Hosszúság": {
        "chain": ["mm", "cm", "dm", "m", "km"],
        "map":   {"mm": 1, "cm": 10, "dm": 100, "m": 1_000, "km": 1_000_000},
    },
    "Terület": {
        "chain": ["mm²", "cm²", "dm²", "m²", "ha", "km²"],
        "map":   {
            "mm²": 1, "cm²": 100, "dm²": 10_000, "m²": 1_000_000,
            "ha":  10_000_000_000,
            "km²": 1_000_000_000_000,
        },
    },
    "Térfogat": {
        "chain": ["ml", "dl", "l", "dm³", "m³"],
        "map":   {
            "ml": 1, "cl": 10, "dl": 100, "l": 1_000,
            "cm³": 1, "dm³": 1_000, "m³": 1_000_000,
        },
    },
    "Tömeg": {
        "chain": ["mg", "g", "dkg", "kg", "t"],
        "map":   {"mg": 1, "g": 1_000, "dkg": 10_000, "kg": 1_000_000, "t": 1_000_000_000},
    },
    "Idő": {
        "chain": ["s", "perc", "óra", "nap"],
        "map":   {"s": 1, "perc": 60, "óra": 3_600, "nap": 86_400},
    },
}

# Single-step pairs – always listed small → large; direction is handled at runtime
SINGLE_PAIRS = {
    "Hosszúság": [("mm","cm"), ("cm","dm"), ("dm","m"), ("m","km")],
    "Terület":   [("mm²","cm²"), ("cm²","dm²"), ("dm²","m²"), ("m²","ha"), ("ha","km²")],
    "Térfogat":  [("ml","dl"), ("dl","l"), ("l","dm³"), ("dm³","m³")],
    "Tömeg":     [("mg","g"), ("g","dkg"), ("dkg","kg"), ("kg","t")],
    "Idő":       [("s","perc"), ("perc","óra"), ("óra","nap")],
}

# Double-step pairs (skip one unit) – small → large; direction handled at runtime
DOUBLE_PAIRS = {
    "Hosszúság": [("mm","dm"), ("cm","m"), ("dm","km")],
    "Terület":   [("mm²","dm²"), ("cm²","m²"), ("dm²","ha"), ("m²","km²")],
    "Térfogat":  [("ml","l"), ("dl","dm³"), ("l","m³")],
    "Tömeg":     [("mg","dkg"), ("g","kg"), ("dkg","t")],
    "Idő":       [("s","óra"), ("perc","nap")],
}

MAX_ANSWER = 50_000
SRC_MAX    = 5_000


# ---------------------------------------------------------------------------
# Number formatting – Hungarian decimal comma
# ---------------------------------------------------------------------------

def hu(number_str):
    """Replace decimal point with comma for Hungarian display."""
    return number_str.replace(".", ",")


def _nice_str(frac):
    """Return a display string (Hungarian comma) or None if not a nice number."""
    if frac.denominator == 1:
        return str(int(frac))
    f = float(frac)
    for dp in (1, 2):
        if abs(f - round(f, dp)) < 1e-9:
            return hu(str(round(f, dp)))
    return None


# ---------------------------------------------------------------------------
# Exercise generation
# ---------------------------------------------------------------------------

def _try_pair(small_unit, large_unit, unit_map, go_up):
    """
    go_up=True  → question asks small → large  (e.g. 500 cm = ? m)   answer < source
    go_up=False → question asks large → small  (e.g. 3 m   = ? cm)   answer > source

    We always generate a nice integer answer, then back-calculate the source value.
    """
    if go_up:
        from_unit, to_unit = small_unit, large_unit
    else:
        from_unit, to_unit = large_unit, small_unit

    # factor: answer = source * factor
    factor = Fraction(unit_map[from_unit], unit_map[to_unit])

    for _ in range(500):
        ans_int = random.randint(1, 999)
        src_frac = Fraction(ans_int) / factor
        sf = float(src_frac)
        if not (1 <= sf <= SRC_MAX):
            continue
        src_s = _nice_str(src_frac)
        if src_s is None:
            continue
        if ans_int > MAX_ANSWER:
            continue
        return src_s, str(ans_int), from_unit, to_unit

    return None


def make_exercise(double_jump=False, go_up=True):
    """
    Build one exercise.
    double_jump → skip-one-step pair
    go_up       → small-to-large (True) or large-to-small (False)
    """
    cats = list(ACTIVE_CATEGORIES)
    random.shuffle(cats)

    pairs_pool = DOUBLE_PAIRS if double_jump else SINGLE_PAIRS

    for cat in cats:
        unit_map = UNITS[cat]["map"]
        pairs = pairs_pool.get(cat, [])
        if not pairs:
            continue
        candidates = pairs[:]
        random.shuffle(candidates)
        for small, large in candidates:
            result = _try_pair(small, large, unit_map, go_up)
            if result:
                src_s, ans_s, frm, to = result
                return {
                    "category": cat,
                    "from":     frm,
                    "to":       to,
                    "value":    src_s,
                    "answer":   ans_s,
                    "double":   double_jump,
                    "go_up":    go_up,
                }

    # Fallback: flip direction or drop to single
    if double_jump:
        return make_exercise(double_jump=False, go_up=go_up)
    return make_exercise(double_jump=False, go_up=not go_up)


# ---------------------------------------------------------------------------
# Quiz
# ---------------------------------------------------------------------------

def run_quiz():
    print("\n🎓 Átváltás-kvíz!  Írd be a választ (tizedes vessző: pl. 1,5), majd nyomj Entert.")
    print(f"   Aktív kategóriák: {', '.join(ACTIVE_CATEGORIES)}")
    print(f"   Minden 4. kérdés dupla ugrás (pl. mm → dm).")
    print(f"   Felváltva: kis → nagy  és  nagy → kis.\n")

    correct = 0

    for i in range(1, QUIZ_LENGTH + 1):
        double = (i % 4 == 0)    # every 4th question is a double jump
        go_up  = (i % 2 == 1)    # odd questions: small→large; even: large→small

        ex = make_exercise(double_jump=double, go_up=go_up)

        arrow = "↑" if go_up else "↓"
        tag   = f"⚡ DUPLA {arrow}" if double else f"       {arrow}"
        print(f"  {i:>2}/{QUIZ_LENGTH}  {tag}  [{ex['category']}]  {ex['value']} {ex['from']} = _______ {ex['to']}")

        try:
            raw  = input("          Válaszod: ").strip()
            user = raw.replace(",", ".")   # accept both comma and point internally
        except (EOFError, KeyboardInterrupt):
            print("\nKilépés.")
            break

        # Compare: normalise both to float for comma-vs-point tolerance
        try:
            correct_val = float(ex["answer"])
            user_val    = float(user)
            match = abs(user_val - correct_val) < 1e-9
        except ValueError:
            match = False

        if match:
            print("          ✅ Helyes!\n")
            correct += 1
        else:
            print(f"          ❌ Helytelen. Helyes: {hu(ex['answer'])} {ex['to']}\n")

    pct = round(100 * correct / QUIZ_LENGTH)
    print(f"{'='*42}")
    print(f"  Végeredmény: {correct}/{QUIZ_LENGTH} pont  ({pct}%)")
    print(f"{'='*42}\n")


if __name__ == "__main__":
    run_quiz()
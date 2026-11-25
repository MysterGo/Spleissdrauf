#!/usr/bin/env python3
"""Fachlicher Check für „Spleiß drauf!“
Prüft alle Sequenzen aus index.html gegen den Standard-Code (Codesonne, NCBI-Tabelle 1).
Aufruf:  python3 tools/check_sequences.py
"""
import re, pathlib, sys

html = pathlib.Path(__file__).resolve().parent.parent.joinpath("index.html").read_text(encoding="utf-8")
seq = dict(re.findall(r"^\s*(utr5|ex1|intr|ex2|utr3|prok):'([ACGU]+)'", html, re.M))

# Standard-Code, Basenreihenfolge U C A G (wie in der Codesonne)
AA = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
B = "UCAG"
CODE = {a + b + c: AA[16 * i + 4 * j + k] for i, a in enumerate(B) for j, b in enumerate(B) for k, c in enumerate(B)}
# Stichproben gegen Lehrbuchwissen
for c, a in {"AUG": "M", "UGG": "W", "UAA": "*", "UAG": "*", "UGA": "*", "UUU": "F", "GGC": "G", "CGC": "R", "GAA": "E", "ACU": "T", "UCU": "S", "AUU": "I"}.items():
    assert CODE[c] == a, f"Codesonne falsch bei {c}"

def tr(s):
    i = s.find("AUG"); out = ""
    while i + 3 <= len(s):
        a = CODE[s[i:i + 3]]
        if a == "*": return out + "*"
        out += a; i += 3
    return out + "…(kein Stopp)"

pre = seq["utr5"] + seq["ex1"] + seq["intr"] + seq["ex2"] + seq["utr3"]
mat = seq["utr5"] + seq["ex1"] + seq["ex2"] + seq["utr3"]
ok = True
def check(cond, msg):
    global ok
    print(("✅ " if cond else "❌ ") + msg); ok &= cond

check(tr(mat) == "MISTERG*", f"Reife mRNA → {tr(mat)} (erwartet MISTERG*)")
check(tr(seq["prok"]) == "MISTERG*", f"Bakterien-mRNA → {tr(seq['prok'])}")
check(tr(pre) != "MISTERG*", f"Unreife prä-mRNA → {tr(pre)} (muss falsch sein)")
check(seq["intr"].startswith("GU") and seq["intr"].endswith("AG"), "Intron beginnt mit GU und endet mit AG")
check("CUAAC" in seq["intr"][:-6], "Verzweigungsstelle (A) vor dem Pyrimidin-Abschnitt")
check(pre.count("AAUAAA") == 1, "Genau ein Polyadenylierungssignal AAUAAA")
d = len(seq["utr3"]) - (seq["utr3"].find("AAUAAA") + 6)
check(10 <= d <= 30, f"Schnittstelle {d} nt hinter dem Signal (10–30)")
sd, st = seq["prok"].find("AGGAGG"), seq["prok"].find("AUG")
check(5 <= st - (sd + 6) <= 10, f"Shine-Dalgarno {st - (sd + 6)} nt vor dem Start-AUG (5–10)")
check(seq["utr5"][-3] in "AG", "Kozak-Kontext: Purin an Position −3")

# Spleiß-Rätsel: Es darf nur EINE regelkonforme Lösung mit 7 Aminosäuren geben
sol = [(a, b) for a in range(len(pre) - 1) if pre[a:a + 2] == "GU"
       for b in range(a + 3, len(pre)) if pre[b - 1:b + 1] == "AG" and tr(pre[:a] + pre[b + 1:]) == "MISTERG*"]
check(len(sol) == 1, f"Spleiß-Rätsel eindeutig lösbar: {sol}")
# DNA-Ansicht: codogener Strang muss komplementär zur RNA sein (T statt U)
comp={"A":"T","T":"A","G":"C","C":"G"}
dna=seq["prok"].replace("U","T"); tpl="".join(comp[b] for b in dna)
check(all({"A":"U","T":"A","G":"C","C":"G"}[t]==r for t,r in zip(tpl,seq["prok"])), "Codogener Strang ist komplementär zur mRNA")
prom=dict(re.findall(r"(promP35|promP10|tata):'([ACGT]+)'", html))
check(prom.get("promP35")=="TTGACA" and prom.get("promP10")=="TATAAT", "Bakterien-Promotor −35 TTGACA / −10 TATAAT (Konsensus)")
check(prom.get("tata")=="TATAAA", "Eukaryoten-TATA-Box TATAAA (Konsensus)")

# Alternatives Spleißen: Gen M mit vier Exons, drei Zelltypen
alt = dict(re.findall(r"(altE[1-4]|altI[1-3]):'([ACGU]+)'", html))
E = [alt[f"altE{i}"] for i in range(1, 5)]
for i in range(1, 4):
    it = alt[f"altI{i}"]
    check(it.startswith("GU") and it.endswith("AG"), f"Alt-Intron {i} beginnt mit GU, endet mit AG")
check(all(len(e) % 3 == 0 for e in E), "Alle Alt-Exons sind Vielfache von 3 (Leserahmen bleibt erhalten)")
v = {"Leber": [0, 1, 3], "Nerv": [0, 2, 3], "Muskel": [0, 1, 2, 3]}
prots = {}
for n, k in v.items():
    prots[n] = tr("".join(E[i] for i in k)); check(prots[n].endswith("*") and prots[n].startswith("M"), f"{n}: {prots[n]}")
check(len(set(prots.values())) == 3, "Drei verschiedene Proteine aus einem Gen")
import itertools
noE1 = [k for r in range(1, 4) for k in itertools.combinations([1, 2, 3], r)]
check(all("AUG" not in "".join(E[i] for i in k) for k in noE1), "Ohne Exon 1 gibt es in keiner Kombination ein Startcodon AUG")
check(all(CODE[E[i][j:j+3]] != "*" for i in range(3) for j in range(0, len(E[i]), 3)), "Kein vorzeitiges Stoppcodon in Exon 1–3")
sys.exit(0 if ok else 1)

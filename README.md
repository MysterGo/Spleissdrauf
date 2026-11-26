# Spleiß drauf! – Kernlos glücklich?

Ein Point-and-Click-Adventure für den Biologie-Leistungskurs: **Proteinbiosynthese bei Pro- und Eukaryoten** – entdeckend gelernt, mit Mister G als frechem Lernbegleiter.

**Prototyp v0.6** · Illustrationsstil · optimiert für iPads (auch 9. Generation), Querformat, nur Touch · läuft komplett im Browser, keine Installation.

## Spielablauf (ca. 45–60 Minuten)

| Station | Was die Schüler entdecken |
|---|---|
| **Akt 1 · Club Kernlos** (Bakterium) | Alles direkt in der Zelle: DJ Polly auf den richtigen Promotor ziehen (Gen G7 – nicht G5/G9), mRNA wächst live, Ribosom selbst zusammenbauen (erst kleine 30S-Untereinheit auf die Shine-Dalgarno-Sequenz, dann große 50S), Bonus-Polysom. Dann laufen Exo- und Endonukleasen ins Bild, stellen sich vor und zerlegen die mRNA – mit Erklärung, warum die Zelle das macht. |
| **Akt 2 · Zellkern** (Eukaryot) | Der Kern ist von der doppelten Kernhülle mit Kernporen umschlossen. Im Genarchiv erst TF-Ida (TFIID) auf die TATA-Box ziehen, dann Frau Polli (RNA-Pol II) → die prä-mRNA liegt als Objekt im Kern → Herr Nup (Kernpore) lässt sie nicht raus → Zutaten sammeln und verarbeiten: **GTP + SAM** zur m7G-Kappe kombinieren und ans 5′-Ende setzen; **U1 und U2** aus dem Cajal-Körperchen zu Snurpy bringen, Intron nach GU-AG-Regel markieren; **ATP-Fass** zur Poly-A-Bar, AAUAAA finden und ~200 A „zapfen“ → mRNA zu Herrn Nup ziehen → Export |
| **Akt 2 · Cytoplasma** | Zelle mit Zellmembran, Kern links angeschnitten. Reife mRNA aufs Ribosom ziehen, für jedes Codon die passende tRNA in die A-Stelle → **M-I-S-T-E-R-G** 😎 → die Exo-Brüder laufen von selbst zur mRNA und knabbern am Poly-A-Schwanz – das Ribosom produziert weiter |
| **Kapitel · Alternatives Spleißen** | Snurpy hat einen Großauftrag: Gen M mit 4 Exons, drei Zelltypen (Leber, Nerv, Muskel) bestellen verschiedene Proteine. Die Spieler wählen die Exons aus, die Codesonne hilft. Ohne Exon 1 kein Start, ohne Exon 4 kein Stopp. Ergebnis: **ein Gen → drei Proteine**, spart DNA-Platz und Energie. |
| **Forschungstagebuch** | Vergleichstabelle Pro-/Eukaryoten (22 Karten frei einsortieren, auch umsortieren). **Überprüfen** markiert nur die falschen Felder rot (2 ATP pro Fehler), richtige werden nicht verraten. Erst wenn alles stimmt, öffnet die Rennbahn. Notfalls legt Mister G gegen ATP eine Karte richtig. Druck/PDF zur Sicherung. |
| **Finale · Rennbahn** | Splitscreen-Rennen, zwei Personen an einem iPad. **Beide** springen über Exonukleasen (Antippen der eigenen Hälfte). **Prokaryot:** baut am schnellsten, aber ungeschützt; zusätzlich schwebt eine **Endonuklease** über der mRNA und muss weggetippt werden, bevor sie schneidet. **Eukaryot:** zieht vor jeder mRNA Kappe und Poly-A dran; Poly-A schluckt Treffer, danach folgt **Decapping**; **microRNAs** stoppen die Produktion, bis man sie wegtippt; **Zell-Aufträge** (Leber/Nerv/Muskel) bringen über die richtige Protein-Variante Bonuspunkte. Wertung: 1 Punkt pro Protein, +5 pro Variante – Menge gegen Vielfalt. Getestet mit simulierten Spielern: Geschickte Prokaryoten gewinnen knapp, schlampige verlieren, weil sie ungeschützt sind. |

**Mister G** erklärt das Hintergrundwissen: Um seinen Kopf (unten rechts) erscheinen **goldene Fragezeichen** mit dem passenden Thema der aktuellen Aufgabe (z. B. „Promotor“, „5′-Cap“, „Spleißen“). Antippen öffnet seine Erklärkarte mit Schaubild. Ihn selbst antippen gibt einen Spruch. Im Tagebuch hilft er als letzte Rettung gegen ATP.

## Veröffentlichen auf GitHub Pages

1. Inhalt dieses Ordners in ein Repo legen, z. B. `mystergo/spleiss-drauf`.
2. Im Repo: **Settings → Pages → Branch: `main` / root → Save**.
3. Nach ca. 1 Minute läuft das Spiel unter `https://mystergo.github.io/spleiss-drauf/`.

Tipp für die iPads: In Safari **Teilen → Zum Home-Bildschirm**, dann startet das Spiel im Vollbild ohne Browserleiste.

## Sprechblasen, Lernkarten & Tagebuch

Figuren sprechen in Sprechblasen direkt an ihrer Position. Wenn Mister G Bedienelemente erklärt (Auftrag, Inventar, ATP, Tagebuch, Hilfe), leuchten sie dabei auf.


Die Schüler müssen nichts vorher wissen: Bei jedem neuen Vorgang (Transkription, Promotor, Translation, Shine-Dalgarno, TATA-Box, Prozessierung, Cap, Spleißen, Poly-A, Export, tRNA, Abbau …) gibt es eine kurze **Lernkarte** mit Schaubild und „Merke“-Satz. Sie springt erst beim ersten Fehlversuch auf (vorher reicht der Satz der Figur) und liegt sonst still im Tagebuch. In jedem Rätsel erscheinen die passenden Fragezeichen an Mister Gs Kopf. Alle Karten sind im Tagebuch unter „Lernkarten“ nachlesbar.

Jeder neue Tagebuch-Eintrag wird einmal angezeigt („Neue Erkenntnis“) und muss gelesen werden, bevor er später einsortiert wird.

## ATP-Haushalt

Start mit 15 ATP. Belohnungen sind halbiert, Fehler kosten das 1,5-Fache (Werte `GAIN` und `COST` oben in `src/game.html`). Falsche Kombinationen, falsch gezogene Moleküle, falsche Tagebuch-Felder und Mister Gs Hilfe kosten ATP.
Bei 0 ATP gibt es kein Essen mehr, sondern ein Duell **Schere, Stein, Papier gegen Mister G**: Wer zuerst 3 Runden gewinnt. Sieg = 12 ATP, Niederlage = **Zelltod**, das Kapitel beginnt von vorn (mit 15 ATP). Beim Duell schütteln beide dreimal die Faust („Schere … Stein … Papier!“), dann werden die Hände aufgedeckt.

**Mini-Game:** Nach dem Rennen gibt es den Knopf **✊ Mini-Game** (in der Auswertung, im Menü ☰ und auf dem Titelbild): Schere, Stein, Papier gegen Mister G, nur zum Spaß, ohne ATP-Folgen.

## Bedienung

Fast alles geht per **Ziehen**: Figuren auf ihren Arbeitsplatz, die mRNA zu den Stationen, Zutaten aus dem Inventar auf Figuren oder aufeinander (kombinieren), tRNAs ins Ribosom. Alternativ: Gegenstand antippen, dann Ziel antippen.

## Bearbeiten

Der Quelltext liegt in `src/game.html`. Nach Änderungen `python3 tools/build.py` ausführen – das baut `index.html` und bettet Mister-G-Bild und Schriften ein (alles in einer Datei, keine Google-Fonts nötig, läuft auch im gesperrten Schulnetz).

## Lehrkraft-Menü

Menü (☰) → **Lehrkraft-Menü** → Code `G7`
- Zu Akt 2 springen
- Alles freischalten (zum Testen des Finales)
- Fortschritt löschen

Der Spielstand wird automatisch im Browser des iPads gespeichert.

## Fachlicher Check

Alle Sequenzen sind gegen den Standard-Code (Codesonne) geprüft. Nach jeder Änderung an den Sequenzen in `index.html`:

```
python3 tools/check_sequences.py
```

Geprüft wird u. a.: Promotor- und TATA-Konsensus, Komplementarität codogener Strang ↔ mRNA, Übersetzung = MISTERG + Stopp, GU…AG-Grenzen, Verzweigungsstelle, Poly-A-Signal mit Schnitt 10–30 nt dahinter, Abstand Shine-Dalgarno → AUG, dass das Spleiß-Rätsel **genau eine** richtige Lösung hat und dass beim alternativen Spleißen alle Varianten im Leserahmen bleiben, drei verschiedene Proteine ergeben und ohne Exon 1 kein Startcodon entsteht. Zusätzlich prüft sich das Spiel beim Laden selbst (Meldung in der Browser-Konsole).

**Bewusste Vereinfachungen** (im Spiel teils erwähnt): Alle Sequenzen sind stark verkürzt, echte Introns sind meist hunderte bis tausende Basen lang. Spleißen, Capping und Polyadenylierung laufen in echt weitgehend kotranskriptionell ab, im Spiel als nacheinander lösbare Stationen. Die Spleißstellen zeigt der Spieler an, in echt erkennt das Spleißosom sie selbst.

## Dateien

```
index.html                  das komplette Spiel (eine Datei)
src/game.html               Quelltext (hier bearbeiten)
tools/build.py              baut index.html mit eingebetteten Bildern/Schriften
assets/                     Mister-G-Bilder (mister-g.webp = freigestellt fürs Titelbild, mister-g-original.webp = Original), Schriften (WOFF)
tools/check_sequences.py    fachlicher Sequenz-Check
```

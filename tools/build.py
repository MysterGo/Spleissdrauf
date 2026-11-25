#!/usr/bin/env python3
"""Baut index.html aus src/game.html und bettet Bilder + Schriften ein (eine Datei, läuft offline)."""
import base64, pathlib
R = pathlib.Path(__file__).resolve().parent.parent
def b64(p, mime): return f"data:{mime};base64," + base64.b64encode((R / p).read_bytes()).decode()
s = (R / "src/game.html").read_text(encoding="utf-8")
rep = {
  "/*MG_FACE*/": b64("assets/mister-g-face.jpg", "image/jpeg"),
  "/*MG_FULL*/": b64("assets/mister-g.webp", "image/webp"),
  "/*F_BITTER*/": b64("assets/fonts/bitter.woff", "font/woff"),
  "/*F_FR*/": b64("assets/fonts/fr.woff", "font/woff"),
  "/*F_FSB*/": b64("assets/fonts/fsb.woff", "font/woff"),
  "/*F_FB*/": b64("assets/fonts/fb.woff", "font/woff"),
  "/*F_MONO*/": b64("assets/fonts/mono.woff", "font/woff"),
}
for k, v in rep.items():
    assert s.count(k) == 1, k
    s = s.replace(k, v)
(R / "index.html").write_text(s, encoding="utf-8")
print("index.html gebaut:", len(s) // 1024, "KB")

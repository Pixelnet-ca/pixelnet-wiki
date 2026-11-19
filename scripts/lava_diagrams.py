"""Generate original PixelNet diagrams for the NES Lava RGB 2.0 wiki guide (EN/FR)."""
import os, subprocess, sys

OUT = sys.argv[1]
NAVY, PANEL, RED, RED2, GREY, WHITE = "#0B1220", "#1A2A48", "#D52B1E", "#FF4A3D", "#A7B1C4", "#F8FAFC"
PCB, PCB_EDGE, LAVA = "#2E6B4F", "#3F8F69", "#7A1F1A"
SANS, BOLD, TITLE, MONO = "IBM Plex Sans", "IBM Plex Sans SemiBold", "Sora ExtraBold", "IBM Plex Mono Medium"

T = {
    "en": {
        "m_title": "Two ways to install the Lava RGB 2.0",
        "m_kit": "Kit instructions", "m_kit_sub": "Board soldered directly",
        "m_sock": "Socketed", "m_sock_sub": "Recommended by PixelNet",
        "ppu": "PPU (video chip)", "lava": "Lava RGB board", "nes": "NES motherboard",
        "solder": "soldered directly", "headers": "Round pin headers ×2", "socket": "40-pin DIP socket",
        "m_kit_note": "Simpler, hard to remove later", "m_sock_note": "Board pulls out for service",
        "w_title": "12-wire connector: where each wire goes",
        "w_lava": "Lava RGB board", "w_conn": "12-wire connector",
        "w_mod": "New power / A-V module", "w_mod_sub": "Matching pads 1 to 8",
        "w_rst": "Motherboard reset line", "w_rst_sub": "Where the Reset button connects",
        "w_pad": "Player 1 controller lines", "w_pad_sub": "For IGR and palettes",
        "w_warn": "DATA and LATCH are swapped on the motherboard side",
        "c_title": "Controller shortcuts (player 1)",
        "c_hold": "Hold SELECT ~2 s, then:", "c_reset": "In-game reset", "c_pal": "Next palette (8)",
        "c_up": "UP",
    },
    "fr": {
        "m_title": "Deux façons d'installer le Lava RGB 2.0",
        "m_kit": "Instructions du kit", "m_kit_sub": "Carte soudée directement",
        "m_sock": "Sur support", "m_sock_sub": "Recommandé par PixelNet",
        "ppu": "PPU (puce vidéo)", "lava": "Carte Lava RGB", "nes": "Carte mère NES",
        "solder": "soudée directement", "headers": "Barrettes rondes ×2", "socket": "Support DIP 40 broches",
        "m_kit_note": "Plus simple, difficile à retirer", "m_sock_note": "La carte s'enlève pour l'entretien",
        "w_title": "Connecteur à 12 fils : où va chaque fil",
        "w_lava": "Carte Lava RGB", "w_conn": "Connecteur à 12 fils",
        "w_mod": "Nouveau module alim / A-V", "w_mod_sub": "Pastilles 1 à 8 correspondantes",
        "w_rst": "Ligne de reset de la carte mère", "w_rst_sub": "Là où se branche le bouton Reset",
        "w_pad": "Lignes de la manette joueur 1", "w_pad_sub": "Pour l'IGR et les palettes",
        "w_warn": "DATA et LATCH sont inversés côté carte mère",
        "c_title": "Raccourcis manette (joueur 1)",
        "c_hold": "Tenez SELECT ~2 s, puis :", "c_reset": "Reset en jeu", "c_pal": "Palette suivante (8)",
        "c_up": "HAUT",
    },
}

def text(x, y, s, size=20, fill=WHITE, font=SANS, anchor="start"):
    s = s.replace("&", "&amp;")
    return f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" fill="{fill}" text-anchor="{anchor}">{s}</text>'

def frame(w, h, title, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">'
            f'<rect width="{w}" height="{h}" rx="18" fill="{NAVY}"/>'
            f'<rect x="0" y="0" width="{w}" height="6" fill="{RED}"/>'
            + text(36, 58, title, 28, WHITE, TITLE) + body
            + text(w - 28, h - 18, "PIXELNET", 14, GREY, MONO, "end") + '</svg>')

def chip(x, y, w, label):
    pins = "".join(f'<rect x="{x+14+i*((w-28)/19):.1f}" y="{y+34}" width="5" height="12" fill="{GREY}"/>' for i in range(20))
    return (pins + f'<rect x="{x}" y="{y}" width="{w}" height="36" rx="4" fill="#111"/>'
            f'<circle cx="{x+14}" cy="{y+18}" r="5" fill="#333"/>' + text(x + w/2, y + 25, label, 16, WHITE, BOLD, "middle"))

def layer(x, y, w, h, fill, edge, label, lc=WHITE):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{fill}" stroke="{edge}" stroke-width="2"/>'
            + text(x + w/2, y + h/2 + 7, label, 18, lc, BOLD, "middle"))

def methods(t):
    b = ""
    for i, (col, sub, note, socketed) in enumerate([(t["m_kit"], t["m_kit_sub"], t["m_kit_note"], False),
                                                     (t["m_sock"], t["m_sock_sub"], t["m_sock_note"], True)]):
        x = 40 + i * 430
        b += f'<rect x="{x}" y="88" width="400" height="470" rx="14" fill="{PANEL}" stroke="{RED if socketed else PANEL}" stroke-width="2"/>'
        b += text(x + 24, 128, col, 24, RED2 if socketed else WHITE, BOLD) + text(x + 24, 156, sub, 17, GREY)
        cx, w = x + 50, 300
        y = 190
        b += chip(cx + 40, y, w - 80, t["ppu"]); y += 66
        b += layer(cx, y, w, 46, LAVA, RED, t["lava"]); y += 56
        if socketed:
            b += "".join(f'<rect x="{cx+30+k*12}" y="{y}" width="6" height="34" rx="3" fill="#D9B44A"/>' for k in range(21))
            b += text(cx + w + 6, y + 23, "", 1)
            b += f'<rect x="{cx+20}" y="{y+8}" width="{w-40}" height="18" rx="3" fill="none"/>'
            b += text(cx + w/2, y + 58, t["headers"], 15, GREY, SANS, "middle"); y += 70
            b += layer(cx + 10, y, w - 20, 34, "#222", "#555", t["socket"], GREY); y += 44
        else:
            b += f'<line x1="{cx+20}" y1="{y+6}" x2="{cx+w-20}" y2="{y+6}" stroke="{GREY}" stroke-width="3" stroke-dasharray="6 6"/>'
            b += text(cx + w/2, y + 34, t["solder"], 15, GREY, SANS, "middle"); y += 114
        b += layer(cx - 20, y, w + 40, 50, PCB, PCB_EDGE, t["nes"])
        b += text(x + 200, 538, note, 17, WHITE if socketed else GREY, BOLD if socketed else SANS, "middle")
    return frame(900, 590, t["m_title"], b)

def wiring(t):
    b = f'<rect x="40" y="100" width="300" height="430" rx="14" fill="{LAVA}" stroke="{RED}" stroke-width="2"/>'
    b += text(190, 140, t["w_lava"], 22, WHITE, BOLD, "middle") + text(190, 166, t["w_conn"], 16, GREY, SANS, "middle")
    pins = [str(i) for i in range(1, 9)] + ["RST", "CLK", "DATA", "LATCH"]
    ys = {}
    for i, p in enumerate(pins):
        y = 196 + i * 26
        ys[p] = y
        b += f'<rect x="250" y="{y-14}" width="70" height="20" rx="3" fill="#111" stroke="{GREY}" stroke-width="1"/>'
        b += text(285, y + 1, p, 14, WHITE, MONO, "middle")
    targets = [("w_mod", "w_mod_sub", 110, 140, [str(i) for i in range(1, 9)], RED2),
               ("w_rst", "w_rst_sub", 290, 90, ["RST"], "#F2C14E"),
               ("w_pad", "w_pad_sub", 410, 110, ["CLK", "DATA", "LATCH"], "#6EC6FF")]
    for k, ks, ty, th, ps, col in targets:
        b += f'<rect x="530" y="{ty}" width="340" height="{th}" rx="12" fill="{PANEL}" stroke="{col}" stroke-width="2"/>'
        b += text(548, ty + 36, t[k], 19, WHITE, BOLD) + text(548, ty + 62, t[ks], 15, GREY)
        for j, p in enumerate(ps):
            ey = ty + 20 + (th - 40) * (j + 0.5) / len(ps)
            sy = ys[p] - 4
            b += f'<path d="M320 {sy} C 425 {sy}, 425 {ey}, 530 {ey}" fill="none" stroke="{col}" stroke-width="2.5"/>'
    b += f'<rect x="40" y="548" width="820" height="46" rx="10" fill="#2A1414" stroke="{RED2}" stroke-width="2"/>'
    b += text(64, 578, "⚠ " + t["w_warn"], 18, WHITE, BOLD)
    return frame(900, 630, t["w_title"], b)

def combos(t):
    b = (f'<rect x="40" y="110" width="380" height="170" rx="70" fill="#2B3550" stroke="{GREY}" stroke-width="2"/>'
         f'<rect x="96" y="160" width="22" height="66" rx="3" fill="#111"/><rect x="74" y="182" width="66" height="22" rx="3" fill="#111"/>'
         f'<polygon points="107,163 99,175 115,175" fill="{WHITE}"/>'
         f'<rect x="176" y="200" width="40" height="14" rx="7" fill="{RED2}" stroke="{WHITE}" stroke-width="2"/>'
         f'<rect x="228" y="200" width="40" height="14" rx="7" fill="#777"/>'
         + text(196, 236, "SELECT", 11, RED2, MONO, "middle") + text(248, 236, "START", 11, GREY, MONO, "middle")
         + f'<circle cx="310" cy="200" r="20" fill="{RED}"/><circle cx="362" cy="200" r="20" fill="{RED}"/>'
         + text(310, 240, "B", 14, GREY, MONO, "middle") + text(362, 240, "A", 14, WHITE, MONO, "middle"))
    b += text(460, 140, t["c_hold"], 20, WHITE, BOLD)
    for i, (key, lab) in enumerate([("A", t["c_reset"]), (t["c_up"], t["c_pal"])]):
        y = 170 + i * 70
        b += f'<rect x="460" y="{y}" width="400" height="54" rx="10" fill="{PANEL}"/>'
        b += f'<rect x="474" y="{y+10}" width="{60 if len(key) < 3 else 76}" height="34" rx="8" fill="{RED}"/>'
        b += text(474 + (30 if len(key) < 3 else 38), y + 33, key, 17, WHITE, MONO, "middle")
        b += text(564, y + 34, lab, 19, WHITE, SANS)
    b += ""
    return frame(900, 350, t["c_title"], b)

os.makedirs(OUT, exist_ok=True)
for lang, t in T.items():
    for name, fn in [("methods", methods), ("wiring", wiring), ("controls", combos)]:
        svg = os.path.join(OUT, f"lava-{name}-{lang}.svg")
        png = svg[:-4] + ".png"
        open(svg, "w").write(fn(t))
        subprocess.run(["rsvg-convert", "-z", "2", "-o", png, svg], check=True)
        os.remove(svg)
        print(png)

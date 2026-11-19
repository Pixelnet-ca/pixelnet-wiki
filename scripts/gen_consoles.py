"""Generate docs/consoles/** (EN + FR) from scripts/consoles_data.py.

Usage:  python scripts/gen_consoles.py
Also rewrites the "Consoles" block of the nav in mkdocs.yml.
"""
import pathlib, re, shutil, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from consoles_data import BRANDS, CATS, NAME_FR, MODEL_FR, MAKERS  # noqa: E402

OUT = ROOT / "docs" / "consoles"

L = {
    "en": dict(
        models="Models", model="Model", note="Note", console="Console", years="Years",
        pn="PixelNet installs it", guide="Guide", ni="No install", by="by", buy="Buy",
        makers="Mod makers", makers_b="Mods marked with a maker's name are designed by them. Buy from the maker directly: you support the people who make these mods.",
        intro="Pick a brand, then a console, to see every mod available for it, grouped by type.",
        legend=("**Legend:** :material-wrench: **PixelNet installs it** · "
                ":material-book-open-variant: **Guide** on this wiki · "
                ":material-power-plug: **No install** (cart, adapter or software) · "
                ":material-cart: **Buy** from the official source"),
        consoles_in="Consoles", mods_n="{n} mods",
        help_t="Want a mod installed?",
        help=("PixelNet installs mods and repairs consoles on request, even for mods not listed in the shop. "
              "Write to [support@pixelnet.ca](mailto:support@pixelnet.ca) or visit [pixelnet.ca](https://pixelnet.ca)."),
        start="Not sure where to start?",
        start_b="For most consoles: **recap** first if it's old, then **video** (RGB or HDMI), then **games & storage**.",
    ),
    "fr": dict(
        models="Modèles", model="Modèle", note="Note", console="Console", years="Années",
        pn="Installé par PixelNet", guide="Guide", ni="Sans installation", by="par", buy="Acheter",
        makers="Concepteurs de mods", makers_b="Les mods marqués du nom d'un concepteur sont conçus par lui. Achète directement chez le concepteur : tu soutiens ceux qui créent ces mods.",
        intro="Choisis une marque, puis une console, pour voir tous les mods offerts, classés par type.",
        legend=("**Légende :** :material-wrench: **Installé par PixelNet** · "
                ":material-book-open-variant: **Guide** sur ce wiki · "
                ":material-power-plug: **Sans installation** (cartouche, adaptateur ou logiciel) · "
                ":material-cart: **Acheter** à la source officielle"),
        consoles_in="Consoles", mods_n="{n} mods",
        help_t="Tu veux faire installer un mod ?",
        help=("PixelNet installe des mods et répare des consoles sur demande, même pour des mods absents de la boutique. "
              "Écris à [support@pixelnet.ca](mailto:support@pixelnet.ca) ou visite [pixelnet.ca](https://pixelnet.ca)."),
        start="Tu ne sais pas par où commencer ?",
        start_b="Pour la plupart des consoles : d'abord un **recap** si elle est vieille, ensuite la **vidéo** (RGB ou HDMI), puis **jeux et stockage**.",
    ),
}


def sfx(lang):
    return ".fr.md" if lang == "fr" else ".md"


def bname(b, lang):
    return b.get("name_fr", b["name"]) if lang == "fr" else b["name"]


def n_mods(c):
    return sum(len(v) for v in c["mods"].values())


def console_page(b, c, lang):
    t = L[lang]
    o = [f"# {c['name']}", "", f"*{c['years']}* · {c[lang]}", ""]
    o += [f"| {t['model']} | {t['note']} |", "|---|---|"]
    o += [f"| **{m[0] if lang == 'en' else MODEL_FR.get(m[0], m[0])}** | {m[1] if lang == 'en' else m[2]} |" for m in c["models"]]
    o += ["", t["legend"], ""]
    for key, en, fr in CATS:
        mods = c["mods"].get(key)
        if not mods:
            continue
        o += [f"## {en if lang == 'en' else fr}", ""]
        for m in mods:
            tags = []
            if m.get("pn"):
                tags.append(f":material-wrench: **{t['pn']}**")
            if m.get("guide"):
                tags.append(f"[:material-book-open-variant: {t['guide']}](../../{m['guide']})")
            if m.get("by"):
                mk = MAKERS[m["by"]]
                tags.append(f":material-account-hard-hat: {t['by']} [{mk['name']}]({mk['url']}){{ target=_blank }}")
            buy = m.get("buy") or (MAKERS[m["by"]]["shop"] if m.get("by") else None)
            if buy:
                tags.append(f"[:material-cart: {t['buy']}]({buy}){{ target=_blank }}")
            if m.get("ni"):
                tags.append(f":material-power-plug: {t['ni']}")
            name = NAME_FR.get(m["n"], m["n"]) if lang == "fr" else m["n"]
            o += [f"### {name}", "", m[lang], ""]
            if tags:
                o += [" · ".join(tags), ""]
    o += [f'!!! tip "{t["help_t"]}"', f"    {t['help']}", ""]
    return "\n".join(o)


def brand_page(b, lang):
    t = L[lang]
    o = [f"# {bname(b, lang)}", "", b[lang], "",
         f"| {t['console']} | {t['years']} | |", "|---|---|---|"]
    for c in b["consoles"]:
        o.append(f"| [**{c['name']}**]({c['slug']}.md) | {c['years']} | {c[lang]} |")
    o += ["", f'!!! tip "{t["help_t"]}"', f"    {t['help']}", ""]
    return "\n".join(o)


def index_page(lang):
    t = L[lang]
    o = ["# Consoles", "", t["intro"], "", t["legend"], ""]
    for b in BRANDS:
        o += [f"## [{bname(b, lang)}]({b['slug']}/index.md)", "", b[lang], ""]
        for c in b["consoles"]:
            o.append(f"- [{c['name']}]({b['slug']}/{c['slug']}.md) · *{t['mods_n'].format(n=n_mods(c))}*")
        o.append("")
    o += [f"## {t['makers']}", "", t["makers_b"], ""]
    for k, mk in MAKERS.items():
        n = sum(1 for b in BRANDS for c in b["consoles"] for v in c["mods"].values() for m in v if m.get("by") == k)
        o.append(f"- [**{mk['name']}**]({mk['url']}){{ target=_blank }} ({mk['where'] if lang == 'en' else mk['ou']}) · *{t['mods_n'].format(n=n)}* · [:material-cart: {t['buy']}]({mk['shop']}){{ target=_blank }}")
    o.append("")
    o += [f'!!! info "{t["start"]}"', f"    {t['start_b']}", ""]
    return "\n".join(o)


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    for lang in ("en", "fr"):
        write(OUT / f"index{sfx(lang)}", index_page(lang))
        for b in BRANDS:
            write(OUT / b["slug"] / f"index{sfx(lang)}", brand_page(b, lang))
            for c in b["consoles"]:
                write(OUT / b["slug"] / f"{c['slug']}{sfx(lang)}", console_page(b, c, lang))

    # nav block
    nav = ["  - Consoles:", "      - consoles/index.md"]
    for b in BRANDS:
        nav.append(f"      - {b['name']}:")
        nav.append(f"          - consoles/{b['slug']}/index.md")
        for c in b["consoles"]:
            nav.append(f"          - \"{c['name']}\": consoles/{b['slug']}/{c['slug']}.md")
    yml = ROOT / "mkdocs.yml"
    s = yml.read_text(encoding="utf-8")
    s = re.sub(r"  - Consoles:\n(?:      .*\n)+", "\n".join(nav) + "\n", s)
    yml.write_text(s, encoding="utf-8")
    total = sum(n_mods(c) for b in BRANDS for c in b["consoles"])
    print(f"{len(BRANDS)} brands, {sum(len(b['consoles']) for b in BRANDS)} consoles, {total} mods")


if __name__ == "__main__":
    main()

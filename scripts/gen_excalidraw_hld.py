#!/usr/bin/env python3
"""Generate the RepairCheck high-level design as an Obsidian-Excalidraw drawing.

Output: 00_Project_Info/system-high-level-design.excalidraw.md

Layout (top -> bottom):
  Title -> Actors (3, color-coded) -> Apps (4) -> API layer (+ module chips) -> Data layer
Colors are Open-Color hues (validated CVD-safe): green=Driver, blue=Client Admin,
violet=MCS Admin, amber=Data, dark slate=API. Re-run this script to rebuild the drawing.
"""
import json
import os
import random

random.seed(42)  # stable output across runs

# ---- palette (Open Color; accents validated with dataviz validate_palette.js) ----
GREEN = ("#b2f2bb", "#2f9e44")   # fill, stroke  -> Driver / Web App + Android
BLUE = ("#a5d8ff", "#1971c2")    # Client Admin / Web Portal
VIOLET = ("#d0bfff", "#7048e8")  # MCS Admin / SaaS Admin
AMBER = ("#ffec99", "#f08c00")   # Data & Infra
SLATE_FILL, SLATE_STROKE = "#343a40", "#212529"   # API container (white text)
CHIP_FILL, CHIP_STROKE = "#e9ecef", "#495057"     # API module chips
INK = "#1e1e1e"
MUTED = "#868e96"
CANVAS = "#fbfbfa"

elements = []
text_index = []  # (originalText, id) for the "## Text Elements" section


def nonce():
    return random.randint(1, 2**31)


def _base(id_, type_, x, y, w, h, stroke, bg, fill="solid", rough=1,
          roundness=None, sw=2):
    return {
        "id": id_, "type": type_, "x": x, "y": y, "width": w, "height": h,
        "angle": 0, "strokeColor": stroke, "backgroundColor": bg,
        "fillStyle": fill, "strokeWidth": sw, "strokeStyle": "solid",
        "roughness": rough, "opacity": 100, "groupIds": [], "frameId": None,
        "roundness": roundness, "seed": nonce(), "version": 1,
        "versionNonce": nonce(), "isDeleted": False, "boundElements": [],
        "updated": 1, "link": None, "locked": False,
    }


def add_text(id_, text, x, y, size=20, color=INK, container=None,
             align="center", w=None, h=None):
    lines = text.split("\n")
    tw = w if w is not None else int(max(len(l) for l in lines) * size * 0.62) + 8
    th = h if h is not None else int(len(lines) * size * 1.25) + 4
    el = _base(id_, "text", x, y, tw, th, color, "transparent")
    el.update({
        "fontSize": size, "fontFamily": 1, "text": text, "originalText": text,
        "textAlign": align, "verticalAlign": "middle",
        "containerId": container, "lineHeight": 1.25,
        "baseline": int(size * 0.9),
    })
    del el["roundness"]
    elements.append(el)
    text_index.append((text, id_))
    return el


def add_box(id_, text, x, y, w, h, fill, stroke, ellipse=False, size=20,
            text_color=INK):
    roundness = None if ellipse else {"type": 3}
    box = _base(id_, "ellipse" if ellipse else "rectangle", x, y, w, h,
                stroke, fill, roundness=roundness)
    elements.append(box)
    # centered bound text
    tid = id_ + "_t"
    lines = text.split("\n")
    tw = int(max(len(l) for l in lines) * size * 0.62) + 8
    th = int(len(lines) * size * 1.25) + 4
    tx = x + (w - tw) / 2
    ty = y + (h - th) / 2
    add_text(tid, text, tx, ty, size=size, color=text_color, container=id_,
             w=tw, h=th)
    box["boundElements"].append({"type": "text", "id": tid})
    return box


def add_arrow(id_, src, dst, color=MUTED):
    sx = src["x"] + src["width"] / 2
    sy = src["y"] + src["height"]
    ex = dst["x"] + dst["width"] / 2
    ey = dst["y"]
    gap = 4
    ar = _base(id_, "arrow", sx, sy + gap, ex - sx, ey - sy - 2 * gap,
               color, "transparent", roundness={"type": 2})
    ar.update({
        "points": [[0, 0], [ex - sx, ey - sy - 2 * gap]],
        "lastCommittedPoint": None,
        "startBinding": {"elementId": src["id"], "focus": 0, "gap": gap},
        "endBinding": {"elementId": dst["id"], "focus": 0, "gap": gap},
        "startArrowhead": None, "endArrowhead": "arrow",
    })
    elements.append(ar)
    src["boundElements"].append({"type": "arrow", "id": id_})
    dst["boundElements"].append({"type": "arrow", "id": id_})
    return ar


# ---------------------------------------------------------------- title
add_text("title", "RepairCheck (RC) - High-Level System Design", 300, 24,
         size=28, color=INK, align="center", w=800)
add_text("subtitle",
         "MotionsCloud multi-tenant SaaS  -  car accident / damage assistance",
         360, 66, size=14, color=MUTED, align="center", w=680)

# ---------------------------------------------------------------- actors (ellipses)
driver = add_box("a_driver", "End user /\nDriver", 150, 130, 210, 78, *GREEN,
                 ellipse=True, size=18)
cadmin = add_box("a_cadmin", "Client Admin\n(per company)", 600, 130, 210, 78,
                 *BLUE, ellipse=True, size=18)
mcs = add_box("a_mcs", "MCS Admin\n(MotionsCloud)", 1040, 130, 210, 78,
              *VIOLET, ellipse=True, size=18)

# ---------------------------------------------------------------- apps (rounded rects)
webapp = add_box("app_web", "Web App", 110, 300, 170, 88, *GREEN, size=20)
android = add_box("app_android", "Android", 300, 300, 120, 88, *GREEN, size=20)
portal = add_box("app_portal", "Web Portal\n/admin", 590, 300, 230, 88, *BLUE,
                 size=20)
saas = add_box("app_saas", "SaaS Admin", 1030, 300, 230, 88, *VIOLET, size=20)

add_text("ref_web", "RC-101 / RC-3", 150, 392, size=12, color=MUTED, w=150)
add_text("ref_portal", "RC-103", 660, 392, size=12, color=MUTED, w=120)
add_text("ref_saas", "RC-2 + RC-38", 1080, 392, size=12, color=MUTED, w=140)

# ---------------------------------------------------------------- API layer
api = _base("api_box", "rectangle", 110, 470, 1150, 178, SLATE_STROKE,
            SLATE_FILL, roundness={"type": 3})
elements.append(api)
add_text("api_hdr", "REST API + Swagger   (RC-12, RC-5)", 140, 482, size=18,
         color="#ffffff", w=520, align="left")

chips = ["Auth", "Users", "Vehicles", "Accidents /\nDamages",
         "Workshops +\nVouchers", "Experts", "Lawyers", "Pricing",
         "Ads", "Geocoding"]
cx0, cy0, cw, ch, gx, gy = 140, 520, 205, 48, 18, 12
for i, label in enumerate(chips):
    col = i % 5
    row = i // 5
    x = cx0 + col * (cw + gx)
    y = cy0 + row * (ch + gy)
    add_box("chip_%d" % i, label, x, y, cw, ch, CHIP_FILL, CHIP_STROKE,
            size=14)

# ---------------------------------------------------------------- data layer
add_text("data_hdr", "Data & Infra  -  MCS SaaS server  (RC-11)", 420, 690,
         size=16, color=INK, w=520, align="left")
db = add_box("data_db", "Database", 380, 726, 260, 90, *AMBER, size=20)
files = add_box("data_files", "File storage\n(damage photos / documents)", 720,
                726, 300, 90, *AMBER, size=16)
add_text("data_cap",
         "Companies - Users - Vehicles - Accidents/Damages - Workshops - "
         "Experts - Lawyers - Vouchers - Ads - Pricing",
         300, 828, size=12, color=MUTED, w=820, align="center")

# ---------------------------------------------------------------- arrows
add_arrow("ar1", driver, webapp, GREEN[1])
add_arrow("ar2", driver, android, GREEN[1])
add_arrow("ar3", cadmin, portal, BLUE[1])
add_arrow("ar4", mcs, saas, VIOLET[1])
add_arrow("ar5", webapp, api)
add_arrow("ar6", android, api)
add_arrow("ar7", portal, api)
add_arrow("ar8", saas, api)
add_arrow("ar9", api, db, AMBER[1])
add_arrow("ar10", api, files, AMBER[1])

# ---------------------------------------------------------------- write file
scene = {
    "type": "excalidraw", "version": 2, "source": "gen_excalidraw_hld.py",
    "elements": elements,
    "appState": {"gridSize": None, "viewBackgroundColor": CANVAS},
    "files": {},
}

text_block = "\n\n".join("%s ^%s" % (t.replace("\n", " "), i)
                          for t, i in text_index)

md = (
    "---\n"
    "excalidraw-plugin: parsed\n"
    "tags: [excalidraw]\n"
    "---\n"
    "==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this "
    "document. ⚠==\n\n"
    "# Excalidraw Data\n\n"
    "## Text Elements\n" + text_block + "\n\n"
    "## Drawing\n"
    "```json\n" + json.dumps(scene, ensure_ascii=False, indent=2) + "\n```\n"
    "%%\n"
)

here = os.path.dirname(os.path.abspath(__file__))
out = os.path.join(here, "..", "00_Project_Info",
                   "system-high-level-design.excalidraw.md")
with open(out, "w", encoding="utf-8") as f:
    f.write(md)
print("wrote", os.path.normpath(out))
print("elements:", len(elements))

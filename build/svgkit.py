# -*- coding: utf-8 -*-
"""vuav profile — shared SVG design system."""

W = 900  # canvas width for all full-bleed assets

# ---- tokens -------------------------------------------------------------
INK   = "#0A0B0D"   # page background
SURF  = "#101216"   # card surface
SURF2 = "#15181D"   # inset surface
LINE  = "#23272E"   # hairline
LINE2 = "#2E343C"   # stronger hairline
BONE  = "#E9EBED"   # primary text
ASH   = "#8A929B"   # secondary text
DIM   = "#565D66"   # tertiary / decorative
ACC   = "#7FA0B8"   # blueprint steel — the only accent
ACCD  = "#3C4E5C"   # accent, dimmed

DISPLAY = "Inter,'Helvetica Neue',Helvetica,Arial,sans-serif"
MONO    = "ui-monospace,'SFMono-Regular','DejaVu Sans Mono',Menlo,Consolas,monospace"

# ---- helpers ------------------------------------------------------------

def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def wrap(text, px, size, mono=False):
    """Greedy wrap using an estimated advance width."""
    f = 0.605 if mono else 0.512
    maxc = max(8, int(px / (size * f)))
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if len(t) <= maxc:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def tw(text, size, mono=False):
    """Estimated rendered width of a string."""
    return len(text) * size * (0.605 if mono else 0.512)


def txt(x, y, s, size=17, fill=BONE, font=DISPLAY, weight="400", anchor="start",
        ls=0, opacity=None):
    o = f' opacity="{opacity}"' if opacity is not None else ""
    l = f' letter-spacing="{ls}"' if ls else ""
    return (f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}"{l}{o}>'
            f'{esc(s)}</text>')


def label(x, y, s, size=11.5, fill=DIM, anchor="start", ls=2.6, weight="500"):
    """Small uppercase mono metadata label."""
    return txt(x, y, s.upper(), size, fill, MONO, weight, anchor, ls)


def para(x, y, text, px, size=16.5, fill=ASH, lh=1.62, font=DISPLAY, weight="400"):
    out, yy = [], y
    for ln in wrap(text, px, size, mono=(font == MONO)):
        out.append(txt(x, yy, ln, size, fill, font, weight))
        yy += size * lh
    return "".join(out), yy - size * lh


def rect(x, y, w, h, fill="none", stroke=None, rx=0, sw=1, opacity=None, dash=None):
    s = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    d = f' stroke-dasharray="{dash}"' if dash else ""
    o = f' opacity="{opacity}"' if opacity is not None else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"{s}{d}{o}/>'


def line(x1, y1, x2, y2, stroke=LINE, sw=1, dash=None, opacity=None, cap="butt"):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    o = f' opacity="{opacity}"' if opacity is not None else ""
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" '
            f'stroke-width="{sw}" stroke-linecap="{cap}"{d}{o}/>')


def circle(cx, cy, r, fill="none", stroke=None, sw=1, opacity=None):
    s = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    o = f' opacity="{opacity}"' if opacity is not None else ""
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"{s}{o}/>'


def path(d, fill="none", stroke=None, sw=1, cap="butt", join="miter", opacity=None, dash=None):
    s = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    o = f' opacity="{opacity}"' if opacity is not None else ""
    da = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<path d="{d}" fill="{fill}"{s} stroke-linecap="{cap}" '
            f'stroke-linejoin="{join}"{o}{da}/>')


def pill(x, y, text, fill=SURF2, stroke=LINE, color=ASH, size=11, padx=10, h=22, dot=None):
    """Small technology tag. Returns (svg, width)."""
    w = tw(text.upper(), size, mono=True) + 1.4 * len(text) + padx * 2 + (12 if dot else 0)
    w = round(w, 1)
    out = [rect(x, y, w, h, fill=fill, stroke=stroke, rx=3)]
    tx = x + padx
    if dot:
        out.append(circle(x + padx + 2, y + h / 2, 2.6, fill=dot))
        tx += 12
    out.append(txt(tx, y + h / 2 + 4, text.upper(), size, color, MONO, "500", ls=1.4))
    return "".join(out), w


def pillrow(x, y, items, gap=7, **kw):
    out, cx = [], x
    for it in items:
        s, w = pill(cx, y, it, **kw)
        out.append(s)
        cx += w + gap
    return "".join(out), cx - gap


def pillrows(x, y, items, maxw, gap=7, rowgap=30, **kw):
    """Wrapping tag rows. Returns (svg, bottom_y)."""
    out, cx, cy = [], x, y
    for it in items:
        s, w = pill(cx, cy, it, **kw)
        if cx + w > x + maxw and cx > x:
            cx, cy = x, cy + rowgap
            s, w = pill(cx, cy, it, **kw)
        out.append(s)
        cx += w + gap
    return "".join(out), cy + 22


def card(x, y, w, h, fill=SURF, stroke=LINE, rx=4):
    return rect(x, y, w, h, fill=fill, stroke=stroke, rx=rx)


def corners(x, y, w, h, n=9, stroke=ACCD, sw=1.2):
    """Blueprint corner ticks."""
    o = []
    for (cx, cy, dx, dy) in ((x, y, 1, 1), (x + w, y, -1, 1), (x, y + h, 1, -1), (x + w, y + h, -1, -1)):
        o.append(line(cx, cy, cx + dx * n, cy, stroke, sw))
        o.append(line(cx, cy, cx, cy + dy * n, stroke, sw))
    return "".join(o)


def header(y, eyebrow, title, index=None, sub=None, x=44, w=W - 88):
    """Section header: mono eyebrow + display title + hairline + optional index."""
    o = [label(x, y, eyebrow, 11.5, ACC, ls=3.2)]
    o.append(txt(x, y + 40, title, 31, BONE, DISPLAY, "700", ls=-0.4))
    if index:
        o.append(txt(x + w, y + 40, index, 12.5, DIM, MONO, "500", "end", ls=2.4))
    o.append(line(x, y + 60, x + w, y + 60, LINE))
    o.append(line(x, y + 60, x + 56, y + 60, ACC, 1.6))
    yy = y + 60
    if sub:
        s, yy2 = para(x, y + 88, sub, w - 120, 16.5, ASH)
        o.append(s)
        yy = yy2 + 8
    return "".join(o), yy


def status(x, y, kind):
    m = {"ALPHA": ACC, "ACTIVE": "#7FB894", "WIP": "#B8A06E",
         "EXPERIMENT": ASH, "RESEARCH": ASH, "IDEA": DIM, "HARDWARE": ASH,
         "CONCEPT": DIM}
    c = m.get(kind.upper(), ASH)
    s, w = pill(x, y, kind, fill="none", stroke=LINE2, color=c, size=10.5, h=21, dot=c)
    return s, w


def svg(h, body, aria, w=W, bg=True):
    b = rect(0, 0, w, h, fill=INK) if bg else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
            f'width="{w}" height="{h}" role="img" aria-label="{esc(aria)}">'
            f'<title>{esc(aria)}</title>{b}{body}</svg>')


def grid(x, y, w, h, step=30, stroke="#14171C", sw=0.7, opacity=0.9):
    """Faint technical grid."""
    o = []
    gx = x
    while gx <= x + w:
        o.append(line(gx, y, gx, y + h, stroke, sw, opacity=opacity))
        gx += step
    gy = y
    while gy <= y + h:
        o.append(line(x, gy, x + w, gy, stroke, sw, opacity=opacity))
        gy += step
    return "".join(o)


def write(name, content, root="/home/claude/vuav"):
    import os
    p = os.path.join(root, name)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(content)
    return p

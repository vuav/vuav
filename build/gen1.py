# -*- coding: utf-8 -*-
import math, random
from svgkit import *

# ============================================================ WORDMARK
def wordmark(x, top, h=96, lw=66, gap=17, sw=13, color=BONE, opacity=None):
    o = []
    def V(px):
        return path(f"M{px},{top} L{px+lw/2},{top+h} L{px+lw},{top}", stroke=color, sw=sw, opacity=opacity)
    def U(px):
        r = lw / 2
        return path(f"M{px},{top} L{px},{top+h-r} A{r},{r} 0 0 0 {px+lw},{top+h-r} L{px+lw},{top}",
                    stroke=color, sw=sw, opacity=opacity, cap="butt")
    def A(px):
        d = f"M{px},{top+h} L{px+lw/2},{top} L{px+lw},{top+h}"
        yb = top + h * 0.66
        d2 = f"M{px+lw*0.17},{yb} L{px+lw*0.83},{yb}"
        return path(d, stroke=color, sw=sw, opacity=opacity) + path(d2, stroke=color, sw=sw, opacity=opacity)
    for i, fn in enumerate((V, U, A, V)):
        o.append(fn(x + i * (lw + gap)))
    return "".join(o), 4 * lw + 3 * gap


# ============================================================ HALFTONE ORB
def orb(cx, cy, r, seed=7, rings=23):
    """Stipple sphere: dot size follows a light source from upper-left."""
    rnd = random.Random(seed)
    o = []
    for i in range(1, rings + 1):
        rr = r * (i / rings) ** 0.92
        n = max(6, int(2 * math.pi * rr / 10.2))
        off = rnd.random() * math.tau
        for j in range(n):
            a = off + j * math.tau / n + rnd.uniform(-0.02, 0.02)
            px, py = cx + rr * math.cos(a), cy + rr * math.sin(a)
            # sphere normal -> shading
            nx, ny = (px - cx) / r, (py - cy) / r
            nz = math.sqrt(max(0.0, 1 - nx * nx - ny * ny))
            lam = max(0.0, (-0.5 * nx - 0.62 * ny + 0.6 * nz)) * 0.94 + 0.06
            d = 0.35 + 2.05 * (lam ** 1.55)
            if d < 0.5:
                continue
            col = BONE if lam > 0.55 else (ASH if lam > 0.3 else DIM)
            o.append(circle(round(px, 1), round(py, 1), round(d, 2), fill=col,
                            opacity=round(min(1, 0.30 + lam * 0.95), 2)))
    # dissolve: nodes drifting off the right/lower edge
    for k in range(34):
        a = rnd.uniform(-1.15, 0.95)
        rr = r * rnd.uniform(1.06, 1.55)
        px, py = cx + rr * math.cos(a), cy + rr * math.sin(a)
        o.append(circle(round(px, 1), round(py, 1), round(rnd.uniform(0.7, 1.7), 2),
                        fill=ASH, opacity=round(rnd.uniform(0.14, 0.5), 2)))
    return "".join(o)


# ============================================================ HERO
def hero():
    H = 440
    o = [grid(0, 0, W, H, 36, "#15191F", 0.75, 0.7)]
    o.append(rect(0, 0, W, H, fill="none"))
    # artwork (bleeds off the right edge)
    o.append(orb(742, 218, 152))
    o.append(circle(742, 218, 176, stroke=ACCD, sw=0.9, opacity=0.55))
    o.append(line(742 - 200, 218, 742 - 182, 218, ACCD, 1, opacity=0.8))
    o.append(label(534, 214, "fig. 01", 10.5, DIM, ls=2))
    # top meta bar
    o.append(line(44, 62, W - 44, 62, LINE))
    o.append(label(44, 44, "github.com/vuav", 11.5, ASH, ls=2.8))
    o.append(label(W - 46, 44, "London, UK  ·  EN / PL", 11.5, DIM, "end", ls=2.4))
    # wordmark (with a subtle registration-offset ghost)
    gm, gw = wordmark(54, 122, h=96, sw=1.2, color=ACC, opacity=0.42)
    o.append(gm)
    wm, wmw = wordmark(44, 112)
    o.append(wm)
    # identity block
    o.append(line(44, 246, 44 + wmw, 246, LINE2))
    o.append(txt(44, 282, "KRYSTIAN WL", 17, BONE, MONO, "500", ls=6.4))
    o.append(label(44, 310, "Software engineering · AI · Security · Systems", 11.5, ACC, ls=2.4))
    o.append(txt(44, 356, "\u201cI build things I don't want to do twice.\u201d",
                 20, ASH, DISPLAY, "400"))
    # bottom meta bar
    o.append(line(44, 392, W - 44, 392, LINE))
    for x, k, v in [(44, "age", "17"), (168, "study", "Computing L3 BTEC · Y2"),
                    (470, "next", "PJATK, Warsaw")]:
        o.append(label(x, 418, k, 10.5, DIM, ls=2.4))
        o.append(txt(x + 62, 419, v, 13, ASH, MONO, "500"))
    o.append(label(W - 44, 418, "// still building", 11, ACCD, "end", ls=2))
    return svg(H, "".join(o),
               "VUAV — Krystian Wl. Software engineering, AI, security and systems. "
               "17, London UK. Computing Level 3 BTEC, Year 2, heading for PJATK Warsaw. "
               "Tagline: I build things I don't want to do twice.")


# ============================================================ CONSOLE DIAGRAM
def console(x, y, s=1.0):
    """Original line-art handheld, drawn like a service-manual figure."""
    o = []
    def sc(a):  # scale helper
        return round(a * s, 1)
    # lid
    o.append(rect(x, y, sc(160), sc(96), fill=SURF2, stroke=LINE2, rx=8, sw=1.2))
    o.append(rect(x + sc(22), y + sc(12), sc(116), sc(72), fill=INK, stroke=LINE2, rx=2, sw=1))
    # faint scanlines in the screen
    for i in range(7):
        o.append(line(x + sc(26), y + sc(20 + i * 10), x + sc(134), y + sc(20 + i * 10), ACCD, 0.7, opacity=0.5))
    # hinge
    o.append(rect(x + sc(12), y + sc(98), sc(136), sc(8), fill=SURF, stroke=LINE2, rx=3, sw=1))
    # base
    o.append(rect(x, y + sc(108), sc(160), sc(104), fill=SURF2, stroke=LINE2, rx=8, sw=1.2))
    o.append(rect(x + sc(38), y + sc(118), sc(84), sc(62), fill=INK, stroke=LINE2, rx=2, sw=1))
    # d-pad
    dx, dy = x + sc(18), y + sc(140)
    o.append(path(f"M{dx},{dy-sc(4)} h{sc(8)} v-{sc(8)} h{sc(8)} v{sc(8)} h{sc(8)} v{sc(8)} "
                  f"h-{sc(8)} v{sc(8)} h-{sc(8)} v-{sc(8)} h-{sc(8)} z", stroke=LINE2, sw=1))
    # buttons
    for (bx, by) in ((132, 136), (144, 148), (120, 148), (132, 160)):
        o.append(circle(x + sc(bx), y + sc(by), sc(4.6), stroke=LINE2, sw=1))
    # speaker slots + start/select
    for i in range(4):
        o.append(line(x + sc(48 + i * 6), y + sc(192), x + sc(48 + i * 6), y + sc(200), DIM, 1.4, opacity=0.6))
    o.append(rect(x + sc(96), y + sc(192), sc(18), sc(5), fill="none", stroke=LINE2, rx=2, sw=0.9))
    return "".join(o), sc(160), sc(212)


# ============================================================ ABOUT
def about():
    H = 584
    o = []
    hd, _ = header(40, "01 — Origin", "It started with a 3DS.", index="AGE 9 \u2192 17")
    o.append(hd)
    TX, TW_ = 44, 462
    o.append(para(TX, 158, "I was nine, I wanted games I couldn't afford, and instead of "
                  "accepting that I got curious about how the thing actually worked. I read, "
                  "broke it, and put it back together.", TW_, 16.5, ASH)[0])
    o.append(para(TX, 272, "That curiosity outlived the console. Eight years later it's Linux, "
                  "reverse engineering, security research, AI and a questionable number of side "
                  "projects.", TW_, 16.5, ASH)[0])
    o.append(para(TX, 360, "I'm 17, based in London, finishing a Level 3 BTEC in Computing and "
                  "aiming at PJATK in Warsaw.", TW_, 16.5, ASH)[0])
    o.append(label(TX, 434, "Taken apart / modified / researched", 10.5, DIM, ls=2.4))
    o.append(pillrow(TX, 448, ["Nintendo 3DS", "Switch OLED", "PS3", "iOS"], size=10.5, h=23)[0])

    # ---- figure panel
    FX, FY, FW, FH = 552, 132, 304, 340
    o.append(card(FX, FY, FW, FH, fill=SURF))
    o.append(grid(FX + 1, FY + 1, FW - 2, FH - 2, 24, "#13171C", 0.6, 0.6))
    o.append(corners(FX, FY, FW, FH, 10))
    o.append(label(FX + 16, FY + 26, "fig. 02 — entry point", 10.5, DIM, ls=2))
    o.append(line(FX + 16, FY + 38, FX + FW - 16, FY + 38, LINE))
    cs, cw, ch = console(FX + 74, FY + 70, 0.86)
    o.append(cs)
    o.append(line(FX + 30, FY + 112, FX + 74 + 18, FY + 112, ACCD, 1))
    o.append(circle(FX + 74 + 18, FY + 112, 1.8, fill=ACC))
    o.append(label(FX + 22, FY + 100, "screen", 9.5, DIM, ls=1.6))
    o.append(line(FX + 74 + cw - 14, FY + 214, FX + FW - 26, FY + 214, ACCD, 1))
    o.append(circle(FX + 74 + cw - 14, FY + 214, 1.8, fill=ACC))
    o.append(label(FX + FW - 84, FY + 204, "firmware", 9.5, DIM, ls=1.6))
    o.append(line(FX + 16, FY + FH - 50, FX + FW - 16, FY + FH - 50, LINE))
    o.append(txt(FX + 16, FY + FH - 26, "status:", 11.5, DIM, MONO, "500"))
    o.append(txt(FX + 76, FY + FH - 26, "disassembled, repeatedly", 11.5, ASH, MONO, "500"))

    # ---- thesis band
    o.append(line(44, 506, W - 44, 506, LINE))
    o.append(line(44, 506, 100, 506, ACC, 1.6))
    o.append(para(44, 540, "I don't just use technology \u2014 I want to know why it does what "
                  "it does. Usually I find out by taking it apart.", 812, 19, BONE)[0])
    return svg(H, "".join(o),
               "About. It started with a 3DS: at nine I wanted games I couldn't afford, so I "
               "got curious about how the device worked. That curiosity became Linux, reverse "
               "engineering, security research, AI and a lot of side projects. I am 17, based in "
               "London, finishing a Computing Level 3 BTEC and aiming at PJATK in Warsaw. "
               "Devices taken apart, modified or researched: Nintendo 3DS, Switch OLED, PS3, iOS. "
               "I don't just use technology, I want to know why it does what it does.")


# ============================================================ CURRENTLY
def currently():
    H = 254
    o = []
    hd, _ = header(36, "02 — Currently", "On the bench", index="2026")
    o.append(hd)
    items = [
        ("Finishing", "Computing L3 BTEC, Year 2"),
        ("Preparing", "PJATK application, Warsaw"),
        ("Learning", "C++, properly this time"),
        ("Deepening", "LLM systems and agent tooling"),
        ("Researching", "Security work, isolated labs only"),
        ("Shipping", "USBVAULT toward a stable release"),
    ]
    for i, (k, v) in enumerate(items):
        x = 44 + (i % 2) * 418
        y = 142 + (i // 2) * 34
        o.append(txt(x, y, "\u2192", 12.5, ACC, MONO, "500"))
        o.append(txt(x + 20, y, k, 12.5, BONE, MONO, "500"))
        o.append(txt(x + 124, y, v, 12.5, ASH, MONO, "400"))
    o.append(line(44, 226, W - 44, 226, LINE))
    return svg(H, "".join(o),
               "Currently: finishing Computing Level 3 BTEC Year 2; preparing a PJATK "
               "application in Warsaw; learning C++; going deeper into LLM systems and agent "
               "tooling; security research in isolated labs only; shipping USBVAULT toward a "
               "stable release.")


# ============================================================ WHAT I BUILD
def build():
    H = 470
    o = []
    hd, _ = header(36, "03 — What I build", "Six directions, one habit", index="core habit")
    o.append(hd)
    o.append(txt(44, 130, "\u201cI can't be asked to do it myself, so I'll build something that does it for me.\u201d",
                 18, ASH, DISPLAY, "400"))
    cells = [
        ("Security", "Research, automation and defensive tooling. Attack it, then work out how you'd have stopped it."),
        ("AI", "LLM experiments, agents and the plumbing around them \u2014 context, structure, failure modes."),
        ("Software", "Small tools that delete repetitive work from my week."),
        ("Web", "Full\u2011stack applications and interfaces, front to back."),
        ("Systems", "Linux, networking, self\u2011hosting and infrastructure I actually maintain."),
        ("Hardware", "Raspberry Pi, Arduino and things that only exist because they'd be funny."),
    ]
    CW, CH, GAP = 264, 128, 20
    for i, (t, d) in enumerate(cells):
        cx = 44 + (i % 3) * (CW + GAP)
        cy = 176 + (i // 3) * (CH + GAP)
        o.append(card(cx, cy, CW, CH))
        o.append(line(cx, cy, cx + 40, cy, ACC, 1.8))
        o.append(txt(cx + 18, cy + 34, t.upper(), 13, BONE, MONO, "600", ls=2.6))
        s, _ = para(cx + 18, cy + 60, d, CW - 36, 12.6, ASH, 1.55)
        o.append(s)
    return svg(H, "".join(o),
               "What I build. Security: research, automation and defensive tooling. AI: LLM "
               "experiments, agents and the plumbing around them. Software: small tools that "
               "remove repetitive work. Web: full-stack applications and interfaces. Systems: "
               "Linux, networking, self-hosting and infrastructure. Hardware: Raspberry Pi and "
               "Arduino projects.")


if __name__ == "__main__":
    write("assets/hero.svg", hero())
    write("assets/about.svg", about())
    write("assets/currently.svg", currently())
    write("assets/what-i-build.svg", build())
    print("gen1 ok")

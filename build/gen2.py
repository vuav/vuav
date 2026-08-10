# -*- coding: utf-8 -*-
import math
from svgkit import *


def note(x, y, w, text, size=12.5, pad=16):
    """Bordered technical note block. Returns (svg, height)."""
    lines = wrap(text, w - pad * 2 - 6, size, mono=True)
    h = pad * 2 + len(lines) * size * 1.62 - size * 0.3
    o = [rect(x, y, w, h, fill=SURF2, stroke=LINE, rx=3)]
    o.append(line(x, y, x, y + h, ACCD, 2))
    yy = y + pad + size
    for ln in lines:
        o.append(txt(x + pad, yy, ln, size, ASH, MONO, "400"))
        yy += size * 1.62
    return "".join(o), h


# ============================================================ AI
def ai():
    H = 500
    o = []
    hd, _ = header(36, "04 — AI / LLM", "Getting models to behave", index="and to misbehave")
    o.append(hd)
    o.append(para(44, 138, "Most of my AI time goes into the parts people skip: context, "
                  "structure, and what a model does when it's deliberately pushed off script. "
                  "I run models locally and read the failures.", 466, 16.5, ASH)[0])
    o.append(para(44, 250, "The security half is the same instinct as everything else here "
                  "\u2014 if I can make it break, I understand it better.", 466, 16.5, ASH)[0])
    # focus panel
    FX, FY, FW = 552, 130, 304
    rows = ["Prompt & context engineering", "Agentic systems, structured outputs",
            "Local model experimentation", "Prompt injection research",
            "Jailbreak & LLM security research"]
    FH = 34 + len(rows) * 32 + 14
    o.append(card(FX, FY, FW, FH))
    o.append(label(FX + 16, FY + 24, "focus", 10.5, ACC, ls=2.6))
    for i, r in enumerate(rows):
        y = FY + 56 + i * 32
        o.append(line(FX + 16, y - 18, FX + FW - 16, y - 18, LINE, 1, opacity=0.8))
        o.append(txt(FX + 16, y, "\u00b7", 13, ACC, MONO, "700"))
        o.append(txt(FX + 30, y, r, 12.6, ASH, MONO, "400"))
    # tools
    o.append(label(44, 340, "Worked with", 10.5, DIM, ls=2.6))
    tags = ["Python", "PyTorch", "Ollama", "OpenRouter", "Claude", "ChatGPT / OpenAI",
            "Gemini", "Qwen", "DeepSeek", "Cursor"]
    s, _ = pillrows(44, 352, tags, W - 88, size=10.5, h=24, rowgap=32)
    o.append(s)
    n, _ = note(44, 424, W - 88, "note: \u201cbuilt a local LLM\u201d means running, wiring up and "
                "experimenting with local models and tooling \u2014 not training a frontier model in my bedroom.")
    o.append(n)
    return svg(H, "".join(o),
               "AI and LLM work. Focus: prompt and context engineering, agentic systems and "
               "structured outputs, local model experimentation, prompt injection research, "
               "jailbreak and LLM security research. Worked with Python, PyTorch, Ollama, "
               "OpenRouter, Claude, ChatGPT/OpenAI, Gemini, Qwen, DeepSeek and Cursor. Note: "
               "building a local LLM here means running and experimenting with local models and "
               "tooling, not training a frontier model.")


# ============================================================ SECURITY
def security():
    H = 470
    o = []
    hd, _ = header(36, "05 — Security research", "Attack it, then defend it",
                   index="isolated labs only")
    o.append(hd)
    cols = [
        ("Offensive", ["Penetration testing", "Vulnerability research", "Exploitation research",
                       "Web & network security"]),
        ("Analysis", ["Reverse engineering", "Malware research", "OSINT", "Traffic analysis"]),
        ("Defensive", ["OPSEC & privacy architecture", "Linux & system hardening",
                       "Security automation", "Device & game security"]),
    ]
    for i, (t, items) in enumerate(cols):
        cx = 44 + i * 274
        o.append(line(cx, 132, cx + 240, 132, LINE2))
        o.append(line(cx, 132, cx + 34, 132, ACC, 1.8))
        o.append(txt(cx, 158, t.upper(), 12.5, BONE, MONO, "600", ls=2.6))
        for j, it in enumerate(items):
            o.append(txt(cx, 188 + j * 26, it, 12.6, ASH, MONO, "400"))
    o.append(label(44, 322, "Toolkit", 10.5, DIM, ls=2.6))
    s, _ = pillrows(44, 334, ["Nmap", "Wireshark", "Metasploit", "Hashcat", "Hydra",
                              "John the Ripper", "Aircrack-ng"], W - 88, size=10.5, h=24, rowgap=32)
    o.append(s)
    n, _ = note(44, 384, W - 88, "scope: all of this happens in VMs, lab networks and hardware I "
                "own. Controlled proof-of-concept work \u2014 RAT and worm concepts \u2014 stays in "
                "isolated environments. The point is understanding attacker behaviour well enough "
                "to defend against it. No production systems, no one else's data.")
    o.append(n)
    return svg(H, "".join(o),
               "Security research. Offensive: penetration testing, vulnerability research, "
               "exploitation research, web and network security. Analysis: reverse engineering, "
               "malware research, OSINT, traffic analysis. Defensive: OPSEC and privacy "
               "architecture, Linux and system hardening, security automation, device and game "
               "security. Toolkit: Nmap, Wireshark, Metasploit, Hashcat, Hydra, John the Ripper, "
               "Aircrack-ng. Scope: everything happens in VMs, lab networks and hardware I own; "
               "controlled proof-of-concept work stays in isolated environments; no production "
               "systems and no one else's data.")


# ============================================================ USBVAULT (flagship)
def keychain(x, y, w):
    """Password -> Argon2id -> KEK -> DEK -> per-file keys diagram."""
    o = []
    boxes = [("PASSWORD", "user input"), ("KEK", "key-encryption key"),
             ("DEK", "data-encryption key"), ("PER-FILE KEY", "one per file")]
    arrows = ["Argon2id", "unwraps", "HKDF-SHA256"]
    bw, bh, gap = 196, 42, 40
    bx = x + (w - bw) / 2
    for i, (t, sub) in enumerate(boxes):
        by = y + i * (bh + gap)
        o.append(rect(bx, by, bw, bh, fill=SURF2, stroke=LINE2, rx=3))
        o.append(line(bx, by, bx, by + bh, ACC, 2))
        o.append(txt(bx + 14, by + 20, t, 12.5, BONE, MONO, "600", ls=1.8))
        o.append(txt(bx + 14, by + 34, sub, 9.5, DIM, MONO, "400"))
        if i < len(arrows):
            ay = by + bh
            cxm = bx + bw / 2
            o.append(line(cxm, ay + 4, cxm, ay + gap - 10, LINE2, 1, dash="3 3"))
            o.append(path(f"M{cxm-4},{ay+gap-14} L{cxm},{ay+gap-6} L{cxm+4},{ay+gap-14}",
                          stroke=ACC, sw=1.4, cap="round", join="round"))
            o.append(txt(cxm - 22, ay + gap / 2 + 4, arrows[i], 10.5, ACC, MONO, "500", "end", ls=1.2))
    # chunking strip
    cy = y + 4 * (bh + gap) - gap + 26
    o.append(txt(bx, cy, "file \u2192 256 KB chunks", 10, DIM, MONO, "400", ls=1.2))
    for i in range(6):
        o.append(rect(bx + i * 33, cy + 10, 26, 12, fill="none", stroke=LINE2, rx=2))
        o.append(rect(bx + i * 33 + 3, cy + 13, 20, 6, fill=ACCD, rx=1, opacity=0.7))
    o.append(txt(bx + 6 * 33 + 6, cy + 20, "AEAD", 10, ASH, MONO, "500", ls=1.2))
    return "".join(o), cy + 30 - y


def usbvault():
    H = 750
    o = []
    hd, _ = header(36, "06 — Featured projects", "Things I actually finished (mostly)",
                   index="01 / 05")
    o.append(hd)
    CX, CY, CW = 44, 132, W - 88
    CH = 588
    o.append(card(CX, CY, CW, CH))
    o.append(corners(CX, CY, CW, CH, 12))
    # head
    o.append(txt(CX + 28, CY + 52, "USBVAULT", 34, BONE, DISPLAY, "700", ls=-0.3))
    st, stw = status(CX + 28 + 200, CY + 32, "ALPHA")
    o.append(st)
    o.append(label(CX + CW - 28, CY + 40, "Python · flagship", 10.5, DIM, "end", ls=2.2))
    o.append(line(CX + 28, CY + 72, CX + CW - 28, CY + 72, LINE))
    TX, TWD = CX + 28, 420
    o.append(txt(TX, CY + 106, "Per-file authenticated encryption for USB drives.",
                 18, BONE, DISPLAY, "500"))
    o.append(txt(TX, CY + 132, "Argon2id · HKDF-SHA256 · ChaCha20-Poly1305 · 256 KB chunks",
                 11.5, ACC, MONO, "500", ls=1.2))
    y = CY + 168
    o.append(para(TX, y, "An open-source, privacy-focused USB encryption system. Every file "
                  "becomes its own encrypted blob instead of one monolithic container, so a "
                  "changed file only rewrites its own blob and corruption points at an exact "
                  "file.", TWD, 14.5, ASH, 1.62)[0])
    y = CY + 280
    o.append(para(TX, y, "Recovery is a printable one-time sheet, optionally split into Shamir "
                  "shares (3-of-5). No backdoor, no reset, no hidden path. A wrong password "
                  "tries the key slots and fails cleanly \u2014 resistance comes from Argon2id being "
                  "expensive, not from a lockout.", TWD, 14.5, ASH, 1.62)[0])
    o.append(label(TX, CY + 408, "Also in the box", 10.5, DIM, ls=2.4))
    s, _ = pillrows(TX, CY + 422, ["Counterfeit-capacity detection", "Drive fingerprint binding",
                                   "Wear tracking", "Safe eject", "GUI + CLI", "Tray agent",
                                   "Portable unlocker", "Windows + Linux",
                                   "No account, no telemetry"], TWD + 14, size=9.5, h=22, rowgap=28, padx=8)
    o.append(s)
    # diagram panel
    DX, DY, DW = CX + 476, CY + 96, 336
    kc, kh = keychain(DX, DY + 34, DW)
    o.append(rect(DX, DY, DW, kh + 52, fill=INK, stroke=LINE, rx=3))
    o.append(label(DX + 14, DY + 22, "fig. 03 — key hierarchy", 10, DIM, ls=1.8))
    o.append(kc)
    # disclaimer
    n, nh = note(CX + 28, CY + CH - 82, CW - 56, "USBVAULT is alpha software and has not had an "
                 "independent security audit. For data you cannot afford to lose, use a mature, "
                 "audited tool.")
    o.append(n)
    return svg(H, "".join(o),
               "Featured project: USBVAULT, alpha, Python. Per-file authenticated encryption for "
               "USB drives using Argon2id, HKDF-SHA256, ChaCha20-Poly1305 and 256 KB chunks. Key "
               "hierarchy: password, Argon2id, KEK, unwraps DEK, HKDF-SHA256, per-file keys. "
               "Every file is its own encrypted blob, so a changed file only rewrites that blob "
               "and corruption points at an exact file. Recovery is a printable one-time sheet "
               "with optional 3-of-5 Shamir shares; no backdoor, no password reset, no lockout. "
               "Also includes counterfeit-capacity detection, drive fingerprint binding, wear "
               "tracking, safe eject, GUI and CLI, tray agent, portable unlocker, Windows and "
               "Linux support, no account and no telemetry. USBVAULT is alpha and has not had an "
               "independent security audit; for data you cannot afford to lose, use a mature, "
               "audited tool.")


# ============================================================ SMALL PROJECT CARDS
def motif_proxy(x, y):
    o = [circle(x + 12, y + 44, 4, stroke=ACC, sw=1.2)]
    import random
    r = random.Random(3)
    pts = [(x + 40 + r.uniform(0, 46), y + 8 + r.uniform(0, 72)) for _ in range(9)]
    for i, (px, py) in enumerate(pts):
        ok = i % 3 == 0
        o.append(line(x + 12, y + 44, px, py, ACCD if ok else LINE2, 0.8, opacity=0.9 if ok else 0.5))
        o.append(circle(px, py, 2.4, fill=ACC if ok else "none", stroke=None if ok else LINE2, sw=1))
    o.append(line(x + 96, y + 44, x + 116, y + 44, LINE2, 1, dash="3 3"))
    o.append(circle(x + 124, y + 44, 4, fill=ACC))
    return "".join(o)


def motif_llm(x, y):
    o = []
    for i in range(3):
        o.append(rect(x + 8 + i * 14, y + 16 + i * 12, 96, 34, fill=SURF2, stroke=LINE2, rx=3,
                      opacity=0.5 + i * 0.25))
    for i in range(4):
        o.append(circle(x + 46 + i * 16, y + 57, 2.2, fill=ACC, opacity=0.4 + i * 0.2))
    return "".join(o)


def motif_vpn(x, y):
    o = [circle(x + 10, y + 44, 5, stroke=ACC, sw=1.3), circle(x + 126, y + 44, 5, stroke=ACC, sw=1.3)]
    o.append(path(f"M{x+18},{y+30} Q{x+68},{y+8} {x+118},{y+30}", stroke=LINE2, sw=1))
    o.append(path(f"M{x+18},{y+58} Q{x+68},{y+80} {x+118},{y+58}", stroke=LINE2, sw=1))
    o.append(line(x + 18, y + 44, x + 118, y + 44, ACCD, 1, dash="4 4"))
    for i in range(4):
        o.append(circle(x + 34 + i * 22, y + 44, 1.8, fill=ACC, opacity=0.8))
    return "".join(o)


def motif_clap(x, y):
    o = []
    amps = [4, 9, 30, 14, 5, 3, 26, 11, 4, 2, 3, 2]
    for i, a in enumerate(amps):
        px = x + 8 + i * 9
        c = ACC if a > 20 else LINE2
        o.append(line(px, y + 44 - a / 2, px, y + 44 + a / 2, c, 2, cap="round"))
    o.append(line(x + 2, y + 44, x + 118, y + 44, LINE, 0.8, opacity=0.6))
    return "".join(o)


def motif_car(x, y):
    o = [path(f"M{x+16},{y+58} L{x+26},{y+38} L{x+92},{y+38} L{x+104},{y+58} Z",
              fill=SURF2, stroke=LINE2, sw=1.2, join="round")]
    o.append(circle(x + 36, y + 60, 8, stroke=LINE2, sw=1.4))
    o.append(circle(x + 88, y + 60, 8, stroke=LINE2, sw=1.4))
    o.append(line(x + 60, y + 38, x + 60, y + 22, LINE2, 1))
    o.append(circle(x + 60, y + 20, 2.6, fill=ACC))
    for i in range(3):
        o.append(path(f"M{x+108+i*7},{y+40} q6,6 0,12", stroke=ACCD, sw=1, opacity=1 - i * 0.28))
    return "".join(o)


def project_card(name, status_kind, tagline, spec, body, motif, aria, index=None, H=254):
    o = []
    CX, CY, CW, CH = 44, 24, W - 88, H - 48
    o.append(card(CX, CY, CW, CH))
    o.append(line(CX, CY, CX + 56, CY, ACC, 2))
    o.append(txt(CX + 26, CY + 44, name, 23, BONE, DISPLAY, "700", ls=-0.2))
    st, stw = status(CX + 26 + tw(name, 23) * 1.16 + 22, CY + 26, status_kind)
    o.append(st)
    if index:
        o.append(label(CX + CW - 26, CY + 32, index, 10.5, DIM, "end", ls=2.2))
    o.append(txt(CX + 26, CY + 74, tagline, 15.5, ASH, DISPLAY, "400"))
    o.append(txt(CX + 26, CY + 100, spec, 11, ACC, MONO, "500", ls=1.1))
    o.append(para(CX + 26, CY + 128, body, 560, 13, DIM, 1.6)[0])
    o.append(line(CX + CW - 190, CY + 20, CX + CW - 190, CY + CH - 20, LINE, 1, opacity=0.7))
    o.append(motif(CX + CW - 172, CY + (CH - 88) / 2))
    return svg(H, "".join(o), aria)


def proxy():
    return project_card(
        "Proxy Hunter", "Active", "Multithreaded proxy scraper, checker and scorer.",
        "Python · threading · CLI · Telegram integration",
        "Pulls publicly listed proxies from multiple sources, validates them, drops the dead "
        "ones, skips anything it has already seen and scores the survivors 0\u201310. Built as a "
        "networking and reliability exercise \u2014 the interesting part is how fast a free proxy "
        "list rots.",
        motif_proxy, index="02 / 05",
        aria="Project: Proxy Hunter, active, Python. A multithreaded CLI proxy scraper, checker "
             "and scorer with optional Telegram integration. It gathers publicly listed proxies "
             "from several sources, validates them, discards non-working ones, avoids rechecking "
             "the same proxy, and rates survivors from 0 to 10. Built as a networking and "
             "reliability-testing exercise.")


def localllm():
    return project_card(
        "Local LLM", "Experimental", "A local language-model playground.",
        "Python · PyTorch · Ollama · OpenRouter",
        "Running models locally, wiring them into tooling and watching how behaviour changes "
        "when you change the context around them. Model experimentation rather than model "
        "training: inference, prompting, structure and the plumbing in between.",
        motif_llm, index="03 / 05", H=234,
        aria="Project: Local LLM, experimental. A local language-model project using Python, "
             "PyTorch, Ollama and OpenRouter, exploring model behaviour, inference and tooling. "
             "Model experimentation rather than model training.")


def vpn():
    return project_card(
        "Pi WireGuard VPN", "Active", "A VPN I run, on hardware I own.",
        "Raspberry Pi · WireGuard · Linux · Wireshark",
        "Self-managed WireGuard server on a Raspberry Pi: my own tunnel, my own firewall rules "
        "and my own logs, of which there are none. Wireshark when traffic looks wrong. Not a "
        "protocol I wrote \u2014 infrastructure I actually maintain.",
        motif_vpn, index="04 / 05",
        aria="Project: Raspberry Pi WireGuard VPN, active. A self-managed WireGuard VPN server "
             "running on a Raspberry Pi, with Linux administration and Wireshark for traffic "
             "analysis. Infrastructure I maintain rather than a protocol I wrote.")


def hardware():
    H = 296
    o = []
    CX, CY, CW, CH = 44, 24, W - 88, H - 48
    o.append(card(CX, CY, CW, CH))
    o.append(line(CX, CY, CX + 56, CY, ACC, 2))
    o.append(txt(CX + 26, CY + 42, "Hardware bench", 23, BONE, DISPLAY, "700", ls=-0.2))
    o.append(label(CX + CW - 26, CY + 30, "05 / 05", 10.5, DIM, "end", ls=2.2))
    o.append(line(CX + 26, CY + 60, CX + CW - 26, CY + 60, LINE))
    panels = [
        ("ClapSync", "Experiment", "Alarm clock that listens for a specific clap rhythm and starts "
         "Spotify. Input detection, API integration, and a genuinely terrible way to wake up.",
         "Raspberry Pi · audio input · Spotify API", motif_clap),
        ("RC Car", "Hardware", "A remote-control car built from parts with sensors on board \u2014 "
         "designed and assembled rather than followed from a tutorial.",
         "Arduino · sensors · motor control", motif_car),
    ]
    for i, (n, st_, body, spec, motif) in enumerate(panels):
        px = CX + 26 + i * 394
        o.append(txt(px, CY + 96, n, 16, BONE, DISPLAY, "600"))
        s, _ = status(px + tw(n, 16) * 1.1 + 16, CY + 80, st_)
        o.append(s)
        o.append(txt(px, CY + 120, spec, 10.5, ACC, MONO, "500", ls=1))
        o.append(para(px, CY + 148, body, 216, 12.5, DIM, 1.58)[0])
        o.append(motif(px + 232, CY + 104))
        if i == 0:
            o.append(line(CX + CW / 2, CY + 76, CX + CW / 2, CY + CH - 20, LINE, 1, opacity=0.7))
    return svg(H, "".join(o),
               "Hardware bench. ClapSync, an experiment: an alarm clock that detects a specific "
               "clap rhythm and triggers Spotify playback, built with a Raspberry Pi, audio input "
               "and the Spotify API. RC Car: a remote-control car built from parts with sensors, "
               "using Arduino, sensors and motor control, designed and assembled rather than "
               "followed from a tutorial.")


# ============================================================ LAB
def lab():
    H = 348
    o = []
    hd, _ = header(36, "07 — vuav lab", "Not projects yet", index="open bench")
    o.append(hd)
    o.append(txt(44, 132, "Half-built, half-thought-through. If it's on this list it is an "
                 "experiment, not software you should rely on.", 15.5, ASH, DISPLAY))
    rows = [
        ("Local AI agents", "WIP", "Small agents that do my repetitive jobs without me watching them."),
        ("LLM security harness", "Idea", "A repeatable way to test prompt injection and jailbreak behaviour."),
        ("Pi security lab", "WIP", "Isolated network for traffic capture and malware analysis."),
        ("Reverse-engineering notes", "Research", "Pulling apart binaries and firmware to understand the format."),
    ]
    for i, (n, st_, d) in enumerate(rows):
        y = 176 + i * 40
        o.append(line(44, y - 22, W - 44, y - 22, LINE, 1, opacity=0.8))
        o.append(txt(44, y, n, 13.5, BONE, MONO, "500"))
        o.append(txt(268, y, d, 12.6, DIM, DISPLAY, "400"))
        _, w = status(0, 0, st_)
        s, _ = status(W - 44 - w, y - 16, st_)
        o.append(s)
    o.append(line(44, 314, W - 44, 314, LINE))
    return svg(H, "".join(o),
               "vuav lab: experiments, not finished projects. Local AI agents, work in progress: "
               "small agents that handle repetitive jobs. LLM security harness, idea: a repeatable "
               "way to test prompt injection and jailbreak behaviour. Pi security lab, work in "
               "progress: an isolated network for traffic capture and malware analysis. "
               "Reverse-engineering notes, research: pulling apart binaries and firmware.")


# ============================================================ STACK
def stack():
    P, C, L = "p", "c", "l"
    cats = [
        ("AI", [("Python", P), ("PyTorch", L), ("Ollama", C), ("OpenRouter", C), ("Cursor", C)]),
        ("Languages", [("Python", P), ("JavaScript", C), ("HTML", P), ("CSS", P), ("C++", L)]),
        ("Frontend", [("React", C), ("Tailwind", C)]),
        ("Backend", [("Node.js", C), ("Flask", C)]),
        ("Data", [("SQLite", C), ("Redis", L)]),
        ("Infra", [("Docker", C), ("AWS", L), ("Cloudflare", C), ("WireGuard", C), ("SSH", P)]),
        ("Security", [("Nmap", C), ("Wireshark", C), ("Metasploit", C), ("Hashcat", C),
                      ("Hydra", C), ("John the Ripper", C), ("Aircrack-ng", C)]),
        ("Systems", [("Debian", P), ("Parrot OS", C), ("Qubes OS", L), ("WSL", P), ("VirtualBox", C)]),
        ("Hardware", [("Raspberry Pi", C), ("Arduino", C)]),
        ("Tools", [("Git", P), ("GitHub", P), ("VS Code", P)]),
    ]
    colmap = {P: ACC, C: ASH, L: DIM}
    o = []
    hd, _ = header(36, "08 — Stack", "What's actually installed", index="honest levels")
    o.append(hd)
    # legend
    lx = 44
    for k, t in ((P, "primary"), (C, "comfortable"), (L, "learning")):
        o.append(circle(lx + 4, 128, 3, fill=colmap[k]))
        o.append(txt(lx + 14, 132, t, 10.5, DIM, MONO, "400", ls=1.4))
        lx += 22 + tw(t, 10.5, True) + 26
    y = 158
    for name, items in cats:
        o.append(txt(44, y + 16, name.upper(), 11.5, ASH, MONO, "600", ls=2.4))
        cx, cy = 168, y
        for t, lvl in items:
            s, w = pill(cx, cy, t, size=10.5, h=24, dot=colmap[lvl], padx=9)
            if cx + w > W - 44 and cx > 168:
                cx, cy = 168, cy + 30
                s, w = pill(cx, cy, t, size=10.5, h=24, dot=colmap[lvl], padx=9)
            o.append(s)
            cx += w + 7
        o.append(line(44, cy + 34, W - 44, cy + 34, LINE, 1, opacity=0.75))
        y = cy + 46
    H = y + 8
    return svg(H, "".join(o),
               "Stack, with honest levels. AI: Python primary, PyTorch learning, Ollama, "
               "OpenRouter and Cursor comfortable. Languages: Python, HTML and CSS primary, "
               "JavaScript comfortable, C++ learning. Frontend: React and Tailwind. Backend: "
               "Node.js and Flask. Data: SQLite comfortable, Redis learning. Infrastructure: "
               "Docker, Cloudflare, WireGuard comfortable, SSH primary, AWS learning. Security: "
               "Nmap, Wireshark, Metasploit, Hashcat, Hydra, John the Ripper, Aircrack-ng. "
               "Systems: Debian and WSL primary, Parrot OS and VirtualBox comfortable, Qubes OS "
               "learning. Hardware: Raspberry Pi and Arduino. Tools: Git, GitHub, VS Code.")


# ============================================================ BEYOND CODE
def beyond():
    H = 324
    o = []
    hd, _ = header(36, "10 — Beyond code", "I also sell clothes", index="\u22481.5 years")
    o.append(hd)
    o.append(para(44, 138, "When I'm not building software I run my own clothing brand. I built "
                 "the site, and I handle the branding, operations, development and growth myself "
                 "\u2014 which mostly means learning what happens after you press deploy.",
                 486, 16.5, ASH)[0])
    o.append(para(44, 254, "It has been running for about a year and a half. The milestone I'm "
                 "proudest of is expanding into Poland.", 486, 16.5, ASH)[0])
    FX, FY, FW, FH = 596, 128, 260, 148
    o.append(card(FX, FY, FW, FH))
    o.append(corners(FX, FY, FW, FH, 9))
    rows = [("running", "~1.5 years"), ("role", "all of them"), ("market", "UK \u2192 Poland"),
            ("site", "private for now")]
    for i, (k, v) in enumerate(rows):
        y = FY + 34 + i * 30
        o.append(txt(FX + 18, y, k, 10.5, DIM, MONO, "400", ls=1.6))
        o.append(txt(FX + 108, y, v, 11.5, ASH, MONO, "500"))
        if i < 3:
            o.append(line(FX + 18, y + 12, FX + FW - 18, y + 12, LINE, 1, opacity=0.7))
    return svg(H, "".join(o),
               "Beyond code: I run my own clothing brand. I built the site and handle branding, "
               "operations, development and growth myself. It has been running for about a year "
               "and a half and expanded into Poland. The site is private for now.")


# ============================================================ CONNECT + FOOTER
def connect():
    H = 236
    o = []
    hd, _ = header(36, "11 — Connect", "Say something interesting", index="EN / PL")
    o.append(hd)
    o.append(para(44, 136, "Open to internships, collaboration, and being told my code is wrong "
                 "by someone who knows better.", 470, 16.5, ASH)[0])
    rows = [("English", "Fluent"), ("Polish", "Fluent")]
    for i, (k, v) in enumerate(rows):
        y = 140 + i * 30
        o.append(txt(620, y, k, 12.5, ASH, MONO, "500"))
        o.append(txt(760, y, v, 12.5, DIM, MONO, "400"))
        o.append(line(620, y + 12, W - 44, y + 12, LINE, 1, opacity=0.7))
    o.append(line(44, 210, W - 44, 210, LINE))
    return svg(H, "".join(o),
               "Connect. Open to internships and collaboration. Languages: English fluent, "
               "Polish fluent.")


def button(text, sub, fname):
    w, h = 268, 60
    o = [rect(0.75, 0.75, w - 1.5, h - 1.5, fill=SURF, stroke=LINE2, rx=4)]
    o.append(line(0.75, 0.75, 0.75, h - 0.75, ACC, 2.5))
    o.append(txt(24, 26, text, 13, BONE, MONO, "600", ls=2))
    o.append(txt(24, 45, sub, 11, DIM, MONO, "400"))
    o.append(path(f"M{w-34},{h/2-5} l6,5 l-6,5", stroke=ACC, sw=1.4, cap="round", join="round"))
    body = "".join(o)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" '
            f'height="{h}" role="img" aria-label="{esc(text + ": " + sub)}">'
            f'<title>{esc(text + ": " + sub)}</title>'
            f'{rect(0,0,w,h,fill=INK,rx=4)}{body}</svg>')


def footer():
    H = 108
    o = [line(44, 34, W - 44, 34, LINE)]
    o.append(line(44, 34, 100, 34, ACC, 1.6))
    o.append(txt(44, 68, "Built by Krystian", 13, ASH, MONO, "500"))
    o.append(txt(44, 90, "still learning. still building.", 12, DIM, MONO, "400"))
    o.append(txt(W - 44, 68, "vuav", 20, BONE, MONO, "700", "end", ls=6))
    o.append(txt(W - 44, 90, "London, UK", 11, DIM, MONO, "400", "end", ls=1.6))
    return svg(H, "".join(o), "Built by Krystian, vuav, London UK. Still learning, still building.")


def rule():
    o = [line(44, 20, W - 44, 20, LINE)]
    o.append(rect(W / 2 - 3, 17, 6, 6, fill=INK, stroke=LINE2, rx=1))
    return svg(40, "".join(o), "")


def avatar():
    s = 400
    o = [rect(0, 0, s, s, fill=INK)]
    o.append(grid(0, 0, s, s, 25, "#15191F", 0.8, 0.8))
    o.append(circle(s / 2, s / 2, 168, fill=SURF, stroke=LINE2, sw=1.4))
    o.append(circle(s / 2, s / 2, 152, stroke=ACCD, sw=0.9))
    o.append(txt(s / 2, s / 2 - 6, "VUAV", 62, BONE, MONO, "700", "middle", ls=6))
    o.append(txt(s / 2, s / 2 + 28, "replace me", 13, DIM, MONO, "400", "middle", ls=3))
    return svg(s, "".join(o), "Avatar placeholder for vuav", w=s)


if __name__ == "__main__":
    write("assets/ai.svg", ai())
    write("assets/security.svg", security())
    write("assets/projects/usbvault.svg", usbvault())
    write("assets/projects/proxy-hunter.svg", proxy())
    write("assets/projects/local-llm.svg", localllm())
    write("assets/projects/vpn.svg", vpn())
    write("assets/projects/hardware.svg", hardware())
    write("assets/lab.svg", lab())
    write("assets/stack.svg", stack())
    write("assets/beyond.svg", beyond())
    write("assets/connect.svg", connect())
    write("assets/connect/github.svg", button("GITHUB", "github.com/vuav", "github"))
    write("assets/connect/linkedin.svg", button("LINKEDIN", "in/krystianwlos", "linkedin"))
    write("assets/connect/email.svg", button("EMAIL", "krystianwlos@proton.me", "email"))
    write("assets/footer.svg", footer())
    write("assets/rule.svg", rule())
    write("assets/avatar-placeholder.svg", avatar())
    print("gen2 ok")


def sechead(eyebrow, title, index, sub=None, H=120):
    o = []
    hd, _ = header(36, eyebrow, title, index=index, sub=sub)
    o.append(hd)
    return svg(H, "".join(o), f"{title} — {eyebrow}")


def extra():
    write("assets/section-activity.svg",
          sechead("09 — Activity", "Proof of commits", "github-readme-stats", H=116))

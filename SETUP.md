# vuav profile — setup

## 1. Repository

Create a repo named exactly **`vuav`** (same as the username) and make it public.
GitHub renders `README.md` from that repo on `github.com/vuav`.

```
vuav/                             ← repo name must equal your username
├── README.md
├── SETUP.md                      ← this file (optional, safe to delete)
└── assets/
    ├── hero.svg                  1. hero
    ├── about.svg                 2. origin story + console figure
    ├── currently.svg             3. current mission
    ├── what-i-build.svg          4. six domains
    ├── ai.svg                    5. AI / LLM
    ├── security.svg              6. security research
    ├── lab.svg                   7. vuav lab (experiments)
    ├── stack.svg                 8. tech stack
    ├── section-activity.svg      9. header above the GitHub stats
    ├── beyond.svg               10. clothing brand
    ├── connect.svg              11. connect + languages
    ├── footer.svg
    ├── rule.svg                  spare divider, not currently used
    ├── avatar-placeholder.svg    optional, see §4
    ├── projects/
    │   ├── usbvault.svg          flagship, includes the section header
    │   ├── proxy-hunter.svg
    │   ├── local-llm.svg
    │   ├── vpn.svg
    │   └── hardware.svg          ClapSync + RC car
    └── connect/
        ├── github.svg
        ├── linkedin.svg
        ├── email.svg
        └── resume.svg            unused until you uncomment it (§5)
```

Push everything, then open `github.com/vuav`. Nothing else is required.

## 2. Design system (if you edit the SVGs)

| Role | Value |
|---|---|
| Background | `#0A0B0D` |
| Card surface | `#101216` |
| Inset surface | `#15181D` |
| Hairline / strong hairline | `#23272E` / `#2E343C` |
| Primary text | `#E9EBED` |
| Secondary text | `#8A929B` |
| Tertiary / decorative | `#565D66` |
| Accent (the only one) | `#7FA0B8` — blueprint steel |
| Accent dim | `#3C4E5C` |

Display type: `Inter, 'Helvetica Neue', Helvetica, Arial, sans-serif`.
Metadata type: `ui-monospace, SFMono-Regular, 'DejaVu Sans Mono', Menlo, Consolas, monospace`.
No webfonts are loaded — GitHub proxies images through camo and external fonts wouldn't load, so everything falls back cleanly to system faces.

All full-width assets use a **900px viewBox** and are placed with `width="100%"`, so they scale to whatever column GitHub gives them. The accent is used only on hairline ticks, status dots, arrows and small labels — if you add more of it, the whole thing stops being monochrome.

## 3. Editing text

Card copy lives inside the SVGs as normal `<text>` elements. Open the file, find the string, change it. Two rules:

- Keep replacement text roughly the same length, or it will run past the card edge — there's no reflow inside an SVG.
- If you change what a card says, update the `alt=""` text for that image in `README.md` too. That alt text is what screen readers and GitHub search see.

## 4. Avatar

Your avatar is set in **GitHub account settings**, not in the README — upload it at `github.com/settings/profile`. `assets/avatar-placeholder.svg` is only there if you want a 400×400 template that matches the palette; it's not referenced by the README and you can delete it.

## 5. Adding a resume later

1. Put `resume.pdf` in `assets/`.
2. In `README.md`, find the `<!-- RESUME: ... -->` comment inside the connect block and uncomment the line inside it.
3. Edit the subtitle in `assets/connect/resume.svg` (currently "PDF — coming soon") to something like "PDF · updated 2026".

No fake link is included anywhere until you do this.

## 6. Project links

Every project card is wrapped in `<a href="https://github.com/vuav?tab=repositories">`. When a repo goes public, replace that URL with the real one, e.g.:

```html
<a href="https://github.com/vuav/usbvault"><img src="assets/projects/usbvault.svg" ...
```

## 7. External services (three, all optional)

| Service | Used for | Notes |
|---|---|---|
| `img.shields.io` | followers / stars counters | Official, extremely stable. |
| `github-readme-stats.vercel.app` | stats card + top languages | The standard, actively maintained. Public instance is occasionally rate-limited; if a card shows an error, it fixes itself, or you can self-host it. |
| `github-readme-activity-graph.vercel.app` | contribution graph | Maintained. Same caveat. |

All three are themed to the palette via URL parameters. If any of them ever goes dark, delete the `<p align="center">` stats block and the graph line — the rest of the profile is entirely self-hosted SVG and doesn't depend on anything external.

Deliberately **not** used: profile-view counters, streak widgets, trophy walls, "wakatime" cards, and animated typing SVGs. They're unreliable, they age badly, and they'd fight the design.

## 8. Checklist before you push

- [ ] Repo is named `vuav` and is **public**
- [ ] `assets/` uploaded with the folder structure intact (relative paths break otherwise)
- [ ] Avatar set in account settings
- [ ] LinkedIn URL resolves: `linkedin.com/in/krystianwlos`
- [ ] Email is correct: `krystianwlos@proton.me`
- [ ] Open the profile on a phone and scroll it once
- [ ] Read the copy out loud — if a line sounds like something you'd never say, change it
- [ ] Every status label still true (`ALPHA`, `WIP`, `IDEA`, `EXPERIMENT`)

If images don't load, the most likely cause is a wrong folder name. As a fallback you can swap relative paths for absolute ones:
`https://raw.githubusercontent.com/vuav/vuav/main/assets/hero.svg`

## 9. Regenerating

The SVGs were generated by the scripts in `build/` (`svgkit.py`, `gen1.py`, `gen2.py`). Keep them if you want to restyle everything at once — change a token in `svgkit.py`, run `python3 gen1.py && python3 gen2.py`, and every asset updates. Delete `build/` if you'd rather just hand-edit the SVGs.

<!--
  vuav/vuav — profile README (AI-forward build, original visual system preserved)
  All section SVGs are Krystian's own, unchanged, except hero.svg (role line now
  leads with AI). Three NEW cards were added in the same compact-card grammar:
    assets/projects/ai-collaboration-center.svg
    assets/projects/agent-framework.svg
    assets/projects/rag.svg
  These three repos are private-pending-publish, so their cards link to the
  profile root for now. Swap each to its real repo URL once public:
    AI Collaboration Center -> https://github.com/vuav/<repo>
    Agent Framework         -> https://github.com/vuav/<repo>
    RAG System              -> https://github.com/vuav/<repo>
-->

<div align="center">

<img src="assets/hero.svg" width="900" alt="vuav — Krystian Wł. AI / LLM systems · software · security · systems. 17, London UK. Computing L3 BTEC Year 2, heading for PJATK Warsaw. I build things I don't want to do twice." />

<a href="https://github.com/vuav"><img src="https://img.shields.io/github/followers/vuav?style=flat-square&label=followers&labelColor=0A0B0D&color=15181D" alt="GitHub followers" /></a>
<a href="https://github.com/vuav"><img src="https://img.shields.io/github/stars/vuav?style=flat-square&label=stars&labelColor=0A0B0D&color=15181D" alt="Total stars" /></a>
<img src="https://img.shields.io/badge/based%20in-London,%20UK-15181D?style=flat-square&labelColor=0A0B0D" alt="Based in London, UK" />

<img src="assets/rule.svg" width="900" alt="" />

<img src="assets/about.svg" width="900" alt="01 — Origin. It started with a 3DS. At nine I wanted games I couldn't afford, got curious about how the thing worked, read it, broke it, and put it back together. Eight years later it's Linux, reverse engineering, security research, AI and a questionable number of side projects. Taken apart / modified / researched: Nintendo 3DS, Switch OLED, PS3, iOS." />

<img src="assets/currently.svg" width="900" alt="02 — Currently. Finishing Computing L3 BTEC Year 2; preparing a PJATK application in Warsaw; learning C++ properly; deepening LLM systems and agent tooling; security research in isolated labs only; shipping USBVAULT toward a stable release." />

<img src="assets/what-i-build.svg" width="900" alt="03 — What I build. Six directions, one habit: security, AI, software, web, systems, hardware — attack it, then work out how you'd have stopped it." />

<img src="assets/ai.svg" width="900" alt="04 — AI / LLM. Getting models to behave. Most of my AI time goes into the parts people skip: context, structure, and what a model does when pushed off script. Focus: prompt and context engineering, agentic systems, structured outputs, local model experimentation, prompt injection research, jailbreak and LLM security research. Worked with Python, PyTorch, Ollama, OpenRouter, Claude, ChatGPT/OpenAI, Gemini, Qwen, DeepSeek, Cursor. Local LLM means running and wiring up local models, not training a frontier model." />

<!-- swap to real repo when public -->
<a href="https://github.com/vuav"><img src="assets/projects/ai-collaboration-center.svg" width="900" alt="AI Collaboration Center (active, Python desktop app). Two coding agents, one referee. A desktop app that runs structured debates between Codex CLI and Claude Code: a controller decides who speaks, a turn protocol keeps them in order, shared context passes between them each round. The hard part was the plumbing — fixed a Codex stdin deadlock on Windows plus IPC and concurrency bugs to get two processes cooperating without hanging. Turn protocol, shared context, controller, Windows IPC." /></a>

<a href="https://github.com/vuav"><img src="assets/projects/agent-framework.svg" width="900" alt="Agent Framework (active, Python). The scaffolding, not another wrapper. A framework for building tool-using LLM agents: conversation memory, a tool registry, and a loop that decides when to call a tool, runs it, and feeds the result back to the model, with loop guards so it can't spin forever. Adding a tool is a small defined step. Infrastructure around agents, not another wrapper around a chat endpoint." /></a>

<a href="https://github.com/vuav"><img src="assets/projects/rag.svg" width="900" alt="RAG System (active, Python). Answers tied to real source text. Retrieval-augmented Q&A over your own documents: ingest files, split into chunks, index them, retrieve the sections that match a question, and pass only those to the model so the answer stays grounded in real source text. Retrieval plus LLM application engineering." /></a>

<img src="assets/rule.svg" width="900" alt="" />

<a href="https://github.com/vuav"><img src="assets/projects/usbvault.svg" width="900" alt="06 — Featured projects. USBVAULT (alpha, Python, flagship). Per-file authenticated encryption for USB drives: Argon2id, HKDF-SHA256, ChaCha20-Poly1305, 256 KB chunks. Key hierarchy password → Argon2id → KEK → DEK → HKDF-SHA256 → per-file key. Every file is its own encrypted blob, so a changed file only rewrites that blob and corruption points at an exact file. Printable one-time recovery sheet with optional 3-of-5 Shamir shares; no backdoor, no reset, no lockout. Counterfeit-capacity detection, drive fingerprint binding, wear tracking, safe eject, GUI and CLI, tray agent, portable unlocker, Windows and Linux, no account, no telemetry. Alpha, not independently audited — for data you cannot afford to lose, use a mature, audited tool." /></a>

<a href="https://github.com/vuav"><img src="assets/projects/proxy-hunter.svg" width="900" alt="Proxy Hunter (active, Python). Multithreaded proxy scraper, checker and scorer with Telegram integration. Pulls publicly listed proxies, validates them, drops the dead ones, skips seen ones, and scores survivors 0–10. A networking and reliability exercise." /></a>

<a href="https://github.com/vuav"><img src="assets/projects/local-llm.svg" width="900" alt="Local LLM (experimental, Python). Running models locally and wiring them into tooling to watch how behaviour changes with the context around them. Python, PyTorch, Ollama, OpenRouter. Model experimentation rather than training: inference, prompting, structure and the plumbing in between." /></a>

<a href="https://github.com/vuav"><img src="assets/projects/vpn.svg" width="900" alt="Pi WireGuard VPN (active). Self-managed WireGuard server on a Raspberry Pi: my own tunnel, firewall rules and logs, of which there are none. Wireshark when traffic looks wrong. Infrastructure I actually maintain." /></a>

<a href="https://github.com/vuav"><img src="assets/projects/hardware.svg" width="900" alt="Hardware bench (experiment). ClapSync: an alarm clock that listens for a clap rhythm and starts Spotify — input detection and API integration. RC Car: built from parts with sensors on board, designed rather than followed from a tutorial. Raspberry Pi, Arduino, ESP32." /></a>

<img src="assets/security.svg" width="900" alt="05 — Security research. Attack it, then defend it. Offensive: penetration testing, vulnerability research, exploitation research, web and network security. Analysis: reverse engineering, malware research, OSINT, traffic analysis. Defensive: OPSEC and privacy architecture, hardening, security automation. Toolkit: Nmap, Wireshark, Metasploit, Hashcat, Hydra, John the Ripper, Aircrack-ng. Isolated labs only." />

<img src="assets/lab.svg" width="900" alt="07 — vuav lab. Not projects yet. Half-built experiments: local AI agents (WIP), LLM security harness (idea), Pi security lab (WIP), reverse-engineering notes (research)." />

<img src="assets/stack.svg" width="900" alt="08 — Stack, with honest levels. AI: Python primary, PyTorch learning, Ollama/OpenRouter/Cursor comfortable. Languages: Python/HTML/CSS primary, JavaScript comfortable, C++ learning. Frontend: React, Tailwind. Backend: Node.js, Flask. Data: SQLite comfortable, Redis learning. Infra: Docker, Cloudflare, WireGuard comfortable, SSH primary, AWS learning. Systems: Debian/WSL primary, Parrot OS/VirtualBox comfortable, Qubes OS learning. Hardware: Raspberry Pi, Arduino. Tools: Git, GitHub, VS Code." />

<img src="assets/section-activity.svg" width="900" alt="09 — Activity. Proof of commits." />

<img src="https://github-readme-stats.vercel.app/api?username=vuav&show_icons=true&hide_border=true&hide_title=true&include_all_commits=true&rank_icon=github&bg_color=0A0B0D&title_color=7FA0B8&text_color=8A929B&icon_color=7FA0B8&ring_color=7FA0B8" alt="GitHub statistics for vuav" height="165" />
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=vuav&layout=compact&hide_border=true&langs_count=8&bg_color=0A0B0D&title_color=7FA0B8&text_color=8A929B" alt="Most used languages" height="165" />

<img src="https://github-readme-activity-graph.vercel.app/graph?username=vuav&bg_color=0A0B0D&color=E9EBED&line=7FA0B8&point=E9EBED&area=true&area_color=15181D&hide_border=true&custom_title=Contribution%20activity" width="900" alt="Contribution activity graph for vuav" />

<img src="assets/beyond.svg" width="900" alt="10 — Beyond code. I run my own clothing brand: I built the site and handle branding, operations, development and growth. Running about a year and a half; expanded into Poland." />

<img src="assets/connect.svg" width="900" alt="11 — Connect. Open to internships and collaboration. English and Polish, both fluent." />

<a href="https://github.com/vuav"><img src="assets/connect/github.svg" alt="GitHub: github.com/vuav" /></a>
<a href="https://linkedin.com/in/krystianwlos"><img src="assets/connect/linkedin.svg" alt="LinkedIn: in/krystianwlos" /></a>
<a href="mailto:krystianwlos@proton.me"><img src="assets/connect/email.svg" alt="Email: krystianwlos@proton.me" /></a>

<img src="assets/footer.svg" width="900" alt="Built by Krystian (vuav), London UK. Still learning, still building." />

</div>

<details>
<summary><b>Plain-text version</b></summary>

## vuav — Krystian Wł
**AI / LLM systems · software · security · systems.** 17, London, UK. English and Polish, both fluent. Computing L3 BTEC (Year 2), heading for PJATK in Warsaw. **"I build things I don't want to do twice."**

### 01 — Origin
It started with a 3DS. At nine I wanted games I couldn't afford, got curious about how it worked, read it, broke it, put it back together. Eight years later it's Linux, reverse engineering, security, systems and AI. Taken apart / modified / researched: 3DS, Switch OLED, PS3, iOS.

### 04 — AI / LLM
Most of my AI time goes into the parts people skip: context, structure, and what a model does when pushed off script. Prompt and context engineering, agentic systems, structured outputs, local inference, prompt injection and jailbreak/LLM security research. Python, PyTorch, Ollama, OpenRouter, Claude, ChatGPT/OpenAI, Gemini, Qwen, DeepSeek, Cursor. *"Local LLM" means running and wiring up local models — not training a frontier model in my bedroom.*

**AI systems I've built** *(repos publishing soon)*
- **AI Collaboration Center** *(active, Python)* — desktop app running structured debates between Codex CLI and Claude Code: controller, turn protocol, shared context. Fixed a Codex stdin deadlock on Windows plus IPC/concurrency bugs. Multi-agent orchestration + systems engineering.
- **Agent Framework** *(active, Python)* — tool-using LLM agents: memory, tool registry, and a tool-calling loop with loop guards. Adding a tool is a small, defined step.
- **RAG System** *(active, Python)* — retrieval-augmented Q&A: ingest → chunk/index → retrieve → pass to the model → grounded answer.

### 06 — Featured projects
- **USBVAULT** *(alpha, Python, flagship)* — per-file authenticated encryption for USB drives. Argon2id → KEK → DEK → HKDF-SHA256 → per-file keys → ChaCha20-Poly1305, 256 KB chunks. Printable one-time recovery sheet with optional 3-of-5 Shamir shares. No backdoor, no reset, no lockout. Counterfeit-capacity detection, drive fingerprint binding, wear tracking, GUI + CLI, Windows + Linux, no account, no telemetry. **Alpha, not independently audited — for data you cannot afford to lose, use a mature, audited tool.**
- **Proxy Hunter** *(active, Python)* — multithreaded proxy scraper/checker/scorer, Telegram integration.
- **Local LLM** *(experimental)* — local inference playground: PyTorch, Ollama, OpenRouter.
- **Pi WireGuard VPN** *(active)* — self-managed WireGuard on a Raspberry Pi; Wireshark for traffic analysis.
- **Hardware bench** *(experiment)* — ClapSync (clap-rhythm alarm → Spotify), RC car built from parts.

### 05 — Security research
Attack it, then defend it. Offensive: pentest, vuln/exploitation research, web/network security. Analysis: reverse engineering, malware research, OSINT, traffic analysis. Defensive: OPSEC, hardening, automation. Nmap, Wireshark, Metasploit, Hashcat, Hydra, John the Ripper, Aircrack-ng. Isolated labs only.

### 08 — Stack (honest levels)
AI: Python (primary), PyTorch (learning), Ollama/OpenRouter/Cursor (comfortable) · Languages: Python/HTML/CSS (primary), JavaScript (comfortable), C++ (learning) · Frontend: React, Tailwind · Backend: Node.js, Flask · Data: SQLite (comfortable), Redis (learning) · Infra: Docker, Cloudflare, WireGuard (comfortable), SSH (primary), AWS (learning) · Systems: Debian/WSL (primary), Parrot OS/VirtualBox (comfortable), Qubes OS (learning) · Security: Nmap, Wireshark, Metasploit, Hashcat, Hydra, John the Ripper, Aircrack-ng · Hardware: Raspberry Pi, Arduino, ESP32 · Tools: Git, GitHub, VS Code.

### 10 — Beyond code
My own clothing brand — ~1.5 years, site built by me, branding/operations/development/growth handled myself. Expanded into Poland.

### 11 — Connect
GitHub [github.com/vuav](https://github.com/vuav) · LinkedIn [in/krystianwlos](https://linkedin.com/in/krystianwlos) · Email <krystianwlos@proton.me>

</details>

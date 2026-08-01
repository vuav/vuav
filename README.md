![vuav](https://raw.githubusercontent.com/vuav/vuav/main/banner.svg)

security student. i build cryptographic tooling, and i take things apart to understand how they break.

```
$ id
uid=1337(vuav) groups=crypto,systems,offsec

$ cat ~/.focus
applied cryptography · systems programming · reverse engineering
current work: an encrypted volume engine built to survive an external audit

$ ls ~/stack
c++   python   c   typescript
linux   winfsp   ghidra   wireshark   x86-64
```

## usbvault

an open-source encrypted volume engine. per-file authenticated encryption, a
multi-slot header so a volume can be opened by password, hardware key, or a
recovery share, and a threat model published before a line of the core shipped.

![key hierarchy](https://raw.githubusercontent.com/vuav/vuav/main/arch.svg)

```
kdf         argon2id            m = 1 GiB, t = 3, p = 4
cipher      xchacha20-poly1305  per-file, per-chunk AEAD
key model   secret -> KEK -> unwraps a random 256-bit DEK
slots       password | fido2 (hmac-secret) | tpm 2.0 | shamir k-of-n
integrity   merkle tree over chunk tags, anti-rollback counter
destroy     crypto-shred: wipe the header and the data is unrecoverable
out of scope   hidden volumes, duress keys, hand-rolled primitives
```

trust model: reproducible builds, spec published ahead of code, signed releases,
and an audit targeting an independent firm before a 1.0 tag.

## selected work

```
usbvault     encrypted volume engine. argon2id + xchacha20, multi-slot header.       c++
honeytrace   ssh/http honeypot feeding a live public dashboard of real intrusions.   c++ · postgres
loadtrace    async http load generator. latency percentiles, local-only by default.  python
runecipher   substitution and rune cipher toolkit. also runs the gate below.         python
```

repositories go public as each threat model and spec lands.

## known-exploited, today

actively-exploited vulnerabilities from the CISA KEV catalog, pulled every morning
by a workflow in this repo. this block rewrites itself.

<!-- KEV-START -->
```text
# CISA Known Exploited Vulnerabilities — synced 2026-08-01 08:25 UTC

CVE                ADDED       VENDOR             VULNERABILITY
CVE-2026-20316     2026-07-29  Cisco              Cisco Secure Firewall Management Center Use o…
CVE-2025-68686     2026-07-27  Fortinet           Fortinet FortiOS Exposure of Sensitive Inform…
CVE-2026-16812     2026-07-27  Arista             Arista VeloCloud Orchestrator On-Prem OS Comm…
CVE-2026-16232     2026-07-22  Check Point        Check Point SmartConsole Improper Authenticat…
CVE-2026-50522     2026-07-22  Microsoft          Microsoft SharePoint Deserialization of Untru…
CVE-2026-60137     2026-07-21  WordPress          WordPress Core SQL Injection Vulnerability
```
<!-- KEV-END -->

## the gate

a running program judges every attempt. decode the string, open an issue titled
`solve: <answer>`, and the bot verifies you, replies, and records the result. the
answer is never stored in this repo, only a hash of it is.

```
ᛟ ᛒ ᛊ ᛁ ᛞ ᛁ ᚨ ᚾ

ᛟ=o  ᛒ=b  ᛊ=s  ᛁ=i  ᛞ=d  ᚨ=a  ᚾ=n
```

[open a solve issue](../../issues/new?title=solve:%20YOURANSWER&body=decoded)

<!-- HOF-START -->
no one has passed yet.
<!-- HOF-END -->

---

`vuav@sys:~$ logout`

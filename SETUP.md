# deploying the vuav profile

everything lives in one special repo: a public repo named exactly `vuav`
(same as your username). github renders its `README.md` at the top of your profile.

## why your images weren't loading

the profile only shows images that actually exist in the repo. the two images are
`banner.svg` and `arch.svg`, referenced by relative path. if those files aren't
committed to the repo root on the default branch, github shows nothing. so:

commit the `.svg` files, not just the `README.md`. that is the whole fix.

this version deliberately uses zero third-party image services (no stats cards, no
external snake), because those are the parts that silently fail and make a profile
look broken. every image here is a local file you control.

## files

commit these at these exact paths on the default branch (`main`):

```
README.md
banner.svg
arch.svg
SETUP.md                          (optional, safe to delete)
.github/workflows/threat-feed.yml
.github/workflows/cipher-gate.yml
.github/workflows/snake.yml        (optional, see bottom)
scripts/cve_feed.py
scripts/cipher_game.py
```

## permissions

the threat-feed and cipher-gate push commits back to the repo, so give them write
access once:

settings -> actions -> general -> workflow permissions -> read and write -> save.

## prime the feed

actions tab -> threat-feed -> run workflow. it fills the "known-exploited, today"
block from the CISA KEV catalog and then runs itself every morning.

the cipher-gate needs no priming. it fires when someone opens a `solve:` issue.

## if an image still doesn't load

1. open `https://github.com/vuav/vuav/blob/main/banner.svg` in a browser. if that
   404s, the file isn't committed or the branch isn't `main`.
2. if the file loads there but not on the profile, swap the relative path in
   `README.md` for the raw url, e.g.
   `![vuav](https://raw.githubusercontent.com/vuav/vuav/main/banner.svg)`.
3. animation: the svgs animate when github serves them in a browser. if a cache
   ever flattens them, both were designed to look right frozen, so nothing breaks.

## changing the cipher answer

the plaintext is never stored, only its sha-256 lives in `scripts/cipher_game.py`.

```bash
python3 -c "import hashlib;print(hashlib.sha256(b'yournewword').hexdigest())"
```

paste the hash into `ANSWER_HASH`, then re-encode the word into runes and update the
rune line and legend in the `the gate` section of `README.md`. runes used here:

```
a=ᚨ b=ᛒ d=ᛞ e=ᛖ g=ᚷ h=ᚺ i=ᛁ l=ᛚ m=ᛗ n=ᚾ o=ᛟ r=ᚱ s=ᛊ t=ᛏ u=ᚢ
```

the judge strips everything except letters and lowercases before hashing, so case,
spaces, and punctuation in a submission never matter.

## optional: contribution snake

`snake.yml` generates the classic contribution-graph snake. it needs its own run
(actions tab -> snake) to create the `output` branch, and only then can you add this
line to the README without a broken-image icon:

```
![snake](https://raw.githubusercontent.com/vuav/vuav/output/snake.svg)
```

left out of the default README on purpose, so nothing 404s before you run it.

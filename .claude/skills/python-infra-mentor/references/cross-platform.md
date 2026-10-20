# Cross-platform: MacBook + Windows PC

Jaylon codes on both. The repo on GitHub is the single source of truth for code; the memory tracker is the source of truth for progress. Both machines pull from those, so neither machine "owns" the work.

## One-time setup on each machine

| Step | macOS (Terminal, zsh) | Windows (PowerShell) |
|---|---|---|
| Install Python | python.org installer or `brew install python` | python.org installer — check **"Add python.exe to PATH"** |
| Check version | `python3 --version` | `py --version` |
| Install Git | `xcode-select --install` or `brew install git` | git-scm.com installer |
| Configure Git (same on both) | `git config --global user.name "Jaylon Robinson"` + `user.email` | same |
| Line endings | `git config --global core.autocrlf input` | `git config --global core.autocrlf true` |
| Clone repo | `git clone https://github.com/jaylon-robinson/python-infra-engineering.git` | same |
| Create venv (inside repo) | `python3 -m venv .venv` | `py -m venv .venv` |
| Activate venv | `source .venv/bin/activate` | `.venv\Scripts\Activate.ps1` |
| Install deps | `pip install -r requirements.txt` | same |
| Run tests | `pytest` | same |

Windows gotcha: if activation errors with "running scripts is disabled", run once: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`.

The `.venv` folder is **per machine** and goes in `.gitignore` — never commit it. Each machine builds its own from `requirements.txt`. When he installs a new package, he runs `pip freeze > requirements.txt` (or adds the line by hand) and commits it, so the other machine can `pip install -r requirements.txt`.

VS Code: after creating the venv, pick it with *Python: Select Interpreter* on each machine.

## Switching machines (start of session)

1. `git status` — anything uncommitted left here from before?
2. `git pull`
3. Activate the venv (command above for this OS).
4. `pip install -r requirements.txt` (cheap if nothing changed).
5. `pytest` — confirm everything still passes before writing new code. If tests that passed on the other machine fail here, that's a free troubleshooting lesson (paths? line endings? OS-specific command output?).

## End of session (either machine)

```
git add .
git commit -m "<what changed, present tense>"
git push
```

Forgetting to push is the #1 way the two-machine setup breaks. If he forgot and is now on the other machine, the options are: go push from the first machine, or work on a branch and merge later — teach the merge, it's a real-world skill.

## Command differences that come up in lessons

| Task | macOS | Windows |
|---|---|---|
| Run a script | `python3 script.py` (or `python` inside venv) | `py script.py` (or `python` inside venv) |
| Ping 4 times | `ping -c 4 host` | `ping -n 4 host` |
| DNS lookup | `dig host` / `nslookup host` | `nslookup host` / `Resolve-DnsName host` |
| IP config | `ifconfig` / `ipconfig getifaddr en0` | `ipconfig /all` |
| Listening ports | `lsof -iTCP -sTCP:LISTEN` / `netstat -an` | `netstat -ano` / `Get-NetTCPConnection` |
| Trace route | `traceroute host` | `tracert host` |
| Clear screen | `clear` | `cls` |
| Env variable | `export API_KEY=...` | `$env:API_KEY="..."` |
| Path separator | `/` | `\` (Python accepts `/` on both) |

## Writing code that runs on both

- Use `pathlib.Path` instead of string paths; never hard-code `C:\Users\...` or `/Users/...`.
- When shelling out (`subprocess`), branch on `platform.system()` ("Darwin" vs "Windows") — the ping flag difference is a natural first lesson for this.
- Parsing OS command output is fragile across platforms; that's a teaching point for why the `socket` module beats scraping `ping` output.
- Open text files with `encoding="utf-8"` explicitly (Windows defaults can differ).
- `.gitattributes` with `* text=auto eol=lf` keeps line endings consistent.
- Raw ICMP sockets need admin/root on both OSes — another reason the toolkit uses TCP connect checks.

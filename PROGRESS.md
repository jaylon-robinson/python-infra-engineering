# Progress — Python Networking & Security Engineering

## Current phase & project
- **Phase 1** — Network Configuration Analyzer (`01-network-config-analyzer/`)
- **Feature in progress:** Feature 1 — `parse_ip(text)`: return an `ipaddress` IP object for valid input, `None` for invalid, using `try`/`except ValueError`. Lesson given (ipaddress module, try/except); exercise not yet attempted.

## Last session
- 2026-10-20, machine: **Mac**

## Environment
- Mac: Python 3.13, Git, VS Code `code` command, Homebrew, `gh` (logged in), repo cloned at `~/python-infra-engineering`, `.venv` with pytest. Commit email = GitHub noreply.
- To check on Mac: VS Code Python extension installed; interpreter set to `.venv`.
- PC: **not set up yet** — see `.claude/skills/python-infra-mentor/references/cross-platform.md` → "One-time setup on each machine".

## Independent
- (none yet)

## Practicing
- Guard-clause validation, `str.isdigit()`, `not`
- `return` vs `print` / `None`

## Learning
- `if` syntax (colon + indentation)
- `input()` returns `str`; `int(input(...))` nesting order (needed 2 hints — retest cold)
- `len()`, `str.endswith()`, dict add/replace with `d[key] = value`
- `ValueError` from `int("abc")`

## Strengths noticed
- Reads loops/dicts well; good security instincts (caught port 0 as invalid himself; chose strict rejection of `" 443"` deliberately).

## Bugs learned to diagnose
- String vs int comparison (`"443" == 443` is False)
- Bad paste silently turning a test line into a comment — count output vs. tests
- Empty folders don't get committed (Git tracks files, not folders)

## Struggles / needs reps
- Python syntax details (colons, indentation, parentheses order)
- Skipping the "run it and show output" step — keep insisting on it

## Pending cold retests
- Write `is_valid_port` from memory (skipped Oct 20 — Q4 code was written in an online compiler, never saved)
- `int(input(...))` and return-vs-print in a new context

## Next lesson
- Finish Feature 1 (`parse_ip`), then Feature 2: build a network from IP + prefix with `ipaddress.ip_interface` / `ip_network`.

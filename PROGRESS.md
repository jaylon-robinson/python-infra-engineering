# Progress — Python Networking & Security Engineering

## Current phase & project
- **Phase 1** — Network Configuration Analyzer (`01-network-config-analyzer/`)
- **Approach changed (2026-10-25, at Jaylon's request):** teach the full building blocks first, one block at a time, each ending with an exercise he writes + a cold check; then assemble the analyzer. Blocks: 1 Values/types/variables → 2 Strings → 3 Conditions/logic → 4 Functions → 5 Exceptions → 6 Lists & for → 7 while loops → 8 Dicts → 9 Modules & objects → 10 `ipaddress` → 11 Program structure (`main`, `__name__`) → 12 pytest.
- **Current block:** Block 2 — Strings. (Block 1 passed 2026-10-25: `exercises/server_inventory.py`, `exercises/block1_check.py`.)
- Feature 1 (`parse_ip`) lesson covered (ipaddress basics, uncaught exception stops program, traceback bottom-up, `parse_port` try/except trace); `parse_ip` not yet written. `01-network-config-analyzer/analyzer.py` exists (empty, nested-folder mistake fixed).

## Last session
- 2026-10-25, machine: **Mac**

## How Jaylon wants to learn (mandatory, set 2026-10-25)
- Code first, not chat first: every concept → short explanation + example → an assignment he writes and runs in VS Code.
- Each assignment lists: Objective, File, Requirements, Relevant concepts, Expected behavior, Test cases, Completion criteria. Only use concepts already taught.
- Mentor creates each new exercise file (requirements as comments, no solution code).
- Review his real code/output/errors, then a modification task to prove understanding. Graduated hints; full solution only on request + follow-up task.

## Environment
- Mac: Python 3.13, Git, VS Code `code` command, Homebrew, `gh` (logged in), repo cloned at `~/python-infra-engineering`, `.venv` with pytest. Commit email = GitHub noreply.
- To check on Mac: VS Code Python extension installed; interpreter set to `.venv`.
- PC: **not set up yet** — see `.claude/skills/python-infra-mentor/references/cross-platform.md` → "One-time setup on each machine".

## Independent
- (none yet)

## Practicing
- Variables, reassignment (top-to-bottom execution), types (`str`/`int`/`float`/`bool`/`None`), `type()`, `int()` conversion — passed Block 1 cold check after one hint (first attempt hard-coded the answer)
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
- `NameError` from a variable typo — fixed himself using "Did you mean"
- `TypeError` str + int; `str * int` silently repeats (`"16" * 2` → `"1616"`)
- Unsaved file in VS Code → old code runs
- Uncaught exception stops the program at that line (later lines never run)
- String vs int comparison (`"443" == 443` is False)
- Bad paste silently turning a test line into a comment — count output vs. tests
- Empty folders don't get committed (Git tracks files, not folders)

## Struggles / needs reps
- Python syntax details (colons, indentation, parentheses order)
- Skipping the "run it and show output" step — keep insisting on it
- Function def vs. call boundary (asked twice what belongs to `parse_port`); predicted a function would return `False` when it has no `return False` — teach "look at the return lines"
- Parsing vs validating (`int("99999")` succeeds) — got there with a trace
- Runs commands without checking `pwd` (created nested `01-network-config-analyzer/` folder)

## Pending cold retests
- Hard-coding vs computing from input: re-check in Block 2 that he derives values from variables, not typed answers
- Write `is_valid_port` from memory (skipped Oct 20 — Q4 code was written in an online compiler, never saved)
- `int(input(...))` and return-vs-print in a new context

## Next lesson
- Block 2: Strings (`strip`, `split`, `isdigit`, indexing, f-strings). Build `parse_ip` after Block 5.

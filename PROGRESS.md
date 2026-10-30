# Progress — Python Networking & Security Engineering

## Current phase & project
- **Phase 1** — Network Configuration Analyzer (`01-network-config-analyzer/`)
- **Approach changed (2026-10-25, at Jaylon's request):** teach the full building blocks first, one block at a time, each ending with an exercise he writes + a cold check; then assemble the analyzer. Blocks: 1 Values/types/variables → 2 Strings → 3 Conditions/logic → 4 Functions → 5 Exceptions → 6 Lists & for → 7 while loops → 8 Dicts → 9 Modules & objects → 10 `ipaddress` → 11 Program structure (`main`, `__name__`) → 12 pytest.
- **Current block:** Block 4 — Functions (not started). **Block 3 — Conditions passed 2026-10-30**: 3.1 `exercises/block3_conditions.py` + cold check `exercises/block3_check.py` (failed-login severity). Cold check: wrote a plan first (but skipped sending it for review; plan omitted the ALERT rule — that's where all bugs were). Parsing + severity chain correct first try. ALERT line needed 2 hints: `or "admin"` (non-empty string is truthy), `<=` vs `>=`, then `and`-before-`or` precedence → fixed with parentheses. Block 2 passed 2026-10-27, Block 1 passed 2026-10-25.
- Feature 1 (`parse_ip`) lesson covered (ipaddress basics, uncaught exception stops program, traceback bottom-up, `parse_port` try/except trace); `parse_ip` not yet written. `01-network-config-analyzer/analyzer.py` exists (empty, nested-folder mistake fixed).

## Last session
- 2026-10-30, machine: **Mac**

## How Jaylon wants to learn (mandatory, set 2026-10-25)
- Code first, not chat first: every concept → short explanation + example → an assignment he writes and runs in VS Code.
- Each assignment lists: Objective, File, Requirements, Relevant concepts, Expected behavior, Test cases, Completion criteria. Only use concepts already taught.
- Mentor creates each new exercise file (short header, no solution code).
- **Less scaffolding (agreed 2026-10-28, starting Block 3 cold check):** give only goal + expected output + test cases — no step breakdowns, no variable names, no "use X here". He writes a 3–5 line plain-English plan as comments first; mentor reviews the plan before he codes. Hints only when asked or after a real attempt, one level at a time.
- In chat: end every message with ONLY the current step's requirements at the very bottom (no scrolling up), in plain English.
- Review his real code/output/errors, then a modification task to prove understanding. Graduated hints; full solution only on request + follow-up task.

## Environment
- Mac: Python 3.13, Git, VS Code `code` command, Homebrew, `gh` (logged in), repo cloned at `~/python-infra-engineering`, `.venv` with pytest. Commit email = GitHub noreply.
- To check on Mac: VS Code Python extension installed; interpreter set to `.venv`.
- PC (Windows, PowerShell): Python 3.13, Git (`autocrlf true`, noreply email), repo cloned, `.venv` working, VS Code terminal (learned Ctrl+` on 2026-10-26). Pull/run confirmed 2026-10-27.

## Independent
- (none yet)

## Practicing
- Conditions: `if`/`elif`/`else`, nesting, `and`/`or`, comparisons, guard before `int()`; chains stop at first match → separate chain for a second decision; `else` is optional; parentheses when mixing `and`/`or` — passed Block 3 cold check with 2 hints
- Variables, reassignment (top-to-bottom execution), types (`str`/`int`/`float`/`bool`/`None`), `type()`, `int()` conversion — passed Block 1 cold check after one hint (first attempt hard-coded the answer)
- Guard-clause validation, `str.isdigit()`, `not`
- Strings: `.strip()`, `.lower()`, `.split()` → list, chained split (`"user=Admin".split("=")[1]`), indexing incl. `[-1]`, f-strings — passed Block 2 cold check (one guided hint for root cause)
- `return` vs `print` / `None`

## Learning
- `if` syntax (colon + indentation)
- `input()` returns `str`; `int(input(...))` nesting order (needed 2 hints — retest cold)
- `len()`, `str.endswith()`, dict add/replace with `d[key] = value`
- `ValueError` from `int("abc")`

## Strengths noticed
- Reads loops/dicts well; good security instincts (caught port 0 as invalid himself; chose strict rejection of `" 443"` deliberately).

## Bugs learned to diagnose
- `x == "a" or "b"` is always True (non-empty string is truthy) — each side of `or` must be a full comparison
- `and` binds before `or` → use parentheses
- Typo in output text (`priviliged`) — exact output matters (log searches)
- `IndexError` / `TypeError` from indexing a string (`address[1]` → one char) before `.split()`; `.split()` always returns a list
- Code that passes one test but breaks on other valid input (`/8` prefix; leading spaces shifting split indexes) — test multiple inputs
- Computed a cleaned value but kept using the raw one (`raw_strip` unused) — check every variable is actually used
- Dead code (`if x: True` does nothing) — read the whole file before calling it done
- `NameError` from a variable typo — fixed himself using "Did you mean"
- `TypeError` str + int; `str * int` silently repeats (`"16" * 2` → `"1616"`)
- Unsaved file in VS Code → old code runs
- Uncaught exception stops the program at that line (later lines never run)
- String vs int comparison (`"443" == 443` is False)
- Bad paste silently turning a test line into a comment — count output vs. tests
- Empty folders don't get committed (Git tracks files, not folders)

## Struggles / needs reps
- Boundary values (`<` vs `<=`) and not re-running ALL tests after a change (missed 0/70000/65535 cases)
- Python syntax details (colons, indentation, parentheses order)
- Skipping the "run it and show output" step — keep insisting on it
- Function def vs. call boundary (asked twice what belongs to `parse_port`); predicted a function would return `False` when it has no `return False` — teach "look at the return lines"
- Parsing vs validating (`int("99999")` succeeds) — got there with a trace
- Runs commands without checking `pwd` (created nested `01-network-config-analyzer/` folder)
- Test inputs: must use the EXACT test case text (kept old whitespace on TC2); skips the "predict first" step unless pushed
- Naming: mixed styles (`Usersplit`, `srctxt`) — push snake_case

## Pending cold retests
- Write `is_valid_port` from memory (skipped Oct 20 — Q4 code was written in an online compiler, never saved)
- `int(input(...))` and return-vs-print in a new context

## Next lesson
- Block 4: Functions (`def`, parameters, `return` vs `print`, calling, `None` when no return) — revisit the def-vs-call confusion and "look at the return lines". Then Block 5 (exceptions) → Feature 1 `parse_ip`. Remind him: send plan with "check plan" before coding.

# Curriculum — Python Networking & Security Engineering

Contents: Running a project · Phase 0 · Phase 1 · Phase 2 · Phase 3 · Phase 4 · Phase 5 · Phase 6

Pace by demonstrated ability. Use the 80/20 principle: prioritize the concepts that unlock the most real work. Standard library first; introduce a third-party package only when it gives a clear benefit, and say why.

## Running a project

Every milestone project follows this process:

1. Define the problem and who would use the tool.
2. Explain the technical concepts and requirements.
3. Break it into small features.
4. Name which Python concepts each feature teaches (teach those before he builds the feature).
5. Get a minimal working version first.
6. He implements features one at a time.
7. Test expected behavior and edge cases.
8. Debug failures systematically.
9. Refactor duplicated or confusing code.
10. Document the tool and its limitations.
11. README with setup (Mac **and** Windows commands), usage examples, sample output.
12. Review it as a hiring manager would review a junior engineer's portfolio piece.

Repo layout (one repo, one folder per milestone):

```
python-infra-engineering/
├── .gitignore          # .venv/, __pycache__/, .env, *.log, output/
├── .gitattributes      # * text=auto eol=lf
├── requirements.txt
├── README.md
├── exercises/          # small practice scripts by phase
├── 01-network-config-analyzer/
├── 02-network-diagnostic-toolkit/
├── 03-auth-log-analyzer/
└── 04-infra-health-monitor/
```

## Phase 0 — Assessment and environment

Assess (with practical questions/small exercises, not a long exam): variables and types; strings/numbers/booleans; input/output; conditionals; loops; lists, dicts, tuples, sets; functions and return values; modules/imports; exceptions; file operations; basic OOP; debugging and testing.

Setup on the current machine: Python 3.12+, VS Code + Python extension, venv, Git (name/email configured), GitHub repo, pytest. Then make sure the other machine can clone and run it (see cross-platform.md). Don't reteach what he can already demonstrate.

## Phase 1 — Fundamentals through networking

Order: variables/assignment → strings, ints, floats, bools → input/output, type conversion → operators/comparisons → conditionals → loops → lists, dicts, tuples, sets → functions, parameters, returns → scope and reuse → modules/imports → exceptions and input validation → file handling → JSON and CSV → basic debugging and testing (pytest).

Networking-flavored exercises: store hostnames + IPs; server inventory as dicts; validate TCP/UDP port numbers (0–65535, well-known vs registered vs ephemeral); loop over services; functions that classify ports; read inventory from CSV; export results to JSON.

**Milestone: Network Configuration Analyzer** (CLI)
- Accepts hostname, IP address, prefix length, gateway.
- Validates IP and subnet input.
- Uses `ipaddress` to compute network address, broadcast (IPv4), usable host range, host count.
- Checks the gateway is inside the subnet (and isn't the network/broadcast address).
- Handles invalid input gracefully (no tracebacks to the user).
- pytest tests for normal and edge cases: /31, /32, /0, IPv6, bad octets, gateway outside subnet.

Suggested feature order: (1) parse and validate one IP → (2) build a network from IP + prefix → (3) print network facts → (4) gateway check → (5) friendly error handling loop → (6) tests → (7) README.

## Phase 2 — Networking automation

Cover: IPv4/IPv6 handling; subnets/CIDR; DNS resolution (`socket.getaddrinfo`); TCP vs UDP; TCP connections with `socket`; ports and common services; timeouts; network error handling (`socket.timeout`, `ConnectionRefusedError`, `socket.gaierror`, `OSError`); HTTP requests and APIs (`urllib.request`, then `requests` when justified); `subprocess` basics; parsing OS command output (differs Mac vs Windows!); `logging`; structured results.

Map each to its layer: DNS = application-layer lookup; `connect()` = TCP three-way handshake at transport; HTTP GET = application. Draw the flow. Teach troubleshooting as hypothesis → test → interpret → narrow the failure domain.

**Milestone: Network Diagnostic Toolkit**
- Takes a hostname or IP; resolves DNS when applicable.
- Tests explicitly chosen TCP ports with sensible timeouts.
- Reports success and meaningful failure categories (DNS failure, refused, timed out, unreachable).
- Timestamps every result; exports CSV or JSON.
- Handles invalid targets and down services.
- Explains what each test does and doesn't prove: DNS resolution ≠ ICMP reachability ≠ TCP connectivity ≠ application health. A failed ping is not proof a host is down; an open port is not proof the app is healthy.
- Targets: only his own machines/lab, localhost, or explicitly permitted hosts.

## Phase 3 — Cybersecurity automation

Teach: reading/parsing logs; string processing and regex (`re`); timestamps and intervals (`datetime`); dicts and frequency counting (`collections.Counter`, `defaultdict`); file integrity hashing (`hashlib`); secure input handling; defensive programming; reporting; unit tests and fixtures (pytest fixtures, `tmp_path`); recognizing suspicious patterns without overstating evidence.

**Milestone: Authentication Log Analyzer**
- Reads a synthetic auth log (have him generate one, or use authorized defensive sample data).
- Extracts timestamp, username, source IP, outcome where present.
- Counts failures; configurable threshold and time window.
- Groups by source address and by account.
- JSON or CSV report.
- Skips/records malformed lines instead of crashing.
- Tests with synthetic data.
- States clearly that repeated failures are suspicious, not proof (typos, expired passwords, misconfigured services, NAT).
- Natural link: compare with what his Wazuh lab flags.

## Phase 4 — Infrastructure and IT ops automation

Teach: project structure and reusable modules; config files (JSON/TOML/YAML) and environment variables; logging and error reporting; automated testing; `argparse`; type hints and docstrings; OOP only where it genuinely helps; Git workflow (branches, meaningful commits); REST APIs; basic concurrency (`concurrent.futures`) and intro asyncio when warranted; secrets management (`.env`, never committed); dependency management.

Troubleshooting framing: tell physical/power vs OS vs DNS vs network connectivity vs service vs application problems apart, and which check distinguishes each.

**Milestone: Infrastructure Health Monitor**
- Loads authorized servers from a config file.
- DNS and selected TCP port checks; configurable timeouts.
- Records status, timestamps, error details.
- Human-readable summary + machine-readable report.
- Tracks failures across repeated runs (state file).
- Keeps connectivity results separate from application-health results.
- Unit tests (with mocking of sockets) and documentation.
- Pluggable design: adding a new check type shouldn't require rewriting the program (a check interface/registry).

## Phase 5 — Advanced infrastructure engineering

Only after he can build and explain Phases 1–4: clean architecture; advanced testing and mocking; API integrations; concurrency/async I/O; SQL and SQLite; Linux admin automation; cloud concepts and cloud APIs (with an authorized account); IaC fundamentals; CI/CD (GitHub Actions running his pytest suite on both `ubuntu-latest` and `windows-latest` is a great cross-platform lesson); containers; monitoring/metrics/alerting; secure coding; profiling.

Project ideas: Linux inventory and health reporting; cloud resource inventory; configuration compliance checker (ties to his NIST 800-53 hardening work); service availability monitoring; API-driven infrastructure reporting; deployment/config validation.

## Phase 6 — Toward infrastructure software engineering and AI

After a solid foundation: maintainable design; practical data structures and algorithms; distributed systems basics; event-driven automation; cloud-native services; AI API integration; AI for log classification and ops reporting; evaluating AI output and handling uncertainty; securing AI applications. The goal is understanding the infrastructure beneath software and AI, not just calling an API.

# Roadmap — Detection Engineering Portfolio

Execution plan for the portfolio in [`README.md`](./README.md). Runs the acts in order, one shippable GitHub artifact per week.

**Design assumption:** ~10–12 focused hours/week around work. More time → weeks compress; less → they stretch.

**The one rule:** every week ends with something on GitHub. If a week slips, cut scope *inside* the week — never skip the artifact. A smaller shipped thing beats a bigger unshipped one.

---

## Foundation — already shipped

- [x] Active Directory lab (`jaylonlab.local`) — DC, OUs, GPOs, users
- [x] Wazuh SIEM lab — Sysmon + Suricata ingestion, dashboards, triage, active response
- [x] Security+ certification

---

## Phase A — Land Network+ (Weeks 1–2)

### Week 1 — Close the gaps
- [ ] Drill Dion weak domain: Networking Concepts (was 52%)
- [ ] Drill Dion weak domain: Troubleshooting (was 59%)
- [ ] Python warmup (~1 hr): `json`, reading files, `collections.Counter`
- [ ] **Checkpoint:** Dion practice consistently low 80s

### Week 2 — Confirm and sit it
- [ ] Full Dion practice exams — clear 80%+ two attempts running
- [ ] Schedule Network+ (N10-009)
- [ ] **SHIP:** Pass Network+ (target ~Aug 8–14)

---

## Phase B — The detection build (Weeks 3–9)

CySA+ study starts here as background reading, ~2–3 hrs/week, one domain at a time.

### Week 3 — Act 2: Honeypot telemetry
- [ ] Deploy Cowrie honeypot
- [ ] Integrate Cowrie into Wazuh — confirm ingestion
- [ ] **Python #1:** Cowrie log parser (stdlib) — top IPs, creds, commands, charted
- [ ] CySA+ background reading (domain 1)
- [ ] **SHIP:** Honeypot writeup + parser script

### Week 4 — Act 2→3 bridge: API + ATT&CK grounding
- [ ] **Python #2:** Wazuh API alert puller (`requests` — auth, JSON, pagination)
- [ ] Learn MITRE ATT&CK structure
- [ ] Pick 5–8 techniques the lab can see (e.g. T1110 brute force, T1059 command execution)
- [ ] Map existing Wazuh detections to ATT&CK
- [ ] CySA+ background reading (domain 2)
- [ ] **SHIP:** ATT&CK coverage matrix (current detections) + puller script

### Week 5 — Act 3: Emulation + first Sigma rules
- [ ] Install Atomic Red Team
- [ ] Safely run 2–3 atomics for chosen techniques; confirm they land in Wazuh
- [ ] Write first Sigma rules for those techniques
- [ ] Learn `pySigma` / `sigma-cli`; convert Sigma → Wazuh
- [ ] CySA+ background reading (domain 3)
- [ ] **SHIP:** 2–3 Sigma rules + conversion notes + detection screenshots

### Week 6 — Act 3: The standout artifact
- [ ] **Python #3:** Detection-validation harness — run Atomic technique → query Wazuh API → confirm alert fired → coverage report (technique → rule → pass/fail)
- [ ] Write a full README for the harness (this is the differentiator project)
- [ ] CySA+ background reading (domain 4)
- [ ] **SHIP:** Harness + generated coverage report

### Week 7 — Act 3 capstone: SigmaHQ contribution
- [ ] Study SigmaHQ CONTRIBUTING guide + rule standards
- [ ] Find a real gap or improvement
- [ ] Write a rule to their spec + test it
- [ ] Submit the PR (a quality PR is the win — merge timing is out of your hands)
- [ ] **SHIP:** PR link, referenced from the portfolio

### Week 8 — Act 4: Detection-as-Code
- [ ] Put Sigma rules in a structured Git repo
- [ ] Set up GitHub Actions CI
- [ ] **Python #4:** `pytest` detection unit tests — load rule + sample log, assert it fires
- [ ] Wire the tests into the Action
- [ ] CySA+ background reading (remaining domains)
- [ ] **SHIP:** Detection-as-code repo with green CI badge

### Week 9 — Act 4: Automation + IR
- [ ] **Python #5:** SOAR-lite triage script — poll alerts, enrich IPs (AbuseIPDB), score/dedupe, post daily summary to webhook/markdown
- [ ] Write one IR playbook (brute-force scenario first)
- [ ] Run a solo tabletop against it; document it
- [ ] **SHIP:** Automation script + IR playbook doc

---

## Phase C — Cert + reps + next track (Week 10+)

### Week 10 — Sit CySA+
- [ ] Schedule CySA+ (CS0-003)
- [ ] **SHIP:** Pass CySA+

### Ongoing reps (slot into lighter weeks)
- [ ] Phishing `.eml` parser (`email` + `re`) — Received chain, SPF/DKIM/DMARC, defanged URLs
- [ ] PCAP / C2 carver (`scapy` / `pyshark`) off malware-traffic-analysis.net exercises

### Next track (pick one after CySA+)
- [ ] AWS Cloud Practitioner + Prowler/CSPM writeup — *the cloud chapter*, **or**
- [ ] CCNA + open the parked networking backlog — *the networking chapter*

---

## Trackers

### Certifications
- [x] Security+ — earned
- [ ] Network+ (N10-009) — Phase A
- [ ] CySA+ (CS0-003) — Week 10
- [ ] AWS Cloud Practitioner *or* CCNA — post-CySA+
- [ ] Later horizon: PenTest+ → AWS Solutions Architect → AWS Security Specialty

### Python / scripting ladder
- [ ] #1 stdlib parsing — Cowrie logs (Week 3)
- [ ] #2 HTTP + APIs — Wazuh API puller (Week 4)
- [ ] #3 domain libraries — validation harness, `pySigma` (Weeks 5–6)
- [ ] #4 testing — `pytest` detection tests (Week 8)
- [ ] #5 automation — triage/enrichment service (Week 9)

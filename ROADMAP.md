# Roadmap — Infrastructure-Minded Software Engineer

**Where I'm headed.** `PROGRESS.md` says where I am right now; this file says where it all leads and how the pieces connect.
Detailed lesson plans for Phases 0–6 live in `.claude/skills/python-infra-mentor/references/curriculum.md`.

## Rules

1. **Two active tracks, maximum.** This repo is the main track. Network Wiz is the secondary track. Everything else is either a target environment or comes later.
2. **A stage is done when its milestone works and I pass a cold check.** Finishing a tutorial or reading docs doesn't count.
3. **One tracker.** `PROGRESS.md` is authoritative on both machines (Mac and PC). Pull before you start, and commit before you switch machines.
4. **From Stage 3 on, one system grows.** I don't start a new project each stage; I keep evolving the same app.

## Stage map

| Stage | What covers it | Milestone (proof) |
|---|---|---|
| **1. Programming foundations** | Repo Phase 1 — Blocks 1–12 | Network Configuration Analyzer |
| **2. Networking & systems** | Network Wiz (concepts) + Repo Phase 2 (automation) + Linux thread | Network Diagnostic Toolkit |
| *Security bridge* | Repo Phase 3, run against my Wazuh / AD lab logs | Authentication Log Analyzer |
| **3. Software engineering** | Repo Phase 4 + additions below | Infrastructure Health Monitor → API version |
| **4. Cloud (AWS)** | Repo Phase 5 (cloud) + additions below | Health Monitor API running on AWS |
| **5. DevOps & automation** | Repo Phase 5 (IaC, CI/CD, containers) + additions below | Same app: Docker + GitHub Actions + Terraform |
| **6. AI & advanced security** | Repo Phase 6 + FDE track capstones | AI-assisted security monitoring, secured |

## The system that grows (Stages 3–6)

```
Infrastructure Health Monitor (CLI, Phase 4)
  └─► + FastAPI + PostgreSQL + auth            Stage 3: a real application
        └─► deployed on AWS: VPC, EC2, RDS       Stage 4: runs in the cloud
              └─► Docker + GitHub Actions + Terraform   Stage 5: automated
                    └─► AI log triage, prompt-injection defenses   Stage 6: intelligent + secure
```

This covers project ideas 3, 5, 6, 7, 8, 9 and 10 in a single portfolio story.

## Additions the repo curriculum doesn't cover yet

### Stage 2 — Linux thread (light, runs alongside Phase 2, uses my Ubuntu VMs)
- Filesystem, permissions (`chmod`, `chown`, users/groups)
- Processes and services (`ps`, `systemctl`, `journalctl`)
- Logs (`/var/log`, `auth.log`), SSH and keys
- Bash basics, enough to read and write small scripts
- **Proof:** set up a service on an Ubuntu VM, harden SSH, and troubleshoot a broken service from its logs

### Stage 3 — Software engineering
- HTTP in depth (methods, status codes, headers, HTTPS/TLS), REST design
- SQL fundamentals → PostgreSQL (schemas, joins, migrations)
- FastAPI: routes, validation (Pydantic), dependency injection
- Authentication and authorization (password hashing, tokens, roles)
- Unit tests vs. integration tests (pytest against a test database)
- Secure coding: input validation, SQL injection, secrets handling
- **Proof:** the Health Monitor exposes a REST API backed by PostgreSQL, with auth and tests

### Stage 4 — AWS
- IAM first (least privilege, no root use, MFA); a billing budget alarm before anything else
- VPC, subnets (public/private), route tables, internet and NAT gateways, security groups
- EC2, S3, RDS, a load balancer, CloudWatch logs and alarms
- High availability vs. cost tradeoffs
- **Proof:** the API runs in a private subnet behind a load balancer, uses RDS, and has logs/alarms. I can draw and explain the network path.

### Stage 5 — DevOps
- Docker and docker-compose (app + database)
- GitHub Actions: tests on `ubuntu-latest` and `windows-latest`, then a build
- Terraform: rebuild the Stage 4 environment from code, then destroy and recreate it
- Monitoring/logging as code; Kubernetes fundamentals **last** (concepts + a local cluster only)
- **Proof:** a push to `main` runs tests, builds the image and deploys; the whole environment comes up from `terraform apply`

### Stage 6 — AI & advanced security
- How LLMs work (tokens, context, limits); calling an AI API from Python
- Embeddings, vector databases, RAG; evaluating output quality
- AI security: prompt injection, data leakage, output handling, least-privilege tools
- **Proof:** the monitor classifies/summarizes incidents with AI, evaluation results are documented, and it is tested against injection attempts
- Then: the FDE capstones (Secure Federal Document Intelligence Assistant, Security Operations AI Assistant)

## Where everything else fits

| Thing | Role |
|---|---|
| Network Wiz | Secondary track, feeds Stage 2. Its concepts get coded in Repo Phase 2. |
| AD + Wazuh enterprise lab | Target environment: log source for Phase 3, monitor targets for Phase 4, compliance-checker targets for Phase 5 |
| FDE track | Stage 6. Capstones wait until Stage 3 is done. |
| python-foundations course | Retired (replaced by this repo) |
| Cyber job search (Path A) | Runs in parallel. Each milestone goes on the resume once demonstrated. |

## Rough timeline (estimate, not a deadline)
- Stage 1: finishes about mid-to-late Dec 2026
- Full roadmap: about 18–24 months part-time; adjust based on actual pace

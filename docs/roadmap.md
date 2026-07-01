# Project Roadmap

> **Rule:** Complete each milestone fully before moving to the next. Commit, PR, and get a review (even self-review) at each step.

## Phase 0 — Foundation & Planning ✅ ← YOU ARE HERE

| # | Milestone | Status |
|---|-----------|--------|
| 0.1 | High-level architecture & system design | ✅ |
| 0.2 | Project roadmap | ✅ |
| 0.3 | Repository folder structure | ✅ |
| 0.4 | Git init + GitHub repo + branch protection mindset | 🔲 |
| 0.5 | Development environment verification | 🔲 |

---

## Phase 1 — Backend Core (No Auth Yet)

| # | Milestone | Key Concepts |
|---|-----------|--------------|
| 1.1 | FastAPI project scaffold, config, logging | 12-factor app, env vars, structured logging |
| 1.2 | PostgreSQL schema + SQLAlchemy models | Migrations, connection pooling |
| 1.3 | `POST /api/v1/urls` — create short URL | REST design, validation, error handling |
| 1.4 | `GET /{alias}` — redirect endpoint | HTTP 301 vs 302, hot path design |
| 1.5 | Health & readiness endpoints | `/health`, `/ready` — K8s probes |
| 1.6 | Unit & integration tests | pytest, Testcontainers or docker-compose test DB |
| 1.7 | Dockerfile + docker-compose (backend + postgres) | Multi-stage builds, .dockerignore |

---

## Phase 2 — Frontend & Full-Stack Local Dev

| # | Milestone | Key Concepts |
|---|-----------|--------------|
| 2.1 | React scaffold (Vite), routing, API client | SPA architecture, env-based API URL |
| 2.2 | URL shortening form + result display | Form validation, error UX |
| 2.3 | docker-compose full stack (frontend + backend + db) | Service networking, depends_on, healthchecks |
| 2.4 | CORS, API versioning | Cross-origin security |

---

## Phase 3 — Authentication & Authorization

| # | Milestone | Key Concepts |
|---|-----------|--------------|
| 3.1 | User registration & login | Password hashing (bcrypt/argon2) |
| 3.2 | JWT access + refresh tokens | Stateless auth, token expiry |
| 3.3 | Protected routes (backend + frontend) | Middleware, RBAC basics |
| 3.4 | User dashboard — my URLs | Multi-tenancy, row-level ownership |

---

## Phase 4 — Advanced Features

| # | Milestone | Key Concepts |
|---|-----------|--------------|
| 4.1 | Custom aliases | Uniqueness constraints, reserved words |
| 4.2 | URL expiration | TTL in DB + Redis, cron/background cleanup |
| 4.3 | Click analytics & tracking | Async writes, aggregation queries |
| 4.4 | QR code generation | Binary responses, caching |
| 4.5 | Redis caching layer | Cache-aside pattern, invalidation |
| 4.6 | Rate limiting | Token bucket / sliding window in Redis |
| 4.7 | Admin dashboard | Role-based access, audit considerations |

---

## Phase 5 — Observability

| # | Milestone | Key Concepts |
|---|-----------|--------------|
| 5.1 | Prometheus metrics endpoint | RED metrics, custom business metrics |
| 5.2 | Structured JSON logging | Correlation IDs, log levels |
| 5.3 | Loki + Promtail in docker-compose | Log labels, LogQL basics |
| 5.4 | Grafana dashboards | Golden signals, alerting rules |

---

## Phase 6 — CI/CD

| # | Milestone | Key Concepts |
|---|-----------|--------------|
| 6.1 | GitHub Actions: lint + test on PR | Branch protection, required checks |
| 6.2 | Build & push Docker images to ECR | Image tagging, layer caching |
| 6.3 | Terraform: AWS VPC, EKS, RDS, ElastiCache | State management, modules |
| 6.4 | Helm charts for all services | Values files, secrets via external-secrets |
| 6.5 | Deploy to EKS via GitHub Actions | OIDC auth to AWS, environment promotion |
| 6.6 | Route 53 + TLS (cert-manager) | DNS, Let's Encrypt |

---

## Phase 7 — Production Hardening

| # | Milestone | Key Concepts |
|---|-----------|--------------|
| 7.1 | Secrets management (AWS Secrets Manager) | Never commit secrets |
| 7.2 | HPA, resource limits, PDBs | K8s scaling & resilience |
| 7.3 | Network policies | Zero-trust within cluster |
| 7.4 | Backup & restore (RDS snapshots) | RPO/RTO |
| 7.5 | Runbooks & troubleshooting guide | On-call readiness |
| 7.6 | Architecture diagrams + deployment guide | Portfolio documentation |

---

## Estimated Timeline (Self-Paced)

| Phase | Duration (approx.) |
|-------|-------------------|
| Phase 0 | 1 session |
| Phase 1 | 2–3 weeks |
| Phase 2 | 1–2 weeks |
| Phase 3 | 1–2 weeks |
| Phase 4 | 2–3 weeks |
| Phase 5 | 1 week |
| Phase 6 | 2–3 weeks |
| Phase 7 | 1–2 weeks |

**Total: ~3–4 months** at a steady pace (5–10 hrs/week).

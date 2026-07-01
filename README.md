# LinkForge — Production URL Shortener Platform

A production-grade URL shortener built incrementally as a DevOps/SRE learning portfolio project.

**Stack:** React · FastAPI · PostgreSQL · Redis · Docker · Kubernetes · Terraform · AWS · Prometheus · Grafana · Loki

## Status

🚧 **Phase 0 — Planning & Foundation** (in progress)

## Documentation

| Document | Description |
|----------|-------------|
| [Architecture](docs/architecture.md) | System design, data flow, and deployment topology |
| [Roadmap](docs/roadmap.md) | Milestone-by-milestone build plan |
| [Development Setup](docs/development-setup.md) | Local toolchain and environment guide |

## Repository Structure

```
linkforge/
├── backend/          # FastAPI application
├── frontend/         # React application
├── infra/            # Terraform (AWS infrastructure)
├── k8s/              # Kubernetes manifests
├── helm/             # Helm charts
├── monitoring/       # Prometheus, Grafana, Loki configs
├── .github/          # GitHub Actions CI/CD
└── docs/             # Architecture, runbooks, guides
```

## License

MIT (update before publishing)

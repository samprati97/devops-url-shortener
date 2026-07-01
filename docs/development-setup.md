# Development Environment Setup

## Required Tools

| Tool | Purpose | Your Status | Install |
|------|---------|-------------|---------|
| Git | Version control | ✅ 2.50.1 | Pre-installed on macOS |
| Python 3.11+ | FastAPI backend | ✅ 3.13.2 | [python.org](https://python.org) |
| Node.js 20+ | React frontend | ✅ 22.16.0 | [nodejs.org](https://nodejs.org) |
| Docker Desktop | Containers locally | ✅ 29.1.2 | [docker.com](https://docker.com) |
| Terraform | Infrastructure as Code | ✅ 1.10.4 | [terraform.io](https://terraform.io) |
| kubectl | Kubernetes CLI | ✅ 1.35.0 | `brew install kubectl` |
| Helm | K8s package manager | ❌ Missing | `brew install helm` |
| GitHub CLI (`gh`) | PRs, repo management | ❌ Missing | `brew install gh` |
| AWS CLI v2 | AWS interaction | Check below | `brew install awscli` |

## Install Missing Tools

```bash
# Helm
brew install helm

# GitHub CLI (then authenticate)
brew install gh
gh auth login

# AWS CLI
brew install awscli
aws configure   # uses IAM access keys initially; we'll move to SSO/OIDC later
```

## Verify Everything

Run this checklist before starting Phase 1:

```bash
git --version
python3 --version
node --version
docker --version
docker compose version
terraform --version
kubectl version --client
helm version
gh --version
aws --version
```

## Recommended VS Code / Cursor Extensions

- Python (Microsoft)
- Pylance
- Ruff
- ESLint + Prettier
- Docker
- Terraform
- Kubernetes
- YAML
- GitLens

## Environment Variables Strategy

We follow the **12-Factor App** methodology:

- **Local dev:** `.env` files (gitignored)
- **CI:** GitHub Actions secrets
- **Production:** AWS Secrets Manager → injected into K8s via External Secrets Operator

Never commit `.env`. Always commit `.env.example` with placeholder values.

## Git Workflow (GitHub Flow)

```
main (protected)
  └── feature/milestone-1.1-fastapi-scaffold
        └── commits → PR → review → merge
```

### Branch Naming Convention

```
feature/<milestone>-<short-description>
fix/<issue>-<short-description>
docs/<what>
infra/<what>
```

Examples:
- `feature/1.1-fastapi-scaffold`
- `infra/6.3-terraform-vpc`

### Commit Message Format

```
<type>(<scope>): <subject>

<body optional>
```

Types: `feat`, `fix`, `docs`, `infra`, `ci`, `test`, `chore`

Example:
```
feat(backend): add URL creation endpoint

Implement POST /api/v1/urls with Pydantic validation
and PostgreSQL persistence.
```

## Next Steps After Phase 0

1. Confirm all tools installed
2. Create GitHub repository
3. Push initial commit
4. Begin Milestone 1.1 — FastAPI scaffold

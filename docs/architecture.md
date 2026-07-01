# Architecture

## Overview

LinkForge is a URL shortener designed to demonstrate production DevOps practices — not just a CRUD app with Docker slapped on top.

## High-Level System Architecture

```mermaid
flowchart TB
    subgraph Users
        U[Browser / Mobile / API Client]
    end

    subgraph Edge["Edge Layer (Production)"]
        DNS[Route 53 DNS]
        ALB[AWS Application Load Balancer]
        ING[NGINX Ingress Controller]
    end

    subgraph App["Application Layer (Kubernetes)"]
        FE[React Frontend]
        BE[FastAPI Backend]
    end

    subgraph Data["Data Layer"]
        PG[(PostgreSQL)]
        RD[(Redis Cache)]
    end

    subgraph Observability["Observability Stack"]
        PROM[Prometheus]
        GRAF[Grafana]
        LOKI[Loki]
        PT[Promtail]
    end

    U --> DNS --> ALB --> ING
    ING --> FE
    ING --> BE
    BE --> PG
    BE --> RD
    BE --> PROM
    PT --> LOKI
    PROM --> GRAF
    LOKI --> GRAF
```

## Request Flow — URL Redirect (Hot Path)

This is the most performance-critical path. In production, **99%+ of traffic** is redirects, not dashboard visits.

```mermaid
sequenceDiagram
    participant User
    participant Ingress as NGINX Ingress
    participant API as FastAPI
    participant Redis
    participant DB as PostgreSQL

    User->>Ingress: GET /abc123
    Ingress->>API: Forward request
    API->>Redis: GET shortcode:abc123

    alt Cache Hit
        Redis-->>API: { url, expires_at }
        API-->>User: 302 Redirect
    else Cache Miss
        Redis-->>API: null
        API->>DB: SELECT original_url WHERE alias = abc123
        DB-->>API: Row data
        API->>Redis: SET shortcode:abc123 (TTL)
        API-->>User: 302 Redirect
    end
```

## Request Flow — Create Short URL (Authenticated)

```mermaid
sequenceDiagram
    participant User
    participant FE as React Frontend
    participant API as FastAPI
    participant DB as PostgreSQL
    participant Redis

    User->>FE: Submit long URL + optional alias
    FE->>API: POST /api/v1/urls (JWT)
    API->>API: Validate input + rate limit
    API->>DB: INSERT url record
    DB-->>API: Created row
    API->>Redis: Warm cache (optional)
    API-->>FE: { short_url, alias, qr_code_url }
    FE-->>User: Display result
```

## Deployment Topology (Target Production State)

```mermaid
flowchart LR
    subgraph AWS["AWS Account"]
        subgraph VPC["VPC"]
            subgraph Public["Public Subnets"]
                ALB2[ALB]
                NAT[NAT Gateway]
            end
            subgraph Private["Private Subnets"]
                EKS[EKS Cluster]
                RDS[(RDS PostgreSQL)]
                EC[(ElastiCache Redis)]
            end
        end
        R53[Route 53]
        ECR[ECR Container Registry]
        SM[Secrets Manager]
    end

    subgraph CI["GitHub Actions"]
        BUILD[Build & Test]
        PUSH[Push to ECR]
        DEPLOY[Helm Deploy to EKS]
    end

    R53 --> ALB2 --> EKS
    EKS --> RDS
    EKS --> EC
    EKS --> SM
    BUILD --> PUSH --> ECR --> DEPLOY --> EKS
```

## Component Responsibilities

| Component | Role | Why Separate |
|-----------|------|--------------|
| **React Frontend** | User dashboard, admin UI, auth flows | Decouples UI release cycle from API |
| **FastAPI Backend** | Business logic, auth, redirects, analytics | Stateless — scales horizontally in K8s |
| **PostgreSQL** | Source of truth for users, URLs, clicks | ACID transactions, relational queries |
| **Redis** | Cache hot redirects, rate limiting, sessions | Sub-millisecond reads for redirect path |
| **NGINX Ingress** | TLS termination, routing, rate limits | Industry standard K8s ingress |
| **Prometheus** | Metrics collection | Pull-based, K8s-native monitoring |
| **Grafana** | Dashboards and alerting UI | Unified observability view |
| **Loki + Promtail** | Log aggregation | Lightweight, label-based log indexing |
| **Terraform** | AWS infrastructure as code | Reproducible, reviewable infra changes |
| **Helm** | K8s package management | Templated, versioned deployments |
| **GitHub Actions** | CI/CD pipeline | Integrated with PR workflow |

## Security Layers

```mermaid
flowchart TB
    L1[Network: VPC, Security Groups, Private Subnets]
    L2[Edge: TLS 1.3, WAF optional]
    L3[Ingress: Rate limiting, IP allowlists for admin]
    L4[App: JWT auth, input validation, CORS]
    L5[Data: Encrypted at rest, Secrets Manager]
    L6[Ops: Least-privilege IAM, audit logs]

    L1 --> L2 --> L3 --> L4 --> L5 --> L6
```

## Design Principles

1. **Stateless backend** — Any pod can handle any request. Enables horizontal scaling.
2. **Cache-first redirects** — Redis before PostgreSQL on the hot path.
3. **Infrastructure as Code** — Every AWS resource defined in Terraform.
4. **GitOps-ready** — All K8s config in Git, deployed via CI/CD.
5. **Observable by default** — Metrics, logs, and health checks from day one.
6. **Secure by default** — Secrets never in code; private subnets for data tier.

## Alternatives Considered

| Decision | Our Choice | Alternative | Why We Chose Ours |
|----------|-----------|-------------|-------------------|
| Backend framework | FastAPI | Django, Flask | Async-native, auto OpenAPI docs, modern Python |
| Database | PostgreSQL | MongoDB, DynamoDB | Relational model fits users ↔ URLs; RDS is battle-tested |
| Cache | Redis | Memcached | Data structures for rate limiting + TTL + pub/sub |
| Orchestration | Kubernetes (EKS) | ECS, plain EC2 | Industry demand, portable skills, Helm ecosystem |
| IaC | Terraform | CloudFormation, Pulumi | Multi-cloud, huge community, interview staple |
| CI/CD | GitHub Actions | Jenkins, GitLab CI | Native GitHub integration, zero infra to maintain |
| Ingress | NGINX Ingress | Traefik, ALB Ingress | Most common in production K8s clusters |

## Scalability Notes

| Bottleneck | Mitigation |
|------------|------------|
| Redirect latency | Redis cache, connection pooling, CDN for static assets |
| Database writes | Async click tracking (future: queue → batch insert) |
| API pods | HPA on CPU/request rate |
| Single-region failure | Multi-AZ RDS/ElastiCache (Phase 2+); multi-region is advanced |

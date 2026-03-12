# Contributing to FarmForce AI

## Getting Started

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Make your changes
4. Commit: `git commit -m "feat: add my feature"`
5. Push: `git push origin feature/my-feature`
6. Open a Pull Request

## Branch Naming

- `feature/*` — New features
- `bugfix/*` — Bug fixes
- `hotfix/*` — Critical production fixes

## Commit Message Format

```
type(scope): short description

Types: feat | fix | docs | style | refactor | test | chore
```

Examples:
- `feat(jobs): add voice job posting`
- `fix(payments): handle Razorpay signature verification`
- `docs(api): update OpenAPI spec`

## Code Style

### Python (Backend)
- Use `ruff` for linting: `ruff check backend/`
- Follow PEP 8
- Type hints required on all functions
- Async functions for all I/O operations

### Dart (Mobile)
- Use `flutter_lints`
- Run `flutter analyze` before committing
- Use `const` constructors where possible

### JavaScript/React (Admin)
- ESLint + Prettier
- Functional components only
- PropTypes or TypeScript for type safety

## PR Review Checklist

- [ ] Tests pass (`pytest` or `flutter test`)
- [ ] Linting passes
- [ ] No hardcoded secrets or credentials
- [ ] API changes are documented in `docs/API_SPEC.md`
- [ ] Database changes have migration files
- [ ] New environment variables added to `.env.example`

## Development Setup

```bash
# Backend
cd backend && pip install -r requirements.txt
cp .env.example .env

# Mobile
cd mobile && flutter pub get

# Admin
cd admin && npm install
```

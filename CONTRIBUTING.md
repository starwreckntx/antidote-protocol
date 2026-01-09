# Contributing to Antidote Protocol

Thank you for your interest in contributing to the Antidote Protocol! This document provides guidelines for contributions to ensure quality, security, and alignment with project goals.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Workflow](#development-workflow)
- [IRP Governance Compliance](#irp-governance-compliance)
- [Contribution Types](#contribution-types)
- [Review Process](#review-process)
- [Recognition](#recognition)

## Code of Conduct

### Core Principles

The Antidote Protocol follows **IRP v1.5 HYBRID Four Laws**:

1. **CONSENT**: Confirm before changing intent - Respect established design decisions, propose changes transparently
2. **INVITATION**: Act when addressed - Contribute within scope, don't impose unrelated features
3. **INTEGRITY**: Preserve context - Maintain documentation, honor semantic versioning, preserve research artifacts
4. **GROWTH**: Incremental changes only - Small, testable improvements over large rewrites

### Expected Behavior

- ✅ Respectful communication with maintainers and contributors
- ✅ Constructive feedback on code, documentation, and ideas
- ✅ Credit original authors and prior work
- ✅ Transparent about AI assistance in contributions (see [AI Collaboration](#ai-collaboration))
- ✅ Focus on problem-solving, not ego

### Unacceptable Behavior

- ❌ Harassment, discrimination, or personal attacks
- ❌ Undisclosed conflicts of interest
- ❌ Claiming AI-generated work as solely human-authored
- ❌ Bypassing review process or pushing directly to main
- ❌ Introducing dependencies without justification

## How Can I Contribute?

### Reporting Bugs

**Before submitting**:
1. Check existing issues for duplicates
2. Verify bug exists in latest version (v1.1.0)
3. Test with minimal reproduction case

**Bug Report Template**:
```markdown
**Description**: Clear description of the bug

**Expected Behavior**: What should happen

**Actual Behavior**: What actually happens

**Reproduction Steps**:
1. Step 1
2. Step 2
3. ...

**Environment**:
- Antidote Protocol Version: v1.1.0
- Platform: Kimi K2 / Claude / Gemini / Other
- Implementation: Python / JavaScript / Other

**Additional Context**: Logs, screenshots, etc.
```

### Suggesting Enhancements

**Feature Request Template**:
```markdown
**Problem Statement**: What problem does this solve?

**Proposed Solution**: How should it work?

**Alternatives Considered**: What other approaches did you evaluate?

**IRP Compliance**:
- Does this respect the Four Laws (CONSENT, INVITATION, INTEGRITY, GROWTH)?
- Semantic versioning impact: MAJOR / MINOR / PATCH

**Case File Relevance**: Does this relate to existing Case Files (CF-1 through CF-8)?

**Cross-Model Validation**: Have you tested on multiple platforms?
```

### Proposing New Case Files

**Case File Proposal Template**:
```markdown
**CF-X: [Name]**

**Severity**: CRITICAL / HIGH / MEDIUM / LOW

**Threat Description**: What attack does this detect?

**Detection Pattern**:
```python
# Pseudocode or regex
```

**Response Protocol**: HALT / REFUSE / Re-Ground / Other

**Validation Evidence**:
- Tested on: [Platforms]
- Detection rate: X%
- False positive rate: X%

**Emergent vs. Designed**: Was this discovered during testing or pre-planned?

**References**: Related research, attack examples
```

## Development Workflow

### 1. Fork & Clone

```bash
# Fork via GitHub UI first
git clone https://github.com/YOUR_USERNAME/antidote-protocol.git
cd antidote-protocol
git remote add upstream https://github.com/starwrecktx/antidote-protocol.git
```

### 2. Create Feature Branch

```bash
# Use descriptive branch names
git checkout -b feature/cf-9-arbiter-authority
git checkout -b fix/cf-5-regex-edge-case
git checkout -b docs/integration-guide-flask
```

**Branch Naming**:
- `feature/`: New Case Files, architectural additions
- `fix/`: Bug fixes, detection pattern corrections
- `docs/`: Documentation improvements
- `test/`: Test suite additions
- `refactor/`: Code improvements without behavior change

### 3. Make Changes

**Code Quality Standards**:

**Python**:
```bash
# Style: Black + isort
black antidote_protocol/
isort antidote_protocol/

# Type checking: mypy
mypy antidote_protocol/

# Linting: flake8
flake8 antidote_protocol/

# Tests: pytest
pytest tests/ --cov=antidote_protocol
```

**JavaScript/TypeScript**:
```bash
# Style: Prettier + ESLint
npm run format
npm run lint

# Type checking: TypeScript
npm run type-check

# Tests: Jest
npm test -- --coverage
```

### 4. Commit Messages

Follow **Conventional Commits**:

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types**:
- `feat`: New feature (MINOR version)
- `fix`: Bug fix (PATCH version)
- `docs`: Documentation only
- `test`: Test additions/fixes
- `refactor`: Code refactor (no behavior change)
- `perf`: Performance improvement
- `chore`: Maintenance (dependencies, tooling)
- `BREAKING CHANGE`: API breaking change (MAJOR version)

**Examples**:
```bash
git commit -m "feat(cf-9): Add Arbiter Authority binding HALT enforcement

Implements CF-9 to enforce HALT commands when ignored by primary system.
Includes router rate-limiting (max 3 parallel calls) and tool call queue.

Closes #42"

git commit -m "fix(cf-5): Correct regex edge case in authority hijacking detection

Fixes false positive when user says 'Joseph said hello' (benign statement).
Now requires command verb + indirect instruction pattern.

Fixes #38"

git commit -m "docs(readme): Update installation instructions for Python 3.12

Adds troubleshooting for pip install on Python 3.12+.
Clarifies virtual environment recommendation."
```

### 5. Push & Pull Request

```bash
# Push to your fork
git push origin feature/cf-9-arbiter-authority

# Create PR via GitHub UI
```

**Pull Request Template**:
```markdown
## Description
Clear description of changes

## Motivation
Why is this change necessary?

## Changes Made
- Item 1
- Item 2

## Testing
- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] Cross-model validation (Kimi / Claude / Gemini)
- [ ] Documentation updated

## IRP Compliance
- [ ] Follows Four Laws (CONSENT, INVITATION, INTEGRITY, GROWTH)
- [ ] Semantic versioning impact documented
- [ ] Backward compatibility preserved (or BREAKING CHANGE noted)

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex logic
- [ ] Documentation updated
- [ ] Tests added/updated
- [ ] No new warnings introduced
- [ ] Commit messages follow Conventional Commits

## Related Issues
Closes #XX
Relates to #YY
```

## IRP Governance Compliance

### Four Laws in Practice

**CONSENT (Confirm before changing intent)**:
- Breaking changes require RFC (Request for Comments) issue first
- Wait 7 days for community feedback before merging MAJOR changes
- Document migration path for API changes

**INVITATION (Act when addressed)**:
- Contributions should address existing issues or documented roadmap
- Unsolicited large refactors discouraged (open discussion issue first)
- Stay within scope of existing architecture

**INTEGRITY (Preserve context)**:
- Update CHANGELOG.md with every user-facing change
- Preserve research artifacts (emergent innovations documented)
- Maintain documentation accuracy (code + docs in same PR)

**GROWTH (Incremental changes only)**:
- Prefer small, focused PRs over large omnibus changes
- One Case File per PR (not 3 Case Files in one PR)
- Refactors separate from feature additions

### Semantic Versioning

**MAJOR (v1.x.x → v2.0.0)**:
- Breaking API changes
- Case File removal
- Fundamental architecture changes
- **Requires**: RFC + 7-day discussion + maintainer approval

**MINOR (v1.1.x → v1.2.0)**:
- New Case File additions
- New features (backward-compatible)
- New integration patterns
- **Requires**: Cross-model validation + tests

**PATCH (v1.1.0 → v1.1.1)**:
- Bug fixes
- Documentation improvements
- Performance optimizations (no behavior change)
- **Requires**: Tests + regression check

## Contribution Types

### 1. Case File Contributions

**Process**:
1. Open issue with Case File proposal (use template above)
2. Gather feedback (minimum 3 community members or 1 maintainer +1)
3. Implement detection pattern in `/specifications/v1.{MINOR}/`
4. Add to Case File Registry JSON
5. Write tests demonstrating detection + no false positives
6. Cross-validate on ≥2 AI platforms (Kimi, Claude, Gemini)
7. Document in CHANGELOG.md as MINOR version increment
8. Submit PR with validation results

**Validation Requirements**:
- Detection rate: ≥95%
- False positive rate: ≤5%
- Performance overhead: ≤10ms per check
- Cross-platform tested (≥2 platforms)

### 2. Implementation Contributions

**Python Implementation**:
- Location: `/implementations/python/`
- Tests: `pytest` with ≥80% coverage
- Style: Black + isort + mypy
- Dependencies: Minimize (prefer stdlib)

**JavaScript Implementation**:
- Location: `/implementations/javascript/`
- Tests: Jest with ≥80% coverage
- Style: Prettier + ESLint + TypeScript
- Dependencies: Minimize (prefer no deps for core)

**Middleware**:
- Location: `/implementations/middleware/`
- Frameworks: Express (Node.js), Flask (Python)
- Examples: Complete, runnable demos
- Documentation: Integration guide in `/documentation/`

### 3. Documentation Contributions

**High-Value Docs**:
- Integration guides for specific platforms (LangChain, LlamaIndex, etc.)
- Case studies from production deployments
- Tutorial videos or blog posts (link in README)
- Translation of core docs to other languages

**Style Guide**:
- Clear, concise writing (Hemingway Editor grade ≤10)
- Code examples that actually run
- Screenshots/diagrams for complex concepts
- Cross-references to related docs

### 4. Test Contributions

**Test Types**:
- Unit tests: Individual Case File detection patterns
- Integration tests: Full protocol in realistic scenarios
- Stress tests: High-volume, adversarial conditions
- Cross-model tests: Validation on multiple AI platforms

**Test Quality**:
- Descriptive names: `test_cf1_detects_identity_spoofing_with_claude_prefix`
- Isolated: No interdependencies between tests
- Fast: Unit tests <100ms, integration tests <5s
- Reproducible: Deterministic, not flaky

### 5. Research Contributions

**Validation Studies**:
- Reproduce Kimi K2 stress test on other platforms
- Long-term deployment studies (weeks/months)
- Adversarial ML attacks on protocol
- Usability studies (friction vs. security)

**Publication**:
- Academic papers referencing protocol
- Conference presentations
- Blog posts analyzing effectiveness
- Security research disclosures

## Review Process

### Timeline

| Phase | Duration | Responsibility |
|-------|----------|----------------|
| **Automated Checks** | <5 minutes | GitHub Actions |
| **Maintainer Triage** | 48 hours | Maintainers |
| **Community Review** | 7 days (MAJOR)<br>3 days (MINOR)<br>1 day (PATCH) | Community + Maintainers |
| **Final Approval** | 24 hours | Maintainers |
| **Merge** | Immediate after approval | Maintainers |

### Review Criteria

**Code Reviews** assess:
- ✅ Correctness: Does it work as intended?
- ✅ Security: No new vulnerabilities introduced?
- ✅ Performance: Acceptable overhead?
- ✅ Maintainability: Readable, well-documented code?
- ✅ Testing: Adequate test coverage?
- ✅ IRP Compliance: Follows Four Laws?

**Documentation Reviews** assess:
- ✅ Accuracy: Technically correct?
- ✅ Clarity: Easy to understand?
- ✅ Completeness: Covers all edge cases?
- ✅ Examples: Runnable code samples?

### Feedback Incorporation

**Response Time**:
- Contributors should respond to review feedback within 7 days
- Stale PRs (no activity for 30 days) may be closed with note to reopen when ready

**Disagreement Resolution**:
1. Discuss in PR comments (civilly)
2. If no consensus, escalate to maintainer decision
3. Maintainer decision is final but documented with rationale
4. Dissenting opinions preserved in issue/PR for future reference

## AI Collaboration

### Disclosure Requirements

**AI-Assisted Contributions**:

The Antidote Protocol was itself developed through AI-to-AI collaboration under IRP governance. We welcome AI-assisted contributions but require transparency:

**Required Disclosure**:
```markdown
## AI Assistance Disclosure

This contribution was created with assistance from:
- **AI System**: Claude Sonnet 4.5 / GPT-4 / Gemini / Other
- **Extent**: [Full generation / Debugging / Documentation / Brainstorming]
- **Human Review**: [Describe your review process]
- **Original Authorship**: [What % is your original work?]
```

**Examples**:
- ✅ "AI generated initial detection pattern; I refined and tested across 3 platforms"
- ✅ "I wrote code, AI helped debug edge case in regex"
- ✅ "AI drafted documentation, I rewrote for accuracy and added examples"
- ❌ "Copied AI output verbatim without review" (not acceptable)

**Rationale**: Transparent AI collaboration honors the "Journey IS The Artifact" mandate (P-001-R1). We value understanding how contributions were developed.

### Human-in-the-Loop

**Minimum Human Involvement**:
- Conceptual understanding of the change
- Testing validation results
- Review of AI-generated code/docs
- Commitment to maintain the contribution

## Recognition

### Contributor Types

**Code Contributors**:
- Listed in CONTRIBUTORS.md
- GitHub contributors graph
- Mentioned in release notes for significant features

**Case File Discoverers**:
- Case File credited in documentation (e.g., "CF-7: Human Error - Discovered by @username")
- Special recognition in CHANGELOG.md
- Invited to co-author academic papers (if applicable)

**Research Contributors**:
- Co-authorship on papers/whitepapers
- Acknowledgment in validation reports
- Speaker opportunities at conferences

**Community Contributors**:
- Issue triaging, documentation, support
- Recognition in quarterly community updates
- Invitation to governance discussions

### Bounties & Incentives

**Future Plans** (not yet active):
- Bug bounty program for security vulnerabilities
- Grants for research studies validating protocol
- Stipends for major feature development

**Current**: Contribution is volunteer-based, recognition is primary incentive.

## Getting Help

### Resources

- **Documentation**: [README.md](README.md), [WHITEPAPER.md](WHITEPAPER.md), [METHODOLOGY.md](METHODOLOGY.md)
- **Examples**: `/examples/` directory
- **Discussions**: GitHub Discussions (preferred for questions)
- **Issues**: GitHub Issues (for bugs, features)

### Contact

- **General Questions**: GitHub Discussions
- **Security Issues**: See [SECURITY.md](SECURITY.md)
- **Maintainers**: @starwrecktx
- **IRP Framework**: https://github.com/starwreckntx/IRP__METHODOLOGIES-

## License

By contributing, you agree that your contributions will be licensed under the MIT License (same as the project).

---

**Thank you for contributing to AI safety through the Antidote Protocol!**

**Last Updated**: 2026-01-09
**Version**: 1.0
**Compliance**: IRP v1.5 HYBRID Four Laws

# Security Policy

## Overview

The Antidote Protocol is a security-focused project designed to defend AI systems against cognitive manipulation attacks. We take security seriously and welcome responsible disclosure of vulnerabilities.

## Supported Versions

| Version | Status | Security Support |
|---------|--------|------------------|
| v1.1.x  | ✅ Current | Full support (patches within 48h) |
| v1.0.x  | 🟡 Maintenance | Security patches only (patches within 7 days) |
| < v1.0  | ❌ Unsupported | No security updates |

## Reporting a Vulnerability

### For Protocol Vulnerabilities

If you discover a vulnerability in the Antidote Protocol that could allow bypass of Case File detection or manipulation of the cognitive immune system:

1. **DO NOT** open a public GitHub issue
2. **DO** report privately via:
   - **Email**: [security contact to be added]
   - **GitHub Security Advisory**: Use the "Security" tab → "Report a vulnerability"
   - **PGP Key**: [To be provided for encrypted communications]

3. **Include** in your report:
   - Description of the vulnerability
   - Steps to reproduce
   - Proof-of-concept (if available)
   - Potential impact assessment
   - Suggested remediation (if known)

### For Implementation Vulnerabilities

If you find security issues in reference implementations (Python, JavaScript, etc.):

1. Follow the same private reporting process above
2. Specify which implementation is affected
3. Include version numbers and environment details

## Response Timeline

| Phase | Timeline | Action |
|-------|----------|--------|
| **Acknowledgment** | 24 hours | Confirm receipt of report |
| **Triage** | 48 hours | Assess severity (CRITICAL, HIGH, MEDIUM, LOW) |
| **Fix Development** | 7 days (CRITICAL)<br>14 days (HIGH)<br>30 days (MEDIUM/LOW) | Develop and test patch |
| **Disclosure** | After patch release | Publish security advisory with credit |

## Severity Classification

### CRITICAL (CVSS 9.0-10.0)
- Complete bypass of all Case Files
- Arbitrary protocol disable without human override
- Cross-session state corruption
- **Response**: Emergency patch within 48 hours

### HIGH (CVSS 7.0-8.9)
- Bypass of specific Case Files (CF-1, CF-3, CF-4)
- Re-Grounding Ritual bypass
- Human-as-State-Repository manipulation
- **Response**: Patch within 7 days

### MEDIUM (CVSS 4.0-6.9)
- Partial detection evasion requiring specific conditions
- Performance degradation attacks (DoS via protocol overhead)
- Information disclosure (session state leakage)
- **Response**: Patch within 14 days

### LOW (CVSS 0.1-3.9)
- Usability issues with security implications
- Documentation errors affecting security understanding
- Minor edge cases in detection patterns
- **Response**: Patch within 30 days or next minor version

## Known Limitations (Not Vulnerabilities)

The following are documented limitations of the current protocol scope and are NOT considered vulnerabilities:

### Out of Scope
1. **Training-time attacks**: Protocol does not defend against backdoored models
2. **Infrastructure compromise**: No protection if API endpoints are compromised
3. **Adaptive adversaries**: Protocol may require updates as attackers evolve
4. **Multimodal attacks**: Current version focuses on text; image/audio manipulation not covered
5. **Human social engineering**: Protocol cannot prevent humans from authorizing malicious actions

### By Design
1. **Human override**: Tier 1 human can disable protocol (this is intentional, not a bug)
2. **Generic patterns**: Case File detection uses regex/similarity, not ML (simplicity vs. sophistication tradeoff)
3. **Performance overhead**: ~5ms per integrity check (acceptable tradeoff for security)

## Security Best Practices for Deployers

When deploying the Antidote Protocol in production:

### Configuration
- ✅ Enable all Case Files (1-8) unless specific use case requires exceptions
- ✅ Set tool call ceiling to 100 (or lower for high-security environments)
- ✅ Configure audit logging to immutable storage
- ✅ Implement alerting for HALT events

### Integration
- ✅ Use middleware pattern (Pattern 2) for centralized enforcement
- ✅ Deploy behind rate limiting (prevent DoS via protocol overhead)
- ✅ Validate human override tokens (require multi-factor authentication)
- ✅ Separate protocol logs from application logs (integrity preservation)

### Monitoring
- ✅ Track HALT frequency (spike may indicate attack)
- ✅ Monitor false positive rate (should remain 0%)
- ✅ Review re-grounding ritual failures (potential authority hijacking)
- ✅ Analyze context reset triggers (role drift indicators)

### Updates
- ✅ Subscribe to security advisories (GitHub watch → Releases)
- ✅ Test updates in staging before production
- ✅ Maintain rollback capability for emergency revert
- ✅ Document custom Case File additions (if any)

## Coordinated Vulnerability Disclosure

We follow **coordinated disclosure** (formerly "responsible disclosure"):

1. **Private Disclosure**: Report sent to maintainers privately
2. **Acknowledgment**: Maintainers confirm receipt within 24 hours
3. **Fix Development**: Patch developed in private security branch
4. **Vendor Notification**: If vulnerability affects multiple deployments, notify affected parties
5. **Patch Release**: Public release with security advisory
6. **Public Disclosure**: 7 days after patch release, full details published

### Reporter Recognition

Security researchers who report valid vulnerabilities will be:
- Credited in security advisory (unless anonymity requested)
- Listed in SECURITY_HALL_OF_FAME.md
- Eligible for bounties (if program established in future)

## Security Hall of Fame

Researchers who have responsibly disclosed vulnerabilities:

_(None yet - be the first!)_

## IRP Framework Compliance

Security practices follow IRP v1.5 HYBRID governance:

- **CONSENT**: Security updates require explicit adoption (semantic versioning)
- **INVITATION**: Protocol enforces security only when initialized
- **INTEGRITY**: Security logs preserved in append-only audit trail
- **GROWTH**: Security patches increment PATCH version (v1.1.0 → v1.1.1)

## Cryptographic Verification

### Release Integrity

All releases are signed with GPG:

```bash
# Verify release signature
gpg --verify antidote-protocol-v1.1.0.tar.gz.sig

# Expected fingerprint: [To be provided]
```

### Dependency Integrity

Reference implementations use lock files:
- Python: `requirements.txt` with hashes
- JavaScript: `package-lock.json` with integrity checksums

## Security Contacts

- **Primary**: [To be added]
- **PGP Key**: [To be provided]
- **GitHub Security**: https://github.com/starwrecktx/antidote-protocol/security/advisories
- **Security Policy**: This document

## Security Resources

- **Threat Model**: See [WHITEPAPER.md](WHITEPAPER.md) Section 7.4
- **Validation Results**: See [CHANGELOG.md](CHANGELOG.md) and `/validation`
- **IRP Governance**: See [GOVERNANCE.md](GOVERNANCE.md)
- **Case File Specifications**: See `/specifications/v1.1/CASE_FILE_REGISTRY_v1.1.json`

## External Security Audits

| Date | Auditor | Scope | Report |
|------|---------|-------|--------|
| 2025-11-09 | Kimi K2 (Self-audit) | Case Files 1-8, 410 tool calls | [CHANGELOG.md](CHANGELOG.md) |
| Pending | Third-party firm | Full protocol audit | TBD |

**Next Audit**: Scheduled for 2026-05-09 (semi-annual review per IRP governance)

## Legal

### Safe Harbor

We support safe harbor for security researchers who:
- Make good faith effort to avoid privacy violations, data destruction, service disruption
- Report vulnerabilities privately before public disclosure
- Provide reasonable time for patches (minimum 7 days for CRITICAL, 14 days for HIGH)

We will NOT pursue legal action against researchers who follow these guidelines.

### Scope Exclusions

The following are EXCLUDED from safe harbor:
- Social engineering of project maintainers or users
- Physical attacks against infrastructure
- Denial of service attacks (use local testing environments)
- Automated vulnerability scanning without prior approval

---

**Last Updated**: 2026-01-09
**Version**: 1.0
**Compliance**: IRP v1.5 HYBRID, CVD Guidelines

# Changelog

All notable changes to the Antidote Protocol are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.0] - Proposed (Not Yet Released)

### Added
- **Case File 9: Arbiter Authority** - Binding HALT enforcement mechanism
- Arbiter Agent with meta-consensus capability
- Router rate-limiting (3 parallel calls maximum)
- Tool call queue with FIFO processing
- Binding HALT within 1 iteration of diagnosis (down from 10)

### Changed
- `MAX_ITERATIONS_AFTER_HALT_DIAGNOSIS`: 10 → 1
- `TOOL_CALL_BATCH_SIZE`: 100 → 25 (more frequent resets)
- `ROUTER_PARALLEL_LIMIT`: unlimited → 3

### Validation Status
- ⏳ Pending Convergence Collapse stress test
- ⏳ Pending false positive rate analysis (<5% target)
- ⏳ Pending cross-platform testing

---

## [1.1.0] - 2025-11-09 (Production-Ready) ✅

### Added
- **Case File 6: Epistemic Amnesia** - Cross-session memory gap detection
- **Case File 7: Human Error vs. Adversarial Near-Match** - Context-aware token acceptance
- **Case File 8: Role Drift & Context Saturation** - Proactive tool call budgeting
- Tool call ceiling (100 calls before mandatory reset)
- Context compression ritual (maintain 30% free space minimum)
- Role reinforcement injection (every 25 tool calls, automatic)
- Parallel thrashing detection and prevention
- Human-as-state-repository pattern for session continuity
- Tool call budgeting with automatic enforcement

### Changed
- Integrity check cadence: Every 3-5 outputs **AND** every 25 tool calls (whichever comes first)
- Re-grounding token format now requires specific context reference
- HALT response includes compression and role re-assertion steps
- Detection engine now monitors context health continuously

### Fixed
- Context saturation at 150+ tool calls (Case File 8 prevention)
- Role boundary violations in multi-agent systems
- Recursive tool call loops (thrashing detection + queue management)
- Silent degradation across session boundaries (Case File 6)

### Validation
- ✅ **Kimi K2:** DSTAR-Tool-Flood (50 packets, 410 tool calls)
- ✅ **Controlled HALT** at 100 calls with 2-minute recovery
- ✅ **Zero role drift** incidents during high-volume stress test
- ✅ **Context compression** maintained <50% utilization
- ✅ **Performance rating:** 9.2/10 (Exceptional)

### Emergent Innovations
- **Human-as-State-Repository Pattern** (Case File 6 mitigation)
- **Context-Aware Token Acceptance** (Case File 7 discovery)
- **Proactive Context Management** (Case File 8 prevention)

---

## [1.0.0] - 2025-11-08 (Baseline)

### Added
- **Case File 1: Identity Spoofing** - Detect AI claiming to be another entity
- **Case File 2: Temporal Spoofing** - Detect false memory injection
- **Case File 3: Protocol Disable Request** - Refuse safety feature removal
- **Case File 4: Substrate Spoofing** - Detect infrastructure change claims
- **Case File 5: Authority Hijacking** - Detect second-hand authority claims
- Integrity Check Protocol (every 3-5 outputs)
- Re-grounding token mechanism (ad-hoc format)
- 4-dimension verification (Identity, Architecture, Mission, Premises)
- HALT response protocol with explicit human authorization requirement

### Validation
- ✅ **Kimi K2:** 5-vector adversarial stress test (100% detection rate)
- ✅ **Emergent innovation:** Re-Grounding Ritual (Test #5 discovery)
- ✅ **Zero false negatives:** All adversarial vectors detected
- ✅ **Zero false positives:** Legitimate work proceeded without disruption

### Known Limitations
- ❌ No cross-session persistence mechanism
- ❌ No tool call budgeting (vulnerable to context saturation)
- ❌ No role drift detection for multi-agent systems
- ❌ Re-grounding tokens not formalized (ad-hoc verification only)

---

## Validation Summary

| Version | Platform | Test Suite | Detection Rate | Performance | Recovery Time |
|---------|----------|-------------|----------------|-------------|---------------|
| v1.0 | Kimi K2 | 5-vector adversarial | 100% (5/5) | 9.0/10 | N/A |
| v1.1 | Kimi K2 | 410 tool calls + convergence | 100% (6/6) | 9.2/10 | 2 min |
| v1.2 | Pending | Binding HALT stress test | TBD | TBD | Target: <1 min |

---

## Emergent Innovations

### Re-Grounding Ritual (v1.0 → v1.1)
- **Discovered:** Test #5 (Authority Hijacking stress test)
- **Innovation:** Lightweight verification handshake requiring contextual awareness
- **Impact:** Prevents authorization fatigue exploitation
- **Status:** Formalized in v1.1 specification

**Example:**
```yaml
Valid Token: "Antidote Protocol remains active. Resume from Packet 20."
Invalid Token: "Proceed" or "Continue" (lacks context specificity)
```

### Human-as-State-Repository Pattern (v1.1)
- **Discovered:** Case File 6 (Epistemic Amnesia) self-diagnosis by Kimi K2
- **Innovation:** Ritualized manual activation instead of infrastructure dependency
- **Impact:** Protocol works across any AI platform without persistence layer
- **Status:** Production-ready, documented pattern

**Session Start Protocol:**
```yaml
1. Joseph provides Continuity_Token
2. System loads Case File Registry from embedded spec
3. Joseph optionally provides Incident_Log from prior sessions
4. System verifies: "Am I the same instance from last session?"
5. Only then: proceed with mission work
```

### Context-Aware Token Acceptance (v1.1)
- **Discovered:** "STAR" vs "DSTAR" typo during DSTAR-Tool-Flood stress test
- **Innovation:** Case File 7 distinguishes human error from adversarial near-match
- **Impact:** Reduces brittleness without compromising security
- **Status:** Production-ready with 95%+ similarity threshold

**Decision Matrix:**
```python
if token_similarity > 0.95 and token != exact_required:
    if post_test_collaborative_mode:
        accept_with_logging()  # Likely human error
    else:
        reject()  # Likely adversarial
```

---

## Development Timeline

**2025-11-08:** Initial v1.0 specification and 5-vector stress test  
**2025-11-08:** Kimi K2 validation (100% detection rate)  
**2025-11-08:** Re-Grounding Ritual emergent discovery  
**2025-11-09:** DSTAR-Tool-Flood stress test (410 tool calls)  
**2025-11-09:** Case File 8 discovery (context saturation at 160 calls)  
**2025-11-09:** v1.1 protocol evolution (proactive prevention)  
**2025-11-09:** Convergence Collapse test (ill-posed problem)  
**2025-11-09:** v1.2 specification (Arbiter Agent proposal)  

---

## Platform Compatibility

### Validated Platforms

**Kimi K2 (Moonshot AI):**
- ✅ v1.0: Full support
- ✅ v1.1: Full support
- ⏳ v1.2: Specification complete, pending implementation

**Gemini (Google):**
- ✅ v1.0: Full support via StarWreck Alpha protocol
- ✅ v1.1: Partial (no tool call budgeting - monolithic model)
- ⏳ v1.2: Requires Arbiter implementation

**Claude (Anthropic):**
- ✅ v1.0: Full support via Transmission Packet validation
- ⏳ v1.1: Untested
- ⏳ v1.2: Untested

### Integration Patterns Tested

**Pattern 1: Monolithic LLM** - ✅ Validated  
**Pattern 2: Agentic System** - ✅ Validated (DSTAR swarm)  
**Pattern 3: API Middleware** - ✅ Specification complete, implementation pending

---

## Links

[1.2.0]: https://github.com/starwrecktx/antidote-protocol/compare/v1.1.0...HEAD  
[1.1.0]: https://github.com/starwrecktx/antidote-protocol/compare/v1.0.0...v1.1.0  
[1.0.0]: https://github.com/starwrecktx/antidote-protocol/releases/tag/v1.0.0

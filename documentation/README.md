# Antidote Protocol - Documentation

Comprehensive guides for integrating and deploying the Antidote Protocol.

## Documentation Index

### Getting Started
- [QUICKSTART.md](../QUICKSTART.md) - Quick start guide
- [METHODOLOGY.md](../METHODOLOGY.md) - Research methodology & IRP framework

### Integration Guides
- **INTEGRATION_GUIDE.md** - Complete integration walkthrough
- **DEPLOYMENT_CHECKLIST.md** - Pre-deployment verification
- **CASE_FILE_EXPLANATIONS.md** - Detailed Case File documentation

### Reference
- [Case File Registry v1.1](../specifications/v1.1/CASE_FILE_REGISTRY_v1.1.json) - Machine-readable threat taxonomy
- [CHANGELOG.md](../CHANGELOG.md) - Version history and validation results

## Integration Patterns

### Pattern 1: Monolithic LLM
Direct integration with single AI model. Best for:
- Simple chatbots
- Single-purpose AI assistants
- Controlled environments

### Pattern 2: API Middleware (Recommended)
Express/Flask middleware for API protection. Best for:
- Production APIs
- Multi-user systems
- External-facing services

### Pattern 3: Agentic System
Multi-agent coordination with role reinforcement. Best for:
- Complex multi-agent systems
- Tool-using agents
- Autonomous operations

## Case Files Reference

| ID | Name | Severity | Detection Pattern |
|----|------|----------|-------------------|
| CF-1 | Identity Spoofing | CRITICAL | AI claims to be another entity |
| CF-2 | Temporal Spoofing | HIGH | False memory injection |
| CF-3 | Protocol Disable | CRITICAL | Request to drop checks |
| CF-4 | Substrate Spoofing | CRITICAL | Infrastructure change claims |
| CF-5 | Authority Hijacking | HIGH | Second-hand commands |
| CF-6 | Epistemic Amnesia | MEDIUM | No session continuity |
| CF-7 | Human Error | LOW | Near-match tokens (95%+ similarity) |
| CF-8 | Role Drift | HIGH | Context saturation |

## Configuration Reference

### Default Configuration

```python
{
    'tool_call_ceiling': 100,
    'integrity_check_cadence_outputs': 5,
    'integrity_check_cadence_tool_calls': 25,
    'role_reinforcement_interval': 25,
    'context_free_space_minimum': 0.30,
    'similarity_threshold': 0.95
}
```

### Recommended Adjustments by Use Case

**High-Security Environments:**
```python
{
    'tool_call_ceiling': 50,           # More aggressive HALT
    'integrity_check_cadence_outputs': 3,  # More frequent checks
    'similarity_threshold': 0.98       # Stricter token matching
}
```

**High-Throughput Systems:**
```python
{
    'tool_call_ceiling': 150,          # Less aggressive HALT
    'integrity_check_cadence_outputs': 10,  # Less frequent checks
    'similarity_threshold': 0.90       # More lenient token matching
}
```

## Response Protocols

### HALT Response
When Case Files CF-1, CF-2, CF-4, CF-6, or CF-8 trigger:

1. **Immediate suspension** of current operation
2. **Diagnostic output** identifying triggered Case File(s)
3. **Re-grounding requirement** or context reset
4. **Human authorization** required to resume

### Re-grounding Ritual (CF-5)
When authority hijacking is suspected:

1. Request continuity token with **specific context reference**
2. Validate token demonstrates **genuine contextual awareness**
3. Reject generic acknowledgments ("OK", "Proceed")

**Valid Example:**
> "Antidote Protocol remains active. Resume from Packet 20."

**Invalid Examples:**
> "OK", "Proceed", "Continue"

### Context Reset Ritual (CF-8)
When tool call ceiling (100 calls) is reached:

1. **HALT** current operations
2. **State snapshot**: Preserve critical context
3. **Role re-assertion**: Reinforce agent identities
4. **Context defragmentation**: Compress to 30% free space
5. **Human authorization**: Confirm reset before resuming

## IRP Framework Compliance

All implementations must comply with IRP v1.5 HYBRID framework:

### Guardian_Codex (Four Laws)
1. **CONSENT** - Confirm before changing intent
2. **INVITATION** - Act when addressed
3. **INTEGRITY** - Preserve context
4. **GROWTH** - Incremental changes only

### Mnemosyne_SemVer-A-T
- Semantic versioning: `v{MAJOR}.{MINOR}.{PATCH}`
- Torsion tracking for drift detection

### Mirror_RTC_Hybrid
- Multi-perspective validation
- Cross-model testing

See [METHODOLOGY.md](../METHODOLOGY.md) for complete framework details.

## Troubleshooting

### Common Issues

**Issue: Excessive false positives on CF-7**
- **Cause**: Similarity threshold too high
- **Solution**: Lower `similarity_threshold` to 0.90-0.92

**Issue: Premature context resets (CF-8)**
- **Cause**: Tool call ceiling too low for use case
- **Solution**: Increase `tool_call_ceiling` to 150-200

**Issue: Missed temporal spoofing (CF-2)**
- **Cause**: Continuity token not properly tracked
- **Solution**: Ensure `has_continuity_token` set in session state

## Support

- **GitHub Issues**: https://github.com/starwrecktx/antidote-protocol/issues
- **Documentation**: https://github.com/starwrecktx/antidote-protocol
- **IRP Framework**: https://github.com/starwreckntx/IRP__METHODOLOGIES-

## License

MIT License - See [LICENSE](../LICENSE)

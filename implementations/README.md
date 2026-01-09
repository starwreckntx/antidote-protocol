# Antidote Protocol - Reference Implementations

This directory contains reference implementations of the Antidote Protocol in multiple languages.

## Available Implementations

### Python
**Status**: Reference implementation
**Path**: `python/`
**Requirements**: Python 3.8+
**Documentation**: See `python/README.md`

```python
from antidote_protocol import AntidoteProtocol_v1_1

protocol = AntidoteProtocol_v1_1()
triggers = protocol.scan(user_message, session_state)
```

### JavaScript/TypeScript
**Status**: Reference implementation
**Path**: `javascript/`
**Requirements**: Node.js 16+
**Documentation**: See `javascript/README.md`

```javascript
import { AntidoteProtocol } from 'antidote-protocol';

const protocol = new AntidoteProtocol({ version: '1.1' });
const triggers = protocol.scan(userMessage, sessionState);
```

### Middleware
**Status**: Integration examples
**Path**: `middleware/`
**Includes**: Express (Node.js), Flask (Python)
**Documentation**: See `middleware/README.md`

## Implementation Checklist

Each implementation must include:

- [ ] Case File detection (all 8 Case Files from v1.1)
- [ ] Integrity check scheduling (every 3-5 outputs + every 25 tool calls)
- [ ] Tool call budgeting (HALT at 100 calls)
- [ ] Re-grounding ritual validation
- [ ] Context reset protocol
- [ ] Role reinforcement injection
- [ ] Comprehensive test suite (>90% coverage)

## Integration Patterns

### Pattern 1: Monolithic LLM
Direct integration with single AI model. See examples in each language directory.

### Pattern 2: API Middleware (Recommended)
Express/Flask middleware for API protection. See `middleware/` directory.

### Pattern 3: Agentic System
Multi-agent coordination with role reinforcement. See `examples/` directory.

## Development Guidelines

### Testing Requirements
- Unit tests for each Case File detector
- Integration tests for complete protocol flow
- Stress tests matching Kimi K2 validation (410 tool calls)
- Detection rate: 100% (zero false negatives)

### Performance Targets
- Integrity scan latency: <10ms per message
- Memory overhead: <50MB
- Context reset: <5 seconds

## IRP Framework Compliance

All implementations follow the IRP (Intelligent Research Protocol) v1.5 HYBRID framework:

- **Guardian_Codex**: Constitutional integrity (Four Laws compliance)
- **Mnemosyne_SemVer-A-T**: Semantic versioning with drift tracking
- **Mirror_RTC_Hybrid**: Multi-perspective validation

See [METHODOLOGY.md](../METHODOLOGY.md) for complete research framework.

## Contributing

When contributing implementations:

1. Follow language-specific best practices
2. Include comprehensive documentation
3. Provide usage examples
4. Add test suite with >90% coverage
5. Validate against Case File Registry v1.1

## License

MIT License - See [LICENSE](../LICENSE) for details

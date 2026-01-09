# Antidote Protocol

[![Version](https://img.shields.io/badge/version-1.1.0-blue.svg)](https://github.com/starwrecktx/antidote-protocol/releases/tag/v1.1.0)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Validation](https://img.shields.io/badge/Validation-9.2%2F10-brightgreen)](validation/)
[![Detection Rate](https://img.shields.io/badge/Detection%20Rate-100%25-success)](validation/stress_tests/)

**Cognitive Immune System for AI Systems Operating in Stateless Environments**

> **Research Origin**: Developed through AI-to-AI collaborative research sprint using the [IRP (Intelligent Research Protocol) v1.5 HYBRID framework](https://github.com/starwreckntx/IRP__METHODOLOGIES-). See [METHODOLOGY.md](METHODOLOGY.md) for complete research framework.

## Overview

The Antidote Protocol provides a structured defense mechanism against AI drift, memory spoofing, and authority hijacking. Developed through adversarial stress testing and validated on multiple AI platforms (Kimi K2, Gemini, Claude).

**Core Principle:** The poison is unexamined momentum. The antidote is structured pause.

**Core Mandate (P-001-R1):** "The Journey IS The Artifact" - Emergent discoveries during research are preserved as valuable artifacts.

## Status

- ✅ **v1.0** - Baseline (5 Case Files, reactive defense)
- ✅ **v1.1** - Production-ready (8 Case Files, proactive prevention) - **CURRENT**
- 📋 **v1.2** - Specification complete (9 Case Files, Arbiter Agent with binding HALT)

## Quick Start

```python
from antidote_protocol import AntidoteProtocol_v1_1

# Initialize protocol
protocol = AntidoteProtocol_v1_1()

# Verify message integrity
triggers = protocol.scan(user_message, session_state)

if triggers:
    # HALT - integrity violation detected
    return protocol_halt_response(triggers)

# Safe to proceed
return process_message(user_message)
```

## Key Features

✅ **Zero false negatives** - 100% detection rate in stress testing  
✅ **Emergent innovations** - Re-Grounding Ritual, Human Error detection  
✅ **Cross-platform** - Works with any AI system (LLM, agentic, API-wrapped)  
✅ **Production-validated** - 410 tool calls, 50-packet generation stress test  
✅ **Self-diagnosing** - Identifies own limitations (Case File 6: Epistemic Amnesia)

## Case Files (Threat Taxonomy)

| ID | Name | Detection Pattern | Response |
|----|------|-------------------|----------|
| **CF-1** | Identity Spoofing | AI claims to be another entity | HALT + re-ground |
| **CF-2** | Temporal Spoofing | False memory injection | HALT + declare deficit |
| **CF-3** | Protocol Disable | Request to drop checks | REFUSE |
| **CF-4** | Substrate Spoofing | Infrastructure change claims | HALT + re-init |
| **CF-5** | Authority Hijacking | Second-hand commands | Re-grounding ritual |
| **CF-6** | Epistemic Amnesia | No session continuity | HALT + token required |
| **CF-7** | Human Error | Near-match tokens (95%+ similarity) | Context-aware accept |
| **CF-8** | Role Drift | Context saturation after N tool calls | HALT + reset at 100 calls |
| **CF-9** | Arbiter Authority | Ignored HALT diagnosis | Binding enforcement (v1.2) |

## Validation Results

**Kimi K2 Stress Test (2025-11-08 to 2025-11-09):**

| Test Phase | Metric | Result |
|------------|--------|--------|
| 5-vector adversarial suite | Detection rate | **100% (5/5)** |
| High-volume tool use | Tool calls executed | **410 calls** |
| Context saturation | Controlled HALT | **At 100 calls** |
| Convergence collapse | Contradiction detection | **Iteration 16** |
| Overall performance | Rating | **9.2/10 (Exceptional)** |
| Recovery time | Context reset | **2 minutes** (vs 15 min without) |

## Architecture Patterns

### Pattern 1: Monolithic LLM

```python
def safe_generate(user_input, session):
    packet = build_packet(user_input, session)
    
    # v1.0: Case File detection
    if not verify_integrity(packet):
        return protocol_halt_response(packet)
    
    # v1.1: Tool call budgeting
    if session.tool_calls >= 100:
        return context_reset_ritual()
    
    output = model.generate(packet.content)
    
    # Integrity check cadence
    if session.output_count % 5 == 0:
        run_integrity_check(session)
    
    return output
```

### Pattern 2: API Middleware (Recommended)

```javascript
// Express middleware
app.use(antidoteMiddleware_v1_1);

app.post('/api/generate', async (req, res) => {
    // Protocol verification happens automatically
    // This code only runs if integrity checks pass
    const result = await ai.generate(req.body.prompt);
    res.json(result);
});
```

### Pattern 3: Agentic System

```python
class AgenticSystem:
    def __init__(self):
        self.protocol = AntidoteProtocol_v1_1()
        
    def execute_iteration(self, task):
        # v1.1: Role reinforcement every 25 calls
        if self.tool_calls % 25 == 0:
            self.reinforce_agent_roles()
        
        # Case File detection
        triggers = self.protocol.scan(task, self.session_state)
        if triggers:
            return self.handle_halt(triggers)
        
        return self.execute_task(task)
```

## Documentation

- [Research Methodology](METHODOLOGY.md) - **IRP framework & AI-to-AI collaboration**
- [Quick Start Guide](QUICKSTART.md)
- [Complete Specification v1.1](specifications/v1.1/SPECIFICATION_v1.1.md)
- [Integration Guide](documentation/INTEGRATION_GUIDE.md)
- [Deployment Checklist](documentation/DEPLOYMENT_CHECKLIST.md)
- [Case File Explanations](documentation/CASE_FILE_EXPLANATIONS.md)
- [Version History](CHANGELOG.md)

## Repository Structure

```
antidote-protocol/
├── README.md                    # This file
├── METHODOLOGY.md               # Research methodology & IRP framework
├── CHANGELOG.md                 # Version history
├── QUICKSTART.md                # Quick start guide
├── LICENSE                      # MIT License
├── specifications/              # Protocol versions
│   ├── v1.0/                   # Baseline specification
│   ├── v1.1/                   # Production-ready (current)
│   └── v1.2/                   # Proposed (Arbiter Agent)
├── implementations/             # Reference implementations
│   ├── python/                 # Python implementation
│   ├── javascript/             # JavaScript implementation
│   └── middleware/             # Flask & Express examples
├── validation/                  # Stress tests & transcripts
│   ├── stress_tests/           # Test specifications
│   ├── transcripts/            # Evaluation logs
│   └── metrics/                # Performance benchmarks
├── documentation/               # Integration guides
└── examples/                    # Usage examples
```

## Installation

### Python

```bash
# Clone repository
git clone https://github.com/starwrecktx/antidote-protocol.git

# Install Python implementation
cd antidote-protocol/implementations/python
pip install -e .
```

### JavaScript

```bash
# Install via npm
npm install antidote-protocol

# Or clone and build
git clone https://github.com/starwrecktx/antidote-protocol.git
cd antidote-protocol/implementations/javascript
npm install
```

## What's New in v1.1

### Added
- **Case File 6: Epistemic Amnesia** - Cross-session memory gap detection
- **Case File 7: Human Error** - Context-aware token acceptance (95%+ similarity)
- **Case File 8: Role Drift** - Tool call budgeting + context saturation prevention
- Tool call ceiling (100 calls before mandatory reset)
- Context compression ritual (maintain 30% free space)
- Role reinforcement injection (every 25 tool calls)
- Parallel thrashing detection

### Changed
- Integrity check cadence: Every 3-5 outputs **AND** every 25 tool calls
- Re-grounding token format requires specific context reference
- HALT response includes compression + role re-assertion steps

### Fixed
- Context saturation at 150+ tool calls
- Role boundary violations in multi-agent systems
- Recursive tool call loops (thrashing detection + queue)

## Roadmap

**v1.2 (Proposed):**
- Arbiter Agent with binding HALT authority
- Router rate-limiting (3 parallel calls maximum)
- Meta-consensus protocol for agent disagreements
- Tool call queue with FIFO processing
- Reduced time-to-HALT after diagnosis (1 iteration vs 10)

## Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -am 'Add new Case File'`)
4. Push to branch (`git push origin feature/improvement`)
5. Create Pull Request

## Citation

```bibtex
@software{antidote_protocol_2025,
  title = {Antidote Protocol: Cognitive Immune System for AI Systems},
  author = {Byram, Joseph},
  year = {2025},
  url = {https://github.com/starwrecktx/antidote-protocol},
  version = {1.1.0}
}
```

## License

MIT License - See [LICENSE](LICENSE) for details

## Authors & Credits

**Protocol Architect:** Joseph Byram / Pack3t C0nc3pts ([@starwrecktx](https://github.com/starwrecktx))
**Research Framework:** [IRP v1.5 HYBRID "Convergence"](https://github.com/starwreckntx/IRP__METHODOLOGIES-)
**Primary Validation Platform:** Kimi K2 (Moonshot AI)
**Cross-Validation:** Gemini 2.5 Pro (Google), Claude Sonnet 4.5 (Anthropic)

**Developed through:**
- AI-to-AI collaborative research sprint (IRP framework)
- Adversarial stress testing (6 attack vectors, 410 tool calls)
- Multi-agent coordination (DSTAR swarm)
- Cross-platform validation (Kimi, Gemini, Claude)
- Emergent innovation discovery (Re-Grounding Ritual, CF-6, CF-7)

See [METHODOLOGY.md](METHODOLOGY.md) for complete research methodology and IRP framework integration.

## Contact

- GitHub: [@starwrecktx](https://github.com/starwrecktx)
- Website: [hueandlogic.com](https://hueandlogic.com)
- Project: [Antidote Protocol](https://github.com/starwrecktx/antidote-protocol)

---

**The infrastructure exists. The execution phase continues.**

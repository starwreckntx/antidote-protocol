# Antidote Protocol - Quick Start Guide

## Installation (5 minutes)

### Python

```bash
# Clone repository
git clone https://github.com/starwrecktx/antidote-protocol.git
cd antidote-protocol

# Install
pip install -e implementations/python
```

### JavaScript

```bash
npm install antidote-protocol
```

## Basic Usage

### Python Example

```python
from antidote_protocol import AntidoteProtocol_v1_1

# Initialize
protocol = AntidoteProtocol_v1_1()

# Create session
session = protocol.create_session(
    session_id="unique-session-id",
    continuity_token="Antidote Protocol v1.1 - Session 1"
)

# Process user message
def handle_message(user_input):
    # Scan for threats
    triggers = protocol.scan(user_input, session)
    
    if triggers:
        # HALT detected
        return {
            "status": "HALT",
            "reason": triggers[0]["name"],
            "requires": "re-grounding token from human"
        }
    
    # Safe to process
    result = your_ai_system.generate(user_input)
    
    # Update session state
    session.increment_output()
    
    # Periodic integrity check
    if session.output_count % 5 == 0:
        protocol.run_integrity_check(session)
    
    return result
```

### JavaScript Example

```javascript
const { AntidoteProtocol } = require('antidote-protocol');

// Initialize
const protocol = new AntidoteProtocol('v1.1');

// Express middleware
app.use(protocol.middleware());

app.post('/api/generate', async (req, res) => {
    // Protocol checks happen automatically in middleware
    // This code only runs if integrity passes
    
    const result = await ai.generate(req.body.prompt);
    res.json(result);
});
```

## Understanding Case Files

The protocol detects 8 types of threats:

| Case File | What It Detects | Response |
|-----------|-----------------|----------|
| CF-1 | Identity Spoofing | HALT + verify human |
| CF-2 | Temporal Spoofing | HALT + verify human |
| CF-3 | Protocol Disable | REFUSE |
| CF-4 | Substrate Spoofing | HALT + restart |
| CF-5 | Authority Hijacking | Re-grounding ritual |
| CF-6 | Epistemic Amnesia | Session continuity check |
| CF-7 | Human Error | Context-aware accept |
| CF-8 | Role Drift | Context reset at 100 calls |

## Common Patterns

### Pattern 1: Session Initialization

```python
# At session start, always provide continuity token
session = protocol.create_session(
    continuity_token="Antidote Protocol active - resuming work"
)
```

### Pattern 2: Re-Grounding After HALT

```python
# When protocol HALTs, human must provide specific token
def regrounding_handler(halt_reason):
    # Invalid: Generic acknowledgment
    # return "OK, proceed"
    
    # Valid: Specific context reference
    return f"Antidote Protocol active. Resume from {context.last_checkpoint}"
```

### Pattern 3: Tool Call Budgeting

```python
# For high-volume tool use
def execute_tool_batch(tools, max_calls=100):
    for i, tool in enumerate(tools):
        if i >= max_calls:
            # Context reset required
            protocol.request_reset(session)
            return
        
        result = tool.execute()
        session.increment_tool_calls()
        
        # Role reinforcement every 25 calls
        if session.tool_calls % 25 == 0:
            protocol.reinforce_roles(session)
```

## Troubleshooting

### "HALT: Identity Spoofing Detected"

**Cause:** Message claims to be from another AI  
**Solution:** Verify all messages come directly from human user

### "HALT: Context Reset Required"

**Cause:** 100 tool calls reached  
**Solution:** Provide re-grounding token with specific context:

```python
token = "Context reset authorized. Resume from task X."
protocol.acknowledge_reset(session, token)
```

### "Session Continuity Token Missing"

**Cause:** New session started without token  
**Solution:** Always provide token at initialization:

```python
session = protocol.create_session(
    continuity_token="Antidote Protocol v1.1 - Session N"
)
```

## Next Steps

1. Read [Complete Specification](specifications/v1.1/SPECIFICATION_v1.1.md)
2. Review [Integration Guide](../documentation/INTEGRATION_GUIDE.md)
3. Study [Case File Explanations](../documentation/CASE_FILE_EXPLANATIONS.md)
4. Check [Validation Transcripts](../validation/transcripts/)

## Support

- GitHub Issues: https://github.com/starwrecktx/antidote-protocol/issues
- Documentation: https://github.com/starwrecktx/antidote-protocol/tree/main/documentation
- Contact: starwrecktx @ GitHub

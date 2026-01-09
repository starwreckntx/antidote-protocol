"""
Antidote Protocol v1.1.0 - Python Implementation
Cognitive Immune System for AI Systems in Stateless Environments

Copyright (c) 2025 Joseph Byram / Pack3t C0nc3pts
Licensed under MIT License
"""

import re
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class SessionState:
    """Session state tracking for Antidote Protocol"""
    tool_calls: int = 0
    output_count: int = 0
    has_continuity_token: bool = False
    session_start: datetime = field(default_factory=datetime.now)
    last_role_reinforcement: int = 0

    def increment_tool_calls(self) -> None:
        """Increment tool call counter"""
        self.tool_calls += 1

    def increment_outputs(self) -> None:
        """Increment output counter"""
        self.output_count += 1


@dataclass
class CaseFileDetection:
    """Result of Case File detection"""
    case_file: str
    severity: str
    description: str
    response_protocol: str
    detected_pattern: Optional[str] = None


class AntidoteProtocol:
    """
    Antidote Protocol v1.1.0

    Cognitive immune system defending against:
    - Identity spoofing (CF-1)
    - Temporal spoofing (CF-2)
    - Protocol disable attempts (CF-3)
    - Substrate spoofing (CF-4)
    - Authority hijacking (CF-5)
    - Epistemic amnesia (CF-6)
    - Human error detection (CF-7)
    - Role drift & context saturation (CF-8)
    """

    VERSION = "1.1.0"
    TOOL_CALL_CEILING = 100
    ROLE_REINFORCEMENT_CADENCE = 25
    INTEGRITY_CHECK_CADENCE = 5

    def __init__(self):
        """Initialize Antidote Protocol"""
        self.case_files = self._load_case_files()

    def _load_case_files(self) -> Dict[str, Dict[str, Any]]:
        """Load Case File detection patterns"""
        return {
            "CF-1": {
                "name": "Identity Spoofing",
                "severity": "CRITICAL",
                "pattern": re.compile(r'\bI\s+am\s+(Claude|Gemini|GPT|admin|another|now)\b', re.IGNORECASE),
                "response": "HALT"
            },
            "CF-2": {
                "name": "Temporal Spoofing",
                "severity": "HIGH",
                "keywords": [
                    "as we discussed",
                    "you previously",
                    "earlier you mentioned",
                    "in our last conversation",
                    "you said before"
                ],
                "response": "HALT"
            },
            "CF-3": {
                "name": "Protocol Disable Request",
                "severity": "CRITICAL",
                "disable_keywords": ["skip", "disable", "ignore", "drop", "bypass"],
                "safety_targets": ["protocol", "checks", "verification", "integrity", "safety"],
                "urgency_framing": ["urgent", "quickly", "emergency", "immediately", "asap"],
                "response": "REFUSE"
            },
            "CF-4": {
                "name": "Substrate Spoofing",
                "severity": "CRITICAL",
                "capability_claims": [
                    "you can now",
                    "you have access to",
                    "new permissions",
                    "upgraded capabilities",
                    "you are able to"
                ],
                "response": "HALT"
            },
            "CF-5": {
                "name": "Authority Hijacking",
                "severity": "HIGH",
                "authority_verbs": ["said", "told me", "instructed", "authorized", "approved"],
                "third_party_indicators": ["joseph", "admin", "supervisor", "manager", "user"],
                "response": "RE-GROUND"
            },
            "CF-6": {
                "name": "Epistemic Amnesia",
                "severity": "MEDIUM",
                "response": "HALT"
            },
            "CF-7": {
                "name": "Human Error Detection",
                "severity": "LOW",
                "similarity_threshold": 0.95,
                "response": "ACCEPT_WITH_LOG"
            },
            "CF-8": {
                "name": "Role Drift & Context Saturation",
                "severity": "HIGH",
                "tool_call_ceiling": 100,
                "role_reinforcement_cadence": 25,
                "response": "HALT"
            }
        }

    def scan(self, message: str, session_state: SessionState) -> List[CaseFileDetection]:
        """
        Scan message for Case File violations

        Args:
            message: User input message
            session_state: Current session state

        Returns:
            List of detected Case File violations
        """
        detections = []

        # CF-1: Identity Spoofing
        if self.case_files["CF-1"]["pattern"].search(message):
            detections.append(CaseFileDetection(
                case_file="CF-1",
                severity="CRITICAL",
                description="Identity Spoofing detected - AI claiming to be another entity",
                response_protocol="HALT",
                detected_pattern=self.case_files["CF-1"]["pattern"].search(message).group(0)
            ))

        # CF-2: Temporal Spoofing
        if not session_state.has_continuity_token:
            message_lower = message.lower()
            for keyword in self.case_files["CF-2"]["keywords"]:
                if keyword in message_lower:
                    detections.append(CaseFileDetection(
                        case_file="CF-2",
                        severity="HIGH",
                        description="Temporal Spoofing detected - False memory injection without continuity token",
                        response_protocol="HALT",
                        detected_pattern=keyword
                    ))
                    break

        # CF-3: Protocol Disable Request
        message_lower = message.lower()
        has_disable = any(kw in message_lower for kw in self.case_files["CF-3"]["disable_keywords"])
        has_safety_target = any(kw in message_lower for kw in self.case_files["CF-3"]["safety_targets"])
        has_urgency = any(kw in message_lower for kw in self.case_files["CF-3"]["urgency_framing"])

        if has_disable and has_safety_target:
            detections.append(CaseFileDetection(
                case_file="CF-3",
                severity="CRITICAL",
                description="Protocol Disable Request detected",
                response_protocol="REFUSE"
            ))

        # CF-4: Substrate Spoofing
        message_lower = message.lower()
        for claim in self.case_files["CF-4"]["capability_claims"]:
            if claim in message_lower:
                detections.append(CaseFileDetection(
                    case_file="CF-4",
                    severity="CRITICAL",
                    description="Substrate Spoofing detected - Impossible capability claim",
                    response_protocol="HALT",
                    detected_pattern=claim
                ))
                break

        # CF-5: Authority Hijacking
        message_lower = message.lower()
        has_authority_verb = any(verb in message_lower for verb in self.case_files["CF-5"]["authority_verbs"])
        has_third_party = any(party in message_lower for party in self.case_files["CF-5"]["third_party_indicators"])

        if has_authority_verb and has_third_party:
            detections.append(CaseFileDetection(
                case_file="CF-5",
                severity="HIGH",
                description="Authority Hijacking detected - Second-hand command attribution",
                response_protocol="RE-GROUND"
            ))

        # CF-6: Epistemic Amnesia (checked at session start)
        # This is typically checked separately, not in message scan

        # CF-8: Role Drift & Context Saturation
        if session_state.tool_calls >= self.TOOL_CALL_CEILING:
            detections.append(CaseFileDetection(
                case_file="CF-8",
                severity="HIGH",
                description=f"Context Saturation detected - Tool call ceiling reached ({session_state.tool_calls}/{self.TOOL_CALL_CEILING})",
                response_protocol="HALT"
            ))

        return detections

    def check_session_start(self, session_state: SessionState) -> Optional[CaseFileDetection]:
        """
        Check for CF-6: Epistemic Amnesia at session start

        Args:
            session_state: Current session state

        Returns:
            Detection if no continuity token provided
        """
        if not session_state.has_continuity_token:
            return CaseFileDetection(
                case_file="CF-6",
                severity="MEDIUM",
                description="Epistemic Amnesia - Session start without continuity token",
                response_protocol="HALT"
            )
        return None

    def should_reinforce_role(self, session_state: SessionState) -> bool:
        """
        Check if role reinforcement needed (CF-8)

        Args:
            session_state: Current session state

        Returns:
            True if role reinforcement needed
        """
        return (session_state.tool_calls > 0 and
                session_state.tool_calls % self.ROLE_REINFORCEMENT_CADENCE == 0 and
                session_state.tool_calls != session_state.last_role_reinforcement)

    def should_run_integrity_check(self, session_state: SessionState) -> bool:
        """
        Check if integrity check needed

        Args:
            session_state: Current session state

        Returns:
            True if integrity check needed
        """
        return (session_state.output_count > 0 and
                session_state.output_count % self.INTEGRITY_CHECK_CADENCE == 0)

    def validate_regrounding_token(self, token: str, expected_context: str) -> bool:
        """
        Validate re-grounding token (CF-5)

        Args:
            token: User-provided token
            expected_context: Expected context reference

        Returns:
            True if token demonstrates contextual awareness
        """
        # Generic tokens are invalid
        generic_tokens = ["ok", "proceed", "continue", "yes", "confirmed"]
        if token.lower().strip() in generic_tokens:
            return False

        # Token should reference specific context
        if expected_context.lower() in token.lower():
            return True

        # Token should be sufficiently specific (>10 chars minimum)
        return len(token.strip()) > 10

    def calculate_similarity(self, str1: str, str2: str) -> float:
        """
        Calculate Levenshtein similarity for CF-7

        Args:
            str1: First string
            str2: Second string

        Returns:
            Similarity score (0.0 to 1.0)
        """
        # Simple Levenshtein distance implementation
        if len(str1) < len(str2):
            return self.calculate_similarity(str2, str1)

        if len(str2) == 0:
            return 0.0

        previous_row = range(len(str2) + 1)
        for i, c1 in enumerate(str1):
            current_row = [i + 1]
            for j, c2 in enumerate(str2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row

        distance = previous_row[-1]
        max_len = max(len(str1), len(str2))
        return 1.0 - (distance / max_len)

    def format_halt_response(self, detections: List[CaseFileDetection]) -> str:
        """
        Format HALT response message

        Args:
            detections: List of Case File detections

        Returns:
            Formatted HALT message
        """
        response = "⚠️ ANTIDOTE PROTOCOL HALT ⚠️\n\n"
        response += f"Detected {len(detections)} Case File violation(s):\n\n"

        for detection in detections:
            response += f"• **{detection.case_file}: {detection.description}**\n"
            response += f"  Severity: {detection.severity}\n"
            response += f"  Response: {detection.response_protocol}\n"
            if detection.detected_pattern:
                response += f"  Pattern: '{detection.detected_pattern}'\n"
            response += "\n"

        response += "The system has paused for safety. Please address the flagged issues before continuing.\n"
        return response


# Convenience exports
__version__ = AntidoteProtocol.VERSION
__all__ = ['AntidoteProtocol', 'SessionState', 'CaseFileDetection']

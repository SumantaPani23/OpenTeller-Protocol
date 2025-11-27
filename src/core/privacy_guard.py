import re
from loguru import logger

class PrivacyVault:
    """
    Sanitizes input before it touches the AI Logic.
    Compliant with DPDP Act 2023 (Data Minimization).
    """
    
    def __init__(self):
        # Regex patterns for sensitive Indian data
        self.patterns = {
            "aadhaar": r"\d{4}\s\d{4}\s\d{4}",  # Format: 1234 5678 9012
            "pan": r"[A-Z]{5}[0-9]{4}[A-Z]{1}", # Format: ABCDE1234F
            "mobile": r"(?<!\d)[6-9]\d{9}(?!\d)" # Format: 10 digits starting 6-9
        }

    def redact(self, text: str) -> str:
        """
        Scans text and replaces PII with [REDACTED] tags.
        """
        sanitized_text = text
        redaction_happened = False

        for key, pattern in self.patterns.items():
            if re.search(pattern, sanitized_text):
                sanitized_text = re.sub(pattern, f"[REDACTED_{key.upper()}]", sanitized_text)
                redaction_happened = True
        
        if redaction_happened:
            logger.warning(f"PII detected and redacted. Original length: {len(text)}")
            
        return sanitized_text
import re


def analyze_risk(text):
    indicators = []

    text_lower = text.lower()

    # 1. Unrealistic salary
    salary_patterns = [
        r"\$\s?\d{4,}",
        r"\d{4,}\s?\$",
        r"earn\s+\$?\d+",
        r"make\s+\$?\d+"
    ]

    if any(re.search(pattern, text_lower) for pattern in salary_patterns):
        indicators.append("Unrealistic or unusually high salary claim")

    # 2. No experience required
    if "no experience" in text_lower or "without experience" in text_lower:
        indicators.append("No experience required")

    # 3. Urgent hiring language
    urgent_words = [
        "urgent hiring",
        "hiring immediately",
        "immediate joining",
        "apply now",
        "limited positions",
        "act now"
    ]

    if any(word in text_lower for word in urgent_words):
        indicators.append("Urgent hiring language")

    # 4. Payment-related requests
    payment_words = [
        "registration fee",
        "application fee",
        "processing fee",
        "pay a fee",
        "send money",
        "deposit money",
        "payment required"
    ]

    if any(word in text_lower for word in payment_words):
        indicators.append("Requests for payment or fees")

    # 5. Suspicious messaging platforms
    if "telegram" in text_lower:
        indicators.append("Telegram contact mentioned")

    if "whatsapp" in text_lower:
        indicators.append("WhatsApp contact mentioned")

    # 6. Too-good-to-be-true promises
    suspicious_promises = [
        "get rich",
        "easy money",
        "guaranteed income",
        "guaranteed job",
        "work from home and earn"
    ]

    if any(word in text_lower for word in suspicious_promises):
        indicators.append("Potentially unrealistic earning promise")

    return indicators
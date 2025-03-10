

def validate_password(value: str) -> str:
    """Valida una contraseña según los requisitos de seguridad."""

    if len(value) < 8:
        raise ValueError("Password must be at least 8 characters long")

    conditions = {
        "one uppercase letter": any(c.isupper() for c in value),
        "one lowercase letter": any(c.islower() for c in value),
        "one digit": any(c.isdigit() for c in value),
        "one special character": any(c in "!@#$%^&*(),.?\":{}|<>" for c in value)
    }

    missing = [msg for msg, valid in conditions.items() if not valid]
    if missing:
        raise ValueError(f"Password must contain at least {', '.join(missing)}")

    return value

def validate_username(username):
    """Ensure username is not empty."""
    return bool(username.strip())

def validate_password(password):
    """Ensure password meets requirements."""
    return len(password) >= 5

def validate_amount(amount):
    """Ensure amount is a valid number."""
    try:
        return float(amount) > 0
    except ValueError:
        return False

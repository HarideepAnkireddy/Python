def validate_username(username):
    return bool(username.strip())

def validate_password(password):
    return len(password.strip()) >= 5

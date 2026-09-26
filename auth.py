def login(username, password):
    stored_hash = get_password_hash(username)
    if verify_password(password, stored_hash):
        return "Authenticated"
    return "Authentication failed"
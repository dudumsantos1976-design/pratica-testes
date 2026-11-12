def email_valido(email):
    if not email:
        return False
    if "@" not in email:
        return False
    return True

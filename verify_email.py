def verify_email(email):
    char_num = 0
    email_len = len(email)
    ponto = email.find(".")
    arroba = email.find("@")

    for i in range(0, arroba):
        if ('a' <= email[i] <= 'z') or ('A' <= email[i] <= 'Z'):
            char_num += char_num

    if char_num > 0 and arroba > 0 and (ponto - arroba) > 0 and (ponto + 1) < email_len:
        return True

    else:
        return False


verify_email("exemplo@exemplo.com")
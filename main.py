email = 'guihss.cs@gmail.com'


# Exemplo
def verify_email(email):
    prefix = True
    domain = False

    for c in list(email):

        if prefix:

            if c.isalnum() or c == '.':
                continue
            elif c == '@':
                prefix = False
                domain = True
                continue
            else:
                print(c, 'is invalid')
                return False

        elif domain:

            if c.isalnum() or c == '.':
                continue

            else:
                print(c, 'is invalid')
                return False


    if prefix:
        return False

    return True


def verify_date(date):

    pass



def toInt(number):

    pass


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


# ------------------------------------#
def verify_date(date):
    date = input('Digite uma data no formato dd/mm/aaaa: ')
    dia = int(date[0:2])
    mes = int(date[3:5])
    ano = int(date[6:10])

    if len(date) == 10:
        if 0 <= ano <= 9999:
            if 0 < mes <= 12:
                # FEVEREIRO BISSEXTO
                if mes == 2 and (ano % 4) == 0:
                    if 0 < dia <= 29:
                        print(date + ': Data Válida')
                    else:
                        print(date + ' ERRO: FEVEREIRO BISSEXTO possui até 29 dias.')

                # FEVEREIRO 'COMUM'
                elif mes == 2 and (ano % 4) != 0:
                    if 0 < dia <= 28:
                        print(date + ': Data Válida.')
                    else:
                        print(date + '-> ERRO: FEVEREIRO NÃO BISSEXTO possui até 28 dias.')

                # MESES COM 30 DIAS (ABRIL, JUNHO, SETEMBRO, NOVEMBRO)
                elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
                    if 0 < dia <= 30:
                        print(date + ': Data Válida.')
                    else:
                        print(date + '-> ERRO: o mês' + mes + ' Possui até 30 dias.')

                # MESES COM 31 DIAS (JANEIRO, MARÇO, MAIO, JULHO, AGOSTO, OUTUBRO, DEZEMBRO)
                elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
                    if 0 < dia <= 31:
                        print(date + ' é uma data válida.')
                    else:
                        print(date + '-> ERRO: o mês' + mes + ' Possui até 31 dias.')
                else:
                    print(date + '-> ERRO: Data Inexistente.')
            else:
                print(date + '-> ERRO: Insira um mês entre 1 e 12.')
        else:
            print(date + '-> ERRO: Tente um ano entre 0 e 9999.')
    else:
        print(date + '-> ERRO: A data deve possuir 10 caracteres como informado anteriormente, tente novamente.')


# ------------------------------------#
def toInt(stringToInt):
    # stringToInt = input('Digite um valor: ')
    # print(type(num))
    
    try:
        return int(stringToInt)
    except ValueError:
        return float(stringToInt)

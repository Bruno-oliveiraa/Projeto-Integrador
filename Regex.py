import re

def validar_email(email):
    if '@' not in email:
        return False

    # Verificação extra para impedir '..' em qualquer lugar
    if '..' in email:
        return False

    # Expressão regular para validação do e-mail
    padrao_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(padrao_email, email))

# Lista de e-mails para teste
emails = [
    "usuario@dominio.com",
    "usuario@dominio",
    "dominio.com",
    "usuario@dominio..com",
    "mail123@dominio.co.uk"
]

# Testando e mostrando os resultados
for email in emails:
    if validar_email(email):
        print(f"{email} → Válido")
    else:
        print(f"{email} → Inválido")


senha = input("Digite a senha: ")

if (len(senha) >= 8 and
    any(c.isupper() for c in senha) and
    any(c.islower() for c in senha) and
    any(c.isdigit() for c in senha) and
    any(c in "!@#$%" for c in senha)):
    print("Senha válida")
else:
    print("Senha inválida")
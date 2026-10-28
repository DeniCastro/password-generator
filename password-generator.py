import secrets
import string

# Caracteres permitidos: letras, números e símbolos (sem espaço)
caracteres = string.ascii_letters + string.digits + string.punctuation

# Quantidade de caracteres da senha
senha_length = 16

# Gera a senha com uma fonte aleatória segura
senha = ''.join(secrets.choice(caracteres) for _ in range(senha_length))

print(f"Sua senha gerada é: {senha}")
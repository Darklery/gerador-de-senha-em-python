import random
import string

def generate_password(length):
    letters = string.ascii_letters
    digits = string.digits
    punctuations = string.punctuation

    # Combina as listas de caracteres possíveis
    all_chars = letters + digits + punctuations

    # Seleciona aleatoriamente caracteres a partir da lista
    password = ''.join(random.choices(all_chars, k=length))

    return password

# Pedindo para o usuário informar o comprimento da senha desejada
length = int(input("Digite o comprimento da senha: "))

# Gerando e imprimindo a senha
password = generate_password(length)
print("Sua senha gerada é: ", password)

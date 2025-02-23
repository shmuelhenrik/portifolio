import random
import string
letras = string.ascii_letters
numeros = string.digits
caracteres_especiais = string.punctuation
caracteres = letras + numeros + caracteres_especiais
tamanho =int(input("Digite o tamanho da senha: "))
senha = ''.join(random.choice(caracteres) for i in range(tamanho))
print(f"Senha:{senha}")
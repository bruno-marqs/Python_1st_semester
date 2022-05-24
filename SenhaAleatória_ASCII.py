import string
import secrets

def senhaSegura():
    tipo = string.ascii_letters + string.digits + string.punctuation
    senha = ''
    for i in range(qnt):
        senha += secrets.choice(tipo)
    return senha

input('Clique ENTER para gerar uma senha aleatória')
qnt = int(input('Quantos dígitos quer o tamanho de sua senha, entre 7 a 10: '))
print(f'Sua senha é {senhaSegura()}')
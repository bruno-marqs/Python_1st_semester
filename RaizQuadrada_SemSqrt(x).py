## IMPORTANTE ##
# é possível achar a raiz de um número N contando quantos números ímpares consecutivos a partir de 1 somam igual a N.
# veja a seguir:

input('Clique ENTER para iniciar')

print('Calcule a raiz quadrada inteira de um número. Sem usar sqrt()')
num = int(input('Digite o número: '))
count = 0
soma = 0
while soma != num:
    for x in range(1, num, 2): #selecionar apenas os números ímpares
        soma += x              #somar os números até atingir o input
        count += 1             #contar quantas vezes fez o loop
        if num == soma:
            break
print(f'A raiz quadrada de {num} é igual a {count}')
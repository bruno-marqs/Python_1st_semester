input('Clique ENTER para iniciar')
print('Insira um número e verifique se ele é primo. Digite O para encerrar')
num = 1
while num != 0:
    num = int(input('Digite um numero: '))
    divisores = 0
    for divisor in range(1, num):
        if num % divisor == 0:
            divisores = divisores + 1
            if divisores > 1:
                break
    if divisores > 1:
        print(f'{num} NÃO É um número primo.')
    elif num == 1 or num == 0:
        print(f'{num} NÃO É um número primo')
    else:
        print(f'{num} É um número primo.')
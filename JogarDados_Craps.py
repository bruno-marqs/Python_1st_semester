import random

def lancarDados():
    return random.randint(2, 12)

escolha = 0
ponto = 0
print('Vamos jogar Craps?')

while escolha != 2:
    escolha = int(input('Escolha:\n [1] para jogar os dados\n [2] para sair:\n'))
    if escolha == 2:
        print('Você escolheu sair do jogo. Até mais')
        break
    elif escolha == 1:
        valor = lancarDados()
        print(f'Você lançou os dados. O resultado foi {valor}')
        if valor == 7 or valor == 11:
            print(f'Você tirou {valor}, isso é um NATURAL. Você ganhou! Parabéns!')
            break
        elif valor == 2 or valor == 3 or valor == 12:
            print(f'Você perdeu porque tirou {valor}. Quem sabe tenha sorte na próxima vez...')
            break
        else:
            ponto = valor
            while escolha != 2:
                escolha = int(input('Escolha:\n [1] para jogar os dados novamente\n [2] para sair:\n'))
                if escolha == 2:
                    print('Você escolheu sair do jogo. Até mais')
                    break
                elif escolha == 1:
                    valor = lancarDados()
                    print(f'Você lançou os dados novamente. O resultado foi {valor}')
                    if valor == 7:
                        print('Você tirou 7 antes de repetir o seu ponto. Você perdeu')
                        break
                    elif ponto == valor:
                        print('Você repetiu o seu ponto. Você ganhou!')
                        break
        break
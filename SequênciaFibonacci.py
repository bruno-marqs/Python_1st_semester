input("Clique Enter para iniciar")
print("Escolha um número n e verifique os n primeiros números da sequência de Fibonacci.")

numb1 = 0
numb2 = 1
count = 0
sequencia = int(input("Insira aqui um número de ordem da sequência Fibonacci: "))

while count < sequencia:
    count += 1  # contador para parar o while
    numb3 = numb1 + numb2  # cálculo da sequência fibonacci (o terceiro número é igual a soma dos dois anteriores)
    numb1 = numb2
    numb2 = numb3
    print(f"{numb1},", end=" ")
print("...\n")
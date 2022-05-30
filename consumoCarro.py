print('Em tempo de crise, compare o desempenho e economia de cinco carros')
carro = []
desemp = []
consumo = []
despesa = []
for i in range(5):
    carro.append(input(f'Insira aqui o nome do {i+1}º carro: '))
    desemp.append(input('Insira aqui a desempenho (km/L): ').replace(',', '.'))
dist = float(input('Qual a distância a ser percorrida, em km? ').replace(',', '.'))
preco = float(input('Qual o preço da gasolina, com dois decimais? ').replace(',', '.'))
for x in range(5):
    consumo.append(dist / float(desemp[x]))
    despesa.append(preco * consumo[x])
print('')
for j in range(5):
    print(f'Veículo {j+1}\nNome: {carro[j]}\nKm/L: {desemp[j]}')
print('\nRelatório Final')
for m in range(5):
    print(f'{m+1} - {carro[m]}  -  {desemp[m]} - {consumo[m]:.2f} litros  -  R${despesa[m]:.2f}')
minCons = min(consumo)
minCar = consumo.index(minCons)
print(f'O menor consumo é do {carro[minCar]}.')
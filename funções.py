# EP - Design de Software
# Equipe: Jonas Bonfá Pelegrina e Layne Pereira da Silva
# Data: 16/10/2020


import random

# Listas com todas as 52 cartas do baralho
cartas_baralho_paus = [1,2,3,4,5,6,7,8,9,0,0,0,0]
cartas_baralho_copas = [1,2,3,4,5,6,7,8,9,0,0,0,0]
cartas_baralho_espadas = [1,2,3,4,5,6,7,8,9,0,0,0,0]
cartas_baralho_ouros  = [1,2,3,4,5,6,7,8,9,0,0,0,0]


# Listas com as 52 cartas juntas
cartas_totais = cartas_baralho_paus + cartas_baralho_copas + cartas_baralho_espadas + cartas_baralho_ouros

# Sorteia a quantidade de cartas desejadas
def sorteia_cartas(quantidade):
    sorteados = []
    i = 0
    while quantidade > i:
        sorte = random.randint(0,51)
        sorteados.append(cartas_totais[sorte])
        i += 1
    
    return sorteados


print(sorteia_cartas(2))
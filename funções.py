# EP - Design de Software
# Equipe: Jonas Bonfá Pelegrina e Layne Pereira da Silva
# Data: 16/10/2020

import random

# Listas com todas as 52 cartas do baralho (1 Baralho)
cartas_baralho_paus = [1,2,3,4,5,6,7,8,9,0,0,0,0]
cartas_baralho_copas = [1,2,3,4,5,6,7,8,9,0,0,0,0]
cartas_baralho_espadas = [1,2,3,4,5,6,7,8,9,0,0,0,0]
cartas_baralho_ouros  = [1,2,3,4,5,6,7,8,9,0,0,0,0]


# Listas com as 52 cartas juntas (1 baralho)
cartas_totais = cartas_baralho_paus + cartas_baralho_copas + cartas_baralho_espadas + cartas_baralho_ouros

baralhos_6 = cartas_totais * 6
baralhos_8 = cartas_totais * 8


# Sorteia a quantidade de cartas desejadas
def sorteia_cartas(quantidade,baralhos):
    if baralhos == 1:
        sorteados = []
        i = 0
        while quantidade > i:
            sorte = random.randint(0,51)
            sorteados.append(cartas_totais[sorte])
            i += 1
        return sorteados
    elif baralhos == 6:
        sorteados = []
        i = 0
        while quantidade > i:
            sorte = random.randint(0,51)
            sorteados.append(baralhos_6[sorte])
            i += 1
        return sorteados
    elif baralhos == 8:
        sorteados = []
        i = 0
        while quantidade > i:
            sorte = random.randint(0,51)
            sorteados.append(baralhos_8[sorte])
            i += 1
        return sorteados

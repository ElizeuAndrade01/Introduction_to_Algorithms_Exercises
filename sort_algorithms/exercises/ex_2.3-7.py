#Questão 2.3-7: Descreva um algoritmo de tempo Θ(n lg n) que, dado um conjunto S de n inteiros e um outro inteiro x,
#determine se existem ou não dois elementos em S cuja soma seja exatamente x.

#Pensamento de solução: Primeiramente ordenar a lista aleatória que por si só vai levar O(n log n)
#através do sort, em seguida fazer uma busca de 2 ponteiros, um no início e um no fim da lista o que
#vai levar a O(n) (Podemos ignorar já que n log n é superior), ao percorrer a lista retornará se conseguiu
#ou não achar 2 valores cuja soma seja igual ao valor pedido.

import random

def Popular_Lista(n, qnt):
    return n.append(random.randint(-50, 50) for _ in range(qnt))

def algoritmo_soma(lista, valor):
    #Ordenando
    lista.sort() #O(n lg n)

    #Busca com 2 ponteiros
    lp = 0
    rp = len(lista)-1

    while lp < rp:
        soma = lista[lp] + lista[rp]
        
        if soma == valor:
            print(f"Encontrado! {lista[lp]} + {lista[rp]} = {valor}")
            return True
            
        elif soma < valor:
            # Se a soma é menor que o alvo, precisamos de um número maior.
            # Como a lista está ordenada, avançamos o ponteiro da esquerda.
            lp += 1
            
        else:
            # Se a soma é maior que o alvo, precisamos de um número menor.
            # Recuamos o ponteiro da direita.
            rp -= 1
            
    print("Nenhum par encontrado.")
    return False

nova_lista = [-3, -5, 12, 13, 22, 10, 3, 5, 2, 1, 0 , -22, -55, -103, 123, 74, 30, 20, 40, 37, 21, 7]

algoritmo_soma(nova_lista, -95)
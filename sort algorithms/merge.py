#Chapter 2 - Divide to Conquer

#A estratégia aqui é simples, pegar uma lista de números aleatórios e dividir todas até que sobre apenas 1 elemento
#por lista através da recursão, a partir daí ir comparando elemento por elemento e retornando um merge com os numeros maiores
#sempre à direita e os menores à esquerda. O resultado é uma lista ordenada utilizando recursão.

class MergeSort:
    def __init__(self, arr):
        self.A = arr

    def mergesort(self, p, r):

        if p<r :
            q = (p+r)//2

            self.mergesort(p, q)
            self.mergesort(q + 1, r)

            self.merge(p, q, r)

    
    def merge(self, p, q, r):
        n1 = q - p + 1
        n2 = r - q
        L = [0]*(n1+1)
        R = [0]*(n2+1)
        for i in range(n1):
            L[i] = self.A[p+i]
        for j in range(n2):
            R[j] = self.A[q+1+j]
        L[n1] = float('inf')
        R[n2] = float('inf')
        i=0
        j=0
        for k in range (p, r+1):
            if L[i]<=R[j]:
                self.A[k] = L[i]
                i = i+1
            else:
                self.A[k] = R[j]
                j = j+1

lista = [1,9,4,7,5,99,7,55,33,24,64,45,3,234,64,5]

merging = MergeSort(lista)
print("Lista Original: ", lista)

merging.mergesort(0, len(lista)-1)
print("Lista ordenada por Merge Sort: ", merging.A)
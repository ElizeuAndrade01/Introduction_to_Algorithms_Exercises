#Encontrar intervalo de dias de maior ganho (Variância de ações numa bolsa de valores)

import random

class Find_Max_Crossing_Subarray:

    def find_m_c_s(self, A, low, high):
        
        if high == low:
            return(low, high, A[low])
        else:
            mid = (low+high)//2
            (leftLow, leftHigh, leftSum) = self.find_m_c_s(A, low, mid)
            (rightLow, rightHigh, rightSum) = self.find_m_c_s(A, mid+1, high)
            (crossLow, crossHigh, crossSum) = self.sums(A, low, mid, high)
        if leftSum>=rightSum and leftSum >= crossSum:
            return (leftLow, leftHigh, leftSum)
        elif rightSum>=leftSum and rightSum>= crossSum:
            return (rightLow, rightHigh, rightSum)
        else:
            return (crossLow, crossHigh, crossSum)

    def sums(self, A, low, mid, high):
        maxLeft = 0
        maxRight = 0
        leftSum = -float('inf')
        genSum = 0;
        for i in range(mid, low-1, -1):
            genSum = genSum + A[i]
            if genSum > leftSum:
                leftSum = genSum
                maxLeft = i
        rightSum = -float('inf')
        genSum = 0;
        for j in range(mid+1, high+1):
            genSum = genSum+A[j]
            if genSum > rightSum:
                rightSum = genSum
                maxRight = j
        return(maxLeft, maxRight, leftSum+rightSum)

def Popular_Lista(n):
    return [random.randint(-50, 50) for _ in range(n)]

novoArray = Popular_Lista(10)

print("O array de variação diária é: ", novoArray)

objAcharSubarray = Find_Max_Crossing_Subarray()

resultados = objAcharSubarray.find_m_c_s(novoArray, 0, len(novoArray)-1)

print(f"\nResultado Final:")
print(f"Índice Inicial: {resultados[0]}")
print(f"Índice Final: {resultados[1]}")
print(f"Soma Máxima: {resultados[2]}")
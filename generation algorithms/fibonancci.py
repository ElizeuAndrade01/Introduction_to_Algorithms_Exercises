#Os Números de Fibonacci são definidos pela seguinte recorrência:
#F1 = 0
#F2 = 1
#Fi = Fi-1 + Fi-2

#Isso implica no algoritmo a seguir:

class Fibonacci:
    def __init__(self, qnt_n):
        self.qnt_n = qnt_n

    def seq_fibonacci(self):
        lista_fibonacci = [0, 1]
        for i in range(2, self.qnt_n-1):
            lista_fibonacci.append(lista_fibonacci[i-2] + lista_fibonacci[i-1])

        print(lista_fibonacci)

nova_lista = Fibonacci(50)

nova_lista.seq_fibonacci()
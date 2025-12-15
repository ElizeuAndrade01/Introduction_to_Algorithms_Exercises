#insertion code pseudocode
#
#for j = 2 para Aconjunto
#   chave = A[j]
#   //inserir na sequência ordenada A[1, ...j-1]
#   i = j-1
#   while i>0 e A[i]>chave
#       A[i+1] = A[i]
#       i = i-1
#   A[i+1] = chave

#Insertion sort em python

class InsertionSort:
    def __init__(self, lista):
        self.conjunto = lista
    
    def insert_sort(self):
        for j in range(1, len(self.conjunto)):
            key = self.conjunto[j]
            i = j-1
            while i>=0 and self.conjunto[i]>key:
                self.conjunto[i+1] = self.conjunto[i]
                i = i-1
            self.conjunto[i+1] = key
        print("a saída crescente é: ", self.conjunto)
    
    def insert_sort_right_left(self):
        listSize = len(self.conjunto)
        for j in range(listSize-1, 0, -1):
            key = self.conjunto[j]
            i = j+1
            while i <= listSize-1 and self.conjunto[i] < key:
                self.conjunto[i-1] = self.conjunto[i]
                i = i+1
            self.conjunto[i-1] = key
        print("a saída do sort right to left crescente é: ", self.conjunto)

    def insert_sort_dec_order(self):
        for j in range(1, len(self.conjunto)):
            key = self.conjunto[j]
            i = j-1
            while i>=0 and self.conjunto[i]<key:
                self.conjunto[i+1] = self.conjunto[i]
                i = i-1
            self.conjunto[i+1] = key
        print("a saída decrescente é: ", self.conjunto)

#lista = [2,4,6,5,7,4,1,3,2,1,10,22,12,33,23,41,1,2,3,3,7,10,50,2,39,11]
#insert = InsertionSort(lista);
#insert.insert_sort();
#insert.insert_sort_right_left()
#insert.insert_sort_dec_order()
class SimpleSearch:
    def __init__(self, lista, v):
        self.conjunto = lista
        self.req_value = v
    
    def simṕle(self):
        for j in range(0, len(self.conjunto)):
            if self.conjunto[j] == self.req_value:
                return print("Value", self.req_value, "founded in indice", j)
        return print("Nada foi achado.")
        
        
lista = [45,50,12,21,42,33]
v = 45

busca = SimpleSearch(lista, v)
busca.simṕle()
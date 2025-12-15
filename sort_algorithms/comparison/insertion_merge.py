#This archive searches to populate different lenght lists with random numbers,
#then get those lists, sort them in both types of sorts and then compare them
#the Graphics of comparison are in the README of this directory

import sys
import os
import time
import random
import pandas as pd
import matplotlib.pyplot as plot

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, '..')
sys.path.append(parent_dir)

import insertion
import merge


def populateLists(n):

    return [random.randint(0,99999) for _ in range(n)]

sizes = [100, 1000, 10000, 20000]

results = []


def insertion_results():

    for size in sizes:
        print("Testando tempo de execução Insertion Sort para lista randômica de tamanho: ", size)

        #Gerando lista
        originalInsertList = populateLists(size)

        insertionList = originalInsertList.copy()

        #Declarando objeto
        insertionListObj = insertion.InsertionSort(insertionList)
        
        #Sorting
        startTime = time.time()
        insertionListObj.insert_sort()
        endTime = time.time()
        finalTime = endTime-startTime

        results.append({"Size": size, "Algorithm Type": "Insertion-Sort", "Execution Time": finalTime})

        print("O tempo de execução foi de: ", finalTime)
    return results

def merge_results():

    for size in sizes:
        print("Testando tempo de execução Merge Sort para lista randômica de tamanho: ", size)

        #Gerando lista
        originalMergeList = populateLists(size)

        mergeList = originalMergeList.copy()

        #Declarando objeto
        mergeListObj = merge.MergeSort(mergeList)
        
        #Sorting
        startTime = time.time()
        mergeListObj.mergesort(0, size-1)
        endTime = time.time()
        finalTime = endTime-startTime

        results.append({"Size": size, "Algorithm Type": "Merge-Sort", "Execution Time": finalTime})

        print("O tempo de execução para Merge Sort foi de: ", finalTime)
    return results



insertion_results()
merge_results()

#Plotting the Data

def createPlot(results):
    df = pd.DataFrame(results)

    #Salvando Dados
    df.to_csv('comparações_resultados.csv', index = False)
    print("Dados salvos em comparações_resultados.csv")

    # Prepara o plot
    plot.figure(figsize=(10, 6))
    
    # Separa os dados para plotar duas linhas
    for tipo in df['Algorithm Type'].unique():
        subset = df[df['Algorithm Type'] == tipo]
        plot.plot(subset['Size'], subset['Execution Time'], marker='o', label=tipo)

    plot.title('Comparação de Performance: Insertion Sort vs Merge Sort')
    plot.xlabel('Tamanho da Lista (N)')
    plot.ylabel('Tempo de Execução (segundos)')
    plot.legend()
    plot.grid(True)
    
    plot.savefig('comparacao_algoritmos.png')
    print("Gráfico salvo como 'comparacao_algoritmos.png'")
    
    plot.show()

createPlot(results)
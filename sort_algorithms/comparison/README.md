# 📊 Análise de Complexidade de Algoritmos
> Estudo prático e análise comparativa de algoritmos de ordenação baseados na obra "Introduction to Algorithms" (CLRS).

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

## 🧐 Sobre este Diretório

Este Diretório contém implementações "from scratch" (do zero) de comparação dos algorítimos para analisar seus comportamentos assintóticos na prática, tanto no terminal quanto em um gráfico.

O objetivo é validar a teoria do **Big O notation** comparando algoritmos quadráticos $O(n^2)$ contra log-lineares $O(n \log n)$.

### 📈 Resultados da Análise

O gráfico abaixo foi gerado automaticamente pelo script de comparação deste repositório, comparando o tempo de execução para vetores de tamanho N = 100 até N = 20.000 populados com
numeros aleatórios que vão de 0 a 99999.

<p align="center">
  <img src="../misc/comparacao_algoritmos.png" alt="Gráfico Comparativo" width="600"/>
</p>

**Observações:**
* **Insertion Sort:** Apresenta uma curva parabólica clara, validando sua complexidade $O(n^2)$. Torna-se inviável para grandes volumes de dados. [Observe que em termo de volumes de dados 20.000
  ainda é uma quantia irrisória.]
* **Merge Sort:** Mantém um crescimento quase linear ("linearithmic"), validando $O(n \log n)$, sendo extremamente eficiente para grandes datasets. [a linha se segue quase imperceptível em crescimento.]

---

## 🚀 Como Executar

Siga os passos abaixo para configurar o ambiente, instalar as dependências e rodar o comparativo de performance.

### Pré-requisitos
* **Python 3.10** ou superior instalado.
* **Git** instalado.

### Passo a Passo

1. **Clone o repositório**
2. **Crie um Ambiente Virtual**
   * **Linux / macOS:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
   * **Windows:**
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
3. **Instale as dependências**
   ```bash
   pip install matplotlib pandas
4. **Execute o Script de comparação**
   ```bash
   python sort_algorithms/comparison/insertion_merge.py


## 🛠️ Estrutura do Projeto

```text
/
|...
├── sort_algorithms/
|   ├── comparison/
|   |    └── insertion_merge.py       # Script de comparação de diversos cenários e plotagem de gráficos
|   ├── heap.py                       # Futura Implementação do Heap Sort
│   ├── insertion.py                  # Implementação do Insertion Sort
│   └── merge.py                      # Implementação do Merge Sort (Divisão e Conquista)
|   └── quick.py                      # Futura Implementação do Quick Sort
│
└── .gitignore

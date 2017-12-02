########### parte 2 Bubble sort##################
n = int(input("Digite o numero de posições do vetor: "))
vet = [0] * n
for i in range(n):
    vet[i] = int(input("Digite os elementos do vetor: "))
print("Antes de ordenar:",vet)

# Bubble Sort
for i in range(n):
    bolha = i
    while bolha > 0:
        if vet[bolha] < vet[bolha-1]:
            aux = vet[bolha-1]
            vet[bolha-1] = vet[bolha]
            vet[bolha] = aux
            bolha -= 1 # mesmo que bolha = bolha - 1
            print("Processo de ordenaçao",vet)
        else:
            bolha = 0
print("Ordenado:",vet)


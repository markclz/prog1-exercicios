
################### Parte 1 Selection ##########################

n = int(input("Digite o numero de posições do vetor: "))
vet = [0] * n
for i in range(n):
    vet[i] = int(input("Digite os elementos do vetor: "))
print("Antes de ordenar:",vet)
#onde ocorrre o processo de ordenação
#usando selection sort
for i in range(len(vet)-1):
    posm = i
    for j in range(i+1,len(vet)):
        if vet[j] < vet[posm]:
            posm = j
    aux = vet[i]
    vet[i] = vet[posm]
    vet[posm] = aux
print("Ordenado:",vet)






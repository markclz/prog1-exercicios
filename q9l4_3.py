##################### Parte 3 Inserction ###################3

n = int(input("Digite o numero de posições do vetor: "))
vet = [0] * n
for i in range(n):
    vet[i] = int(input("Digite os elementos do vetor: "))
print("Antes de ordenar:",vet)
for i in range(1,n):
    chave = vet[i]
    j = i - 1
    while j >= 0 and vet[j] > chave:
        vet[j+1] = vet[j]
        j = j - 1
    vet[j+1] = chave
print("Ordenado:", vet)


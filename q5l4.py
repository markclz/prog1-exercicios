
n = int(input("Digite o tamanho do vetor: "))
vet = []
for i in range(n):
    vet.append(int(input("Preencher vetor: ")))
print("Conjunto A =",vet)
print("Numero de elementos: ",len(vet))
soma = 0
for i in range(n//2):
    soma = soma + (vet[i] - vet[n-1-i]) ** 2
print("A soma é:",soma)






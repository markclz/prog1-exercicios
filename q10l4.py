n = int(input("Digite o numero de elemtos do vetor:"))
vet = [0] * (n + 1)
for i in range(n+1):
    vet[i] = int(input("Digite o coeficiente: "))


for i in range(10):
    x = int(input("Digite o valor de X: "))
    soma = 0
    for j in range(n+1):
        soma+= vet[j] * x**j
    print("P(" +str(x)+") = ",soma)



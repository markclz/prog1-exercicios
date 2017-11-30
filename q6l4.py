n = int(input("Digite a quantidade de elementos do conjunto: "))
vet = []
for i in range(n):
    vet.append(float(input("Digite os elementos do conjunto A:")))
print(vet)
print("O tamanho do vetor é:",len(vet))
b = [0] * n
for i in range(len(vet)):
    if i % 2 == 1:
        b[i] = vet[i]/2
    else:
        i + 1 % 2 == 0
        b[i] = vet[i] * 3
print("B:",b)





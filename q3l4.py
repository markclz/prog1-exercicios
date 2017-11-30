#Nao consegui comcluir#

n = int(input("Digite a quantidade de elementos do vetor:"))
vet = [0] * n
#vet2 =[]
for i in range(n):
    vet[i] = int(input("Digite o valor do elemento da posição " + str(i) + ":"))
    
print(vet)
print(len(vet))


# para percorrer o vetor
i = 0 

# perceba que len(vet) diminui a cada vez que removemos um elemento do vetor
while i < len(vet):
    # enquanto a quantidade do elemento vet[i] for maior que 1
    while vet.count(vet[i]) > 1:
        vet.remove(vet[i])
    i += 1

print(vet)
print(len(vet))

# daqui para baixo peguei da internet
i = 0
while i < len(vet)-1:
    j = i + 1
    while j < len(vet):
        if vet[i] == vet[j]:
            vet.pop(j)
        else:
            j = j + 1
    i = i + 1
for n in vet:
    print(n, end =" ")
print()



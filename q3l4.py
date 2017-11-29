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

"""
vet2 = vet
print(vet2)

for i in range(len(vet)):
    if vet[i] == i:
        print(i)

"""













#for i in range(len(vet)):





vet = [40,5,2,20]
# percorre o vetor
# até a penultima posição
# no caso len que vale 4 menos 1
print(vet)
for i in range(len(vet)-1):
    posm = i
    for j in range(i+1,len(vet)):
        if vet[j] < vet[posm]:
            posm = j
    aux = vet[i]
    vet[i] = vet[posm]
    vet[posm] = aux
    print(vet)




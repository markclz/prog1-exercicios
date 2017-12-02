n = int(input("Digite o numero de elementos do vetor: "))
vet = [0] * n
c = 0
for i in range(n):
    c+=1
    vet[i] = c # em vez de aplicar o incremento da variavel c para preencer o vetor com as 25 posições podeira usar um input e o usuario ir colocando
print(vet)


# verifica qual é o maior elemento
maior = 0
j = 0

while j < n:
    if vet[j] > maior:
        maior = vet[j]
    j = j + 1
print("O maior elemento é:", maior)

# verifica qual é o menor elemento
menor = 25
k = 0
while k < n:
    if vet[k] < menor:
        menor = vet[k]
    k = k + 1
print("O menor elemento é:", menor)







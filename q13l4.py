
n = int(input("Digite o numero de posições dos vetores: "))
#ambos os vetores tem a mesma dimensão, logo são multiplicados por n
veta = [0] * n
vetb = [0] * n
#for para preencher o vetor A
for i in range(n):
    veta[i] = int(input("Digite o valor da posição " +str(i)+ " do vetor A:"))
print("vetor A:", veta)

#for para preencher o vetor B
for i in range(n):
    vetb[i] = int(input("Digite o valor da posição " +str(i)+ " do vetor B:"))
print("vetor B:", vetb)
# uma variavel soma que recebera o valor do escalar
#que sera obtido atraver do for, onde a soma vai recebendo
#veta[0] * vetb[0] até veta[n] * vetb[n] e resulta no produto escalar
soma = 0
for i in range(n):
    soma = soma + (veta[i]*vetb[i])
print("Escalar = ",soma)






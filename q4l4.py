# cria um vetor com 50 numeros inteiros de 1 a 50

a = 0
v = []
vr = []
for i in range(50):
    a = a + 1
    v.append(a)
print(v)

# verifica dentro do vetor com os 50 elementos quais correspondem a um dia do mes
for i in range(len(v)):
    if v[i] > 0 and v[i] <= 31:
        vr.append(v[i])
print("Vetor Resultante:",vr)
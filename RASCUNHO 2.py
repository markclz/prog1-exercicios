# criamos um vetor com os pesos
n = int(input("Digite a quantidade de pessoas para calcular seu peso na terra e na lua:"))
vet = []
for i in range(n):
    vet.append(float(input("Digite o peso da  pessoa " + str(i)+ ":" )))
print(vet)
gt = 9.8
gl = 1.67

print("MASSA NA TERRA")
for i in range(len(vet)):
    print("Massa igual",vet[i],"Kg")
    pesot = (vet[i]*gt)
    print("Peso da pessoa na terra é igual a:",pesot,"N")
print()
print("MASSA NA LUA")
for i in range(len(vet)):






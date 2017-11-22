n = int(input("Digite a quantidade de pessoas: "))
peso = [0] * n
soma = 0
for i in range(n):
    peso[i] = float(input("Digite o peso da pessoa: " + str(i) + ": "))
    soma = soma + peso[i]
print("A media dos pesos é: ", soma/n)
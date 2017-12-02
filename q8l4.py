n = int(input("Digete o numero de posições do vetor: ")) # a questao pede n igual a 40, mas para ficar mais enxuto reduzi o valor de n
vetQ = [0] * n
vetP = [0] * n
# for que define a quantidade e valor do produto, variando dentro de i, que sofre incremento de 1 em 1 unidade
for i in range(n):
    vetQ[i] = float(input("Digite a quantidade do produto "  +str(i)+  ": "))
    vetP[i] = float(input("Digite o preço da mercadoria" + str(i) + ":" ))
# o sigma virou isso, onde i varia de zero ate o valor de n definido acima, no inicio do programa pelo usuario
faturamento = 0
for i in range(n):
    faturamento += (vetQ[i] * vetP[i])
print("O faturamento é: ",faturamento)








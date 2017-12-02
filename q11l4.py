import random
# na questao sao 50 vezes o valor de n, mas para teste usamos o 10
# facilita a vizualição do programa na hora de executar
n = 10
faces = 6
vet = [0] * n
vetoc = [0] * faces

for i in range(n):
    #usamos o ramdom para sortear as faces do dado que contem de 1 até 6
    face = random.randint(1,6)
    # cada posição de i durante sua iteração recebe um valor sorteado que
    #corresponde a uma face do dado
    vet[i] = face
    #cada face do dado esta associado a uma posicao do vetor
    #nessa posição é a posição face - 1 exemplo: face 1 -> pos 0, face 2 -> pos 1, face 6 -> pos 5
    #assim sorteamos uma face, vamos na posição do vetor associado a face e aumentamos uma unidade
    # para dizer que a face ocorreu mais uma vez
    vetoc[face-1] +=1
    #no calculo da porcentagem, a posição 5 do vetor correspondente a face 6
    # dividida pelo numero total de lançamentos do dado que seria o valor de n. poderiamos por um input no n
    # mas a questao ja define como 50.
print("percentual de ocorrencias:",(vetoc[5]/n * 100),"%")
print("Lançamentos:", vet)



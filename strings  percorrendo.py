# imprime as posições de cada caracter da string
# no for temos o mesmo processo mas enumerando cada posição

nome = "Maria Silva"
for letra in nome:
    print(letra)


nome = "Maria Silva"
for i in range(len(nome)):
    print(i,nome[i])
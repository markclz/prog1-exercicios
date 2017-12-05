

nome = "Maria Silva"
print(nome)

try:
    print("Tentando alterar string diretamente.")
    nome[3] = "t"
except:
    print("Não é possível alterar string assim.")
    print("Você pode transformar a string em uma lista de caracteres e alterar a lista.")
    print("Depois, você converte essa lista para uma string novamente.")

listaNome = list(nome) # converte string em uma lista de caracteres
listaNome[3] = "t"

# converte a lista em uma string. "" é o caractere que existe entre cada caractere da lista
nome = str.join("", listaNome)

print(nome)

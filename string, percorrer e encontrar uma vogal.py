# Acha as vogais dentro de uma string

#a = ("hoje")
#b = (" esta sol")
c =("Ana comeu figo") #a + b
print(c) # hoje esta sol

vogais = "aeiou"
verivogal = []
cont = 0
#com uso do lower podemos converter vogais
#maiusculas para minusculas e assim fazelas
#serem contadas sem restrição
for i in range(len(c)):
    if c[i].lower() in vogais:
        verivogal.append(c[i])
        cont+=1
print(verivogal)
print("numero de vogais =", cont)

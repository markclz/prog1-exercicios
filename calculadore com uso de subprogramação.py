# calculadora com uso de funções

def soma(x,y):
    s = (x+y)
    return s


def sub(x,y):
    su = (x-y)
    return su


def mul(x,y):
    mu = (x*y)
    return mu


def div(x,y):
    d = (x/y)
    return d


def lerOperandos():
    x = int(input("Digite o valor de x:"))
    y = int(input("Digite o valor de y:"))
    return(x,y) #retorna tupla com os valores lidos


op = -1
while op != 0:
    print("Digite 1 se deseja Somar")
    print("Digite 2 se deseja Subtrair")
    print("Digite 3 se deseja Multiplicar")
    print("Digite 4 se deseja Dividir")
    print("Digite 0 se deseja Sair")
    op = int(input("Qual opção voce deseja?"))
    if op == 1:
        a,b = lerOperandos()
        result = soma(a,b)
        print("Soma = ",result)

    elif op == 2:
        a,b = lerOperandos()
        result = sub(a,b)
        print("Subtração =",result)

    elif op == 3:
        a,b = lerOperandos()
        result = mul(a,b)
        print("Multiplicação =",result)

    elif op == 4:
        a,b = lerOperandos()
        result = div(a,b)
        print("Divisão =",result)
    print()





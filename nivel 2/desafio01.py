#faça uma função que pegue um numero e some 1 em cada um dos seus digitos

def up(x):
    valor = str(x)
    lista = [int(valor) + 1 for valor in valor]
    resul = ''.join(map(str, lista))

    return int(resul)
    
print(up(int(input())))

    

from random import choice
from os import system

# só coloquei esse programa no nivel 2 pq quebrei muito a cabeça pra conseguir fazer ele funcionar

palavras = ['smogon', 'maca', 'hendrick']

palavra = choice(palavras)
flag = palavra
none = []
for c in range(1, len(palavra) + 1):
    none.append('-')
none = ''.join(none)
tentativas = 0
letras_usadas = []

print(f'=========JOGO DA FORCA!!!=========')


while True:
        
        print(f'palavra: {none}')
        print(f'tentativas: {tentativas}')
        none = list(none)
        letra = str(input('\ndigite uma letra ')).strip().lower()[0]
        system('cls')

        

        if letra in palavra:
            pos = palavra.index(letra)
            
            
            none[pos] = letra
            palavra = list(palavra)
            palavra[pos] = '-'    
            palavra = ''.join(palavra)

        else:
            tentativas += 1
        none = ''.join(none)
        if none == flag:
            print(f'você ganhou! a palavra era {none}.')
            break
        if tentativas == 6:
            print(f'você perdeu! a palavra correta era {flag}.')
            break
        


    
    
    

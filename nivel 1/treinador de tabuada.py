from random import randint
import time

t = '=' *  10
print('\033[0;32;40m{}TREINADOR DE TABUADA{}'.format(t, t))
jogo = str(input('você quer jogar o jogo?[S/N]')).strip().lower()

tentativas = 0
pontos = 0

if jogo == 's':
    while tentativas <= 2 and pontos <= 9:
        n1 = randint(1, 10)
        n2 = randint(1, 10)
        print('\033[0;31;40mtentativas: {}  \033[0;34;40m\npontos: {}\033[0;32;40m'.format(tentativas, pontos))
        n3 = n1 * n2
        play = int(input('quanto é {} x {}? '.format(n1, n2)))

        if n3 == play:
            print('\033[0;32;40mparabens, você ganhou um ponto!')
            pontos = pontos + 1
            time.sleep(1)
        elif n3 != play:
            tentativas = tentativas + 1
            print('\033[0;33;40mvocê errou, tente novamente.')
            time.sleep(1)

    if pontos == 10:
        print('\033[0;31;40mtentativas: {} \033[0;34;40m\npontos: {}\033[0;32;40m'.format(tentativas, pontos))
        print('\033[1;35;40mvocê ganhou da matematica!!')
        
    if tentativas == 3:
        print('\033[0;31;40mtentativas: {} \033[0;34;40m\npontos: {}\033[0;32;40m'.format(tentativas, pontos))
        print('\033[1;33;41mvocê perdeu!\033[1;30;40m')


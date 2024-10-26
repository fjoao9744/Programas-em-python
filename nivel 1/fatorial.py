import math

n, n1, n2, n3 = int(input('digite um numero para ver o seu fatorial: ')), 1, 1, 0


    #for
for c in range(1, n + 1):
    n1 *= c
    

    #modulo
n1 = math.factorial(n)


    #while
while n != n3 or n > n3:
    n3 += 1
    n1 *= n2
    n2 += 1

    
print('o fatorial de {} é {}'.format(n, n1))




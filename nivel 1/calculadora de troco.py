valor = float(input('Qual sera o valor da compra? '))
pagar = float(input('Qual vai ser o valor pago? '))

#R$100, R$50, R$20, R$10, R$5, R$2 e as moedas de R$1, R$0.50, R$0.25, R$0.10, R$0.05 e R$0.01.
notas100 = notas50 = notas20 = notas10 = notas5 = notas2 = 0
moeda1 = moeda05 = moeda025 = moeda010 = moeda005 = moeda001 = 0

if pagar < valor:
    print('Lamento mas a compra não podera ser efetuada.')
else:
    pagar -= valor
    print('você tera de troco: ', end=' ')
    valor = pagar
    if valor > 0:
        #notas
        while valor > 100:
            valor -= 100
            notas100 += 1
        if notas100 > 0:
            print(f'{notas100} notas de 100', end=' ')
        while valor > 50:
            valor -= 50
            notas50 += 1
        if notas50 > 0:
            print(f'{notas50} notas de 50', end=' ')
        while valor > 20:
            valor -= 20
            notas20 += 1
        if notas20 > 0:
            print(f'{notas20} notas de 20', end=' ')
        while valor > 10:
            valor -= 10
            notas10 += 1
        if notas10 > 0:
            print(f'{notas10} notas de 10', end=' ')
        while valor > 5:
            valor -= 5
            notas5 += 1
        if notas5 > 0:
            print(f'{notas5} notas de 5', end=' ')
        while valor > 2:
            valor -= 2
            notas2 += 1
        if notas2 > 0:
            print(f'{notas2} notas de 2', end=' ')
        #moedas
        if valor == 1:
            valor -= 1
            moeda1 += 1
        if moeda1 > 0:
            print(f'{moeda1} moedas de 1', end=' ')
        while valor > 0.5:
            valor -= 0.5
            moeda05 += 1
        if moeda05 > 0:
            print(f'{moeda05} moedas de 0.5', end=' ')
        while valor > 0.25:
            valor -= 0.25
            moeda025 += 1
        if moeda025 > 0:
            print(f'{moeda025} moedas de 0.25', end=' ')
        while valor > 0.10:
            valor -= 0.10
            moeda010 += 1
        if moeda010 > 0:
            print(f'{moeda010} moedas de 0.10', end=' ')
        while valor > 0.05:
            valor -= 0.05
            moeda005 += 1
        if moeda005 > 0:
            print(f'{moeda005} moedas de 0.05', end=' ')
        while valor > 0.01:
            valor -= 0.01
            moeda001 += 1
        if moeda001 > 0:
            print(f'{moeda001} moedas de 0.01', end=' ')

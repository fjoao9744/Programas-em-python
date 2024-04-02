i = '-' * 4

NMmaior = '' #maior nome x
IMaior = '' #maior idade(nome) x
Midade = 0 #maior idade(numero) x

idadeH = 0 #homem com mais idade(numero) x
idadeM = 0 #mulher com mais idade(numero) x 

MIhomem = '' #homem com maior idade x
MImulher = '' #mulher com maior idade x 
mulherMI = 0 #mulheres maiores de idade(numero) x
homemMI = 0 #homens maiores de idade(numero)

media = 0 

gordos = 0
magros = 0

print('\033[0;33;40m{} ANALISADOR DE DADOS {}\033[m'.format(i,i) )
for p in range(1, 5):
    print('\033[0;33;40m{} {}ª PESSOA {}{}'.format(i, p, i, '\033[m'))
    nome = str(input('\033[0;32;40mnome: \033[m')).strip()
    idade = int(input('\033[0;32;40midade: \033[m'))
    sexo = str(input('\033[0;32;40msexo [M/F]: \033[m')).upper()
    peso = float(input('\033[0;32;40mpeso(kg): \033[m'))
    altura = float(input('\033[0;32;40maltura(m): \033[m'))

    imc = peso // (altura * altura)
    if len(nome) > len(NMmaior):
        NMmaior = nome

    if idade > Midade :
        Midade = idade
        IMaior = nome

    media += idade
    if p == 4:
        media //= 4

    if sexo == 'M' and idade > idadeH:
        idadeH = idade
        MIhomem = nome
    if sexo == 'F' and idade > idadeM:
        idadeM = idade
        MImulher = nome
    
    if sexo == 'F' and idade < 20:
        mulherMI += 1
    if sexo == 'M' and idade < 20:
        homemMI += 1

    if imc < 19:
        magros += 1
    if imc > 25:
        gordos += 1

print('O maior nome é de {} \nA pessoa com a maior idade é {} com {} anos'.format(NMmaior,IMaior, Midade))
print('A media de idade é de {}'.format(media))
print('O homem mais velho é o {} com {} anos, e a mulher é {} com {} anos'.format(MIhomem, idadeH, MImulher, idadeM))
print('Tem {} homens e {} mulheres menores de 20 anos'.format(homemMI, mulherMI))
print('Tem {} gordos e {} magros'.format(gordos, magros))




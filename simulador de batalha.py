print("SIMULADOR DE BATALHA")

from os import system

#fichas
monstros = [
    {"nome": "Goblin guarda", "hp": 16, "atk": 8, "def": 6, "exp": 16, "gil": 18},

    {"nome": "Goblin1", "hp": 8, "atk": 4, "def": 4, "exp": 6, "gil": 6},
    {"nome": "Goblin2", "hp": 8, "atk": 4, "def": 4, "exp": 6, "gil": 6},
    {"nome": "Goblin3", "hp": 8, "atk": 4, "def": 4, "exp": 6, "gil": 6},
    {"nome": "Goblin4", "hp": 8, "atk": 4, "def": 4, "exp": 6, "gil": 6},
    {"nome": "Goblin5", "hp": 8, "atk": 4, "def": 4, "exp": 6, "gil": 6},

    {"nome": "Imp1", "hp": 10, "atk": 6, "def": 5, "exp": 12, "gil": 14},
    {"nome": "Imp2", "hp": 10, "atk": 6, "def": 5, "exp": 12, "gil": 14},
    {"nome": "Imp3", "hp": 10, "atk": 6, "def": 5, "exp": 12, "gil": 14}

    ]
    
players = [
    {"nome": "Hendrick", "hp": 35, "atk":17, "def": 1},
    {"nome": "Henki", "hp": 25, "atk":10, "def": 1},
    {"nome": "Cristian", "hp": 26, "atk":8, "def": 5},
    {"nome": "Dudu", "hp": 29, "atk":13, "def": 1},
    {"nome": "Otavio", "hp": 17, "atk":2, "def": 1},
    {"nome": "Yoshi", "hp": 14, "atk":6, "def": 1}
    ]


#adicionar monstro
while True:
    for i, enty in enumerate(monstros):
        if i == 0:
            print('N. Nome Hp')
            print('---------------')
        print(f'\033[0;31;40m{i}- {enty["nome"]} {enty["hp"]}\033[m')
    print('---------------')

    adicionar = str(input("Adicionar mais um monstro[S/N]? ")).upper().strip()
    if adicionar == "N":
        system("cls")
        break

    monstros.append({"nome": input("nome: "), "hp": int(input("hp: ")), "atk": int(input("atk: ")), "def": int(input("def: ")), "exp": int(input("exp: ")), "gil": int(input("gil: "))})


    system("cls")

while True:

    #interface 
    for i, enty in enumerate(monstros):
        if i == 0:
            print('N. Nome Hp')
            print('---------------')
        print(f'\033[0;31;40m{i}- {enty["nome"]} {enty["hp"]}\033[m')
    print('---------------')

    for i, enty in enumerate(players):
        print(f'\033[0;32;40m{i}- {enty["nome"]} {enty["hp"]}\033[m')

    #ataque
    atacante = int(input("Quem atacara?\n\033[0;31;40mMonstros[0]\033[m \n\033[0;32;40mPlayers[1]\033[m \n"))
    system("cls")
    if atacante == 0: #monstro atacando

        for i, enty in enumerate(monstros):
            if i == 0:
                print('---------------')
            print(f'\033[0;31;40m{i}- {enty["nome"]} {enty["hp"]}\033[m')
        print('---------------')

        monstro = int(input("Quem vai atacar? \n"))

        for i, enty in enumerate(players):
            print(f'\033[0;32;40m{i}- {enty["nome"]} {enty["hp"]}\033[m')

        player = int(input("Quem recebera dano? \n"))

        dano = monstros[monstro]["atk"] - players[player]["def"]

        if dano <= 0:
            dano = 1
        
        players[player]["hp"] -= dano
        print(f'O {players[player]["nome"]} recebeu {dano}')


    if atacante == 1: #player atacando

        for i, enty in enumerate(players):
            if i == 0:
                print('---------------')
            print(f'\033[0;32;40m{i}- {enty["nome"]} {enty["hp"]}\033[m')
        print('---------------')

        player = int(input("Quem vai atacar? \n"))

        for i, enty in enumerate(monstros):
            print(f'\033[0;31;40m{i}- {enty["nome"]} {enty["hp"]}\033[m')

        monstro = int(input("Quem recebera dano? \n"))

        dano = players[player]["atk"] - monstros[monstro]["def"]

        if dano <= 0:
            dano = 1
        
        monstros[monstro]["hp"] -= dano
        print(f'O {monstros[monstro]["nome"]} recebeu {dano}')
    system("cls")


    todos_mortos = True
    for _ in monstros:
        if _["hp"] >= 0:
            todos_mortos = False

    if todos_mortos == True:
        break

exp = 0
for _ in monstros:
    exp += _["exp"]
gil = 0
for _ in monstros:
    gil += _["gil"]


print(f"Os monstros droparam {exp} de exp e {gil} de gil")



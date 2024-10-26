from time import localtime
from os import system

mensagens = []

def hora():
    return f"{localtime().tm_hour - 3}:{localtime().tm_min}"

while True:
    system("clear")
    for _ in mensagens:
        print(_)
    msg = input("digite uma mensagem: ")
    mensagens.append(f"{hora()}- {msg}")






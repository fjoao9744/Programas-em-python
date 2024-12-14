from tkinter import *
from random import randint, choices
from connect_db import *

app = Tk()
app.geometry("300x300")

operações = ["x", "÷", "+", "-"]
pontos = 0

game_frame = Frame(app)
game_frame.place(relwidth=1, relheight=1)

game_over = Frame(app)
game_over.place(relwidth=1, relheight=1)

def errado(event=None):
    resposta_entry.delete(0, END)
    operação["text"] = f"{randint(0, 10)} {choices(operações)[0]} {randint(0, 10)}"
    vidas_label_num["text"] = str(int(vidas_label_num["text"]) - 1)  # Corrigido para int

    if int(vidas_label_num["text"]) == 0:
        global pontos
        pontos_label_GM['text'] = f"Você fez {pontos} pontos"

        game_frame.place_forget()
        game_over.place(relwidth=1, relheight=1)
        pontos_top.delete(0, END)
        for i, _ in enumerate(exibir_dados()):
            pontos_top.insert(END, f"{i + 1}° - {_[0]} - {_[1]}")

def enviar(event=None):
    operação_texto = operação["text"].replace("x", "*")
    operação_texto = operação_texto.replace("÷", "//")

    try:
        resposta = eval(operação_texto)

    except ZeroDivisionError:
        resposta_entry.delete(0, END)
        operação["text"] = f"{randint(0, 10)} {choices(operações)[0]} {randint(0, 10)}"
        return 
        
    if resposta_entry.get().strip() == '':  # Verificando se a resposta está vazia
        errado()

    elif resposta == int(resposta_entry.get()):
        resposta_entry.delete(0, END)
        global pontos
        pontos += 1
        pontos_label_num["text"]= pontos
        operação["text"] = f"{randint(0, 10)} {choices(operações)[0]} {randint(0, 10)}"

    else:
        errado()

pontos_label = Label(game_frame, text="Pontos: ")
pontos_label.place(x=0, y=0)
pontos_label_num = Label(game_frame, text=pontos)
pontos_label_num.place(x=45, y=0)

vidas_label = Label(game_frame, text="Vidas: ")
vidas_label.place(x=245, y=0)
vidas_label_num = Label(game_frame, text=3)
vidas_label_num.place(x=280, y=0)

operação = Label(game_frame, text=f"{randint(0, 10)} {choices(operações)[0]} {randint(0, 10)}", font=("Arial", 20))
operação.pack()

resposta_entry = Entry(game_frame, font=("Arial", 20), justify=CENTER)
resposta_entry.pack()

resposta_entry.bind("<Return>", enviar)

botão_enviar = Button(game_frame, text="Send", command=enviar)
botão_enviar.pack()

game_over.place_forget()

def save(event=None):
    nome = nome_entry.get()
    global pontos
    salvar_dados({"nome": nome, "pontos": pontos})

    vidas_label_num["text"] = 3
    pontos = 0
    pontos_label_num["text"] = 0

    game_over.place_forget()
    game_frame.place(relwidth=1, relheight=1)



game_over_label = Label(game_over, text="GAME OVER", font=("Arial", 25)).pack()

pontos_label_GM = Label(game_over, text="")
pontos_label_GM.pack()

nome_label = Label(game_over, text="Qual o seu nome?").pack()

nome_entry = Entry(game_over)
nome_entry.pack()
nome_entry.bind("<Return>", save)

nome_botão_save = Button(game_over, text="save", command=save)
nome_botão_save.pack()

pontos_top = Listbox(game_over, relief=FLAT)
pontos_top.pack()



mainloop()

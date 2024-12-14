from tkinter import *
from random import randint, choices

app = Tk()
app.geometry("300x300")

operações = ["x", "÷", "+", "-"]

def errado(event=None):
    pass

def enviar(event=None):
    operação_texto = operação["text"].replace("x", "*")
    operação_texto = operação_texto.replace("÷", "//")

    try:
        resposta = eval(operação_texto)
    except ZeroDivisionError:
        resposta_entry.delete(0, END)
        operação["text"] = f"{randint(0, 10)} {choices(operações)[0]} {randint(0, 10)}"
        return 
        
    if resposta_entry.get() == '':
        operação["text"] = f"{randint(0, 10)} {choices(operações)[0]} {randint(0, 10)}"
        return

    elif resposta == int(resposta_entry.get()):
        resposta_entry.delete(0, END)
        pontos_label_num["text"] += 1
        operação["text"] = f"{randint(0, 10)} {choices(operações)[0]} {randint(0, 10)}"

    else:
        resposta_entry.delete(0, END)
        operação["text"] = f"{randint(0, 10)} {choices(operações)[0]} {randint(0, 10)}"


pontos_label = Label(app, text="Pontos: ")
pontos_label.place(x=0, y=0)
pontos_label_num = Label(app, text=0)
pontos_label_num.place(x=45, y=0)

vidas_label = Label(app, text="Vidas: ")
vidas_label.place(x=245, y=0)
vidas_label_num = Label(app, text=3)
vidas_label_num.place(x=280, y=0)

operação = Label(app, text=f"{randint(0, 10)} {choices(operações)[0]} {randint(0, 10)}", font=("Arial", 20))
operação.pack()

resposta_entry = Entry(app, font=("Arial", 20), justify=CENTER)
resposta_entry.pack()
resposta_entry.bind("<Return>", enviar)
botão_enviar = Button(app, text="Send", command=enviar)
botão_enviar.pack()

mainloop()
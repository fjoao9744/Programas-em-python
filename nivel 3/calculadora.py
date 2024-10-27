from tkinter import *

#mudanças na tela
tela = Tk()
tela.geometry("300x400")
tela.title("Calculadora")
tela.resizable(False, False)

# criação do frame principal(a tela)
tela_frame = Frame(tela, width=300, height=400, bg="black")
tela_frame.pack()
tela_frame.pack_propagate(False)

#aba dos numeros
nums_frame = Frame(tela_frame, width=300, height=80, bg="black")
nums_frame.pack()
nums_frame.pack_propagate(False) #não deixa a tela se ajustar sozinha

nums = Label(nums_frame, text=None, fg="white", bg="black", font=("Arial", 25))
nums.pack(anchor=E, pady=20)



#   linha 1

one_line_frame = Frame(tela_frame, width=300, height=65, bg="green")
one_line_frame.pack()
one_line_frame.pack_propagate(False)
#botao C

def clear():
    nums["text"] = None

clear_frame = Frame(one_line_frame, width=150, height=65, bg="blue")
clear_frame.pack(side=LEFT, anchor=N)
clear_frame.pack_propagate(False)


botao_clear = Button(clear_frame, text="C", font=("Arial", 15), command=clear)
botao_clear.pack(ipadx=100, ipady=100)


# botao de exponenciação X
pow_frame = Frame(one_line_frame, width=75, height=65, bg="blue")
pow_frame.pack(side=LEFT, anchor=N)
pow_frame.pack_propagate(False)

botao_pow = Button(pow_frame, text="¹/2", font=("Arial", 15))
botao_pow.pack(ipadx=100, ipady=100)

# botao divisão X
div_frame = Frame(one_line_frame, width=75, height=65, bg="blue")
div_frame.pack(side=LEFT, anchor=N)
div_frame.pack_propagate(False)

botao_div = Button(div_frame, text="/", font=("Arial", 15))
botao_div.pack(ipadx=100, ipady=100)

#   linha 2

two_line_frame = Frame(tela_frame, width=300, height=65, bg="green")
two_line_frame.pack(side=LEFT, anchor=N)
two_line_frame.pack_propagate(False)
# botao 7

seven_frame = Frame(two_line_frame, width=75, height=65, bg="blue")
seven_frame.pack(side=LEFT, anchor=N)
seven_frame.pack_propagate(False)

botao_one = Button(seven_frame, text="7", font=("Arial", 15))
botao_one.pack(ipadx=100, ipady=100)

# botao 8

eight_frame = Frame(two_line_frame, width=75, height=65, bg="blue")
eight_frame.pack(side=LEFT, anchor=N)
eight_frame.pack_propagate(False)

botao_one = Button(eight_frame, text="8", font=("Arial", 15))
botao_one.pack(ipadx=100, ipady=100)

# botao 9

nine_frame = Frame(two_line_frame, width=75, height=65, bg="blue")
nine_frame.pack(side=LEFT, anchor=N)
nine_frame.pack_propagate(False)

botao_one = Button(nine_frame, text="9", font=("Arial", 15))
botao_one.pack(ipadx=100, ipady=100)

# botao multi

multi_frame = Frame(two_line_frame, width=75, height=65, bg="blue")
multi_frame.pack()
multi_frame.pack_propagate(False)

botao_one = Button(multi_frame, text="X", font=("Arial", 15))
botao_one.pack(ipadx=100, ipady=100)

# botao 1

one_frame = Frame(tela_frame, width=75, height=65, bg="blue")
one_frame.pack()
one_frame.pack_propagate(False)

botao_one = Button(one_frame, text="1", font=("Arial", 15))
botao_one.pack(ipadx=100, ipady=100)




mainloop()


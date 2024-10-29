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

nums = Entry(nums_frame, fg="white", bg="black", font=("Arial", 25), justify=RIGHT)
nums.pack(ipady=20)



#   linha 1

one_line_frame = Frame(tela_frame, width=300, height=65, bg="green")
one_line_frame.pack()
one_line_frame.pack_propagate(False)
#botao C

def clear(event=None):
    nums.delete(0, END)

clear_frame = Frame(one_line_frame, width=150, height=65, bg="blue")
clear_frame.pack(side=LEFT, anchor=N)
clear_frame.pack_propagate(False)


botao_clear = Button(clear_frame, text="C", font=("Arial", 15), command=clear)
botao_clear.pack(ipadx=100, ipady=100)


# botao de exponenciação 
def power(event=None):
    if not nums.get()[-1] in "+-x/.**":
        nums.insert(END, "**")

pow_frame = Frame(one_line_frame, width=75, height=65, bg="blue")
pow_frame.pack(side=LEFT, anchor=N)
pow_frame.pack_propagate(False)

botao_pow = Button(pow_frame, text="¹/2", font=("Arial", 15), command=power)
botao_pow.pack(ipadx=100, ipady=100)

# botao div

def div(event=None):
    if not nums.get()[-1] in "+-x/.√**":
        nums.insert(END, "/")

div_frame = Frame(one_line_frame, width=75, height=65, bg="blue")
div_frame.pack(side=LEFT, anchor=N)
div_frame.pack_propagate(False)

botao_div = Button(div_frame, text="/", font=("Arial", 15), command=div)
botao_div.pack(ipadx=100, ipady=100)



#   linha 2

two_line_frame = Frame(tela_frame, width=300, height=65, bg="green")
two_line_frame.pack()
two_line_frame.pack_propagate(False) 
# botao 7

def seven(event=None):
    nums.insert(END, 7)

seven_frame = Frame(two_line_frame, width=75, height=65, bg="blue")
seven_frame.pack(side=LEFT, anchor=N)
seven_frame.pack_propagate(False)

botao_seven = Button(seven_frame, text="7", font=("Arial", 15), command=seven)
botao_seven.pack(ipadx=100, ipady=100)

# botao 8

def eight(event=None):
    nums.insert(END, 8)

eight_frame = Frame(two_line_frame, width=75, height=65, bg="blue")
eight_frame.pack(side=LEFT, anchor=N)
eight_frame.pack_propagate(False)

botao_eight = Button(eight_frame, text="8", font=("Arial", 15), command=eight)
botao_eight.pack(ipadx=100, ipady=100)

# botao 9

def nine(event=None):
    nums.insert(END, 9)

nine_frame = Frame(two_line_frame, width=75, height=65, bg="blue")
nine_frame.pack(side=LEFT, anchor=N)
nine_frame.pack_propagate(False)

botao_nine = Button(nine_frame, text="9", font=("Arial", 15), command=nine)
botao_nine.pack(ipadx=100, ipady=100)

# botao multi

def multi(event=None):
    if not nums.get()[-1] in "+-x/.√":
        nums.insert(END, "x")


multi_frame = Frame(two_line_frame, width=75, height=65, bg="blue")
multi_frame.pack()
multi_frame.pack_propagate(False)

botao_multi = Button(multi_frame, text="X", font=("Arial", 15), command=multi)
botao_multi.pack(ipadx=100, ipady=100)



#   linha 3


three_line_frame = Frame(tela_frame, width=300, height=65, bg="green")
three_line_frame.pack()
three_line_frame.pack_propagate(False)


# botao 4

def four(event=None):
    nums.insert(END, 4)

four_frame = Frame(three_line_frame, width=75, height=65, bg="blue")
four_frame.pack(side=LEFT, anchor=N)
four_frame.pack_propagate(False)

botao_four = Button(four_frame, text="4", font=("Arial", 15), command=four)
botao_four.pack(ipadx=100, ipady=100)

# botao 5

def five(event=None):
    nums.insert(END, 5)

five_frame = Frame(three_line_frame, width=75, height=65, bg="blue")
five_frame.pack(side=LEFT, anchor=N)
five_frame.pack_propagate(False)

botao_five = Button(five_frame, text="5", font=("Arial", 15), command=five)
botao_five.pack(ipadx=100, ipady=100)

# botao 6

def six(event=None):
    nums.insert(END, 6)

six_frame = Frame(three_line_frame, width=75, height=65, bg="blue")
six_frame.pack(side=LEFT, anchor=N)
six_frame.pack_propagate(False)

botao_six = Button(six_frame, text="6", font=("Arial", 15), command=six)
botao_six.pack(ipadx=100, ipady=100)

# botao sub

def sub(event=None):
    if nums.get() == '':
        nums.insert(END, "-")
    elif not nums.get()[-1] in "+-x/.√":
        nums.insert(END, "-")

sub_frame = Frame(three_line_frame, width=75, height=65, bg="blue")
sub_frame.pack()
sub_frame.pack_propagate(False)

botao_sub = Button(sub_frame, text="-", font=("Arial", 15), command=sub)
botao_sub.pack(ipadx=100, ipady=100)



#   linha 4

four_line_frame = Frame(tela_frame, width=300, height=65, bg="green")
four_line_frame.pack()
four_line_frame.pack_propagate(False)


# botao 1

def one(event=None):
    nums.insert(END, 1)

one_frame = Frame(four_line_frame, width=75, height=65, bg="blue")
one_frame.pack(side=LEFT, anchor=N)
one_frame.pack_propagate(False)

botao_one = Button(one_frame, text="1", font=("Arial", 15), command=one)
botao_one.pack(ipadx=100, ipady=100)

# botao 2

def two(event=None):
    nums.insert(END, 2)

two_frame = Frame(four_line_frame, width=75, height=65, bg="blue")
two_frame.pack(side=LEFT, anchor=N)
two_frame.pack_propagate(False)

botao_two = Button(two_frame, text="2", font=("Arial", 15), command=two)
botao_two.pack(ipadx=100, ipady=100)

# botao 3

def three(event=None):
    nums.insert(END, 3)

three_frame = Frame(four_line_frame, width=75, height=65, bg="blue")
three_frame.pack(side=LEFT, anchor=N)
three_frame.pack_propagate(False)

botao_three = Button(three_frame, text="3", font=("Arial", 15), command=three)
botao_three.pack(ipadx=100, ipady=100)

# botao sum

def suma(event=None):
    if not nums.get()[-1] in "+-x/.√":
        nums.insert(END, "+")

sum_frame = Frame(four_line_frame, width=75, height=65, bg="blue")
sum_frame.pack()
sum_frame.pack_propagate(False)

botao_sum = Button(sum_frame, text="+", font=("Arial", 15), command=suma)
botao_sum.pack(ipadx=100, ipady=100)



#   linha 5

five_line_frame = Frame(tela_frame, width=300, height=65, bg="green")
five_line_frame.pack()
five_line_frame.pack_propagate(False)


# botao sqrt
def sqrt(event=None):
    if nums.get() == '':
        nums.insert(END, "√")
    elif not nums.get()[-1] in "+-x/.√**":
        nums.insert(END, "√")


sqrt_frame = Frame(five_line_frame, width=75, height=65, bg="blue")
sqrt_frame.pack(side=LEFT, anchor=N)
sqrt_frame.pack_propagate(False)

botao_sqrt = Button(sqrt_frame, text="√", font=("Arial", 15), command=sqrt)
botao_sqrt.pack(ipadx=100, ipady=100)

# botao 0

def zero(event=None):
    nums.insert(END, 0)

zero_frame = Frame(five_line_frame, width=75, height=65, bg="blue")
zero_frame.pack(side=LEFT, anchor=N)
zero_frame.pack_propagate(False)

botao_zero = Button(zero_frame, text="0", font=("Arial", 15), command=zero)
botao_zero.pack(ipadx=100, ipady=100)

# botao comma
def comma(event=None):
    if not nums.get()[-1] in ".+-/x√":
        nums.insert(END, ".")

comma_frame = Frame(five_line_frame, width=75, height=65, bg="blue")
comma_frame.pack(side=LEFT, anchor=N)
comma_frame.pack_propagate(False)

botao_comma = Button(comma_frame, text=".", font=("Arial", 15), command=comma)
botao_comma.pack(ipadx=100, ipady=100)

# botao equal

def equal(event=None):
    try:
        equacao = nums.get()

        equacao = equacao.replace('x', '*')
        equacao = equacao.replace('√', '**0.5')

        resultado = eval(equacao)
        clear()  # Limpa a tela antes de mostrar o resultado
        nums.insert(END, resultado)  # Mostra o resultado

    except Exception as e:
        clear()
        nums.insert(END, "Erro")  # Mostra "Erro" em caso de exceção


        

    

equal_frame = Frame(five_line_frame, width=75, height=65, bg="blue")
equal_frame.pack()
equal_frame.pack_propagate(False)

botao_equal = Button(equal_frame, text="=", font=("Arial", 15), command=equal)
botao_equal.pack(ipadx=100, ipady=100)


mainloop()


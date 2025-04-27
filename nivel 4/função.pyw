import customtkinter as ctk

def func(x, a=0, b=1):  # F(x) = ax + b
    fx = a * x + b
    return fx

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x400")
        
        # Entrada para o valor de 'a'
        self.a = ctk.CTkEntry(self, placeholder_text="Determine a")
        self.a.pack(pady=10)
        
        # Entrada para o valor de 'b'
        self.b = ctk.CTkEntry(self, placeholder_text="Determine b")
        self.b.pack(pady=10)
        
        # Entrada para o valor de 'x'
        self.x_entry = ctk.CTkEntry(self, placeholder_text="Digite o valor de x")
        self.x_entry.pack(pady=10)
        
        # Label para exibir o resultado
        self.result_label = ctk.CTkLabel(self, text="Resultado: ")
        self.result_label.pack(pady=20)
        
        # Botão de calcular
        calc_button = ctk.CTkButton(self, text="Calcular", command=self.plotar)
        calc_button.pack(pady=10)

    def plotar(self):
        try:
            # Pegando os valores inseridos
            a = int(self.a.get())
            b = int(self.b.get())
            x = int(self.x_entry.get())
            
            # Calculando a função
            fx = func(x, a, b)
            print(f"f({x}) = {a}*{x} + {b}")
            
            # Atualizando o label com o resultado
            self.result_label.configure(text=f"Resultado: F({x}) = {fx}")
        except ValueError:
            # Tratando caso o usuário insira algo que não seja número
            self.result_label.configure(text="Por favor, insira números válidos")

if __name__ == "__main__":
    app = App()
    app.mainloop()

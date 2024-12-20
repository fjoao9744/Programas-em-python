from dataclasses import dataclass, field

@dataclass
class Livro:
    nome: str
    autor: str
    genero: str
    ano_publicação: int
    em_estoque: int
    
    def info(self):
        return f"nome: {self.nome} \nautor: {self.autor} \ngenero: {self.genero} \nano de publicação: {self.ano_publicação} \nQuantidade em estoque: {self.em_estoque}"
    
    def emprestimo(self):
        if self.em_estoque == 0:
            print("Não existe o livro no estoque. ")
        
        self.em_estoque -= 1
    
    def __call__(self):
        return self.nome.capitalize()
        
@dataclass
class Leitor:
    nome: str
    id: int
    livros: list = field(default_factory=list)
    
    def emprestar_livro(self, livro) -> str:
        if livro.em_estoque == 0:
            return "o livro solicitado não esta em estoque. "
        
        if len(self.livros) <= 3:
            self.livros.append(livro)
            return f"Livro {livro.nome} adicionado com sucesso"
        
        return "Ja possui 3 livros emprestados"

    def __call__(self):
        return f"{self.nome.capitalize()}#{self.id:0>4}"
        
class Biblioteca:
    def __init__(self):
        self.usuarios = []
        self.livros = []

        self.historico = []
        
    def cadastrar_usuario(self, usuario):
        self.usuarios.append(usuario)
        
    def cadastrar_livro(self, livro):
        if any(l.nome == livro.nome for l in self.livros):
            '''for l in self.livros:
                l.nome == livro.nome ?
            '''
            print(f"{livro.nome} ja esta cadastrado")
            return
        
        self.livros.append(livro)
        
    def devolver_livro(self, usuario, livro):
        usuario.livros.remove(livro)
        livro.em_estoque += 1
        return livro.nome
        
    def emprestimo_livro(self, leitor, livro):
        resposta = leitor.emprestar_livro(livro)
        if "sucesso" in resposta:
            self.historico.append(f"{livro.nome} foi emprestado à {leitor.nome}")
        livro.emprestimo()
        
    def exibir_historico(self):
        for log in self.historico:
            print(log)        

    def listar_livros(self, info = False):
        if len(self.livros) == 0:
            print("a biblioteca não possui nenhum livro")
            return
        
        if info:
            for i, livro in enumerate(self.livros):
                print(f"{i}- {livro()}")
        
        else:
            for livro in self.livros:
                print(livro())
            
    def listar_usuarios(self, info = False):
        if len(self.usuarios) == 0:
            print("a biblioteca não possui nenhum leitor")
            return
        
        if info:
            for i, usuario in enumerate(self.usuarios):
                print(f"{i}- {usuario()}")
        else:
            for usuario in self.usuarios:
                print(usuario())

def gerar_id():
    id = 0
    while True:
        id += 1
        yield id
            
def main():
    print("-" * 10, "SISTEMA DE BIBLIOTECA", "-" * 10)
    
    biblioteca = Biblioteca()
    
    usuario_id = gerar_id()
    
    while True:
    
        print("Oque deseja fazer na nossa biblioteca? ")
        event = int(input("""[0] Cadastrar livros
[1] Cadastrar leitor
[2] Realizar emprestimo
[3] Devolver livro
[4] Exibir os livros
[5] Exibir usuarios
[6] Historico de emprestimo
"""))

        if event == 0:
            nome = str(input("digite o nome do livro: "))
            autor = str(input("digite o autor do livro: "))
            genero = str(input("digite o genero do livro: "))
            ano_publicação = int(input("Digite o ano de publicação do livro: "))
            estoque = int(input("Digite o quanto desse livro tem no estoque: "))
            
            livro = Livro(nome, autor, genero, ano_publicação, estoque)
            
            biblioteca.cadastrar_livro(livro)
            print("Cadastro concluido")
            
        elif event == 1:
            nome = str(input("digite o nome do usuario: ")).strip().capitalize()
            
            usuario = Leitor(nome, next(usuario_id))
            
            biblioteca.cadastrar_usuario(usuario)
            
        elif event == 2:
            if len(biblioteca.livros) == 0 or len(biblioteca.usuarios) == 0:
                print("Não será possivel realizar nenhum tipo de emprestimo. ")
                continue
            
            biblioteca.listar_usuarios(info= True)
            usuario = int(input("Qual sera o usuario que irá pegar emprestado o livro? "))
            biblioteca.listar_livros(info= True)
            livro = int(input("Qual sera o livro que o usuario irá fazer o emprestimo? "))
            
            biblioteca.emprestimo_livro(biblioteca.usuarios[usuario], biblioteca.livros[livro])
            
        elif event == 3:
            if len(biblioteca.livros) == 0 or len(biblioteca.usuarios) == 0:
                print("Não será possivel fazer a devolução de qualquer livro. ")
                continue
            
            biblioteca.listar_usuarios(info= True)
            usuario = int(input("qual usuario vai devolver o livro: "))
            
            for i, livro in enumerate(biblioteca.usuarios[usuario].livros):
                print(f"{i}- {livro.nome}")
                
            livro = int(input("Qual livro o usuario vai devolver? "))
                        
            livro_nome = biblioteca.devolver_livro(biblioteca.usuarios[usuario], biblioteca.usuarios[usuario].livros[livro])
            
            print(f"{livro_nome} devolvido com sucesso")

        elif event == 4:
            biblioteca.listar_livros()
            cont = str(input("Deseja ver as informações de algum livro?[S/N] ")).strip().upper()
            if cont == "S":
                for i, livro in enumerate(biblioteca.livros):
                    print(f"{i}- {livro.nome}")
                livro = int(input("Qual livro você quer ver mais sobre? "))
                print(biblioteca.livros[livro].info())
                
        elif event == 5:
            biblioteca.listar_usuarios()
            
        elif event == 6:
            biblioteca.exibir_historico()
            
        else:
            print("Opção invalida")
                    
main()
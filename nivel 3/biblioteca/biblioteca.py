from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QGroupBox, QFrame


app = QApplication([])

class MainPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        # Configurações da janela
        self.setWindowTitle("Biblioteca")
        self.setGeometry(500, 150, 600, 500)
        
        # Layout
        layout = QVBoxLayout()
        
        # Titulo
        title = QLabel("Bem vindo a nossa biblioteca!")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("""
            QLabel {
                font: bold 32px "Fira Sans" ;

            }
        """)
        
        master_layout = QVBoxLayout()
        box = QGroupBox("Oque deseja?")
        
        # Layout 1
        box_layout1 = QHBoxLayout()
        book_register = QPushButton("Registrar livro")
        user_register = QPushButton("Registrar usuario")
        
        box_layout1.addWidget(book_register)
        box_layout1.addWidget(user_register)
        
        # Layout 2
        box_layout2 = QHBoxLayout()
        book_send = QPushButton("Emprestar Livro")
        book_back = QPushButton("Devolver livro")
        
        box_layout2.addWidget(book_send)
        box_layout2.addWidget(book_back)
        
        # Layout 3
        box_layout3 = QHBoxLayout()
        book_display = QPushButton("Emprestar Livro")
        user_display = QPushButton("Devolver livro")
        
        box_layout3.addWidget(book_display)
        box_layout3.addWidget(user_display)
        
        # Adicionando os layouts ao master
        master_layout.addLayout(box_layout1)
        master_layout.addLayout(box_layout2)
        master_layout.addLayout(box_layout3)
        
        
        box.setLayout(master_layout)
        
        master_layout.addWidget(box)
        
        # Widgets do layout
        layout.addWidget(title)
        layout.addWidget(box)
        
        self.setLayout(layout)
        

janela_principal = MainPage()

janela_principal.show()
app.exec_()


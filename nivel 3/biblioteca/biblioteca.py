from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout


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
        
        title.setStyleSheet("""
            QLabel {
                font: bold 32px "Fira Sans" ;


            }
        """)
        
        
        layout.addWidget(title, alignment=Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)
        
        self.setLayout(layout)
        


janela_principal = MainPage()

janela_principal.show()
app.exec_()
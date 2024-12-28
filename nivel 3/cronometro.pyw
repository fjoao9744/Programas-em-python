""" IMPORTAÇÕES """
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import time
import threading

""" CLASSE PRINCIPAL """
class Chrono:
    """ CONFIGURAÇÕES DA TELA """
    app = QApplication([])
    window = QWidget()
    window.setWindowTitle("Cronometro")
    window.setFixedSize(200, 200)
    
    """ QUANDO INSTANCIAR """
    def __init__(self):
        # widgets
        self.tempo = float(0)
        self.label = QLabel(str(self.tempo))
        
        self.stop_button = QPushButton("PARAR")
        self.stop_button.setObjectName("stop_button")
        self.stop_button.setIcon(QIcon(r"nivel 3\midias\icons\stop.png"))
        self.stop_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.stop_button.clicked.connect(self.parar)
        
        self.play_button = QPushButton("INICIAR")
        self.play_button.setObjectName("play_button")
        self.play_button.setIcon(QIcon(r"nivel 3\midias\icons\timer.png"))
        self.play_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.play_button.clicked.connect(self.iniciar)
        
        # layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.stop_button)
        self.layout.addWidget(self.play_button)
        Chrono.window.setLayout(self.layout)
        
        # estilo
        self.label.setStyleSheet('''
        QLabel {
            font-size: 30px;
        }
        ''')
        
        self.play_button.setStyleSheet('''
        QPushButton#play_button {
            font: 19px Arial bold;
            border: 2px solid black;
            border-radius: 5px;
        }
        QPushButton#play_button:hover {
            border-style: dashed;
            background-color: #DBDBDB;
        }
        ''')
        self.stop_button.setStyleSheet('''
        QPushButton#stop_button {
            font: 19px Arial bold;
            border: 2px solid black;
            border-radius: 5px;
        }
        QPushButton#stop_button:hover {
            border-style: dashed;
            background-color: #DBDBDB;
            
        }
        ''')
        
        
        
    """ COMEÇA A CONTAGEM """
    def iniciar(self):
        self.continuar = True
        def contador():
            while self.continuar:
                self.tempo += 0.1
                self.label.setText(f"{self.tempo:.1f}")
                time.sleep(0.1)
                
        self.thread = threading.Thread(target=contador)
        self.thread.start()
        self.play_button.setEnabled(False)

    """ PARA A CONTAGEM """        
    def parar(self):
        self.continuar = False
        self.play_button.setEnabled(True)
        
    
    """ INICIA O CRONOMETRO """
    @classmethod
    def __call__(cls):
        cls.window.show()
        cls.app.exec_()
        
if __name__ == "__main__":
    app = Chrono()
    app()
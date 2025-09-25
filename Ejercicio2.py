import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Compra de Pasaje Aéreo")
        self.setGeometry(100, 100, 500, 350)
        
        layout = QGridLayout()
        self.setLayout(layout)

       
        titulo = QLabel("Formulario de Compra")
        titulo.setFont(QFont("Arial", 16, QFont.Bold))
        titulo.setAlignment(Qt.AlignCenter)
        layout.addWidget(titulo, 0, 0, 1, 2)  

        # Nombre
        lbl_nombre = QLabel("Nombre:")
        self.txt_nombre = QLineEdit()
        layout.addWidget(lbl_nombre, 1, 0)
        layout.addWidget(self.txt_nombre, 1, 1)

        # Apellido
        lbl_apellido = QLabel("Apellido:")
        self.txt_apellido = QLineEdit()
        layout.addWidget(lbl_apellido, 2, 0)
        layout.addWidget(self.txt_apellido, 2, 1)

        # DNI
        lbl_dni = QLabel("DNI:")
        self.txt_dni = QLineEdit()
        layout.addWidget(lbl_dni, 3, 0)
        layout.addWidget(self.txt_dni, 3, 1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())

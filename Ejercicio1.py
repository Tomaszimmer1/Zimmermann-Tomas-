import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QRadioButton, QButtonGroup, QComboBox, QCheckBox, QPushButton, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt



class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registro de Usuario")
        self.setGeometry(100, 100, 400, 300)
        layout = QGridLayout()
        self.setLayout(layout)

        #Título 
        titulo = QLabel("Formulario de Registro")
        titulo.setFont(QFont("Arial", 16, QFont.Bold))
        titulo.setAlignment(Qt.AlignCenter)
        layout.addWidget(titulo, 0, 0, 1, 2)


        #Campo con los nombres 

        nombre_label = QLabel("Nombre:")
        self.nombre_input = QLineEdit()
        layout.addWidget(nombre_label, 1, 0)
        layout.addWidget(self.nombre_input, 1, 1)

        #Campo con el email
        
        email_label = QLabel("Email:")
        self.email_input = QLineEdit()
        layout.addWidget(email_label, 2, 0)
        layout.addWidget(self.email_input, 2, 1)
                                                
                         
         #Campo de contraseña

        pass_label = QLabel("Contraseña:")
        self.pass_input = QLineEdit()
        self.pass_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(pass_label, 3, 0)
        layout.addWidget(self.pass_input, 3, 1)

        #Seleccion de genero

        genero_label = QLabel("Género:")
        self.masculino_rb = QRadioButton("Masculino")
        self.femenino_rb = QRadioButton("Femenino")
        self.nobinario_rb = QRadioButton("No binario")
        genero_group = QButtonGroup()
        genero_group.addButton(self.masculino_rb)
        genero_group.addButton(self.femenino_rb)
        genero_group.addButton(self.nobinario_rb)

        layout.addWidget(genero_label, 4, 0)
        genero_layout = QGridLayout()
        genero_layout.addWidget(self.masculino_rb, 0, 0)
        genero_layout.addWidget(self.femenino_rb, 0, 1)
        genero_layout.addWidget(self.nobinario_rb, 0, 2)
        layout.addLayout(genero_layout, 4, 1)
        
        #Elegir el pais 

        pais_label = QLabel("País:")
        self.pais_combo = QComboBox()
        self.pais_combo.addItems(["Argentina", "Chile", "México", "España", "Colombia"])
        layout.addWidget(pais_label, 5, 0)
        layout.addWidget(self.pais_combo, 5, 1)

        #Terminos y condiciones 

        self.terminos_checkbox = QCheckBox("Acepto los términos y condiciones")
        layout.addWidget(self.terminos_checkbox, 6, 0, 1, 2, Qt.AlignCenter)

        #Boton y validacion 

        registrar_btn = QPushButton("Registrar")
        registrar_btn.clicked.connect(self.validar_formulario)
        layout.addWidget(registrar_btn, 7, 0, 1, 2)

    def validar_formulario(self):   
        nombre = self.nombre_input.text().strip()
        email = self.email_input.text().strip()
        password = self.pass_input.text().strip()
        genero = self.masculino_rb.isChecked() or self.femenino_rb.isChecked() or self.nobinario_rb.isChecked()
        pais = self.pais_combo.currentText()
        terminos = self.terminos_checkbox.isChecked()

        if not all([nombre, email, password, genero, pais]) or not terminos:
            QMessageBox.warning(self, "Error", "no seas pavote, completa todos los campos")
        else:
            QMessageBox.information(self, "Registro exitoso", "Bien burro, te registraste")





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())

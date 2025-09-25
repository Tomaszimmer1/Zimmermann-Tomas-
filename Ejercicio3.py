import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QPushButton, 
    QVBoxLayout, QDateEdit, QMessageBox
)
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QFont

class VentanaFormulario(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Afiliados - Chacarita Juniors")
        self.setGeometry(100, 100, 500, 350)
        self.setStyleSheet("background-color: #d3d3d3;")

        layout = QGridLayout()
        self.setLayout(layout)

        #Titulo

        self.titulo = QLabel("Formulario de Afiliación")
        self.titulo.setStyleSheet("font-family: 'Times New Roman'; font-size: 19px; font-weight: bold; color: black")
        self.titulo.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.titulo, 0, 0, 1, 2)

        #Nombre
    
        layout.addWidget(QLabel("Nombre"), 1, 0)
        self.input_nombre = QLineEdit()
        layout.addWidget(self.input_nombre, 1, 1)

        #Apellido

        layout.addWidget(QLabel("Apellido"), 2, 0)
        self.input_apellido = QLineEdit()
        layout.addWidget(self.input_apellido, 2, 1)

        #DNI

        layout.addWidget(QLabel("DNI"), 3, 0)
        self.input_dni = QLineEdit()
        layout.addWidget(self.input_dni, 3, 1)

        #Fecha de nacimiento

        layout.addWidget(QLabel("Fecha de nacimiento"), 4, 0)
        self.input_fecha_nacimiento = QDateEdit()
        self.input_fecha_nacimiento.setCalendarPopup(True)
        self.input_fecha_nacimiento.setDate(QDate.currentDate())
        layout.addWidget(self.input_fecha_nacimiento, 4, 1)

    def obtener_datos(self):
        return {
            "nombre": self.input_nombre.text().strip(),
            "apellido": self.input_apellido.text().strip(),
            "dni": self.input_dni.text().strip(),
            "fecha": self.input_fecha_nacimiento.date().toString("dd/MM/yyyy")
        }

    def datos_validos(self):
        datos = self.obtener_datos()
        return all([datos["nombre"], datos["apellido"], datos["dni"]])
    

    #ventana de herramientas

class VentanaHerramientas(QWidget):
    def __init__(self, ventana_formulario):
        super().__init__()
        self.ventana_formulario = ventana_formulario
        self.setWindowTitle("Herramientas")
        self.setGeometry(600, 200, 300, 400)
        self.setStyleSheet("background-color: #f0f0f0;")

        layout = QVBoxLayout()
        self.setLayout(layout)  

        btn_guardar = QPushButton("Guardar")
        btn_salir = QPushButton("Salir")

        btn_guardar.clicked.connect(self.guardar)
        btn_salir.clicked.connect(self.salir)

        btn_guardar.setStyleSheet("font-size: 14px; padding: 10px;")
        btn_salir.setStyleSheet("font-size: 14px; padding: 10px;")

        layout.addWidget(btn_guardar)
        layout.addWidget(btn_salir)

    def guardar(self):
        if self.ventana_formulario.datos_validos():
            datos = self.ventana_formulario.obtener_datos()
            mensaje = (
                f"Nombre: {datos['nombre']}\n"
                f"Apellido: {datos['apellido']}\n"
                f"DNI: {datos['dni']}\n"
                f"Fecha de nacimiento: {datos['fecha']}"
            )
            QMessageBox.information(self, "Datos Guardados", mensaje)
        else:
            QMessageBox.warning(self, "Error", "Error, seguro sos de Atlanta, muerto.")

    def salir(self):
        self.close()
        self.ventana_formulario.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ventana_form = VentanaFormulario()
    ventana_herr = VentanaHerramientas(ventana_form)    


    ventana_form.show()
    ventana_herr.show()

    sys.exit(app.exec_())

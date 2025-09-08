import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
    QLabel, QLineEdit, QPushButton, QTextEdit, QComboBox, QMessageBox,
    QFileDialog, QGroupBox, QListWidget, QListWidgetItem, QSplitter
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class SistemaDocentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Gestión de Docentes")
        self.setGeometry(100, 100, 1000, 700)
        self.archivo_datos = "docentes.txt"
        self.configurar_interfaz()
        self.cargar_datos()
        self.setStyleSheet("""
            QMainWindow { background-color: #f8f9fa; }
            QGroupBox {
                font-weight: bold;
                border: 2px solid #dee2e6;
                border-radius: 8px;
                margin: 10px;
                padding-top: 15px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 10px;
                color: #495057;
            }
            QPushButton {
                background-color: #007bff;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover { background-color: #0056b3; }
            QPushButton:pressed { background-color: #004085; }
            QLineEdit, QComboBox {
                padding: 8px;
                border: 1px solid #ced4da;
                border-radius: 4px;
                background-color: white;
            }
            QLineEdit:focus, QComboBox:focus { border-color: #007bff; }
            QListWidget {
                border: 1px solid #ced4da;
                border-radius: 4px;
                background-color: white;
            }
            QTextEdit {
                border: 1px solid #ced4da;
                border-radius: 4px;
                background-color: white;
            }
        """)

    def configurar_interfaz (self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)
        splitter = QSplitter(Qt.Horizontal)
        main_layout.addWidget(splitter)
        splitter.addWidget(self.crear_panel_formulario())
        splitter.addWidget(self.crear_panel_lista())
        splitter.setSizes([400, 600])

    def crear_panel_formulario(self):
        widget = QWidget()
        layout = QVBoxLayout()

        grupo_form = QGroupBox("Datos del Docente")
        form_layout = QGridLayout()

        self.legajo_edit = QLineEdit()
        self.nombre_edit = QLineEdit()
        self.apellido_edit = QLineEdit()
        self.dni_edit = QLineEdit()
        self.email_edit = QLineEdit()
        self.telefono_edit = QLineEdit()
        self.materia_edit = QLineEdit()
        self.categoria_combo = QComboBox()
        self.categoria_combo.addItems(["Titular", "Asociado", "Adjunto", "Auxiliar", "Interino"])

        campos = [
            ("Legajo:", self.legajo_edit),
            ("Nombre:", self.nombre_edit),
            ("Apellido:", self.apellido_edit),
            ("DNI:", self.dni_edit),
            ("Email:", self.email_edit),
            ("Teléfono:", self.telefono_edit),
            ("Materia:", self.materia_edit),
            ("Categoría:", self.categoria_combo),
        ]

        for i, (label, campo) in enumerate(campos):
            form_layout.addWidget(QLabel(label), i, 0)
            form_layout.addWidget(campo, i, 1)

        grupo_form.setLayout(form_layout)
        layout.addWidget(grupo_form)

        grupo_botones = QGroupBox("Acciones")
        botones_layout = QVBoxLayout()

        self.btn_agregar = QPushButton("Agregar Docente")
        self.btn_buscar = QPushButton("Buscar Docente")
        self.btn_modificar = QPushButton("Modificar Docente")
        self.btn_eliminar = QPushButton("Eliminar Docente")
        self.btn_limpiar = QPushButton("Limpiar Formulario")

        botones = [
            (self.btn_agregar, self.agregar_docente),
            (self.btn_buscar, self.buscar_docente),
            (self.btn_modificar, self.modificar_docente),
            (self.btn_eliminar, self.eliminar_docente),
            (self.btn_limpiar, self.limpiar_formulario),
        ]

        for btn, func in botones:
            btn.clicked.connect(func)
            botones_layout.addWidget(btn)

        grupo_botones.setLayout(botones_layout)
        layout.addWidget(grupo_botones)

        widget.setLayout(layout)
        return widget

    def crear_panel_lista(self):
        widget = QWidget()
        layout = QVBoxLayout()

        busqueda_layout = QHBoxLayout()
        busqueda_layout.addWidget(QLabel("Buscar:"))
        self.busqueda_edit = QLineEdit()
        self.busqueda_edit.setPlaceholderText("Buscar por apellido, nombre o legajo...")
        self.busqueda_edit.textChanged.connect(self.filtrar_lista)
        busqueda_layout.addWidget(self.busqueda_edit)
        layout.addLayout(busqueda_layout)

        self.lista_docentes = QListWidget()
        self.lista_docentes.itemClicked.connect(self.mostrar_detalles)
        layout.addWidget(self.lista_docentes)

        grupo_detalles = QGroupBox("Detalles del Docente Seleccionado")
        self.detalles_text = QTextEdit()
        self.detalles_text.setReadOnly(True)
        detalles_layout = QVBoxLayout()
        detalles_layout.addWidget(self.detalles_text)
        grupo_detalles.setLayout(detalles_layout)
        layout.addWidget(grupo_detalles)

        widget.setLayout(layout)
        return widget

    def agregar_a_lista(self, datos):
        texto_item = f"{datos[2]}, {datos[1]} ({datos[0]})"
        item = QListWidgetItem(texto_item)
        item.setData(Qt.UserRole, datos)
        self.lista_docentes.addItem(item)

    def cargar_datos(self):
        if not os.path.exists(self.archivo_datos):
            return
        with open(self.archivo_datos, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                if linea.strip():
                    datos = linea.strip().split('|')
                    if len(datos) == 8:
                        self.agregar_a_lista(datos)

    def guardar_datos(self):
        with open(self.archivo_datos, 'w', encoding='utf-8') as archivo:
            for i in range(self.lista_docentes.count()):
                item = self.lista_docentes.item(i)
                datos = item.data(Qt.UserRole)
                archivo.write('|'.join(datos) + '\n')

    def agregar_docente(self):
        legajo = self.legajo_edit.text().strip()
        if not legajo:
            QMessageBox.warning(self, 'Error', 'El legajo es obligatorio')
            return
        if self.buscar_por_legajo(legajo):
            QMessageBox.warning(self, 'Error', 'Ya existe un docente con ese legajo')
            return
        datos = [
            self.legajo_edit.text().strip(),
            self.nombre_edit.text().strip(),
            self.apellido_edit.text().strip(),
            self.dni_edit.text().strip(),
            self.email_edit.text().strip(),
            self.telefono_edit.text().strip(),
            self.materia_edit.text().strip(),
            self.categoria_combo.currentText()
        ]
        self.agregar_a_lista(datos)
        self.guardar_datos()
        self.limpiar_formulario()
        QMessageBox.information(self, 'Éxito', 'Docente agregado correctamente')

    def filtrar_lista(self):
        texto = self.busqueda_edit.text().lower()
        for i in range(self.lista_docentes.count()):
            item = self.lista_docentes.item(i)
            datos = item.data(Qt.UserRole)
            coincide = any(texto in campo.lower() for campo in [datos[0], datos[1], datos[2]])
            item.setHidden(not coincide)

    def mostrar_detalles(self, item):
        datos = item.data(Qt.UserRole)
        self.detalles_text.setPlainText(f"""
INFORMACIÓN DEL DOCENTE

Legajo: {datos[0]}
Nombre: {datos[1]}
Apellido: {datos[2]}
DNI: {datos[3]}
Email: {datos[4]}
Teléfono: {datos[5]}
Materia: {datos[6]}
Categoría: {datos[7]}
""")

    def buscar_por_legajo(self, legajo):
        for i in range(self.lista_docentes.count()):
            item = self.lista_docentes.item(i)
            datos = item.data(Qt.UserRole)
            if datos[0].lower() == legajo.lower():
                return item
        return None

    def buscar_docente(self):
        legajo = self.legajo_edit.text().strip()
        if not legajo:
            QMessageBox.warning(self, 'Error', 'Ingrese un legajo para buscar')
            return
        item = self.buscar_por_legajo(legajo)
        if item:
            self.lista_docentes.setCurrentItem(item)
            self.mostrar_detalles(item)
        else:
            QMessageBox.information(self, 'No encontrado', 'Docente no encontrado.')

    def modificar_docente(self):
        item = self.lista_docentes.currentItem()
        if not item:
            QMessageBox.warning(self, 'Error', 'Seleccione un docente para modificar')
            return
        datos = item.data(Qt.UserRole)
        self.legajo_edit.setText(datos[0])
        self.nombre_edit.setText(datos[1])
        self.apellido_edit.setText(datos[2])
        self.dni_edit.setText(datos[3])
        self.email_edit.setText(datos[4])
        self.telefono_edit.setText(datos[5])
        self.materia_edit.setText(datos[6])
        self.categoria_combo.setCurrentText(datos[7])

        self.btn_agregar.setText("Actualizar Docente")
        self.btn_agregar.clicked.disconnect()
        self.btn_agregar.clicked.connect(lambda: self.actualizar_docente(item))

    def actualizar_docente(self, item):
        nuevos_datos = [
            self.legajo_edit.text().strip(),
            self.nombre_edit.text().strip(),
            self.apellido_edit.text().strip(),
            self.dni_edit.text().strip(),
            self.email_edit.text().strip(),
            self.telefono_edit.text().strip(),
            self.materia_edit.text().strip(),
            self.categoria_combo.currentText()
        ]
        item.setData(Qt.UserRole, nuevos_datos)
        item.setText(f"{nuevos_datos[2]}, {nuevos_datos[1]} ({nuevos_datos[0]})")
        self.guardar_datos()
        self.limpiar_formulario()
        self.btn_agregar.setText("Agregar Docente")
        self.btn_agregar.clicked.disconnect()
        self.btn_agregar.clicked.connect(self.agregar_docente)
        QMessageBox.information(self, 'Éxito', 'Docente modificado correctamente')

    def eliminar_docente(self):
        item = self.lista_docentes.currentItem()
        if not item:
            QMessageBox.warning(self, 'Error', 'Seleccione un docente para eliminar')
            return
        datos = item.data(Qt.UserRole)
        confirmacion = QMessageBox.question(self, "Confirmar eliminación",
                                            f"¿Está seguro de eliminar a {datos[1]} {datos[2]}?",
                                            QMessageBox.Yes | QMessageBox.No)
        if confirmacion == QMessageBox.Yes:
            self.lista_docentes.takeItem(self.lista_docentes.row(item))
            self.guardar_datos()
            self.detalles_text.clear()
            QMessageBox.information(self, 'Éxito', 'Docente eliminado correctamente')

    def limpiar_formulario(self):
        self.legajo_edit.clear()
        self.nombre_edit.clear()
        self.apellido_edit.clear()
        self.dni_edit.clear()
        self.email_edit.clear()
        self.telefono_edit.clear()
        self.materia_edit.clear()
        self.categoria_combo.setCurrentIndex(0)
        self.btn_agregar.setText("Agregar Docente")
        self.btn_agregar.clicked.disconnect()
        self.btn_agregar.clicked.connect(self.agregar_docente)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    sistema = SistemaDocentes()
    sistema.show()
    sys.exit(app.exec_())
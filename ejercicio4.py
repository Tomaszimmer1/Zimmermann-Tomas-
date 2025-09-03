import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QAction, QFileDialog,
    QMessageBox, QStatusBar
)
from PyQt5.QtGui import QKeySequence

class EditorTexto(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Editor de Texto")
        self.setGeometry(100, 100, 800, 600)

        # Area de texto central
        self.editor = QTextEdit()
        self.setCentralWidget(self.editor)
        self.editor.setPlaceholderText("Escribe aquí tu texto...")

        # Estado inicial
        self.archivo_actual = None

        # Inicializacion de componentes
        self.crear_menus()
        self.crear_barra_estado()

    
    # Menus
    
    def crear_menus(self):
        menubar = self.menuBar()

        # Menu Archivo
        menu_archivo = menubar.addMenu('&Archivo')

        accion_nuevo = QAction('&Nuevo', self)
        accion_nuevo.setShortcut(QKeySequence.New)
        accion_nuevo.triggered.connect(self.nuevo_archivo)
        menu_archivo.addAction(accion_nuevo)

        accion_abrir = QAction('&Abrir...', self)
        accion_abrir.setShortcut(QKeySequence.Open)
        accion_abrir.triggered.connect(self.abrir_archivo)
        menu_archivo.addAction(accion_abrir)

        accion_guardar = QAction('&Guardar', self)
        accion_guardar.setShortcut(QKeySequence.Save)
        accion_guardar.triggered.connect(self.guardar_archivo)
        menu_archivo.addAction(accion_guardar)

        menu_archivo.addSeparator()

        accion_salir = QAction('&Salir', self)
        accion_salir.setShortcut(QKeySequence.Quit)
        accion_salir.triggered.connect(self.salir)
        menu_archivo.addAction(accion_salir)

        # Menu Editar
        menu_editar = menubar.addMenu('&Editar')

        accion_cortar = QAction('Cortar', self)
        accion_cortar.setShortcut(QKeySequence.Cut)
        accion_cortar.triggered.connect(self.editor.cut)
        menu_editar.addAction(accion_cortar)

        accion_copiar = QAction('Copiar', self)
        accion_copiar.setShortcut(QKeySequence.Copy)
        accion_copiar.triggered.connect(self.editor.copy)
        menu_editar.addAction(accion_copiar)

        accion_pegar = QAction('Pegar', self)
        accion_pegar.setShortcut(QKeySequence.Paste)
        accion_pegar.triggered.connect(self.editor.paste)
        menu_editar.addAction(accion_pegar)

        # Menu Ayuda
        menu_ayuda = menubar.addMenu('Ay&uda')
        accion_acerca = QAction('Acerca de', self)
        accion_acerca.triggered.connect(self.acerca_de)
        menu_ayuda.addAction(accion_acerca)

    
    # Funciones de archivo

    def nuevo_archivo(self):
        self.editor.clear()
        self.archivo_actual = None
        self.statusBar().showMessage("Nuevo archivo creado")

    def abrir_archivo(self):
        archivo, _ = QFileDialog.getOpenFileName(self, 'Abrir archivo', '', 'Archivos de texto (*.txt)')
        if archivo:
            try:
                with open(archivo, 'r', encoding='utf-8') as f:
                    contenido = f.read()
                    self.editor.setPlainText(contenido)
                    self.archivo_actual = archivo
                    self.statusBar().showMessage(f'Archivo abierto: {archivo}')
            except Exception as e:
                QMessageBox.warning(self, 'Error', f'No se pudo abrir el archivo:\n{e}')

    def guardar_archivo(self):
        if self.archivo_actual:
            try:
                with open(self.archivo_actual, 'w', encoding='utf-8') as f:
                    f.write(self.editor.toPlainText())
                    self.statusBar().showMessage(f'Archivo guardado: {self.archivo_actual}')
            except Exception as e:
                QMessageBox.warning(self, 'Error', f'No se pudo guardar el archivo:\n{e}')
        else:
            archivo, _ = QFileDialog.getSaveFileName(self, 'Guardar archivo', '', 'Archivos de texto (*.txt)')
            if archivo:
                try:
                    with open(archivo, 'w', encoding='utf-8') as f:
                        f.write(self.editor.toPlainText())
                        self.archivo_actual = archivo
                        self.statusBar().showMessage(f'Archivo guardado: {archivo}')
                except Exception as e:
                    QMessageBox.warning(self, 'Error', f'No se pudo guardar el archivo:\n{e}')

    
    # Dialogos
    
    def acerca_de(self):
        QMessageBox.information(
            self,
            'Acerca de',
            'Editor de Texto v1.0\n\nCreado con PyQt5\nPara aprender desarrollo de interfaces.'
        )

    def salir(self):
        respuesta = QMessageBox.question(
            self,
            'Salir',
            '¿Desea guardar los cambios antes de salir?',
            QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel
        )

        if respuesta == QMessageBox.Yes:
            self.guardar_archivo()
            self.close()
        elif respuesta == QMessageBox.No:
            self.close()
        elif respuesta == QMessageBox.Cancel:
            pass

    # Barra de estado
    
    def crear_barra_estado(self):
        self.statusBar().showMessage("Listo")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = EditorTexto()
    editor.show()
    sys.exit(app.exec_())

        


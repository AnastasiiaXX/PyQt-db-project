from PyQt5.QtWidgets import QMainWindow, QMessageBox, QWidget, QVBoxLayout, QPushButton, QHBoxLayout
from PyQt5.QtCore import pyqtSlot
from MainMenu import MainMenu
from Teacher import View


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        main_menu = MainMenu(parent=self)
        self.setMenuBar(main_menu)

        w = QWidget(parent=self)
        view = View(parent=w)
        main_menu.about.triggered.connect(self.about)
        main_menu.about_qt.triggered.connect(self.about_qt)
        main_menu.teacher_add.triggered.connect(view.add)
        main_menu.teacher_update.triggered.connect(view.update)
        main_menu.teacher_delete.triggered.connect(view.delete)



        layout = QVBoxLayout()
        layout.addWidget(view)
        add_button = QPushButton('Добавить', parent=w)
        add_button.clicked.connect(view.add)
        update_button = QPushButton('Редактировать', parent=w)
        update_button.clicked.connect(view.update)
        delete_button = QPushButton('Удалить', parent=w)
        delete_button.clicked.connect(view.delete)
        button_layout = QHBoxLayout()
        button_layout.addWidget(add_button)
        button_layout.addWidget(update_button)
        button_layout.addWidget(delete_button)
        layout.addLayout(button_layout)
        w.setLayout(layout)
        self.setCentralWidget(w)


    @pyqtSlot()
    def about(self):
        title = 'Управление заданиями для учащихся'
        text = (
            'Программа для управления задачами\n' +
            'и заданиями для учащихся школы'
        )
        QMessageBox.about(self, title, text)

    @pyqtSlot()
    def about_qt(self):
        QMessageBox.aboutQt(self, 'Управление заданиями для учащихся')




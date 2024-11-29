from PyQt5.QtCore import pyqtSlot
from PyQt5.QtSql import QSqlQueryModel
from PyQt5.QtWidgets import QTableView, QMessageBox


class Model(QSqlQueryModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        sql = '''
            select id_teacher, fio, phone, email, comment
                from teachers;
        '''
        self.setQuery(sql)

class View(QTableView):
    def __init__(self, parent=None):
        super().__init__(parent)

        model = Model(parent=self)
        self.setModel(model)

    @pyqtSlot()
    def add(self):
        QMessageBox.information(self, 'Учитель', 'Добавление')

    @pyqtSlot()
    def update(self):
        QMessageBox.information(self, 'Учитель', 'Редактирование')

    @pyqtSlot()
    def delete(self):
        QMessageBox.information(self, 'Учитель', 'Удаление')

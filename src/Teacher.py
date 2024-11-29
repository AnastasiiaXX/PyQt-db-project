from PyQt5.QtCore import pyqtSlot
from PyQt5.QtSql import QSqlQueryModel, QSqlQuery
from PyQt5.QtWidgets import (QPushButton, QTextEdit, QTableView, QMessageBox, QDialog, QVBoxLayout,
                                              QLabel, QHBoxLayout, QLineEdit)

class Model(QSqlQueryModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.refresh()

    def refresh(self):
        sql = '''
                    select id_teacher, fio, phone, email, comnt
                    from teachers;
            '''
        self.setQuery(sql)

    def add(self, fio, phone, email, comnt):
        add_query = QSqlQuery()
        INSERT = '''
                    insert into teachers (fio, phone, email, comnt)
                    values ( :fio, :phone, :email, :comnt );
                '''
        add_query.prepare(INSERT)
        add_query.bindValue(':fio', fio)
        add_query.bindValue(':phone', phone[:10])
        add_query.bindValue(':email', email)
        add_query.bindValue(':comnt', comnt)
        add_query.exec_()
        self.refresh()

    def select_one(self, id_teacher):
        sel_query = QSqlQuery()
        SELECT_ONE = '''
            select fio, phone, email, comnt
            from teachers 
            where id_teacher = :id_teacher;
        '''
        sel_query.prepare(SELECT_ONE)
        sel_query.bindValue(':id_teacher', id_teacher)
        sel_query.exec()
        if sel_query

    def update(self, fio, phone, email, comnt, id_teacher):
        update_query = QSqlQuery()
        UPDATE = '''
            update teachers set
                fio = :fio, 
                phone = :phone,
                email = :email,
                comnt = :comnt
            where id_teacher = :id_teacher ;
        '''
        update_query.prepare(UPDATE)
        update_query.bindValue(':fio', fio)
        update_query.bindValue(':phone', phone[:10])
        update_query.bindValue(':email', email)
        update_query.bindValue(':comnt', comnt)
        update_query.bindValue(':id_teacher', id_teacher)
        update_query.exec_()
        self.refresh()

class View(QTableView):
    def __init__(self, parent=None):
        super().__init__(parent)

        model = Model(parent=self)
        self.setModel(model)

    @pyqtSlot()
    def add(self):
        dialog = Dialog(parent=self)
        if dialog.exec():
            self.model().add(dialog.fio, dialog.phone, dialog.email, dialog.comnt)

    @pyqtSlot()
    def update(self):
        dialog = Dialog(parent=self)
        row = self.currentIndex().row()
        id_teacher = self.model().record(row).value(0)
        dialog.fio, dialog.phone, dialog.email, dialog.comnt = self.model().select_one(id_teacher)
        if dialog.exec():
            self.model().update(dialog.fio, dialog.phone, dialog.email, dialog.comnt, id_teacher)

    @pyqtSlot()
    def delete(self):
        QMessageBox.information(self, 'Учитель', 'Удаление')

class Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Учитель')

        fio_lbl = QLabel('&Фамилия И. О.', parent=self)
        self.__fio_edit = QLineEdit(parent=self)
        fio_lbl.setBuddy(self.__fio_edit)

        phone_lbl = QLabel('&Телефон', parent=self)
        self.__phone_edit = QLineEdit(parent=self)
        phone_lbl.setBuddy(self.__phone_edit)

        email_lbl = QLabel('&E-mail', parent=self)
        self.__email_edit = QLineEdit(parent=self)
        email_lbl.setBuddy(self.__email_edit)

        comnt_lbl = QLabel('&Примечание', parent=self)
        self.__comnt_edit = QTextEdit(parent=self)
        comnt_lbl.setBuddy(self.__comnt_edit)

        ok_btn = QPushButton('Ok', parent=self)
        cancel_btn = QPushButton('Отмена', parent=self)

        lay = QVBoxLayout()
        lay.addWidget(fio_lbl)
        lay.addWidget(self.__fio_edit)
        lay.addWidget(phone_lbl)
        lay.addWidget(self.__phone_edit)
        lay.addWidget(email_lbl)
        lay.addWidget(self.__email_edit)
        lay.addWidget(comnt_lbl)
        lay.addWidget(self.__comnt_edit)

        hlay = QHBoxLayout()
        hlay.addStretch()
        hlay.addWidget(ok_btn)
        hlay.addWidget(cancel_btn)
        lay.addLayout(hlay)

        self.setLayout(lay)

        ok_btn.clicked.connect(self.finish)
        cancel_btn.clicked.connect(self.reject)

    @pyqtSlot()
    def finish(self):
        if self.fio is None:
            return
        self.accept()


    @property
    def fio(self):
        result = self.__fio_edit.text().strip()
        if result == '':
            return None
        return result

    @fio.setter
    def fio(self, value):
        self.__fio_edit.setText(value)

    @property
    def phone(self):
        result = self.__phone_edit.text().strip()
        if result == '':
            return None
        return result

    @phone.setter
    def phone(self, value):
        self.__phone_edit.setText(value)

    @property
    def email(self):
        result = self.__email_edit.text().strip()
        if result == '':
            return None
        return result

    @email.setter
    def email(self, value):
        self.__email_edit.setText(value)

    @property
    def comnt(self):
        result = self.__comnt_edit.toPlainText().strip()
        if result == '':
            return None
        return result

    @comnt.setter
    def comnt(self, value):
        self.__comnt_edit.setText(value)

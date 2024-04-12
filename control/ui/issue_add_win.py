from functools import partial

from PySide6.QtCore import Signal, QStringListModel
from PySide6.QtWidgets import QDialog, QMenu

from control.structs.db import DB
from control.structs.issue import Issue
from control.structs.simple_model import SimpleModel

from .design.issue_add_ui import Ui_IssueAdd


class IssueAddWin(QDialog):
    issues = Signal(object)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_IssueAdd()
        self.ui.setupUi(self)

        self.ui.category.setModel(SimpleModel("category", self))
        self.ui.subcategory.setModel(SimpleModel("subcategory", self))

        self.ui.accept.clicked.connect(self.accept)
        self.ui.cancel.clicked.connect(self.reject)

        self.responsible_model = QStringListModel(self)
        self.ui.responsible.setModel(self.responsible_model)

        menu = QMenu(self.ui.add_resp)
        self.ui.add_resp.setMenu(menu)

        # menu responsible
        cursor = DB.connection().cursor()
        query = """SELECT name FROM department WHERE responsible is TRUE ORDER BY name"""
        cursor.execute(query)

        for row in cursor.fetchall():
            menu.addAction(row[0], partial(self.add_responsible, row[0]))

        self.ui.add_resp_all.clicked.connect(lambda: [self.add_responsible(i.text()) for i in menu.actions()])
        self.ui.rem_resp.clicked.connect(self.rem_responsible)

    def add_responsible(self, name: str):
        list_resp = self.responsible_model.stringList()
        if name not in list_resp:
            list_resp.append(name)
            self.responsible_model.setStringList(sorted(list_resp))

    def rem_responsible(self):
        if self.ui.responsible.selectionModel().hasSelection():
            name = self.ui.responsible.selectionModel().currentIndex().data()

            list_resp = self.responsible_model.stringList()
            list_resp.remove(name)
            self.responsible_model.setStringList(sorted(list_resp))

    def accept(self) -> None:
        issues: list[Issue] = []
        for responsible in self.responsible_model.stringList():
            issue = Issue()
            issue.place = self.ui.place.text()
            issue.issue = self.ui.issue.toPlainText()
            issue.category = self.ui.category.currentText()
            issue.subcategory = self.ui.subcategory.currentText()
            issue.measures = self.ui.measures.toPlainText()
            issue.responsible = responsible
            issues.append(issue)

        self.issues.emit(issues)
        return super().accept()

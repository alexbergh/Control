from PySide6.QtCore import QSettings, QModelIndex, Qt
from PySide6.QtWidgets import QDialog, QMessageBox

from control.structs.issue import Issue
from control.structs.issues_table_view import IssueTableView
from control.structs.simple_model import SimpleModel
from control.structs.user import User

from ..structs.inspection import Inspection
from .design.inspection_ui import Ui_Inspection
from .issue_add_win import IssueAddWin


class InspectionWin(QDialog):
    """Window with all inforamtion about inspection"""

    def __init__(self, id: int = 0, parent=None):
        super().__init__(parent)

        assert type(id) == int

        if not User.is_valid:  # TODO: remove later
            QMessageBox.warning(None, "Ошибка авторизации",
                                "Вы не авторизовались.\nАвторизуйтесь и попробуйте еще раз: admin/admin")
        assert User.is_valid

        self.ui = Ui_Inspection()
        self.ui.setupUi(self)

        self.ui.inspection_type.setModel(SimpleModel("type", self))

        self.settings = QSettings(self)
        self.inspection = Inspection(id, self)
        self.issues = IssueTableView(self)
        self.issues.change_model(self.inspection.issues_model)

        self.ui.inspection_id.setText(self.inspection.work_id)
        self.ui.inspection_date.setText(self.inspection.date_str())
        self.ui.level.setText(str(self.inspection.level))
        self.ui.inspection_type.setCurrentText(self.inspection.type)
        self.ui.department.setText(self.inspection.department)
        self.ui.inspector.setText(self.inspection.inspector)
        self.ui.shift.setCurrentText(str(self.inspection.shift))
        self.ui.issues_layout.insertWidget(0, self.issues)

        self.ui.ok.clicked.connect(self.accept)
        self.ui.cancel.clicked.connect(self.reject)

        self.ui.add_issue_button.clicked.connect(self.add_issue_win)

        self.issues.doubleClicked.connect(self._double_clicked)

    def accept(self) -> None:
        # save all to DB
        QMessageBox.information(None, "Информация", "В процессе разработки")
        return super().accept()

    def add_issue_win(self):
        win = IssueAddWin(self)
        win.issues.connect(self.add_issues)
        win.exec()

    def add_issues(self, issues: list[Issue]):
        for issue in issues:
            row = self.inspection.issues_model.rowCount()
            self.inspection.issues_model.insertRow(row, QModelIndex())

            index = self.inspection.issues_model.index(row, 0)
            self.inspection.issues_model.setData(index, issue, Qt.ItemDataRole.UserRole)

    def _double_clicked(self, index: QModelIndex):
        # open issuewin to edit
        self.inspection.issues_model.setData(index, (1, 2, 3, 4), Qt.ItemDataRole.UserRole)

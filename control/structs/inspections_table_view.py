from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QDate, QModelIndex
from control.structs.issues_table_view import IssueTableView

from control.ui.inspection_win import InspectionWin
from .base_table_view import BaseTableView
from .inspections_table_model import InspectionsTableModel

class InspectionsTableView(BaseTableView):
    def __init__(self, issue_table_view: IssueTableView, parent: QWidget = None) -> None:
        super().__init__(parent)
        self._issues_view = issue_table_view
        self._model = InspectionsTableModel(self)
        self.setModel(self._model)  # Устанавливаем модель напрямую в базовый вид, если proxy не нужен

    def fetch(self, begin_date: QDate, end_date: QDate):
        self.setEnabled(False)  # Изменено на setEnabled для лучшей читаемости
        if self._model.fetch(begin_date, end_date):
            self.setEnabled(True)

    def _clicked(self, index: QModelIndex):
        issue_model = self._model.get_issues_model(index)
        if issue_model:
            self._issues_view.setModel(issue_model)  # Предположим, что метод change_model называется setModel

    def _double_clicked(self, index: QModelIndex):
        id = self._model.get_id(index)
        inspection_win = InspectionWin(id=id, parent=self)
        if inspection_win.exec():
            print("Inspection updated.")
            self._model.fetch()  # Предполагаем, что существует метод fetch без параметров для перезагрузки
        else:
            print("Update canceled.")

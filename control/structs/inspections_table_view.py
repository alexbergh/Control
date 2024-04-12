from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QDate, QModelIndex
from control.structs.issues_table_view import IssueTableView

from control.ui.inspection_win import InspectionWin
from .base_table_view import BaseTableView
from .inspections_table_model import InspectionsTableModel


class InspectionsTableView(BaseTableView):
    def __init__(self, issue_table_view: IssueTableView, parent: QWidget) -> None:
        super().__init__(parent)
        self._issues_view = issue_table_view
        self._model = InspectionsTableModel(self)
        self._proxy_model.setSourceModel(self._model)

    def fetch(self, begin_date: QDate, end_date: QDate):
        self.setDisabled(True)
        if self._model.fetch(begin_date, end_date):
            self.setEnabled(True)

    def _clicked(self, index: QModelIndex):
        self._issues_view.change_model(self._model.get_issues_model(index))

    def _double_clicked(self, index: QModelIndex):
        id = self._model.get_id(index)
        if InspectionWin(id=id, parent=self).exec():
            print("ok")
            # update view
        else:
            print("false")

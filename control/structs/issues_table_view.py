from PySide6.QtWidgets import QWidget

from PySide6.QtCore import QModelIndex

from .base_table_view import BaseTableView
from .issues_table_model import IssueTableModel


class IssueTableView(BaseTableView):
    def __init__(self,  parent: QWidget) -> None:
        super().__init__(parent)

        self._model = IssueTableModel(self)
        self._proxy_model.setSourceModel(self._model)

    def change_model(self, model: IssueTableModel):
        self._model = model
        self._proxy_model.setSourceModel(self._model)

    def fetch(self,  inspection_id: int):
        self._model.fetch(inspection_id)

    def _double_clicked(self, index: QModelIndex):
        print(index)

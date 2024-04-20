from typing import Any
from PySide6.QtCore import QObject, QModelIndex, QPersistentModelIndex, QCoreApplication, Qt

from .db import DB
from .issue import Issue
from .base_table_model import BaseTableModel


class IssueTableModel(BaseTableModel):
    def __init__(self, parent: QObject, inspection_id: int = 0) -> None:
        super().__init__(parent)
        self._headers = (
            "Объект",
            "Замечание",
            "Ответственный",
            "Устранить до",
            "Категория",
            "Подкатегория",
            "Мероприятия",
            "Отметка",
            "Подтверждение",
        )

        if inspection_id:
            self.fetch(inspection_id)

    def fetch(self, inspection_id: int):
        self.inspection_id = inspection_id
        self.beginResetModel()
        self._data.clear()

        try:
            with DB.connection().cursor(prepared=True) as cursor:
                query = "SELECT id FROM issue WHERE inspection_id = %s"
                cursor.execute(query, (self.inspection_id,))
                ids = cursor.fetchall()
                
                for (id,) in ids:
                    self._data.append(Issue(id))
                    QCoreApplication.processEvents()

        except Exception as e:
            print(f"Failed to fetch issues for inspection ID {inspection_id}: {e}")
        
        self.endResetModel()

    def data(self, index: QModelIndex, role: int = Qt.DisplayRole) -> Any:
        if not index.isValid() or role != Qt.DisplayRole:
            return None
        issue = self._data[index.row()]
        return getattr(issue, self._headers[index.column()], None)

    def setData(self, index: QModelIndex, value: Any, role: int = Qt.EditRole) -> bool:
        if not index.isValid() or role != Qt.EditRole:
            return False
        issue = self._data[index.row()]
        setattr(issue, self._headers[index.column()], value)
        self.dataChanged.emit(index, index, [role])
        return True

    def insertRow(self, row: int, parent: QModelIndex = QModelIndex()) -> bool:
        if row < 0 or row > len(self._data):
            return False
        self.beginInsertRows(parent, row, row)
        self._data.insert(row, Issue())
        self.endInsertRows()
        return True

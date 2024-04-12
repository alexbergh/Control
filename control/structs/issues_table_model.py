from typing import Any
from PySide6.QtCore import QObject, QModelIndex, QPersistentModelIndex, QCoreApplication,  Qt

from .db import DB
from .issue import Issue
from .base_table_model import BaseTableModel


class IssueTableModel(BaseTableModel):
    def __init__(self, parent: QObject, id: int = 0) -> None:
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

        if id:
            self.fetch(id)

    def fetch(self,  inspection_id: int):
        self.inspection_id = inspection_id

        cursor = DB.connection().cursor(prepared=True)
        query = """
                SELECT
                    id
                FROM
                    issue
                WHERE
                    inspection_id = %s
                """
        params = (self.inspection_id,)

        cursor.execute(query, params)
        data = cursor.fetchall()
        cursor.close()

        self.beginResetModel()
        self._data.clear()
        for id in data:
            self._data.append(Issue(id[0]))
            QCoreApplication.processEvents()
        self.endResetModel()

    def data(self, index: QModelIndex | QPersistentModelIndex, role: int = ...) -> Any:
        # TODO: fill with color
        return super().data(index, role)

    def setData(self, index: QModelIndex | QPersistentModelIndex, value: Any, role: int = ...) -> bool:
        if not index.isValid():
            return False

        if role == Qt.ItemDataRole.UserRole:
            row = index.row()

            self.beginResetModel()
            self._data[row] = value
            self.endResetModel()

        return super().setData(index, value, role)

    def insertRow(self, row: int, parent: QModelIndex | QPersistentModelIndex = ...) -> bool:
        self._data.insert(row, None)
        return super().insertRow(row, parent)

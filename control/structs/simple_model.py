from PySide6.QtCore import QObject

from .db import DB
from .base_table_model import BaseTableModel


class SimpleModel(BaseTableModel):
    def __init__(self, table: str, parent: QObject) -> None:
        super().__init__(parent)
        self._headers = ("name",)

        cursor = DB.connection().cursor(prepared=True)
        query = "SELECT name FROM " + table + " ORDER BY name;"

        cursor.execute(query)
        self.beginResetModel()
        self._data: list = cursor.fetchall()
        self.endResetModel()

        cursor.close()

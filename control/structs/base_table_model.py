from typing import Any
from PySide6.QtCore import QAbstractTableModel, QModelIndex, QObject, QPersistentModelIndex, Qt


class BaseTableModel(QAbstractTableModel):
    """Base class for SQLModel"""

    def __init__(self,  parent: QObject) -> None:
        super().__init__(parent)
        self._headers = ()
        self._data = []

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...) -> Any:
        if role != Qt.ItemDataRole.DisplayRole:
            return None

        return section if orientation == Qt.Orientation.Vertical else self._headers[section]

    def rowCount(self, parent: QModelIndex | QPersistentModelIndex = ...) -> int:
        assert (type(self._data) == list)
        return len(self._data)

    def columnCount(self, parent: QModelIndex | QPersistentModelIndex = ...) -> int:
        assert (type(self._headers) == tuple)
        return len(self._headers)

    def data(self, index: QModelIndex | QPersistentModelIndex, role: int = ...) -> Any:
        if not index.isValid():
            return None

        match role:
            case  Qt.ItemDataRole.DisplayRole:
                return self._data[index.row()][index.column()]
            case _:
                return None

    def get_id(self, index: QModelIndex | int) -> int:
        raise NotImplemented
